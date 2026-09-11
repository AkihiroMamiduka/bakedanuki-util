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
一時的に切り替えます。Python APIに`MDGContextGuard`は公開されていないため、
`MDGContext.makeCurrent()`を使い、評価の成功・失敗のどちらでも元のコンテキストへ戻します。
取得結果は値のsnapshotであり、その後のscene変更には追従しません。

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
`(frame, value)`のlistを時刻の昇順で返します。上流で最初に見つかったtime-input
animCurveを対象にし、指定範囲に実在するキーだけを取得します。カーブや該当キーが
なければ空listです。範囲は両端を含み、`None`の側には境界を設けません。
範囲端にキーがなくても、補間したキーを追加することはありません。
NaN・無限大や逆転した範囲は、カーブの有無にかかわらず`ValueError`です。

```python
keys = keyframe.get_keys()
segment_keys = keyframe.get_keys(start_frame=12.0, end_frame=24.0)
```

同じ単位のキー設定には、戻り値をそのまま`set_keys(keys)`へ渡せます。
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

取得値はカーブに保存されたキーの値です。unitConversionやblend nodeを経由していても、
それらによる変換後のplug値やconstraintの計算結果をsamplingすることはありません。
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

`set_key()` / `set_keys()`は実行時の接続・型・scene状態からAPI経路かcmds経路を選択します。
対象plugに直接接続した既存のTA / TL / TUカーブがあり、plugとカーブの型が一致する
単純な構成では、`MFnAnimCurve.addKey()`と`MAnimCurveChange`で追加・上書きします。
API経路の対象plugは、boolを除くscalar numericとangle / linearです。

次のいずれかに該当する場合は、`MDGModifier.pythonCommandToExecute()`から
`cmds.setKeyframe()`を実行します。

- カーブの新規作成、blend nodeやunitConversionを経由する接続、共有カーブ。
- カーブのinputに明示的な接続がある場合、またはplugとカーブの型が一致しない場合。
- scene内にanimation layerが1つでもある場合。対象plugがlayerに属さなくても含みます。
- 対象plug、カーブのoutputやkeyTimeValueがlockされている場合、または対象node・
  カーブnodeがlockされているかreference由来の場合。
- bool / enum / time属性、TTカーブなどAPI経路の対象外の型。
- 入力側tangentが`step` / `stepnext`、またはTAカーブの`rotationInterpolation`が1以外の場合。

cmds経路ではカーブの選択・作成、animation layerへの値の解決、必要なblend nodeの
作成をMayaへ委ねます。キー設定にはlayer指定や`insertBlend`指定の引数はなく、
Maya側の状態・設定が適用されます。layerを一律にcmdsへ委ねるのは、BaseAnimationの
lockが、layerに属さない直接接続カーブへのキー設定も禁止するためです。
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

### キーの挿入・編集・削除

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
同じカーブを共有する別のplugがある場合も、カーブ全体とその接続を削除します。
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

これらの編集操作とqueryは、上流で最初に見つかったtime-input animCurveを
対象にする従来の探索を使用します。animation layer全体の合成値や、`set_key()` / `set_keys()`で
Mayaが選んだlayerのカーブを必ず扱うAPIではありません。カーブはquery時・編集実行時に
探索し、Undoや再接続をまたいで古いカーブをキャッシュしません。

キー設定のAPI経路の対象拡張と、編集対象カーブ・layerを明示するAPIは今後の検討対象です。
現在のAPI経路は既存の単純なカーブへの編集を対象とします。
任意時刻のplug値は`sample_values()`で取得します。`KeyData` / `AnimCurveData`による
詳細なキー・カーブ情報の保存と復元は次段階の対象で、現在は提供していません。

### 旧APIからの移行

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
