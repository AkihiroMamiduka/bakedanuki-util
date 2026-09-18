# Attributes

このページは `NodeOperator` の attribute / plug 周辺仕様をまとめます。

## 3 つの役割

### AttributeField

`AttributeField` は descriptor です。

ノードクラス定義に置かれ、アクセス元に応じて `AttrOperator` または `PlugOperator` を生成します。

```python
class MyNode(NodeOperator):
    myValue = AddAttr.at.double(default_value=1.0)
```

### AttrOperator

`AttrOperator` はアトリビュート定義側の情報を持ちます。

主な情報は次の通りです。

- `node_cls`
- `long_name`
- `short_name`
- `attr_path`
- `parent_attr_path`
- `multi`
- `extra`
- `default_value`
- `min_value` / `max_value`
- `soft_min_value` / `soft_max_value`
- `child_index`

### PlugOperator

`PlugOperator` は Maya scene 上の plug 操作を担当します。

すべての `PlugOperator` が持つ主な操作は次の通りです。

- `connect()`
- `connect_from()`
- `connect_next_index()`
- `disconnect()`
- `disconnect_from()`
- `src_plug()` / `src_name()` / `src_plug_name()`
- `dst_plugs()` / `dst_names()` / `dst_plug_names()`
- `add_attr()`
- `cmds_add_attr()`
- `set_locked()` / `set_unlocked()`
- `set_locked_direct()` / `set_unlocked_direct()`

値操作はplug型が対応するものだけを提供します。

- `get()`
- `set()`
- `set_direct()`
- `round()`

例えばscalar numericは`get()` / `set()`、typed matrixは`get()` /
`set_direct()`を持ち、message、generic、mixed compoundなど値操作へ
対応しない型にはこれらのmethodがありません。利用できない操作を
例外送出用methodとして残さないため、IDE補完にも表示されません。

`value` / `value_direct` propertyは提供しません。値操作は型注釈と
反映方法が明確な上記methodを使用します。

`keyframe`はscalar numeric / unit / enum plugで提供します。compoundは
対象のscalar childへアクセスしてから使用します。

`set()` は `ModifierManager.dg_mod` 経由で編集します。

`set_direct()` は `MPlug` へ即時反映します。undo には参加しません。

浮動小数点のscalar / scalar compound型は`round(ndigits=0)`を提供します。
呼び出し時点の`get()`結果をPython組み込みの`round()`と同じ偶数丸めで
処理し、`set()`と同じく`ModifierManager.dg_mod`経由で書き戻します。
負の`ndigits`も指定できます。

```python
node.translate.round(3)
node.translate.translateX.round(3)
mod.do_it_dg()
```

angleはdegree、linearはcentimeter、timeはMaya UI time unitという、各型の
`get()` / `set()`と同じ公開単位で丸めます。matrix、typed data、quaternion、
整数型には`round()`を提供せず、`round_direct()`も提供しません。

`round()`は呼び出し時点のscene値を読みます。未実行の`set()`は
`ModifierManager`内に保留されており、`get()`からはまだ見えません。
その値を丸める場合は、次のように一度sceneへ反映してから呼び出します。

```python
node.translate.set(0.506459506684667, 0.0, 0.0)
mod.do_it_dg()

node.translate.round(3)
mod.do_it_dg()
```

`round()`自身はbatchingとundo / redoの実行境界を暗黙に変更しないため、
`do_it_dg()`を自動実行しません。新しく設定する値を一度のbatchで丸めたい場合は、
Python側で丸めてから`set()`へ渡します。animation curveのkeyframe値を
一括処理する機能でもありません。

### 指定時刻の値をサンプリングする

scalar plugの`sample_values(*, frames: Iterable[float]) -> list[tuple[float, float]]`は、
指定時刻の評価済み値を`(frame, value)`のlistで返します。キーがない時刻や、
constraint・unitConversion・animation layer・計算ノードで駆動されたplugにも使用できます。
上流カーブの実在キーを返す`keyframe.get_keys()`とは取得対象が異なります。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
source = nodes.existing.transform("source_ctrl")
target = nodes.existing.transform("target_ctrl")

samples = source.tx.sample_values(frames=range(1, 25))
target.tx.keyframe.set_keys(
    samples, in_tangent_type="linear", out_tangent_type="linear"
)
mod.do_it_dg()
```

`frames`はgeneratorも使用でき、全入力を捕捉・検証してから値を取得します。
順序と重複を維持し、空入力は空listです。NaN・無限大は`ValueError`、
列の代わりに渡した`str` / `bytes`は`TypeError`です。multi属性は要素を指定してください。
compoundやmatrix、typed dataにはこのmethodを提供しません。

frameとtime属性のvalueは、generatorを読む前の呼び出し入口のMaya UI時間単位です。
angleのvalueはdegree、linearのvalueはcentimeterです。valueはすべてfloatとして返し、
bool / enum / 整数は数値、charは文字コードになります。単位は`set_keys()`に対応します。

queryは呼び出し時点のsceneを読み、保留中の変更をflushしません。
タイムスライダーの現在時刻やUndo履歴は変更せず、評価コンテキストを各時刻へ
一時的に切り替えます。`MDGContext.makeCurrent()`を使い、評価の成功・失敗のどちらでも
元のコンテキストへ戻します。
取得結果は値のsnapshotであり、その後のscene変更には追従しません。

新規layerへの初回キー設定直後に先頭サンプルが古い値になる問題に対応し、空でない入力では
対象plugの上流カーブを列挙し、その出力から`cmds.dgdirty(..., propagation=True)`で
再評価を伝播してから値を読みます。準備は呼び出しごとに1回、値の取得は引き続きOpenMayaです。
キー・接続・layer構造・modified flagやUndo / Redo履歴は変更しません。
計算ノードの未接続出力やdriven curveの入力側も辿り、空入力では再評価準備も行いません。
この内部探索は、各経路の最初のカーブで停止する公開`find_anim_curves()`とは用途が異なります。
[Autodesk dgdirty](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/dgdirty.html)

constraintを削除して打ち直す場合は、必要な全属性・全時刻を先に取得し、
その後に削除とキー設定を予約します。別の親空間を持つコントローラー間の姿勢転送は、
local属性値のコピーに加えて座標変換が必要になるため、上位の転送処理で扱います。

このmethodは各時刻を独立に評価します。dynamicsや、前フレームに依存する
parentConstraintのno flipなど、順次評価・simulation・事前cacheを必要とする動作を
汎用的にベイクする機能ではありません。
[Autodesk parentConstraint](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/parentConstraint.html)、
[Autodesk bakeResults](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/bakeResults.html)

### 値操作methodの実装規則

新しい`PlugOperator`型を追加するときは、その型で実行できる値操作だけを
具象class、または全派生classが同じ操作へ対応する共通基底classに実装します。

現在の代表的な対応関係は次の通りです。

| plug family | `get()` | `set()` | `set_direct()` | `round()` |
| --- | --- | --- | --- | --- |
| floating scalar numeric / unit | yes | yes | 原則no | yes |
| integral / bool / enum scalar | yes | yes | 原則no | no |
| floating scalar compound | yes | yes | yes | yes |
| integral scalar compound | yes | yes | yes | no |
| quaternion | yes | yes | yes | no |
| matrix / floatMatrix attribute | yes | yes | no | no |
| string data | yes | yes | yes | no |
| numeric / array / matrix data | yes | no | yes | no |
| addr | yes | no | yes | no |
| message / generic / lightData / mixed compound | no | no | no | no |
| mesh / lattice / nurbs data | no | no | no | no |

未対応操作を、`NotImplementedError`や`UnsupportedOperationError`を送出するだけの
methodとして定義しません。`PlugOperator`や`DataTypePlugOperator`などの共通基底にも
値操作methodを置きません。これにより、実行できない操作がIDE補完へ現れることを
防ぎます。

公開する`get()` / `set()` / `set_direct()` / `round()`には、対象となるMaya型、Python側の
値型、単位、ModifierManager経由か即時反映かをdocstringへ記載します。対応関係を
変更した場合はruntimeのcapability testとPyright contractも同時に更新します。

## キーフレーム

scalar plugの`keyframe`による変更操作は、同じ`ModifierManager`へ予約します。
`mod.do_it_dg()`まではsceneへ反映せず、値設定や接続と同じ履歴でundo / redoできます。
すべての変更methodの戻り値は`None`です。

layer未指定の`.keyframe`は、sceneのベース（root）layerを対象にします。
キー設定だけでなく、取得・挿入・接線変更・削除・詳細データ・weighted操作も同じ対象です。
layerがないsceneでは通常のアニメーションカーブを扱い、別layerには
`.keyframe.anim_layer("Correction")`を使用します。Mayaの選択layer・preferred・keying modeで
対象は変わりません。`BaseAnimation`という名前を固定せず、query・初回実行時にrootを特定します。
予約後のrootの作成・改名にも対応し、ベースがlockされていても別layerへ切り替えません。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
cmp_m = nodes.create.composeMatrix(name="cmp_m")
keyframe = cmp_m.inputRotate.inputRotateX.keyframe

keyframe.set_key(0.0, frame=1.0, out_tangent_type="linear")
keyframe.set_key(90.0, frame=24.0, in_tangent_type=keyframe.tangent.linear)
mod.do_it_dg()

mod.undo_it()
mod.redo_it()
```

`get_keys()`や`frames()`、`key_count()`などのqueryは実行済みのsceneだけを読み、予約中の変更は
含みません。変更methodは`do_it_dg()`を暗黙に呼び出しません。MayaのUndoキューへの登録は
[ModifierManagerのMPxCommand連携](modifier_manager.md)を参照してください。

### 複数キーをまとめて設定する

`set_keys(keys, *, in_tangent_type=None, out_tangent_type=None) -> None`は、
複数キーをまとめて予約します。`keys`には`(frame, value)`の列を
`Iterable[tuple[float, float]]`として渡します。pair内は時刻、値の順です。
単位・tangent・実行時の経路選択は`set_key()`と同じです。

```python
keyframe.set_keys(
    [(1.0, 0.0), (12.0, 45.0), (24.0, 90.0)],
    in_tangent_type="linear",
    out_tangent_type="linear",
)
mod.do_it_dg()
```

listだけでなくgeneratorも呼び出し時にすべて読み取り、値・時刻を捕捉してから予約します。
各要素が2要素のpairでない場合やNaN・無限大を拒否し、列やpairの代わりに
`str` / `bytes`を渡すこともできません。入力の読み取りや検証に失敗しても、
この呼び出しの一部だけを予約することはありません。空の列ならキーを予約しませんが、
managerや対象plugなどの前提は通常どおり検証します。

入力を並べ替えず、その順序で設定します。同じ時刻が複数あれば後の値で上書きします。
tangent引数は全キー共通で、既存キーのtangent typeを維持する仕様も`set_key()`と同じです。
時刻とtime属性の値には、generatorを読み取る前の呼び出し入口のUI時間単位を使用します。

### 実在するキーを取得する

`get_keys(start_frame=None, end_frame=None) -> list[tuple[float, float]]`は、
`(frame, value)`のlistを時刻の昇順で返します。そのチャンネルのtime-input
animCurveを対象にし、指定範囲に実在するキーだけを取得します。対象なし・空カーブ・
該当キーなしは空list、未対応の接続構成は`RuntimeError`です。
範囲は両端を含み、`None`の側には境界を設けません。
範囲端にキーがなくても、補間したキーを追加することはありません。
NaN・無限大や逆転した範囲は、カーブの有無にかかわらず`ValueError`です。

```python
keys = keyframe.get_keys()
segment_keys = keyframe.get_keys(start_frame=12.0, end_frame=24.0)
```

単純な直接接続のカーブでは、戻り値を同じ単位の`set_keys(keys)`へ渡せます。
中間ノードがある属性の`set_keys()`はMayaへ値の解決を委ねるため、生カーブのキーを
そのまま再現する用途には`set_key_data()` / `set_curve_data()`または明示カーブ操作を使います。
queryは即座に実行済みのsceneを読み、予約中の変更をflushしません。
`ModifierManager`を省略した`KeyframeManager`からも使用できます。
引数と戻り値のframeは、呼び出し時点のMaya UI時間単位です。
valueは対象plugの型ではなく、取得したカーブの型から次の単位へ換算します。

| カーブ型 | valueの単位 |
| --- | --- |
| TA | degree |
| TL | centimeter |
| TU | numeric値 |
| TT | 呼び出し時点のMaya UI時間単位 |

取得値はカーブに保存されたキーの値です。単位変換やpairBlendをたどる対象選択は、
後述の[選択ルール](#カーブを取得編集する場合の選択ルール)に従います。
合成・変換後のplug値には`sample_values()`を使用します。
pairにはtangentやweighted、infinityなどの情報を含まないため、カーブ形状全体の
保存・復元用データではありません。

### 引数と単位

| 引数 / plug型 | 公開単位 |
| --- | --- |
| `frame` / pairのframe / `start_frame` / `end_frame` | 各methodを呼んだ時点のMaya UI時間単位 |
| angleの`value` / pairのvalue | degree |
| linearの`value` / pairのvalue | centimeter |
| time属性の`value` / pairのvalue | `set_key()` / `set_keys()`を呼んだ時点のMaya UI時間単位 |
| その他scalarの`value` / pairのvalue | numeric値。bool / enumも数値で指定 |

angle / linearは通常の`PlugOperator.set()`と同じ固定単位です。時刻とtime属性の
値は予約時の時間単位で捕捉します。キー設定のAPI経路ではangleをradian、linearを
centimeterとして渡し、cmds経路では実行時のUI単位へ換算します。
挿入・tangent変更・キー削除も捕捉した時刻をAPIで使用します。
予約後にangle / linear / timeのUI単位を変更しても、予約した物理量は維持します。
`value`や時刻の引数にNaNや無限大は指定できません。有限値、不正なtangent、
`delete_keys()`の逆転した範囲は予約時に検証します。

`in_tangent_type` / `out_tangent_type`には`"linear"`などの文字列、または
`keyframe.tangent.linear`などの定数を指定できます。`set_key()` / `set_keys()`の`None`は
Mayaの既定値を使用し、`set_tangent()`の`None`はその側のtangentを変更しません。

これらのmethodのtangent引数は`TangentTypeName | int | None`で型付けしています。
`TangentTypeName`は次の小文字の文字列を列挙した`Literal`で、対応するIDEでは
引数の文字列補完候補になり、未対応の名前やタイプミスは型チェックで検出できます。

`"auto"`, `"clamped"`, `"fast"`, `"flat"`, `"linear"`, `"plateau"`,
`"slow"`, `"spline"`, `"step"`, `"stepnext"`

変数や自作関数の引数にも型を付ける場合は、
`bd_util.maya.node.operator.attr`から`TangentTypeName`（文字列のみ）、または
`TangentTypeValue`（整数定数・`None`も含む）をimportできます。任意の`str`ではなく
これらの型を使うと、候補を保ったままキーフレームmethodへ渡せます。
実行時の大文字・小文字を区別しない解釈と、不正な値の検証は従来どおりです。

`set_key()` / `set_keys()`の`in_tangent_type="step"`はMayaが警告を出して入力側を
既定値にするため、step補間は`out_tangent_type="step"`へ指定してください。Maya 2027では入力側の
`"stepnext"`も同様に既定値になります。どちらも出力側へ指定することで、
対応するMaya version間で共通の設定として使用できます。
既存キーの上書きではvalueを更新して既存tangent typeを維持し、指定したtangent引数で
既存tangent typeを変更することはありません。変更する場合は`set_tangent()`を使用します。
API経路の上書きにも`addKey()`を使用します。valueだけを変更する`setValue()`と異なり、
breakdownやtangent lockの更新も`cmds.setKeyframe()`と同じ挙動に揃えるためです。

### 対象カーブと実行時エラー

layerを指定しない`set_key()` / `set_keys()`は、実行時の接続・型・scene状態から
API経路かcmds経路を選択します。
対象plugに直接接続した既存のTA / TL / TUカーブがあり、plugとカーブの型が一致する
単純な構成では、`MFnAnimCurve.addKey()`と`MAnimCurveChange`で追加・上書きします。
API経路の対象plugは、boolを除くscalar numericとangle / linearです。

次のいずれかに該当する場合は、`MDGModifier.pythonCommandToExecute()`から
`cmds.setKeyframe()`を実行します。

- カーブの新規作成、blend nodeやunitConversionを経由する接続、共有カーブ。
- カーブのinputや設定属性に明示的な入力接続がある場合、またはplugとカーブの型が一致しない場合。
- scene内にanimation layerが1つでもある場合。対象plugがlayerに属さなくても含みます。
- 対象plug、カーブのoutputやkeyTimeValueがlockされている場合、または対象node・
  カーブnodeがlockされているかreference由来の場合。
- bool / enum / time属性、TTカーブなどAPI経路の対象外の型。
- 入力側tangentが`step` / `stepnext`、またはTAカーブの`rotationInterpolation`が1以外の場合。

cmds経路では対象layerを決めたうえで、カーブの作成、animation layerへの値の解決、
必要なblend nodeの作成をMayaへ委ねます。layer未指定ならsceneのrootを`animLayer`へ明示し、
Mayaの選択状態にかかわらずベースへ設定します。sceneにlayerがなければ通常のキー設定です。
別layerを指定する場合は、後述の`anim_layer()`で操作入口を取得してください。
`insertBlend`指定の引数はありません。layerがある場合はcmds経路を使用し、
対象plugがlayer未所属でもrootのlock / referenceを検査します。
[Autodesk setKeyframe](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/CommandsPython/setKeyframe.html)

通常のキー設定では上流の最初のカーブを探索して編集することはありません。
先行する作成・接続・キー設定が反映された時点で経路を判定するため、同じ予約列で
1個目のキーをcmdsで作成し、後続のキーをAPIで追加することもできます。

`set_keys()`では、単純な既存カーブの取得と経路判定をバッチ内で再利用し、1つの
`MFnAnimCurve`と`MAnimCurveChange`で、入力順に`addKey()`を呼びます。`addKeys()`は
使用しません。カーブがなければ最初の1キーをcmdsで作成・反映し、残りのキーを
APIで扱えるか再判定します。layerや複雑な接続などでは全キーをcmdsへ委譲し、
途中の失敗を戻せるよう、1キーずつ別のcommand callbackとして予約します。

どちらの経路も同じ`do_it_dg()`の履歴へ含み、途中の失敗ではその実行境界の変更を戻します。
カーブの取得結果を別の`set_key()` / `set_keys()`の探索に再利用する永続キャッシュは持ちません。
Undo / Redoは初回実行で記録したmodifierと変更キャッシュを使用し、経路を再判定しません。

対象plugの名前は実行時に`MPlug`から取得するため、予約後の改名にも追従します。
非scalar plug、不正なtangent名、書き込み不可の属性などは予約時に拒否します。
lockや既存driven keyの接続などによりMayaがキーを1個も設定しなかった場合は、
`do_it_dg()`で`RuntimeError`になります。非keyableであることだけでは拒否せず、
明示したplugへの設定をMayaに委ねます。

### MPlugから使用する

`KeyframeManager`を単体で使用する場合は、`modifier_manager`をkeywordで渡します。
`set_key()` / `set_keys()`の単位はscalar `PlugOperator`経由と同じです。

```python
import bd_util as bdu
from maya.api import OpenMaya as om
from bd_util.maya.node.operator.attr import KeyframeManager

mod = bdu.ModifierManager()
selection = om.MSelectionList()
selection.add("existing_transform.rotateX")
keyframe = KeyframeManager(selection.getPlug(0), modifier_manager=mod)
keyframe.set_key(90.0, frame=24.0)
mod.do_it_dg()
```

`modifier_manager`を省略したインスタンスで変更methodを呼ぶと`RuntimeError`です。
queryだけを行う場合は省略できます。

### カーブを取得・編集する場合の選択ルール

layer未指定の`KeyframeManager`は、そのチャンネルのベースの時間入力カーブを取得・編集します。
layerがないsceneやlayer未所属の属性は、通常のチャンネル探索を使用します。
通常の`pairBlend`構成でも、利用者がカーブを探して指定する必要はありません。
ノードを直接指定する操作は、後述の[カーブを明示して操作する](#カーブを明示して操作する)を参照します。

```python
keyframe = node.translate.translateY.keyframe
keys = keyframe.get_keys()
keyframe.delete_key(frame=12)
mod.do_it_dg()
```

| 操作 | 対象の決定 |
| --- | --- |
| `set_key()` / `set_keys()` | ベースまたは指定layerへ設定。layerのない単純な直接接続ならAPI、その他は対象layerを明示したMayaの`setKeyframe`で値を解決 |
| `has_anim_curve()` / `key_count()` / `frames()` / `values()` / `has_key()` / `get_keys()` | ベースまたは指定layerの時間入力カーブ。TA / TL / TU / TT、scalar numeric / bool / enum / unit plug |
| 挿入・接線変更・キー削除・カーブ削除 | 上記と同じカーブを、書込み可否を検査して編集 |
| 詳細データ・weighted操作 | 同じ対象選択に加え、TA / TL / TUとnumeric / angle / distance plugに限定。enum・timeは対象外 |
| `find_anim_curves()` | 接続調査用に上流のDG依存関係にある候補を列挙。全8型を含み、通常操作の対象選択には使用しない |

layer付き属性は、元のplugと対象layerの対応からカーブを解決します。ベースにカーブが
未作成でも別layerのカーブは選びません。通常のチャンネル探索では接続先plugから
次の規則で進み、最初に見つかった対象カーブを使用します。
ノード名やDG全体の列挙順で選ぶことはありません。

| 接続 | たどる入力 |
| --- | --- |
| animCurveの`output` | 時間入力カーブなら選択。driven keyならその経路の探索を終了 |
| `unitConversion` / `unitToTimeConversion` / `timeToUnitConversion`の`output` | `input`。変換係数の入力は対象外 |
| `pairBlend.outTranslateX/Y/Z` / `outRotateX/Y/Z` | 同じ軸の、`currentDriver`が指定する入力1または2。別軸・weight・非選択入力は対象外 |
| `blendWeighted.output` | `input`の既存logical indexが小さい順。最初に見つかるカーブを選び、`weight`は対象外 |
| constraintの出力 | その経路の探索を終了。constraint先からdriver自身のキーは取得・編集しない |

対応ノードの入れ子も同じ規則でたどります。`pairBlend.currentDriver`の選択は、
Mayaの`keyframe` queryと`setKeyframe`のキー設定先に合わせています。
複数のカーブを接続した`blendWeighted`では入力indexが優先順位になり、合成時の寄与率は
判定しません。このような構成の管理は利用者が行います。空カーブも選択対象です。

対象カーブは元のplugと型が一致し、カーブの`output`接続先が1つである必要があります。
カーブの`input`への時間接続とmessage接続は許可し、それ以外の設定属性への入力、
共有出力、TAの独立scalar以外の補間は拒否します。
通常のチャンネル探索で`multiplyDivide`等の未対応の中間ノードを通る場合は
`RuntimeError`です。`has_anim_curve()`も未対応構成を`False`として扱いません。
対象属性と無関係なanimation layerがsceneにある場合も通常のチャンネルを取得でき、
編集時はベースのlock / referenceを検査します。

未接続、driven keyのみ、constraintのみ等で対象カーブがなければ、
`has_anim_curve()`は`False`、キー列は空、`get_curve_data()` / `get_weighted()`は`None`です。
取得する時刻・値・接線はカーブ自身のデータで、単位変換、時間入力の変換、blendの合成を
反映した値ではありません。最終的なplug値の評価には`sample_values()`を使用します。

queryはlock・referenceによる読み取りを制限しません。編集時は対象plug・node・curveの
lock、reference、属性の書込み可否を検査します。対象なしの戻り値やno-opは、これらの
前提条件を満たした場合に適用します。接続やlockはquery時・編集の初回実行時に解決し、
別の呼び出しへキャッシュしません。Redoでは初回に記録した対象への変更を再生します。

layerに属する属性も、未指定ならベースへのキー設定とカーブquery・編集を同じ入口で行えます。
別layerの取得・編集には`anim_layer()`を使用します。
同じ実行単位で未対応の編集を続けて失敗した場合は、先行するキー設定もrollbackします。

### アニメーションレイヤーを指定する

`anim_layer(name: str | AnimLayerNode) -> KeyframeManager`は、「1 plug × 1 layer」を対象とする
操作入口を返します。元の`KeyframeManager`を変更せず、同じplugと`ModifierManager`を
共有するため、別のlayerや通常のノード操作とまとめて予約できます。
`AnimLayerNode`は対応Maya versionの`AnimLayer`を表す型です。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
node = nodes.existing.transform("ctrl")

# Correctionは既存layerで、ctrl.translateYが登録されている前提。
keyframe = node.translate.translateY.keyframe.anim_layer("Correction")
keyframe.set_keys([(1.0, 12.0), (24.0, 18.0)])
keyframe.set_tangent(frame=1.0, out_tangent_type="linear")
mod.do_it_dg()

keys = keyframe.get_keys()
data = keyframe.get_curve_data()
```

文字列で指定するlayerはsceneに存在する必要があります。空の名前、存在しない名前、
animation layer以外のnode名は`ValueError`、文字列・`AnimLayer`以外は`TypeError`です。
属性名やwildcardを含む指定も`ValueError`です。
`nodes.create.animLayer()`の戻り値は作成待ちでも渡せます。名前を先に検索せず、
作成・登録・キー設定を同じModifierManagerへ順に予約してください。
実行前のqueryは`RuntimeError`で、作成や登録を暗黙に実行しません。
layerは名前だけでなくノード同一性を保持し、取得後・予約後の改名にも追従します。
削除後に同名のlayerを作成しても対象は差し替わらず、query・実行時にエラーになります。
属性の所属確認・対象照会・キー設定では、別のDAG階層にある同名node、alias、配列の
logical indexを区別します。

root以外では、元の属性が指定layerに登録済みであることをquery・実行時に検査します。
未登録なら`RuntimeError`です。rootには通常のlayer未所属属性も指定できます。
ベースを扱うだけならlayer指定は不要です。明示する場合は、rootの現在の名前を指定してください。
`anim_layer()`自体はlayerの作成、属性の自動登録、選択中のlayerやbest layerへの自動切替を行いません。
作成・登録には次節の`nodes.create.animLayer()`と`add_plugs()` / `add_nodes()`を使用します。

| 操作 | 指定layerでの意味 |
| --- | --- |
| `set_key()` / `set_keys()` | 元のplugとlayerをMayaの`setKeyframe`へ明示。plugに指定した値から、layerに保存する値をMayaが解決し、必要なら最初のカーブを作成 |
| キー・時刻・値の取得、挿入・接線変更・削除 | 指定layerのカーブだけを取得・編集。別layer・別軸・weightは対象外 |
| 詳細データ・weighted操作 | 指定layerの生カーブを取得・復元。型・単位・境界補完の契約は通常の詳細データAPIと共通 |
| `find_anim_curves()` | 元のplugのDG依存関係を調査。指定layerでは絞り込まず、通常の入口と同じ候補を返す |

キー設定の指定値と、カーブ自身に保存される値は異なる場合があります。
たとえばbase値が1の加算layerで`set_key(12.0, frame=1.0)`を実行すると、
layer側には11が保存される場合があります。`get_keys()`や`get_curve_data()`はこの11を
取得し、`set_key_data()` / `set_curve_data()`は生の値をそのまま復元します。
合成後のplug値が必要な場合は、元のplugの`sample_values()`を使用してください。
複数node・属性をまとめて合成保存したり、layer構造を含めて保存する場合は
[`bdu.AnimationClip`](animation_clip.md)を使用します。詳細データAPIはenumのTUカーブも扱えます。
保存データにはlayer名やlayer構造を含めず、移植先は復元先の入口で決めます。
layer未指定ならベース、別layerへ移植するなら`anim_layer()`を指定します。

登録済み属性でもカーブ未作成なら、`has_anim_curve()`は`False`、キー列は空、
`get_curve_data()` / `get_weighted()`は`None`です。最後のキーを削除して空になった
カーブは引き続き選択し、`has_anim_curve()`は`True`になります。
`set_key_data()` / `set_curve_data()`は、登録済み属性の対象カーブがなければ作成して復元します。
layer未指定ならベース、`anim_layer()`を指定すればそのlayerへ作成します。
事前の`set_key()`は不要で、内部の作成用キーも残りません。
layer作成・属性登録・詳細データ復元を、同じ`do_it_dg()`へ順に予約できます。

queryは保留中modifierを実行せず、lock / reference / mute / weightを理由に読み取りを
制限しません。変更時は指定layerと元のplug・node・対象curveのlock / reference等を
事前検査します。Mayaの明示キー設定がlayer lockを無視する場合も、API側で拒否します。
muteやweightが0でも生カーブは編集対象になり、最終評価への反映はMayaのlayer状態に従います。
予約後の所属変更も初回実行時に再検査し、Undo / Redo・途中失敗時rollbackは通常操作と共通です。

### アニメーションレイヤーの作成と登録

`nodes.create.animLayer(name=None, override=False)`は、sceneのベース（root）の直下へ
layerの作成を予約し、通常の`AnimLayer`を返します。既定は加算layer、`override=True`は
上書きlayerです。rootがなければベースも同じbatchで作成します。既存rootは現在の名前で
解決し、同じbatchで複数layerを作る場合も共有します。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
ctrl = nodes.existing.transform("ctrl")
other = nodes.existing.transform("other_ctrl")

layer = nodes.create.animLayer(name="Correction")
layer.add_plugs([ctrl.translate, ctrl.rotate])
layer.add_nodes([other])
layer.weight.set(0.5)

keyframe = ctrl.tx.keyframe.anim_layer(layer)
keyframe.set_keys([(1.0, 12.0), (24.0, 18.0)])
mod.do_it_dg()
```

| API | 入力と登録範囲 |
| --- | --- |
| `add_plugs(plugs) -> None` | `PlugOperator`・`MPlug`・プラグ名のiterable。指定したプラグを登録。非keyableも指定可能 |
| `add_nodes(nodes) -> None` | `NodeOperator`・`MObject`・ノード名のiterable。ノード自身のkeyable・未lock・書込み可能な対応プラグを初回実行時に列挙 |

単一対象でも`[ctrl.tx]` / `[ctrl]`のように列で渡します。compoundはleafへ展開し、
配列親は実行時の既存要素だけを展開します。配列の一部だけなら`ctrl.samples[3]`を指定します。
空の配列から新しい要素を作らず、重複指定・既存所属は二重登録しません。空入力は何もしません。

対応型はbool・short・long（int）・float・double、angle・linear・time、enumです。
byte / char、message、matrix、typed dataなどは対象外です。`add_nodes()`はこれらと
非keyable・lockされたプラグを除外し、dynamic属性も含む対応プラグだけを登録します。
子孫DAGノードやshapeは自動で含めません。必要ならそれぞれを明示してください。
登録できる型と、KeyframeManagerの詳細データで扱えるカーブ型の制約は別です。

`add_plugs()`は、未対応型やlockされたleafを1つでも含むとエラーです。両APIとも
lock・referenceされたノード、lockされたlayerへの書込みを拒否します。ベースは個別の
所属登録が不要なため、rootへの明示登録もエラーです。Mayaが登録を見送った場合も
成功扱いにせず、同じ実行batchを巻き戻します。

入力列は予約時にコピーし、ノード・属性の同一性を保持します。名前で渡した対象も
改名に追従します。削除・同名再作成されたノードや明示属性へは置き換わりません。
`add_nodes()`の属性列挙と、lock・keyable・所属の検査は実行時なので、先行予約の変更を反映します。
別ModifierManagerで作成した対象を渡す場合は、その作成を先に実行してください。
通常のDAG作成と同様に、作成待ちのtransformは先に`do_it_dag()`が必要です。

既存layerには`nodes.existing.animLayer("Correction")`で同じ登録APIを使用できます。
作成・登録は選択ノードや選択layer・preferredを変更しません。ノード作成と初期値には
MDGModifierを使用し、階層接続・所属とblend nodeの構築はMayaの`animLayer`へ委譲します。
その変更もModifierManagerとMPxCommandのUndo / Redo・失敗時rollbackへ参加します。
[Autodesk animLayer](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/animLayer.html)

### カーブを明示して操作する

`nodes.existing.animCurveTA(...)` / `animCurveTL(...)` / `animCurveTU(...)`の
`.keyframe`は、そのノード自身を対象にした`CurveKeyframeManager`を返します。
`nodes.create`でも同じ入口を使用でき、ノード作成とキー編集をまとめて予約できます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

curve = nodes.existing.animCurveTL("walk_tx")
data = curve.keyframe.get_curve_data(start_frame=1, end_frame=24)
copy = nodes.create.animCurveTL(name="walk_tx_copy")
copy.keyframe.set_curve_data(data)
copy.keyframe.set_key(12.0, frame=10.0)
mod.do_it_dg()
```

`CurveKeyframeManager`は`bd_util.maya.node.operator.attr`からもimportできます。
`CurveKeyframeManager(m_obj, modifier_manager=mod)`の`m_obj`はTA / TL / TUの
`MObject`です。queryだけならmanagerを省略できます。型の分からない名前は
`nodes.existing(name)`で実行時に具体ノードへ解決できます。
カーブ自身の入口は`curve.keyframe`です。`curve.output.keyframe`は出力属性を対象とする
従来の`KeyframeManager`なので、カーブ自身の編集には使いません。

| 項目 | 明示カーブの契約 |
| --- | --- |
| 対象 | 作成時に指定したノードそのもの。改名・出力の再接続でも対象は変わらず、同名の別ノードへ取り替えない |
| 時刻・値 | `frame`は呼出し時のUI時間単位で表したカーブ自身の入力時刻。TAはdegree、TLはcm、TUはunitless |
| 接続 | 出力先なし、共有出力、中間ノードへの出力、`input`の時間接続、message接続を許可 |
| 非対応 | TT、unitless入力のdriven key、TAの独立scalar以外の補間、`input`・message以外の入力接続 |
| 取得 | `get_keys()` / `frames()` / `values()`等。空カーブは空list、`get_curve_data()`は空の場合も`AnimCurveData`、`get_weighted()`は`bool` |
| 編集 | `set_key()` / `set_keys()`、挿入、接線変更、キー削除、weighted変更、詳細データ復元を同じmanagerへ予約 |
| 詳細データ | 属性経由と同じschema 2、境界補完、公開単位、予約時の再検証・独立コピーを使用。復元先の型は一致が必要 |
| 削除済み・作成待ち | queryは`RuntimeError`。保留中modifierを実行しない。作成待ちノードへの編集予約は可能で、実行時に存在を検査 |

`set_key()` / `set_keys()`はカーブ自身の値を`MFnAnimCurve`で設定します。
同時刻は入力順で上書きし、`step` / `stepnext`の指定は出力接線だけを受け付けます。
時間入力が別のノードで変換されていても、scene時刻からの逆算は行いません。
たとえばsceneの10フレーム時にカーブへ20フレーム相当の時間が入る構成では、
`set_key(value, frame=20)`がその入力位置を編集します。

共有カーブを編集すると全出力先へ反映されます。編集時はカーブノードとその属性の
lock / reference、所属animation layerのlock / referenceを検査します。
出力先の属性lockはカーブ自身の値を固定するものではないため、キー編集を制限しません。
無関係なlayerの存在やlockも操作を制限しません。
レイヤー内の生カーブを指定することはできますが、layer選択・合成後の値解決は行いません。
たとえばbase値1に加算されるカーブへ20を設定すると、合成値は21になります。

`set_curve_data()`は既存ノードの全キー・weighted・infinityを置換し、接続は維持します。
`set_key_data()`は作成待ちを含め指定ノードのweightedとinfinityを維持します。
属性経由で未接続時に自動作成する場合のnonweighted規則とは、ノード作成の責務が異なります。

`delete_anim_curve()`は共有先を含めカーブノード全体を削除します。
削除では入力・出力・messageの全接続端についてlock / referenceを事前検査し、
全接続を切断・反映してからノードを削除します。接続先を連鎖して削除せず、
Undoで同じノードと全接続を復元します。ロックされた接続先があれば切断前に拒否します。
最後のキーだけを削除した場合は空のカーブを残します。

queryは実行済みsceneだけを参照し、編集条件は初回実行時に再検査します。
予約後の改名・接続変更・lock変更・削除を考慮し、Redoでは初回の変更を再生します。
同じbatchで後続操作が失敗した場合は、先行するキー編集・接続変更・削除もrollbackします。

### 上流のカーブ候補を取得する

`node.attr.keyframe.find_anim_curves()`は、接続調査や独自のカーブ選択UIに使う補助APIです。
通常の取得・編集はチャンネルのカーブを自動解決するため、この探索は不要です。
指定scalar plugから上流のanimCurve候補を探索し、候補をノード名の昇順で並べ、
同じノードを1回だけ含むtupleで返します。
候補がなければ空tupleです。複数候補から編集対象を自動選択しません。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
node = nodes.existing.transform("ctrl")

curves = node.translate.translateX.keyframe.find_anim_curves(
    filter_type=nodes.types.AnimCurveTL,
)
print([curve.name for curve in curves])

# 列挙結果から、利用者が選んだカーブ名を指定する。
curve = next(curve for curve in curves if curve.name == "walk_tx")
curve.keyframe.set_key(12.0, frame=10.0)
mod.do_it_dg()
```

返却ノードは`nodes.existing`と同じ具体型で、元の`ModifierManager`を共有します。
`filter_type`には`nodes.types.AnimCurveTL`等の具体カーブクラスを渡します。
戻り値の型も絞られるので、TA / TL / TUでは`.keyframe`以下の補完を利用できます。
省略時は全8型が候補になり、`isinstance(curve, nodes.types.AnimCurveTL)`等でも型を
絞れます。TT / UA / UL / UT / UUは候補取得の対象ですが、カーブ自身の`.keyframe`は
未対応です。型filterは結果だけに作用し、不一致のカーブを通り越して探索しません。

探索はMayaのplug単位のDG依存関係に従い、unitConversion、計算ノード、constraint、
animation layerのblendをたどります。各経路で最初に到達したanimCurveの`output`を
候補にし、そこで停止します。カーブの時間driverやdriven keyのさらに上流へは進みません。
カーブの`output`自身を開始点にした場合は、そのカーブが候補になります。
message接続は探索しません。開始点はnumeric / unit / enumのscalar plugに限定し、
compound、未要素化array、typed属性は`TypeError`です。

候補は「Mayaが宣言した依存関係にあるカーブ」です。現在値への寄与、対象軸との一致、
編集可否を保証するものではありません。たとえば`multiplyDivide.outputX`からは別軸の
入力カーブも含まれ、layerのweightやmuteされたlayerのカーブも候補になります。
world-space属性の依存関係も有効にしていますが、DAG親子階層を独自にさかのぼる探索は
行いません。custom nodeもMayaへ宣言した依存関係の範囲で探索します。
この探索の基礎は[AutodeskのMItDependencyGraph](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/py_ref/class_open_maya_1_1_m_it_dependency_graph.html)です。

未接続の出力属性ではMayaのiteratorが内部入力を列挙しないため、開始属性に対して
`getAffectingAttributes()`で得た入力も探索開始点に加えます。arrayは既存indexだけを
使用し、照会のための要素作成、値の評価、仮接続は行いません。

queryは実行済みsceneだけを読み、保留中modifierを実行しません。開始nodeが作成待ち・
削除済みなら`RuntimeError`です。lock / referenceや未対応補間でも候補から除外せず、
取得・編集時に明示カーブ操作の制約を検査します。取得済み候補は、その後の改名・再接続で
別ノードへ変わりません。最新の接続構成の候補が必要なら再度探索してください。
低水準の`KeyframeManager(plug)`でmanagerを省略した場合は、1回の探索で返す全候補に
新しい共通managerを渡します。編集後は`curve.modifier_manager.do_it_dg()`で実行できます。

この候補列には別軸やweightも含むため、先頭の候補を通常操作の対象としては使いません。
`anim_layer()`で取得した入口でも、候補を指定layerだけに絞り込みません。
探索したカーブの`.keyframe`へ渡す値は
カーブ自身の生の値です。layer名による選択、layerの新規作成、合成後のplug値からの逆算は
このAPIでは行いません。

### キーの挿入・編集・削除

以下の対象なしの挙動は、属性経由の`KeyframeManager`についての説明です。

| method | 実行時の処理 | 対象がない場合 |
| --- | --- | --- |
| `insert_key(frame, breakdown=False)` | 前後のカーブ形状を保ってキーを挿入 | カーブがなければ`RuntimeError` |
| `set_tangent(frame, ...)` | 指定した側のtangent typeを変更 | カーブ・キーがなければ何もしない |
| `delete_key(frame)` | 指定時刻のキーを削除 | カーブ・キーがなければ何もしない |
| `delete_keys(start_frame=None, end_frame=None)` | 指定範囲のキーを削除 | カーブ・該当キーがなければ何もしない |
| `delete_anim_curve()` | カーブノード全体を削除 | カーブがなければ何もしない |

`delete_keys()`の境界は両端を含み、`None`を指定した側には境界を設けません。
両方省略すると全キーを削除します。キー削除には`MFnAnimCurve.remove()`を使用し、
最後のキーを削除しても空のカーブは残します。

挿入・tangent変更・キー削除は、`MAnimCurveChange`へ変更を記録します。
カーブノードの削除も同じmanagerの履歴へ含め、Undoでキー・tangent・接続を復元します。
`delete_anim_curve()`は、このplugとの接続だけを切る操作ではありません。
同じカーブを共有する別のplugがある場合は、実行時に拒否してカーブと接続を維持します。
カーブの全出力接続を先に切断・反映してから、別の`MDGModifier`でカーブノードを
削除します。接続先ノードが連鎖して削除されることを避けるため、この2段階を
同じmanagerの実行境界内で順に処理します。

対象カーブとキーは実行時に解決するため、同じ`do_it_dg()`へ予約した設定・編集を
呼び出した順に反映できます。

```python
keyframe.set_key(0.0, frame=1.0)
keyframe.set_key(90.0, frame=24.0)
keyframe.insert_key(frame=12.0)
keyframe.set_tangent(frame=12.0, out_tangent_type="linear")
mod.do_it_dg()

frames = keyframe.frames()
```

これらの操作は上記のチャンネル選択の規則を共有します。constraint先の属性からドライバー側の
カーブを暗黙に編集することはありません。任意時刻のplug値は`sample_values()`で取得します。

### キーを時間方向へ移動する

時間方向の操作は`move_frame()` / `move_frames()` / `scale_frames()`、
値方向の操作は`set_value(s)` / `add_value(s)` / `scale_value(s)`で表します。
操作量は`offset`、倍率は`scale`、拡縮の基準は`pivot`に統一しています。
対象キーを選ぶ`frame` / `start_frame` / `end_frame`は、値方向の操作でも時刻なので名前を維持します。

`move_frame()` / `move_frames()`は、移動対象を位置引数、移動方法をkeyword引数で指定します。
戻り値は`None`で、同じModifierManagerへ予約します。値方向の移動や時間の拡大縮小は行いません。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
ctrl = nodes.existing.transform("ctrl")
keyframe = ctrl.tx.keyframe

keyframe.move_frames(10, 20, offset=15)
mod.do_it_dg()
```

| 用途 | 呼び出し例 |
| --- | --- |
| 単一キーを相対移動 | `move_frame(10, offset=15)` |
| 単一キーを絶対移動 | `move_frame(10, to=15)` |
| 範囲を相対移動 | `move_frames(10, 20, offset=15)` |
| 開始境界を20へ合わせる | `move_frames(10, 20, to_start=20)` |
| 終了境界を30へ合わせる | `move_frames(10, 20, to_end=30)` |
| 10以降を移動 | `move_frames(10, None, offset=15)` |
| 20以前を移動 | `move_frames(None, 20, offset=15)` |
| 全体を移動 | `move_frames(offset=-5)` |
| 最初のキーを0へ合わせる | `move_frames(to_start=0)` |

`move_frame(frame, *, offset=None, to=None, insert_missing=False)`は、
移動量または移動先のどちらか1つを必ず指定します。
`move_frames(start_frame=None, end_frame=None, *, offset=None, to_start=None,
to_end=None, interpolate_start=None, interpolate_end=None, interpolation="smoothstep",
insert_missing=False)`も、移動方法3種類のうち1つだけ指定します。
指定なし・複数指定、非有限数、逆転した範囲、bool以外の`insert_missing`は予約時に拒否します。
型・補完でも移動方法の排他指定を検査します。

範囲は両端を含み、`None`の側は無制限です。明示した境界は、その数値自体を
絶対移動の基準にします。例えば12～28の範囲に20のキーしかなくても、
`move_frames(12, 28, to_start=20)`は+8の移動なので、キーは28へ移ります。
基準側が`None`の場合は対象キーの最初・最後を基準にします。対象キーは初回実行時に
決定するため、同じbatchの先行キー設定や移動も反映します。

時刻と移動量は呼び出し時のUI時間単位で捕捉します。負の時刻・subframeを許可し、
整数フレームへ丸めません。予約後にFPSを変更しても物理的な時刻・移動量を維持します。
時刻の一致はMayaの時間精度に従います。指定するのはカーブ自身の入力時刻で、
接続された時間driverからscene時刻を逆算しません。
Mayaで表現できないほど大きな時刻・移動量は拒否し、移動先の計算が表現範囲を
超えた場合も、別の時刻へ折り返さず実行を失敗させてrollbackします。

移動先と同時刻の対象外キーは削除し、移動元の値・接線・lock・breakdownで置き換えます。
途中のキーは残し、移動対象同士が互いの元時刻へ移る場合は両方を移動します。
例えばキーが0・10・20・30にある場合、10→20なら元の20だけを置換し、
10→25なら20は残ります。0・10を+10した場合は元の20を置換し、0・10の両キーが
10・20へ移ります。キーindexは移動後に変わる場合があります。

既定の`insert_missing=False`は実在キーだけを移動します。`True`なら、単一移動では
元の指定時刻、範囲移動では明示した開始・終了時刻に欠けているキーを挿入してから移します。
両端が同時刻なら1キー、`None`側には追加しません。対象区間に実在キーがなくても、
空でないカーブがあれば境界を補えます。新しいキーはbreakdownではありません。
補間指定時は、後述する補間開始・終了の境界も補います。

```python
keyframe.move_frame(12, to=15, insert_missing=True)
keyframe.move_frames(40, 50, to_start=60, insert_missing=True)
mod.do_it_dg()
```

挿入はMayaの`insertKey()`でカーブ自身の補間・infinity評価に基づいて行い、
境界の値は両方とも挿入前のカーブから取得します。先の挿入による繰り返し周期の変化で、
後の境界値が変わることを防ぎます。隣接接線が調整される場合があります。
これは詳細データの範囲切り出しとは別で、
区間全体の接線を一律fixed化する処理や、繰り返し領域のベイクは行いません。
挿入後の接線情報を移動し、auto・linear等は新しい前後関係に応じて再計算されます。
部分移動では対象外の隣接区間も形状が変わり得ます。fixed接線の方向・重み、
既存キーの接線type・lock・breakdown、カーブのweighted・infinity設定は維持します。
時間値カーブ（TT）の再挿入で短いweighted接線をMayaが再現できない場合は、
接線を変更したまま成功させず、操作を失敗させてrollbackします。

カーブなし・空カーブ・対象キーなしは何も変更しません。カーブを新規作成せず、
移動量0（同じ時刻への絶対移動を含む）では境界挿入も行いません。
これらのno-opでも通常のmanager・対象構成・lock / reference検査は適用します。
対象選択は他の編集と共通で、属性経由はベースまたは`anim_layer()`の指定先、
明示カーブはそのノード自身です。属性経由のTA / TL / TU / TTとbool・enum等も扱えます。
明示カーブの入口は引き続きTA / TL / TUです。

内部では順序を維持できる移動に`setInput()`を使い、上書き・飛び越しでは必要なキーだけを
削除・再挿入します。公開の詳細データAPIや全カーブ置換は経由しません。
挿入・削除・移動・接線復元を1つの`MAnimCurveChange`へ記録し、Undo / Redoでは
上書きされたキーも復元します。途中失敗時は同じ実行batchの先行変更もrollbackします。
queryは保留中modifierを実行せず、Redoは初回に記録した対象への変更を再生します。

#### 移動量を範囲の外側へならす

`move_frames()`には、値編集と同じ`interpolate_start` / `interpolate_end` /
`interpolation`を指定できます。単一の`move_frame()`には追加していません。

```python
keyframe.move_frames(
    20, 30,
    offset=5,
    interpolate_start=10,
    interpolate_end=40,
    interpolation="smoothstep",
)
mod.do_it_dg()
```

移動前の各キーの時刻から影響度`w`を求め、`元の時刻 + 移動量 * w`へ移します。
上の例では10〜20で0から1、20〜30で1、30〜40で1から0になります。
既定の`smoothstep`は`u * u * (3 - 2 * u)`、`linear`は区間内の位置`u`を使います。
移動後の時刻からウェイトを計算し直すことはありません。

| 元の時刻 | 影響度 | 移動後の時刻 |
| --- | --- | --- |
| 10 | 0 | 10 |
| 15 | 0.5 | 17.5 |
| 20 | 1 | 25 |
| 30 | 1 | 35 |
| 35 | 0.5 | 37.5 |
| 40 | 0 | 40 |

表の時刻にキーがある場合の例です。片側だけの補間も可能で、指定した側には
対応する元範囲の明示境界が必要です。`interpolate_start < start_frame`、
`end_frame < interpolate_end`を満たすように指定します。補間区間の幅0・逆転・非有限数、
補間境界へのbool・文字列、不正な補間方式は予約時に拒否します。
補間引数を省略した側と`None`の範囲境界は、従来の範囲指定に従います。
補間境界の単位も予約時のUI時間単位で捕捉します。

`to_start` / `to_end`は、補間区間を含める前の元範囲から移動量を求め、
各キーに同じ規則で重み付けします。明示境界を基準にする既存の仕様は変わりません。
元範囲にキーがなくても、移動量を確定できれば補間区間の既存キーを移動できます。
絶対移動の基準側が`None`で元範囲にキーがない場合は何も変更せず、
補間区間のキーを基準の代わりには使いません。

**補間範囲内の対象キー同士の衝突・順序逆転はエラー**にし、同じbatchの先行変更も
rollbackします。影響度0の端点キーもこの検査に含めます。
例えば上の例の移動量を+15にすると、30のキーが45へ進み、40で止まるキーを追い越すため拒否します。
補間範囲外の対象外キーとの衝突は、従来どおり移動キーで上書きします。
対象外キーの追い越しも従来どおり許可し、途中の非衝突キーは残します。

検査するのは実在キーと明示的に補ったキーです。補間境界にキーがない場合、
その時刻を動かない仮キーとしては扱いません。境界を固定点として検査したい場合は
`insert_missing=True`を指定します。これにより元の開始・終了に加えて補間開始・終了の
最大4境界を補います。全境界の値は挿入前に取得し、同時刻は1回だけ補います。
`insert_missing=False`が既定で、自動サンプリングはしません。移動量0は挿入もしません。

値・手動接線・lock・breakdown・カーブ設定を維持し、イーズの形へ作り直すための
追加接線調整はしません。影響度0の既存キーは移動・再挿入しません。
境界挿入による隣接接線の調整とauto等の再計算はMayaに従います。
キー間隔が変わるため、補間方式は移動量の配分を指定するものであり、曲線の形状や速度の連続性を
保証しません。補間範囲外でも隣接区間の評価値が変わる場合があります。
対象resolver・lock / reference検査・queryの非実行・Undo / Redoは通常の移動と共通です。

### キーを時間方向へ拡縮する

`scale_frames(start_frame=None, end_frame=None, *, scale=None, duration=None,
offset=None, to_start=None, to_end=None, pivot=None, mode="replace_range",
interpolate_start=None, interpolate_end=None, interpolation="smoothstep",
insert_missing=False)`は、既存カーブのキーを時間方向に拡縮します。
戻り値は`None`で、同じModifierManagerへ予約します。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
ctrl = nodes.existing.transform("ctrl")

# 10〜30の動きを100〜140へ収め、配置先区間の既存キーを置き換える
ctrl.tx.keyframe.scale_frames(10, 30, to_start=100, to_end=140)
mod.do_it_dg()
```

| 用途 | 呼び出し例 | 変換後の基準区間 |
| --- | --- | --- |
| 開始位置を固定して2倍 | `scale_frames(10, 30, scale=2)` | 10〜50 |
| 20を固定して2倍 | `scale_frames(10, 30, scale=2, pivot=20)` | 0〜40 |
| 20を固定して10フレームの長さへ | `scale_frames(10, 30, duration=10, pivot=20)` | 15〜25 |
| 15フレームの長さへ | `scale_frames(10, 30, duration=15)` | 10〜25 |
| 開始と終了を指定 | `scale_frames(10, 30, to_start=100, to_end=140)` | 100〜140 |
| 2倍にして終了を固定 | `scale_frames(10, 30, scale=2, to_end=30)` | -10〜30 |
| 2倍にして開始を指定 | `scale_frames(10, 30, scale=2, to_start=100)` | 100〜140 |
| 拡縮して相対移動 | `scale_frames(10, 30, duration=10, offset=5)` | 15〜25 |
| 全体を半分の長さへ | `scale_frames(scale=0.5)` | 最初のキーを固定 |
| 10以降を2倍 | `scale_frames(10, None, scale=2)` | 10を固定 |
| 30以前を2倍 | `scale_frames(None, 30, scale=2)` | 対象の最初のキーを固定 |

拡縮方法は、正の`scale`、正の`duration`、移動先の両端指定のいずれか1つです。
長さは終了と開始の差で、10〜30は20フレームと数えます。倍率・長さには配置方法を1つ
組み合わせられます。`offset`と移動先境界の併用、倍率と長さの併用、
両端指定と倍率・長さの併用は拒否します。配置だけを指定する場合は`move_frames()`を使います。
ピボットと配置を省略すると基準区間の開始を固定します。逆再生・倍率0・区間の0幅への圧縮は扱いません。

範囲は両端を含みます。明示した境界はキーの有無にかかわらず元区間の境界として扱い、`None`側は
対象キーの最初・最後を使います。例えば10・30にはキーがなく、15・25にキーがある場合、
`scale_frames(10, 30, scale=2)`は基準区間を10〜50へ変換し、実在キーを20・40へ移します。
10を固定して、その時刻からの距離を2倍にする計算です。キーを境界へ寄せる操作ではありません。

`pivot`には、拡縮で固定する基準時刻を指定できます。元時刻を`t`、倍率を`s`、
ピボットを`p`とすると、変換後は`p + (t - p) * s`です。例えば10・20・30のキーへ
`scale=2, pivot=20`を指定すると、0・20・40へ移ります。
`duration`とも併用でき、元区間の長さから倍率を求めて同じ変換を使います。
`offset`は拡縮した後に加えるため、併用時はピボット位置もその量だけ移動します。

```python
# 20を中心に2倍へ広げてから、全体を5フレーム移動する
ctrl.tx.keyframe.scale_frames(10, 30, scale=2, pivot=20, offset=5)
mod.do_it_dg()
```

ピボットは区間外・負の時刻・subframeも指定でき、そこにキーがある必要はありません。
`insert_missing=True`でも、ピボット指定だけを理由にキーを追加しません。
`pivot=None`は従来どおりの配置規則を使います。
ピボットを明示した場合、`to_start` / `to_end`との併用は予約時に拒否します。
配置先の境界を合わせる指定では最終的な変換がそこで決まり、ピボット指定の効果がなくなるためです。
ピボットの時間単位も予約時に捕捉し、bool・文字列・非有限数・表現範囲外の時刻を拒否します。

既定の`insert_missing=False`は実在キーだけを拡縮します。`True`なら、既存の空でない
カーブに対して、明示した元の境界を補ってから拡縮します。15・25に実在キーがあり、
10〜30を開始固定で2倍にする例では、境界を補うと10・20・40・50にキーが配置されます。
`None`側には挿入しません。区間内に実在キーがなくても補完できます。
両方の境界値は挿入前に評価し、Mayaの`insertKey()`を使用します。挿入による隣接接線の
調整を含めて拡縮します。繰り返し領域のベイクや全接線のfixed化は行いません。

| mode | 配置先の既存キー |
| --- | --- |
| `replace_range`（既定、部分置き換え） | 変換後の基準区間内を両端込みで置き換える |
| `merge` | 変換後のキーと同時刻の既存キーだけを上書きし、他は残す |

部分置き換えの範囲は実在キーの端ではなく、変換後の基準区間全体です。ピボットや相対移動も反映します。
10〜30を開始固定で2倍にする例では、
キーが20・40にしかなくても、10〜50にある対象外キーを削除します。
どちらのmodeでも元キーは移動し、コピーとして残しません。全対象キーを確保してから
削除・再配置するため、元区間と配置先が重なっても対象キーを失いません。
それ以外のキーを押し出したり、全カーブを置換したりはしません。

キーの値・接線の種類・lock・breakdown、カーブのweighted・infinity設定を維持し、
接線のXも同じ倍率で変換します。auto等はMayaが再計算するため、部分拡縮では
対象外の隣接区間も形状が変わり得ます。対象外キーの保持は、区間外の評価値の不変を
保証するものではありません。旧来の`fast` / `slow`は全体拡縮でもMaya標準の固定された
傾きへ再計算されるため、幾何学的な形状の拡縮とは異なります。

属性経由はTA / TL / TU / TT、明示カーブはTA / TL / TUに対応します。
TA / TL / TUは`addKeysWithTangents()`で短いweighted接線をそのまま復元します。
TTは角度・重みのAPIを使い、Mayaの下限補正等によりweightedのfixed接線を再現できない
場合はエラーにしてrollbackします。極端な圧縮や、元から重み0のfixed接線等が該当します。
未指定はベース、別layerは`anim_layer()`で明示します。layerのweight等の設定や他layerは
自動拡縮しません。時間driverが接続されていても、引数はカーブ自身の入力時刻です。

対象とキーは初回実行時に解決し、同じbatchの先行キー編集を反映します。
フレーム引数は予約時のUI時間単位で捕捉し、予約後のFPS変更でも秒単位の配置・長さを維持します。
負の時刻・subframeを許可し、整数に丸めません。非有限数・bool・文字列は数値指定として拒否します。
表現範囲外の時刻や、精度限界でキー・区間が重なる拡縮はエラーにします。

カーブなし・空カーブ・対象キーなしは、境界補完を行う場合を除き何も変更しません。
カーブは新規作成せず、恒等変換（倍率1で配置も同じ）では境界挿入も行いません。
元の基準区間が0幅なら長さ・両端指定を拒否します。正の倍率は許可し、
単一キーでも接線を拡縮します。引数だけで判定できる不正は予約前、対象キーに依存する不正は
初回実行時に拒否します。no-opでもmanager・対象構成・lock / reference検査を適用します。
queryは保留中の編集を実行しません。Undo / Redoでは置換されたキーも含めて復元し、
途中失敗時は同じbatchの先行編集もrollbackします。

#### 時間拡縮の影響を前後へならす

`scale_frames()`も`move_frames()`・値編集と同じ`interpolate_start` / `interpolate_end`を受け取ります。
補間区間の既存キーまで対象を広げ、元時刻から計算した影響度`w`で拡縮を弱めます。
主区間は影響度1、補間開始・終了は0です。片側指定もでき、補間する側には
明示した主区間の境界が必要です。`interpolate_start < start_frame`、
`end_frame < interpolate_end`を満たす必要があります。
方式は`linear`と、既定の`smoothstep`（`u * u * (3 - 2 * u)`）です。

```python
keys = ctrl.tx.keyframe
keys.scale_frames(
    20, 30,
    scale=1.5,
    interpolate_start=10,
    interpolate_end=50,
    interpolation="smoothstep",
)
mod.do_it_dg()
```

表の時刻にキーがある場合、次のように変わります。キーの値は維持します。

| 元時刻 | 影響度 | 変換後の時刻 |
| --- | --- | --- |
| 10 | 0 | 10 |
| 15 | 0.5 | 13.75 |
| 20 | 1 | 20 |
| 25 | 1 | 27.5 |
| 30 | 1 | 35 |
| 40 | 0.5 | 45 |
| 50 | 0 | 50 |

最初に、補間区間を含めず主区間だけから通常の時間変換`F(t)`と倍率`s`を決めます。
各キーの変換は`new_time = t + (F(t) - t) * w`です。
`pivot`があれば`F(t)`にピボットを反映し、`offset`も含めた変化量へ影響度を掛けます。
部分置き換えはピボットを考慮した主区間の配置先だけで、補間範囲までは広げません。
倍率・長さ・両端合わせと、相対配置・開始/終了合わせのすべてで同じ計算を使います。
`None`側の基準は主区間の実在キー（境界補完指定時は補った主境界も含む）から求めます。
主区間にキーがなくても両端が明示されていれば補間キーを編集できます。
省略した基準を主区間から決められない場合は何もせず、補間キーを代わりに使いません。

接線Xはキーごとの実効倍率`1 + w * (s - 1)`で変換し、Y・値・種類・lock・breakdownを保持します。
影響度0のキーは時刻・接線を編集せず、削除・再挿入もしません。時刻が動かない主区間の
ピボットキーでも、実効倍率が1以外なら接線を拡縮します。auto等のMayaによる再計算は通常どおりです。
これはキーごとの重み付けで、連続した時間変換の微分による接線変換ではありません。
イーズを再現するための追加キーや接線調整は行わず、補間区間の曲線形状・速度の連続性は保証しません。

`replace_range`の置換範囲は、**通常の時間変換で求めた主区間の配置先**だけです。
補間区間や移動した全キーの端までは広げません。置換範囲内でも、今回の対象である補間キーや
影響度0の端点は保持します。補間キーの移動先が置換範囲外にある対象外キーと同時刻になった場合も、
その対象外キーは上書きします。`merge`は同時刻だけを上書きし、それ以外の対象外キーを残します。

影響度0の端点を含む**対象キー同士の衝突・順序逆転はエラー**にして、同じbatch全体をrollbackします。
検査するのは実在キーと明示挿入したキーだけです。欠けた補間端点を仮キーとしては扱わず、
キー間の連続関数の単調性も検査しません。対象外キーの追い越しは許可します。

`insert_missing=False`が既定です。`True`なら主区間と補間区間の最大4つの明示境界だけを補い、
値はすべて挿入前のカーブから評価します。同じ境界は一度だけ挿入し、自動サンプリングはしません。
恒等変換や影響度0のキーしかない場合は何もしません。境界補完による隣接接線の変更は通常どおりです。
負の時刻・subframe・予約時の時間単位捕捉・Undo / Redo・lock / reference検査も通常の拡縮と共通です。
不正な補間境界、数値以外、非有限数、不正な補間方式は予約時に拒否します。

### キーの値を編集する

`set_value()` / `add_value()` / `scale_value()`は単一時刻、複数形の
`set_values()` / `add_values()` / `scale_values()`は両端を含む範囲の既存キーを編集します。
対象時刻は位置引数、値の操作はkeyword引数で指定します。戻り値はすべて`None`で、
同じModifierManagerへ予約します。キーの時刻は変わりません。

| 操作 | 単一キー | 範囲内のキー |
| --- | --- | --- |
| 同じ値へ設定 | `set_value(10, value=5)` | `set_values(10, 30, value=5)` |
| 値を加算 | `add_value(10, offset=5)` | `add_values(10, 30, offset=5)` |
| 値を拡縮 | `scale_value(10, scale=2, pivot=1)` | `scale_values(10, 30, scale=2, pivot=1)` |

複数形の`start_frame=None, end_frame=None`は、`None`側を無制限とします。
両方省略すればカーブ全体、`add_values(10, None, offset=5)`なら10以降、
`add_values(None, 30, offset=5)`なら30以前です。開始と終了が同じでも使えます。
`set_values()`の`value`は全対象キーへ設定する1つの数値です。時刻ごとに異なる値を
渡す場合やカーブを新規作成する場合は、従来の`set_key()` / `set_keys()`を使います。

拡縮は`pivot + (元の値 - pivot) * scale`です。`pivot`の既定は0で、
倍率0はピボット値へまとめ、負の倍率はピボットを中心に反転します。

値・加算量・ピボットは**対象カーブ自身の生値**です。角度はdegree、距離はcm、
単位なしはその数値、時間値は予約時のUI時間単位です。表示単位を変更しても
角度・距離の指定単位は変わりません。`set_key()` / `set_keys()`のような
レイヤー合成結果からの逆算は行わず、別レイヤーのweightやキーも変更しません。
属性経由はTA / TL / TU / TT、明示カーブはTA / TL / TUに対応します。
bool・enum・整数属性でもカーブ上の数値を計算し、整数丸め・clampは行いません。
接続先属性で評価される値は、その属性型の変換に従います。

対象選択は既存の編集と共通です。レイヤー未指定はsceneのベース（root）、
別レイヤーは`anim_layer()`で明示します。明示カーブはそのノード自身を編集します。
対象とキーは初回実行時に解決するため、同じbatchの先行編集も反映します。

#### 範囲の外側へ影響をならす

複数形の3メソッドには、`interpolate_start=None` / `interpolate_end=None` /
`interpolation="smoothstep"`を指定できます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
keys = nodes.existing.transform("ctrl").tx.keyframe

keys.add_values(
    20, 30,
    offset=5,
    interpolate_start=10,
    interpolate_end=40,
)
mod.do_it_dg()
```

この例では10〜20にあるキーの影響度を0から1へ増やし、20〜30は1、30〜40は1から0へ
減らします。10・40の影響度は0で、それより外側のキーは編集しません。
片側だけの補間指定もできます。補間を指定する側には対応する開始・終了の明示が必要で、
`interpolate_start < start_frame <= end_frame < interpolate_end`を満たすように指定します。
`None`側の大小関係は検査対象外です。補間幅0は拒否し、その側の補間引数を省略します。

`linear`は区間内の位置`u`をそのまま、既定の`smoothstep`は`u * u * (3 - 2 * u)`を
影響度`w`に使います。これは既存キーごとの影響度であり、キー間の曲線を
そのイーズの形へ作り直す指定ではありません。キーが少ない場合、補間方式を変えても
結果が同じになることがあります。自動サンプリングや、補間を再現するための接線調整は行いません。

| 操作 | 影響度を含む計算 |
| --- | --- |
| set | `(1 - w) * 元の値 + w * value` |
| add | `元の値 + w * offset` |
| scale | `pivot + (元の値 - pivot) * 実効倍率`。実効倍率は`1 + w * (scale - 1)` |

#### 接線と境界挿入

`set`・`add`は手動接線を維持します。すべてのキーを同じ値へ設定しても、手動接線の
傾きがある場合はキー間が平坦になるとは限りません。
`scale`は各キーの実効倍率で接線Yを拡縮します。weighted接線は変換後の長さを保持し、
nonweighted接線は変換後の方向を保って正規化します。影響度0のキーには適用しません。
接線type・tangent lock・weight lock・breakdown、カーブのweighted・infinity設定は維持します。
auto・linear等の接線はMayaが再計算するため、部分編集では隣接区間の形状も変わり得ます。
旧来の`fast` / `slow`もMaya標準の再計算に従います。

6メソッド共通の`insert_missing=False`が既定です。`True`なら、既存の空でないカーブに対し、
単一メソッドは指定時刻、複数メソッドは明示した開始・終了・補間開始・補間終了の
最大4境界に欠けているキーを補います。同じ時刻は1回だけ、`None`側には挿入しません。
補間端点の影響度0のキーも、明示した境界として補います。
すべての境界値を挿入前のカーブから評価し、Mayaの`insertKey()`で挿入します。
挿入時には隣接接線が調整される場合があり、その結果を基に値編集を行います。
区間内に実在キーがなくても境界を補えますが、カーブなし・空カーブでは新規作成しません。

加算量0・倍率1は、`insert_missing=True`でも境界挿入を行いません。
同じ値への`set`は既存キーを変更しませんが、明示した境界の挿入は行います。
負の時刻・subframeを許可し、時刻と時間値の単位は予約時に捕捉します。
フレーム引数はカーブ自身の入力時刻で、時間driverからの逆算は行いません。
数値引数のbool・文字列・非有限数、逆転範囲、不正な補間指定は予約前に拒否します。
Mayaの表現範囲外の時刻・時間値、計算結果のoverflowはエラーにしてrollbackします。
TTのweighted fixed接線がMayaの下限補正等で再現できない拡縮もrollbackします。

no-opを含め既存のmanager・対象構成・lock / reference検査を適用します。
queryは予約を暗黙に実行しません。Undo / Redoは値・接線・挿入キーをまとめて復元し、
途中失敗時は同じbatchの先行編集もrollbackします。

### 手動接線を維持してキーを削減する

`reduce_keys(start_frame=None, end_frame=None, *, tolerance, preserve_breakdowns=True)`は、
元カーブとの値の誤差を指定して、不要なキーの削除を予約します。戻り値は`None`です。
属性・`anim_layer()`・明示カーブで同じ操作を使用します。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
ctrl = nodes.existing.transform("ctrl")

ctrl.tx.keyframe.reduce_keys(10, 100, tolerance=0.01)
ctrl.rz.keyframe.reduce_keys(tolerance=0.1)
mod.do_it_dg()
```

上の例はtranslateXの10～100フレームを0.01 cm、rotateZの全体を0.1 degreeの
許容誤差で削減します。`tolerance`は必須の非負・有限数で、TAはdegree、TLはcm、
TUはunitlessです。sceneの表示単位に依存せず、時間のずれや回転姿勢・ワールド座標での
距離を意味しません。layerでは、そのlayer自身の生カーブ値を比較します。

範囲は両端包含です。`None`側は無制限で、明示した境界にキーを挿入することはありません。
指定範囲に実在する最初・最後のキーを必ず残し、削減対象が3キー未満なら何もしません。
対象カーブなし・空カーブでも新規作成しません。負の時刻・subframeに対応し、
範囲は呼び出し時のUI時間単位で捕捉します。対象とキーは初回実行時に解決するため、
同じbatchで先に予約したキー設定も削減できます。queryは保留中の処理を実行しません。

保持する情報と変更の範囲です。

- 残すキーの時刻・値・接線type・tangent / weight lock・breakdownを保持します。
  手動のfixed接線は方向・重みも維持し、削減のための接線再設定を行いません。
  auto・linear等の接線はMayaが前後のキーから再計算し、その結果も誤差判定に含めます。
- `preserve_breakdowns=True`ではbreakdownを削除候補から除外します。
  `False`を明示すればbreakdownも候補にできますが、範囲内の両端キーは残します。
- step / stepnextの値が切り替わる区間は両側のキーを保護します。
  値が同じstep区間では、形状を保てる中間キーを削除できます。
- 最初～最後の実在キー間では指定範囲外の形状を維持し、linear infinityの外挿傾きも保持します。
  カーブのweighted・infinity設定や、接続・レイヤーの選択状態は変更しません。
  cycle / cycleRelative / oscillateでは、範囲内の形状変更が他の周期にも反映されます。

誤差は削減途中のカーブではなく、初回実行時の元カーブと常に比較します。
キー時刻とキー間の両方を扱い、キー値が同じでも途中に膨らみがある場合は削減を拒否します。
内部ではBezier区間を分割し、制御点から得られる誤差上界を検査します。
毎フレーム等の固定間隔サンプリングだけで許可する処理ではありません。
`tolerance=0`も使用できますが、浮動小数点の丸め誤差として公開値で
`max(1e-12, 32 ULP)`を許容し、数学的な完全一致を保証する指定ではありません。

初期版はTA / TL / TUに対応します。TT、driven key、quaternion補間、custom tangentは
未対応です。weighted接線で制御点の時刻が逆転する区間や、分割上限内に誤差を確認できない
候補は保守的に残します。前のキーから順に1回ずつ候補を検査するため、
キー数の最小化やMaya標準Key Reducerと同じ結果を保証するAPIではありません。

削減候補はsceneへ登録しない作業用カーブで計画します。本体への変更は
`MFnAnimCurve.remove()`だけで、全カーブ置換・キーの移動・再設定は行いません。
適用後も誤差と保持情報を確認し、想定外の結果や途中失敗では同じbatchの先行変更まで
rollbackします。全削除を同じ`MAnimCurveChange`へ記録し、Undo / Redoに対応します。
通常の対象resolverとlock / reference検査を使用し、no-opでも書込み可否を検査します。

保存済みの複数カーブをまとめて削減する場合は、[AnimationClip.reduce_keys()](animation_clip.md#保存データのキー削減)を使用できます。
こちらはsceneへの予約ではなく、元の保存データを維持して削減済みの新しいclipを返します。

### キー情報とカーブ全体の保存・復元

`get_curve_data() -> AnimCurveData | None`と`set_curve_data(data)`で、
そのチャンネルの時間入力カーブを保存・復元できます。復元は既存カーブの全キーと
weighted・pre/post infinityを置換します。未接続plug、または登録済み属性のベース・指定layerで
対象カーブが未作成なら、空のデータを渡した場合もカーブを作成します。
対象カーブがなければ取得結果は`None`、接続された空カーブなら`keys=()`です。

layer上の新規作成ではMaya標準のキー設定で接続を構築し、作成用キーをすべて除去してから
詳細データを適用します。weightが0・muteのlayerでも、生のカーブ値を復元します。
利用者による仮キーの設定は不要です。復元によるlayerの作成・属性登録は行わず、
必要な作成・登録は同じModifierManagerへ先に予約できます。
通常の未接続plugでは、引き続きOpenMayaでカーブを直接作成します。

対象の入力にconstraint・driven key・空入力のpairBlend・blendWeighted等が接続され、
チャンネルのカーブがない場合は、両復元APIの実行時にエラーにして既存接続を保ちます。
layerの入力側にこれらが接続されている場合も同様です。
これらの構成では、必要なアニメーション接続を先に`set_key()`でMayaに作成させてください。
取得元・復元先に中間ノードがあっても、保存・復元するのは生カーブの形状です。

```python
import json
from pathlib import Path

import bd_util as bdu
from bd_util.maya.node.operator.attr import AnimCurveData

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
source = nodes.existing.transform("source_ctrl")
target = nodes.existing.transform("target_ctrl")

data = source.tx.keyframe.get_curve_data()
if data is not None:
    path = Path("animation.json")
    path.write_text(json.dumps(data.to_dict(), indent=2), encoding="utf-8")
    restored = AnimCurveData.from_dict(json.loads(path.read_text(encoding="utf-8")))
    target.tx.keyframe.set_curve_data(restored)
    mod.do_it_dg()
```

`KeyData`は変更可能なdataclassで、`key.frame += 10`のように直接編集できます。
`AnimCurveData`の共通設定は変更不能ですが、`data.keys`内の各`KeyData`は編集できます。
共通設定を変更したデータを作る場合は`dataclasses.replace()`を使います。
どちらもMayaのnodeやplugへの参照を持ちません。
`AnimCurveData`の構築・設定予約時には各キーを再検証して独立コピーするため、
予約後のデータ編集は実行内容やUndo / Redoへ影響しません。
`to_dict()`も再検証して独立した辞書を返します。`from_dict()`と合わせて、
未知・欠落field、未対応schema、非有限数、無効な接線名、時刻の重複・逆順などを拒否します。

| データ | 内容 |
| --- | --- |
| `KeyData` | `frame`, `value`, `in_tangent_type`, `out_tangent_type`, `in_tangent_xy`, `out_tangent_xy`, `tangents_locked`, `weights_locked`, `breakdown` |
| `AnimCurveData` | `schema_version=2`, `curve_type`, `seconds_per_frame`, `weighted`, `pre_infinity`, `post_infinity`, `keys: tuple[KeyData, ...]` |

`frame`は取得時のUI時間単位、`value`はdegree / cm / unitlessです。
接線XYは取得元のweightedにかかわらず、weighted相当のtangent vector表現です。
Xは秒、Yは値と同じ公開単位で、Bezier handleの変位の3倍を表します。
nonweightedからの取得では、方向を維持してXを隣接キーまでの秒数へ換算します。
隣接キーがない先頭のin / 末尾のout（1キーの場合は両方）は、Mayaのweighted切り替えと
同様に元のベクトルを保持します。表示上のangle / weightとは異なる値です。
nonweightedへ適用するとMayaが正規化するため、重みは失われ、形状が変わり得ます。
元の方向が同じでも異なる重みを持つweightedカーブを、同じキー数・時刻・値のまま
nonweightedで常に再現できるわけではありません。
保存時の`seconds_per_frame`を使って復元するため、FPSが変わっても物理的な時刻を保ちます。
同じフレーム番号へ合わせたい場合は、その値を移植先の秒/フレームへ明示的に変更します。
curve typeとschema versionが公開値・接線の単位規則も規定します。
`AnimCurveData.from_dict()`は現行のschema 2のみを受け付けます。
未対応schemaは`ValueError`になり、旧形式の変換処理は提供しません。
旧データが必要な場合はsceneから取得し直してください。

詳細データ用の`KeyTangentTypeName`はIDEで補完でき、従来の10種類に加えて
`fixed` / `autocustom` / `autoease` / `automix`を保持します。
キー作成時の既定値を意味する`None` / `global`はsnapshotには使用しません。
`InfinityTypeName`は`constant` / `linear` / `cycle` / `cycleRelative` / `oscillate`です。
これらと`CurveTypeName`は`bd_util.maya.node.operator.attr`からimportできます。

一部のキーを扱う場合は、次の対を使います。

```python
keys = source.tx.keyframe.get_key_data(start_frame=1, end_frame=24)
for key in keys:
    key.frame += 10.0
    key.value += 10.0

target.tx.keyframe.set_key_data(keys)
mod.do_it_dg()
```

`get_key_data(start_frame=None, end_frame=None, *, include_boundaries=True)`は、
両端を含む区間の`list[KeyData]`を返します。既定で指定境界を補完し、区間の形状を保つ
接線を取得します。既存キーだけが必要な場合は`include_boundaries=False`を指定します。
範囲省略時は全キーの情報をそのまま取得します。`set_key_data()`には時刻が昇順で
重複しない列を渡します。同時刻のキー情報を上書きし、その他のキーを削除せず、
既存のinfinityも維持します。ただしauto等の接線は前後キーの変更により再計算されます。
たとえば既存の0フレームキーに対して-50 / 50の2キーを渡すと、0フレームキーも残ります。
`set_curve_data()`なら全キーを置換するため、同じ入力では-50 / 50の2キーになります。
一方、両APIが自動作成したカーブには入力データのキーだけが入り、作成用の仮キーは残りません。
`weighted`引数はありません。既存カーブの設定を維持し、新規カーブはMayaの
グローバル設定にかかわらずnonweightedで作成します。接線は移植先の設定へ適用します。
取得元の形状をweightedも含めて復元したい場合は`set_curve_data()`を使ってください。
`seconds_per_frame`省略時は呼び出し時のUI時間単位を、明示時はその時間単位を使います。
保存したデータから設定する場合は`set_key_data(data.keys, seconds_per_frame=data.seconds_per_frame)`
のように渡せます。`frame`変更はキーの時刻だけを変更し、保存された接線XYは変えません。
時間の拡大縮小に合わせてweightedのhandleも伸縮したい場合は、接線Xも明示的に変更します。
空の列は何も予約しません。`get_key_data()`だけではweightedやFPSを保存できないため、
ファイル保存には`AnimCurveData`を使ってください。

### 指定区間のカーブを切り出す

`get_curve_data(start_frame=None, end_frame=None, *, include_boundaries=True)`にも
同じ範囲指定を使用できます。キーに加えてweighted・秒/フレーム・infinityを保持するので、
形状を保って別カーブへ復元する場合はこちらを使います。

```python
data = source.tx.keyframe.get_curve_data(-50, 50)
if data is not None:
    target.tx.keyframe.set_curve_data(data)
    mod.do_it_dg()

# キー情報だけを取得する場合も、既定で境界を補完する。
keys = source.tx.keyframe.get_key_data(-50, 50)
existing_keys = source.tx.keyframe.get_key_data(-50, 50, include_boundaries=False)
```

元のキーが-100 / 100だけでも、境界補完では-50 / 50に相当する2キーを返します。
Mayaの`insertKey()`相当の挿入で隣接接線も調整し、区間内の形状を保存します。
連続接線は再計算を防ぐため`fixed`に変換し、接線とweightのlockを解除したデータを返します。
out tangentの`step` / `stepnext`と既存キーのbreakdownは維持します。
新しい境界キーはbreakdownではありません。これらは返すデータだけの変更です。

取得元のカーブ、選択、現在時刻、Undo / Redo履歴、保留中のmodifierは変更しません。
sceneに追加しない作業用カーブで処理し、成功・失敗のどちらでも解放します。
API編集が変更するsceneのmodified flagも、呼び出し前の状態に戻します。

境界は既存キーと重複させず、同じstart / endは1キーになります。
`None`の側には境界を補完せず、既存キーを取得します。範囲を両方省略した場合は、
接線の種類やlockも含めて元のデータをそのまま取得します。
対象なしの`get_curve_data()`は`None`、空カーブは`keys=()`、`get_key_data()`はどちらも`[]`です。
カーブがなくても、逆転した範囲・非有限の時刻・bool以外の`include_boundaries`は拒否します。

最初・最後のキーより外側は、constant / linearのinfinityを評価して境界を補います。
cycle / cycleRelative / oscillateの繰り返し領域を含む境界補完は`RuntimeError`です。
これらも既存キーの時刻範囲内なら切り出せます。1キーのカーブは定数として扱います。
範囲外の繰り返しをベイクする場合は`sample_values()`を使用してください。

形状の保持対象は切り出した区間内です。infinity設定は引き継ぎますが、切り出し後の
区間外の評価値や繰り返し周期が元と一致するとは限りません。
`set_key_data()`で復元するときは、移植先のweighted設定の違いや残っているキーによって
形状が変わる場合があります。区間全体の復元には`set_curve_data()`を使用してください。

### カーブのweighted設定

`get_weighted() -> bool | None`は実行済みカーブの設定を取得し、対象がなければ`None`です。
`set_weighted(weighted: bool)`はカーブ全体の変更を予約します。同じ設定なら変更せず、
実行時にカーブがなければエラーです。対象範囲・lock / reference等の制約はカーブデータと共通です。

```python
keyframe = target.tx.keyframe
keyframe.set_keys([(1, 0), (24, 10)])
keyframe.set_weighted(True)
mod.do_it_dg()

weighted = keyframe.get_weighted()  # True
```

変更には`MFnAnimCurve.setIsWeighted()`と`MAnimCurveChange`を使い、接線の変換も
Mayaへ委譲します。weightedをFalseへ変えてからTrueへ戻しても失われた重みは戻りません。
元の状態への復元にはUndoを使ってください。

取得は実行済みscene状態のsnapshotで、予約中の操作を実行しません。
編集は入力データを予約時に捕捉し、接続先・lock・layerなどは実行時に検査します。
新規nodeと接続は`MDGModifier`、キーとカーブ設定は`MAnimCurveChange`の履歴に入り、
`ModifierManager` / `MPxCommand`のUndo・Redo・失敗時rollbackに参加します。

詳細データはnumeric / angle / distanceのscalar plugから解決した
`animCurveTA` / `animCurveTL` / `animCurveTU`に対応します。enum・time plugは対象外です。
中間ノードやカーブ設定の対応範囲は上記のチャンネル選択規則と共通です。
復元先のplug・node・curveのlockやreferenceも編集時に拒否します。
time出力・driven key・custom tangentの保存、layer構造は今後の対象です。
node名や独自属性、Graph Editorの表示設定はこのsnapshotの対象外です。
接線の保存・復元にはMayaの浮動小数点精度による丸めが含まれます。

### 旧APIからの移行

時間方向・値方向の編集APIを整理しました。旧メソッド名・旧keyword引数のaliasは提供しません。
以下は`KeyframeManager`と`CurveKeyframeManager`に共通です。

| 変更対象 | 旧名 | 新名 |
| --- | --- | --- |
| 時間方向のメソッド | `move_key` / `move_keys` / `scale_keys` | `move_frame` / `move_frames` / `scale_frames` |
| 時間方向の移動量・値の加算量 | `offset_frames` / `offset_value` | `offset` |
| 単一キーの移動先 | `to_frame` | `to` |
| 範囲の配置先 | `to_start_frame` / `to_end_frame` | `to_start` / `to_end` |
| 時間・値の倍率 | `time_scale` / `value_scale` | `scale` |
| 時間拡縮後の長さ | `duration_frames` | `duration` |
| 時間・値の拡縮基準 | `pivot_frame` / `pivot_value` | `pivot` |

```python
keyframe.move_frame(10, to=15)
keyframe.move_frames(10, 30, offset=5)
keyframe.scale_frames(10, 30, scale=2, pivot=20)
keyframe.scale_frames(10, 30, duration=10, to_start=100)
keyframe.add_values(10, 30, offset=5)
keyframe.scale_values(10, 30, scale=2, pivot=0)
```

対象指定の`frame` / `start_frame` / `end_frame`、`set_value(s)`の`value`、
補間・置換・境界挿入の引数は維持します。単位・既定値・戻り値・編集処理も従来どおりです。
`AnimationClip.restore()`はこの改名の対象に含めず、`offset_frames` / `time_scale`等を引き続き使用します。

layer未指定のキー設定は、Mayaの選択layer・preferred・keying modeへ委ねず、sceneの
ベース（root）layerへ固定します。取得・編集・詳細復元もベースを対象にします。
これまでMayaの選択状態に依存していた処理は、`anim_layer(name)`で対象を明示してください。
layerなしの通常カーブ、`sample_values()`の合成後のplug評価、`find_anim_curves()`の候補範囲は維持します。

query・挿入・接線変更・削除は、DG全体で最初に見つかった上流カーブではなく、
上記の規則でチャンネル自身のカーブを選びます。直接接続に限定していた規則も拡張し、
同じ入口から単位変換やpairBlendをたどれるようになりました。共有出力の制約は維持します。
合成後の値が目的なら`sample_values()`を使用してください。独自構成の調査には
`find_anim_curves()`を使い、選択したTA / TL / TUノードの`.keyframe`で明示編集できます。
layer名による選択には`anim_layer()`を使用します。旧探索を有効にする互換optionは提供しません。

`set_key_data(keys, weighted=...)`の`weighted`引数は廃止しました。引数を削除すると
既存カーブの設定を維持します。設定自体を変更したい場合は`set_weighted()`を明示します。

`set_keys()`の旧形式`set_keys(values, frames=frames, ...)`は廃止しました。
時刻と値を`(frame, value)`のpairへまとめて渡してください。別々の列を持つ既存コードでは、
`zip(..., strict=True)`を使うと、列の長さが異なる場合も切り捨てずに検出できます。

```python
keyframe.set_keys(zip(frames, values, strict=True), out_tangent_type="linear")
```

旧`values` / `frames`引数との互換入口は提供しません。
単位、共通tangent、入力順・同時刻の上書き、予約実行とUndo / Redoの仕様は維持します。

キー設定・挿入のmethod名を変更しました。旧名のaliasは提供しません。

| 旧名 | 新名 |
| --- | --- |
| `keyframe.set(value, frame, ...)` | `keyframe.set_key(value, frame, ...)` |
| `keyframe.insert(frame, breakdown=False)` | `keyframe.insert_key(frame, breakdown=False)` |

引数、`None`戻り値、予約実行、Undo / Redoの仕様は従来どおりです。
`set_tangent()` / `delete_key()` / `delete_keys()` / `delete_anim_curve()`の名前は変わりません。

さらに以前の`keyframe.set_direct()`と`keyframe.insert_direct()`も廃止済みです。
それぞれ`keyframe.set_key()`と`keyframe.insert_key()`へ置き換えてください。
挿入index、変更したかを示すbool、削除したキー数は返さず、変更methodはすべて
`None`を返します。結果をqueryする前に`mod.do_it_dg()`を明示してください。
設定から挿入・編集・削除までを同じ予約列へ積むだけであれば、途中の実行は不要です。

## TransformMatrixの入力

公開APIとしての作成方法、componentの単位・既定値・入力エラーは、
[TransformMatrix](../transform_matrix.md#作成)を正本とします。この節ではmatrix plugとの
接続に関わる仕様だけを記録します。

matrix sequenceの並びはMayaの`MMatrix`と同じrow-majorです。4行4列では各内側の
sequenceを1行として扱い、移動成分は4行目の先頭3要素に置きます。

```python
import bd_util as bdu

values = (
    1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    4.0, 5.0, 6.0, 1.0,
)

matrix = bdu.TransformMatrix(values)
node.matrixIn[0].set(values)
mod.do_it_dg()
```

`list` / `tuple`に限定せず、`range`や`array.array`など、長さを持ち繰り返し走査できる
`Sequence`を受け取ります。generatorのような一度だけ走査する`Iterable`は対象外です。
flatは正確に16要素、nestedは正確に4行4列である必要があり、不正な形状や非numeric
要素には`ValueError`を送出します。元のmutable sequenceを後から変更しても、作成済みの
`TransformMatrix`には影響しません。

`MatrixPlugOperator.set()`と`DataMatrixPlugOperator.set_direct()`も同じmatrix sequenceを
受け取ります。sequenceとの乗算やcolumn-majorの自動判定・自動転置は行いません。
必要な場合は明示的に`TransformMatrix(sequence)`へ変換、または入力側で転置します。

### transform componentからの合成

`TransformMatrix`は、matrix sourceを渡さずkeyword-onlyのtransform componentからも
作成できます。この処理は`MTransformationMatrix`による即時のsnapshot合成であり、
temporary DG nodeの作成や`ModifierManager`への予約は行いません。詳細は
[transform componentから作成](../transform_matrix.md#transform-componentから作成)を
参照してください。

## Channel Box公開状態とlock

すべての`PlugOperator`は、plug単位のlock状態を切り替える次のmethodを持ちます。

- `set_locked()` / `set_unlocked()`
- `set_locked_direct()` / `set_unlocked_direct()`

bool引数で状態を切り替えるのではなく、目的が明確なmethodを使い分けます。
compound親に対するlock操作は、その親plug自体へ設定します。子plugが親のlockを
継承することや、親をunlockしても子自身に設定済みのlockが残ることはMaya標準の
挙動に従います。

Channel Boxで意味のあるscalar / scalar compound型は、公開状態を3状態へ正規化する
次のmethodも持ちます。

| 状態 | queued method | direct method | `keyable` | `channelBox` |
| --- | --- | --- | --- | --- |
| Keyable | `set_keyable()` | `set_keyable_direct()` | `True` | `False` |
| Nonkeyable Displayed | `set_channel_box()` | `set_channel_box_direct()` | `False` | `True` |
| Nonkeyable Hidden | `set_hidden()` | `set_hidden_direct()` | `False` | `False` |

ここでの`set_hidden()`は、plugをChannel BoxのNonkeyable Hidden状態にする操作です。
attribute定義をAttribute Editorなどから隠す`MFnAttribute.hidden`は変更しません。

```python
node.translate.set_hidden()
node.visibility.set_locked()
mod.do_it_dg()
```

suffixを持つscalar compoundに公開状態を設定した場合は、compound親のflagではなく、
表示対象となる各scalar childへ展開します。mixed compoundやgeneric compoundの親には
公開状態methodを提供しませんが、そのscalar childでは利用できます。string、message、
matrix、typed dataなど、Channel Boxのscalar表示対象でない型にも公開状態methodを
提供しません。このcapability分離により、利用できる型でだけIDE補完へ表示されます。

multi attributeの未index親は公開状態の設定対象にできません。`plug[0]`や
`plug[next]`のようにelementを選択してから使用します。scalar compoundのmultiでは、
elementを選択した後、そのchildへ公開状態を展開します。

通常methodはundo対応の`cmds.setAttr`を`ModifierManager.dg_mod`へ予約し、呼び出し順を
保持します。呼び出しただけではsceneへ反映されず、`mod.do_it_dg()`を実行した時点で
反映されます。作成を予約したばかりのnodeにも、DAG作成を反映した後のDG実行として
同じbatchへ積めます。

`*_direct()`は`MPlug`へ即時反映し、undo履歴には参加しません。Channel Box公開状態と
lock状態は互いに独立した概念です。`set_lock_and_hide()`のような複合methodは設けず、
必要な操作を順に呼び出します。

## plug access

```python
node.attr
node.attr.child
node.multiAttr[0]
node.multiAttr[next]
node.multiAttr[0].child
```

`next` は Python builtin の `next` sentinel を利用します。

```python
src.output.connect(dst.input)
dst.input.connect_from("src.output")
dst.input.connect_from(["src", "output"])
dst.input.disconnect_from("src.output")
dst.multiInput.connect_next_index(src.output)
```

`connect()` / `disconnect()` は接続元から接続先を指定します。
`connect_from()` / `disconnect_from()` は接続先から接続元を指定します。

## connection query

接続元は単一の `PlugOperator`、接続先は複数の `PlugOperator` として取得します。

```python
source = dst.input.src_plug()
source_node_name = dst.input.src_name()
source_plug_name = dst.input.src_plug_name()

destinations = src.output.dst_plugs()
destination_node_names = src.output.dst_names()
destination_plug_names = src.output.dst_plug_names()
```

接続元がない場合、`src_plug()` / `src_name()` / `src_plug_name()` は `None` を返します。
接続先がない場合、destination 系メソッドは空 tuple を返します。

`src_name()` / `dst_names()` は `NodeOperator.name`、
`src_plug_name()` / `dst_plug_names()` は `PlugOperator.plug_name` を返します。
同じノードの複数 plug が接続先の場合、`dst_names()` はノード名を重複させ、
3 つの destination 系メソッドで要素数と順序を揃えます。

接続照会は `MPlug.connectedTo()` と同じく、対象 plug 自身への直接接続だけを返します。
multi / compound の親 plug から element や child の接続は集約しません。

接続ノードの `NodeOperator` class で結果を絞り込めます。

```python
joint_source = dst.input.src_plug(
    filter_type=nodes.types.Joint,
)

exact_joint_destinations = src.output.dst_plugs(
    filter_type=nodes.types.Joint,
    include_subclasses=False,
)
```

`include_subclasses=True` が初期値です。
`False` の場合は、解決された `NodeOperator` の class が `filter_type` と完全一致する接続だけを返します。
接続があっても filter に一致しない場合は、source 系は `None`、destination 系は空 tuple を返します。
`filter_type` なしで `include_subclasses=False` を指定すると `ValueError` を送出します。

### connection query の設計境界

`filter_type` が判定するのは、直接接続されているノードです。
`unitConversion` などの中間ノードを通過して上流・下流を探索する機能ではありません。
将来 pass-through traversal を追加する場合も、直接接続を返す初期動作は維持し、
別の option または API として明示します。

接続先の `MPlug` は `ExistingNode` を経由して `PlugOperator` へ解決します。
このとき、照会元と同じ `ModifierManager` を引き継ぎ、既存ノードを変更しないよう
`auto_add_attr=False` で包みます。結果は接続先を改めて解決した wrapper であり、
別経路ですでに取得した `PlugOperator` との Python object identity は保証しません。
同じ plug かどうかは `is` ではなく `MPlug` を表す `plug` で比較します。

destination 系メソッドの順序は `MPlug.connectedTo()` の結果に従い、独自の sort は行いません。
同一の scene 状態では `dst_plugs()` / `dst_names()` / `dst_plug_names()` の要素を
同じ順序で対応させますが、この順序を接続作成順などの意味として扱わないでください。
再現可能な順序が必要な処理では、呼び出し側で `plug_name` などを key に sort します。

現在の `PlugOperator` への解決は、`ExistingNode` で型を解決でき、対象 attribute が
その `NodeOperator` / `AttributeField` に定義されていることを前提とします。
生成後に追加された未知の plug-in node type や runtime extra attribute など、
この前提を満たさない接続は `AttributeError` になる場合があります。
これは「接続なし」を表す `None` / 空 tuple とは別の状態です。
name 系メソッドも対応する plug query の結果から名前を取得するため、同じ解決境界を持ちます。
また、接続状態は scene 編集で変化するため、connection query の結果は cache しません。

## extra attribute

extra attribute は `AddAttr` から定義します。

```python
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr

class MyNode(NodeOperator):
    weight = AddAttr.at.double(default_value=1.0)
    offset = AddAttr.at.double3(default_value=[0.0, 0.0, 0.0])
    rotation = AddAttr.at.double_angle3(default_value=[0.0, 0.0, 0.0])
    orient = AddAttr.at.quat()
```

Python class 上の field 名は、通常そのまま Python 側の access 名と Maya attribute の `longName` になります。

```python
class MyNode(NodeOperator):
    weight = AddAttr.at.float(default_value=1.0)

node.weight
# Maya attribute: weight
```

Maya 側の名前だけを Python 側の access 名と変えたい場合は、`long_name` / `short_name` を指定します。

```python
class MyNode(NodeOperator):
    weight = AddAttr.at.float(
        default_value=1.0,
        long_name="blendWeight",
        short_name="bw",
    )

node.weight
# Maya attribute: blendWeight / bw
```

`AddAttr.at.*(...)` の factory は、主に次の共通 option を受け取ります。

- `long_name`
- `short_name`
- `multi`
- `readable`
- `writable`
- `category`

numeric / unit 系では `default_value`、`min_value` / `max_value`、`soft_min_value` / `soft_max_value` も指定できます。

これらの option は OpenMaya 経由の `add_attr()` と `cmds.addAttr()` 経由の `cmds_add_attr()` の両方で、実際の Maya attribute へ反映されます。

`multi=True` の場合は array attribute として作成され、通常の multi plug と同じように `node.attr[index]` / `node.attr[next]` でアクセスします。

`NodeOperator` 初期化時、`extra=True` の field は対象ノードに存在しなければ自動で追加されます。

`cmds_add_attr()` が必要な型は `cmds` 経由、それ以外は OpenMaya 経由の `add_attr()` を使います。

### typed dataのdefault値

`MFnTypedAttribute`でdefault値に対応する型は、Python値をdata objectへ変換し、
その`MObject`を`MFnTypedAttribute.create()`のdefault引数へ渡します。attributeを
ノードへ追加してから`set_direct()`する方法は使いません。作成時に渡すことで、
現在値だけでなくattribute definitionのdefault値としてMayaへ保持されます。

`DataTypePlugOperator._add_attr_base()`は`default_object_factory`を受け取り、
現在はstring dataが`MFnStringData`による変換を提供します。`None`はdefault未指定を
表し、空文字列などのfalseyな値も有効なdefault値として扱います。

新しいtyped data型で`default_value`を公開する場合は、対応する`MFn*Data.create()`で
Python値から`MObject`を作るfactoryを実装し、`_add_attr_base()`へ渡します。
factoryを用意できない型では`default_value`を公開しません。

### extra enum attribute

追加アトリビュートの enum は、`PlugOperator` と `field` だけで定義します。

```python
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr


class SpaceModePlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    LOCAL = 0
    WORLD = 1

    NAME_MAP = {
        LOCAL: "Local",
        WORLD: "World",
    }


class SpaceModeField(
    AddAttr.define.at.enum.field[SpaceModePlugOperator]
):
    __slots__ = ()


class MyNode(NodeOperator):
    spaceMode = SpaceModeField()
```

この形では追加アトリビュート用の `AttrOperator` を明示的に定義する必要はありません。

`node.spaceMode` は `SpaceModePlugOperator` として補完されます。

```python
node.spaceMode.LOCAL
node.spaceMode.name_by_index(node.spaceMode.WORLD)
node.spaceMode.index_by_name("Local")
```

Maya に作成される enum label は `SpaceModePlugOperator.NAME_MAP` から作られます。

`NAME_MAP` は Maya 上の表示名と enum index の対応です。

追加 enum では `PlugOperator` 側に定義します。

`AddAttr.define.at.enum` は追加アトリビュート用の enum 定義として、`field` と `plug_operator` のみを公開します。

`AddAttr.define.at.enum.field[...]` の型引数は IDE 補完に使われるため、省略せずに記述します。

### extra compound attribute

追加アトリビュートの compound も、基本方針は enum と同じです。

`PlugOperator` と `field` だけを定義し、追加アトリビュート用の `AttrOperator` は明示的に定義しません。

```python
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr


class SpaceOptionDetailPlugOperator(
    AddAttr.define.at.compound.plug_operator
):
    __slots__ = ()

    visible = AddAttr.at.bool(default_value=True)
    blend = AddAttr.at.float(default_value=0.5, min_value=0.0, max_value=1.0)


class SpaceOptionDetailField(
    AddAttr.define.at.compound.field[SpaceOptionDetailPlugOperator]
):
    __slots__ = ()


class SpaceOptionPlugOperator(AddAttr.define.at.compound.plug_operator):
    __slots__ = ()

    enabled = AddAttr.at.bool(default_value=False)
    weight = AddAttr.at.float(default_value=1.0, min_value=0.0)
    detail = SpaceOptionDetailField()
    offset = AddAttr.at.double3(default_value=[0.0, 0.0, 0.0])
    aim = AddAttr.at.double_angle3(default_value=[0.0, 0.0, 0.0])


class SpaceOptionField(
    AddAttr.define.at.compound.field[SpaceOptionPlugOperator]
):
    __slots__ = ()


class MyNode(NodeOperator):
    spaceOption = SpaceOptionField()
```

`node.spaceOption` は `SpaceOptionPlugOperator` として補完されます。

そのため、子アトリビュートも plug から直接辿れます。

```python
node.spaceOption.enabled
node.spaceOption.weight
node.spaceOption.detail.visible
node.spaceOption.detail.blend
node.spaceOption.offset.x
node.spaceOption.aim.z
```

compound child でも、通常は Python class 上の field 名が Python 側の access 名と Maya child attribute の `longName` になります。

```python
class SpaceOptionPlugOperator(AddAttr.define.at.compound.plug_operator):
    __slots__ = ()

    cmp1Float = AddAttr.at.float(default_value=1.0)
    cmp1Double3 = AddAttr.at.double3(default_value=[0.0, 0.0, 0.0])


node.spaceOption.cmp1Float
node.spaceOption.cmp1Double3.x
```

child の Maya 名だけを変えたい場合も `long_name` / `short_name` を使えますが、その場合も Python 側の access 名は field 名のままです。

Maya attribute の作成は `CompoundPlugOperator.add_attr()` が OpenMaya 経由で行います。

compound child の中にさらに compound child を定義できます。

その場合も、各階層の field は `AddAttr.define.at.compound.field[...]` で定義し、型引数にはその階層の `PlugOperator` を渡します。

custom scalar compound も child として定義できます。

現行で対象になる主な型は `double2` / `double3` / `double4` / `quat` / `float2` / `float3` / `long2` / `long3` / `short2` / `short3` / `double_linear2` / `double_linear3` / `double_angle2` / `double_angle3` / `float_linear2` / `float_linear3` / `float_angle2` / `float_angle3` です。

`double_angle3` は Maya 上では親 `double3`、子 `doubleAngle` として作成されます。

現時点では OpenMaya で compound child として作成できる型を対象とし、未対応の child 型は `UnsupportedOperationError` にします。

`AddAttr.define.at.compound` は追加アトリビュート用の compound 定義として、`field` と `plug_operator` のみを公開します。

`AddAttr.define.at.compound.field[...]` の型引数は IDE 補完に使われるため、省略せずに記述します。

## custom scalar compound

compound 系の custom 実装は `define/custom/at/scalar_compound` 配下にあります。

現行で主に扱う型は次の通りです。

- numeric compound
  - `double2`
  - `double3`
  - `double4`
  - `float2`
  - `float3`
  - `long2`
  - `long3`
  - `short2`
  - `short3`
- unit compound
  - `double_linear2`
  - `double_linear3`
  - `double_angle2`
  - `double_angle3`
  - `float_linear2`
  - `float_linear3`
  - `float_angle2`
  - `float_angle3`
- semantic alias
  - `quat`

`quat` は低レベル型としては `double4` 相当で、意味付き alias として扱います。

default は未指定時に `[0.0, 0.0, 0.0, 1.0]` です。

## compound get / set

固定長かつ同種の scalar child で構成される compound の `get()` は、
attribute type に対応する immutable な専用値型を返します。

```python
import bd_util as bdu

result = node.offset.get()

isinstance(result, bdu.Double3)
result.x
result.y
result.z

x, y, z = result
result[0]
result.as_tuple()
```

専用値型は `bd_util.maya.value.scalar_compound` 以下に、attribute type の
継承関係が分かる package 構造で配置します。各専用値型は `bd_util` の
トップレベルからも公開します。

`bd_util` パッケージ内部で専用値型や関連 module を参照する場合は、
`from bd_util.maya...` のような package top 起点の import ではなく、
import 元の module を基準にした相対 import を使用します。
これは内部実装の規約であり、利用者向けコードでは従来どおり
`import bd_util as bdu` から公開 API を利用します。

主な対応は次の通りです。

- `double2/3/4` -> `Double2` / `Double3` / `Double4`
- `float2/3` -> `Float2` / `Float3`
- `long2/3` -> `Long2` / `Long3`
- `short2/3` -> `Short2` / `Short3`
- `double_linear2/3` -> `DoubleLinear2` / `DoubleLinear3`
- `float_linear2/3` -> `FloatLinear2` / `FloatLinear3`
- `double_angle2/3` -> `DoubleAngle2` / `DoubleAngle3`
- `float_angle2/3` -> `FloatAngle2` / `FloatAngle3`
- `quat` -> `Quat`

専用値型は `Sequence` として index access、slice、iteration、unpack、
`tuple()` / `list()` への変換に対応します。値は変更できず、hashable です。

浮動小数点のnumeric値型である`Double2` / `Double3` / `Double4`、
`Float2` / `Float3`は、同じ具体型同士の加減算、scalarによる乗除算、符号反転を
提供します。

```python
value = bdu.Double2(1.0, 2.0) + bdu.Double2(3.0, 4.0)
# Double2(4.0, 6.0)
```

要素積、異なる具体型同士の演算、unit値型と整数値型の演算は定義しません。詳細は
[Numeric Compound Values](../numeric_compound_values.md)を参照してください。

`Quat`はこれらのnumeric値型とは別に、Quaternion固有の積・変換・逆元・正規化・
補間を持ちます。component-wise演算やscalarとの乗算は提供しません。詳細は
[Quat](../quaternion.md)を参照してください。

`set()` と `set_direct()` は、展開引数と sequence の両方を受け取ります。
専用値型も sequence としてそのまま渡せます。

```python
node.offset.set(1.0, 2.0, 3.0)
node.offset.set([1.0, 2.0, 3.0])
node.offset.set((1.0, 2.0, 3.0))
node.offset.set(bdu.Double3(1.0, 2.0, 3.0))

node.offset.set_direct(1.0, 2.0, 3.0)
```

専用値型同士の比較では、値に加えて型も一致する必要があります。
通常の list / tuple と比較したい場合は `tuple(result)`、`list(result)`、
またはテスト用途の `pytest.approx()` などを使用します。

mixed compound の `get()` は専用値型の対象外です。

要素数が child 数と一致しない場合は `TypeError` です。

この validation は child を一部だけ変更してしまう事故を避けるため、実際の set 前に行います。

## limit 設定

custom scalar compound は child attribute に対して次の public method を持ちます。

```python
node.offset.set_min([-1.0, -2.0, -3.0])
node.offset.set_max(10.0)
node.offset.set_soft_min(0.0)
node.offset.set_soft_max([1.0, 2.0, 3.0])
```

値は scalar または child 数と同じ長さの sequence を受け取ります。

- scalar
  - 全 child に同じ値を設定します。
- sequence
  - child ごとに個別値を設定します。

unit 系では、内部で Maya API に渡す形式へ変換してから設定します。

## child names

通常の child 名は suffix から生成されます。

```text
longNameX / shortNamex
longNameY / shortNamey
longNameZ / shortNamez
longNameW / shortNamew
```

既存 Maya attribute に合わせたい場合は `CHILD_ATTR_NAMES` で明示します。

`Transform.translate` / `Transform.rotate` / `Transform.scale` はこの方式で Maya 標準名に合わせます。

```text
translate / t
translateX / tx
translateY / ty
translateZ / tz
```

## lookup

`lookup_attr_cls(node, attr)` は Maya 上の既存 attribute から対応する `AttrOperator` class を返します。

floating point compound は parent の `attributeType` と child の `attributeType` を見て解決します。

child 型が混在している場合、現状は unsupported として `TypeError` を出します。

`double4` かつ long name に `quat` が含まれる場合は `Quat4AttrOperator` に解決します。

## 注意点

- `addr` は Maya 側に存在しますが、基本的に使用しない attribute のため `AddAttr` 公開や自動 add_attr 対応の対象外です。
- `set_direct()` は undo 対応外です。
- `NodeOperator.__getitem__()` の文字列パス解析は現状 active ではありません。
- `lookup.py` は新しい型を追加したら追従が必要です。
