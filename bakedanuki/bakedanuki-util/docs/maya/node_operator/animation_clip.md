# AnimationClip

`bdu.AnimationClip`は複数node・属性のアニメーションをsceneから独立したデータへ保存し、
まとめて復元するAPIです。取得は即時のquery、復元は`ModifierManager`への予約です。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

clip = bdu.AnimationClip.capture(
    [nodes.existing("source:ctrlA"), nodes.existing("source:ctrlB")],
    start_frame=10,
    end_frame=30,
)
clip.restore(mod, namespace="target", mode="replace_range")
mod.do_it_dg()

mod.undo_it()
mod.redo_it()
```

保存時には、保留中の作成・編集を暗黙に実行しません。作成待ちnodeの取得はエラーです。
復元はそれ以前に同じmanagerへ予約されたDG操作の実行後に対象と接続を検査します。
途中の失敗では、その`do_it_dg()`の変更を戻します。MPxCommandでも同じ履歴を使用します。

## 公開API

```python
AnimationClip.capture(
    nodes,
    *,
    attributes=None,
    include_channel_box=False,
    include_static=False,
    start_frame=None,
    end_frame=None,
    layer_mode="flatten",
    layers=None,
    sample_by=1.0,
) -> AnimationClip

clip.reduce_keys(
    start_frame=None,
    end_frame=None,
    *,
    tolerance,
    preserve_breakdowns=True,
) -> AnimationClip

clip.restore(
    modifier_manager,
    *,
    targets=None,
    namespace=None,
    mode="merge",
    offset_frames=None,
    to_start_frame=None,
    to_end_frame=None,
    time_scale=None,
    duration_frames=None,
    restore_layer_settings=False,
    tolerance=1e-6,
) -> None
```

`nodes` / `targets`はnode名、`NodeOperator`、`MObject`のiterableです。
選択中node・layerを対象決定に利用しません。transformを指定してもshapeや子nodeへは展開しません。

## 属性と保存範囲

- `attributes=None`: node自身のkeyable属性を収集します。
- `include_channel_box=True`: keyableに加え、非keyableでchannelBox表示の属性も収集します。
- `attributes=["tx", "rotate", "customValue"]`: 各nodeに共通の属性名を指定します。
  明示時はkeyable / channelBox条件を適用しません。compoundと既存array要素はleafへ展開します。
- `include_static=False`（既定）: 収集した候補から、キーも時間依存もない静的な属性を除外します。
  属性を明示した場合にも適用します。静的な属性の値も保存するときは`True`を指定します。
- 対応型はTA / TL / TUカーブに対応する数値、bool、enum、angle、distanceです。
  自動収集では非対応型を除外し、明示した非対応型や存在しない属性はエラーです。
  time属性・matrix・string・messageは対象外です。
- 保存時はlockされた属性も読み取れます。復元時のlock / reference検査は既存resolverと共通です。
- `start_frame` / `end_frame`は両端を含み、負の時刻とsubframeを扱います。
  省略した端は対象の時間入力カーブの最初・最後のキーから決定します。
  合成保存では上流のweight等のアニメーションも探索し、レイヤー保持では指定layerと必要な設定の
  カーブから決定します。どちらの端も推定できない静的な対象では、両端の指定が必要です。

対象node順を保存します。属性パスはaliasを解決したlong name・compound経路・logical indexです。
空の対象、重複node、全属性が非対応、選択layerに対象チャンネルがない場合はエラーです。
静的な属性の除外によって全体の対象がなくなった場合も`ValueError`です。
一部のnodeだけ対象がなくなった場合は、そのnodeを空のチャンネル一覧として残し、
`targets`の順番・個数による対応付けを維持します。

### 静的な属性を含める場合

```python
clip = bdu.AnimationClip.capture(
    ["ctrlA", "ctrlB"],
    start_frame=10,
    end_frame=30,
    include_static=True,
)
```

静的かどうかは保存区間の値の変化量ではなく、キーとDGの依存関係で判定します。
1キーだけの属性、全キーが同じ値の属性、指定区間の外にだけキーがある属性も保存します。
キー数0のカーブだけが接続されている属性は、アニメーションありとは見なしません。

合成保存では上流のキー・時間node・expressionを探索するため、constraintや計算nodeを
経由して動く属性も含めます。Mayaが宣言した依存関係に基づく判定であり、
weightが0のlayerや一定値のexpressionなど、結果が一定でも依存がある属性は残します。
未接続の静的属性や、静的な値からの接続だけを持つ属性は既定で除外します。

レイヤー保持では指定layerの生値と、その再現に必要な親・rootの設定のアニメーションを
判定します。保存しないlayerのチャンネルにキーがあるだけでは対象にしません。
属性を対象に残した場合は、選択範囲のlayerにある静的な生値も保持します。
例えば「ベースの固定値5 + 上位layerのアニメーション」ではベースの5も保存し、
「ベースのアニメーション + 上位layerの固定値」では上位layerの固定値も保存します。
回転layerでは3軸が相互に影響するため、候補に含まれる他の回転軸の生値も保持します。
保存対象外のlayerのチャンネルを、この補完のために追加することはありません。

`include_static=True`は従来と同じ収集範囲です。取得時に保存元へキーを追加しませんが、
静的な値を含むclipを復元すると、その属性にもキーが作られます。
保存データから除外した属性は、全置換を指定しても復元先の値・キーを変更しません。

## 合成保存（既定）

`layer_mode="flatten"`では`sample_values()`と共通の評価処理を使い、最終的なplug値を保存します。
レイヤー構造は保存データに含めません。保存元のレイヤー、現在時刻、選択状態は変更しません。

`sample_by`は取得時のMaya UI時間単位で、既定は1フレームです。開始時刻から等間隔に採取し、
刻みが割り切れない場合も終了時刻を含めます。数値はlinear、bool / 整数 / enumはstepで復元します。
キー削減は自動実行しません。保存後に`clip.reduce_keys()`を明示して削減できます。
合成保存は元カーブのキー数・接線を保持する方式ではありません。

対象に含めた属性はキーがなくても保存区間を通して評価し、
一定値ならその値を持つサンプルとして保存します。
constraintやexpressionも評価対象ですが、履歴依存のsimulationを時刻順に実行する機能はありません。
推定キー範囲はsimulationや無限の動きを表すものではないため、必要な範囲を明示してください。

復元はベース（sceneのroot）へ行い、`set_keys()`と同じMayaの値解決を使用します。
既存layerの値・weight等を考慮して、サンプル時刻の合成結果が保存値になるよう設定します。
他layerのカーブや設定は変更しません。上位Overrideがベースを完全に覆う場合など、
結果を再現できなければ`RuntimeError`となり、一括操作をrollbackします。

復元後は全対象のサンプル時刻を検証します。`tolerance`は絶対誤差で、角度はdegree、距離はcm、
その他はunitlessです。浮動小数点の丸めには32 ULPを許容します。
サンプル間の連続形状や、後で他layerを編集したときの結果の一致を保証するものではありません。

## レイヤー保持

```python
clip = bdu.AnimationClip.capture(
    ["ctrlA", "ctrlB"],
    attributes=["translate", "rotate"],
    layer_mode="preserve",
)

correction = bdu.AnimationClip.capture(
    ["ctrlA", "ctrlB"],
    layer_mode="preserve",
    layers=["Correction"],
    start_frame=10,
    end_frame=30,
)
```

`layers=None`ならベースと対象属性が所属するlayerを保存します。明示したリストでは指定layerの
チャンネルだけを保存します。ベースも含める場合は、取得時のrootの名前をリストへ追加します。
親layerは階層・設定の復元に必要なため含めますが、指定されていない親のチャンネルは保存しません。
加算layerだけを保存したデータは差分であり、それだけで元sceneの最終値を再現するものではありません。
`layers`を合成保存へ指定するとエラーです。

保存内容は、対象カーブの詳細データとlayerの親子関係・兄弟順、次の設定です。

`override`、`passthrough`、`rotationAccumulationMode`、`scaleAccumulationMode`、
`weight`、`mute`、`solo`、`lock`。設定に時間入力カーブがあれば、その詳細データも保存します。
ベースの設定は`root_settings`に保存し、復元先sceneのrootへ対応させます。
selected / preferred等のUI状態は保存しません。

範囲省略時はカーブ全体のキー・接線・lock・breakdown・weighted・infinityを取得します。
範囲指定時は既存詳細データAPIと同様に境界補完と連続接線のfixed化を行い、元sceneは変更しません。
周期infinityの範囲外切り出し等、詳細データAPIの制約も共通です。
静的な生値には保存区間の境界キーを用意します。生値の復元に合成値からの逆算は適用しません。

不足するlayerは作成し、対象属性を登録します。同名の既存layerは、設定・親・相対順が一致すれば
再利用します。不一致なら既定でエラーです。`restore_layer_settings=True`では保存設定と構成へ
変更します。この指定は共有layerの対象外属性にも影響し、設定カーブは全置換されます。
rootの設定も同じ規則です。既存のlocked / referenced layerを自動解除して編集することはありません。
新規layerの保存されたlock状態は、カーブ復元後に設定します。

## 復元時刻の指定

`restore()`に`offset_frames` / `to_start_frame` / `to_end_frame`を指定すると、
保存区間・全nodeのキー・layerとrootの設定カーブを同じ時間だけ平行移動して復元します。
平行移動はこのうち1つで指定します。開始と終了の両方を指定すると、後述の区間合わせになります。
時刻・拡縮を全省略した場合は、保存時刻へ復元します。

保存・復元先が同じFPSで、保存区間が10〜30の場合です。

| 指定 | 復元区間 |
| --- | --- |
| 指定なし | 10〜30 |
| `offset_frames=15` | 25〜45 |
| `to_start_frame=100` | 100〜120 |
| `to_end_frame=100` | 80〜100 |

```python
clip.restore(mod, to_start_frame=100, mode="replace_range")
mod.do_it_dg()
```

絶対時刻合わせは`clip.start_frame` / `clip.end_frame`を基準にします。
属性ごとの先頭・末尾キーは基準にしません。保存区間が10〜30で、ある属性のキーが15から
始まる場合、`to_start_frame=100`ではそのキーは105へ移ります。
1時刻だけのclipでも開始・終了のどちらの指定でも配置できます。

フレームで指定する引数は`restore()`呼び出し時のMaya UI時間単位で捕捉します。
負の時刻とsubframeを許可し、整数フレームへ丸めません。拡縮未指定では動きの長さを秒で維持します。
例えば24fpsで保存した24〜48のclipを30fpsで`to_start_frame=90`とすると、90〜120へ復元します。
予約後にFPSを変更しても、予約時に決めた物理的な時刻・移動量を維持します。
矛盾する引数の組み合わせ、bool・文字列・非有限数、Mayaの表現範囲を超える時刻、
移動後にキーや区間が時刻精度の限界で重なる指定は、予約前に拒否します。

時刻指定は元のclipやJSONを変更せず、復元用のコピーに適用します。同じclipを複数の時刻へ予約できます。
移動量0や同じ時刻への位置合わせも通常の復元であり、処理を省略しません。
`merge`で同じnodeへ別時刻に復元した場合は、元時刻のキーも残ります。
`replace_range`の置換範囲は移動後の保存区間です。`replace_all`は対象カーブ全体を置換します。
戻り値は`None`で、変更は`ModifierManager`へ予約し、Undo / Redo・失敗時rollbackへ参加します。

レイヤー保持ではweight等の設定キーも移動し、既存layerとは移動後の時刻で比較します。
設定が不一致なら既定でエラーとなり、明示的な`restore_layer_settings=True`で設定を全置換します。
この設定置換は`mode`とは別の指定で、共有layerの対象外属性にも影響します。
nonweighted設定カーブの接線は、Mayaによるベクトル長の正規化を許容し、方向を比較します。
weighted設定カーブの区間内の接線は方向・長さの両方を比較し、Mayaによる微小な丸め誤差を許容します。
先頭キーのin接線と末尾キーのout接線は、補間・infinityに影響しない長さの正規化を許容し、方向を比較します。
合成保存では、移動先時刻の他layerの影響を考慮して値を設定・検証します。

平行移動では時刻以外のキー情報を変更せず、接線・lock・breakdown・weighted・infinityは
既存の復元規則に従います。移動・拡縮指定は復元時のoptionなので、JSONはschema 2のままです。

## 時間拡縮

`time_scale`は時間の長さに掛ける倍率、`duration_frames`は復元後の長さです。
開始と終了の両方を指定すると、保存区間の両端を復元先の両端へ合わせる倍率を自動で求めます。
属性ごとの先頭・末尾キーではなく、`clip.start_frame` / `clip.end_frame`を共通の基準にします。

保存区間が10〜30で、保存時と復元時のFPSが同じ場合です。

| 指定 | 復元区間 |
| --- | --- |
| `time_scale=2` | 10〜50（動きの長さが2倍） |
| `time_scale=0.5` | 10〜20 |
| `duration_frames=30` | 10〜40 |
| `time_scale=2, offset_frames=15` | 25〜65 |
| `time_scale=2, to_start_frame=100` | 100〜140 |
| `duration_frames=30, to_end_frame=100` | 70〜100 |
| `to_start_frame=100, to_end_frame=140` | 100〜140 |

```python
clip.restore(mod, to_start_frame=100, to_end_frame=140, mode="replace_range")
mod.do_it_dg()
```

長さは開始と終了の差です。100〜130の長さは30フレームと数えます。
`time_scale`は単位なしの正の有限数、`duration_frames`は予約時のUI時間単位での正の有限数です。
保存時と異なるFPSでは、保存された秒単位の長さに倍率を掛けるか、予約時の指定長へ合わせます。
予約後にFPSを変えても、予約時に決めた秒単位の配置・長さを保ちます。

- `time_scale`と`duration_frames`は同時に指定できません。
- 開始・終了の両方を指定する場合は、`offset_frames`・`time_scale`・`duration_frames`との併用を拒否します。
- 開始または終了の片側指定は、倍率・長さ指定と組み合わせられます。
- `offset_frames`は開始・終了指定と併用できません。配置未指定では保存区間の開始を固定します。
- 両端指定の終了は開始より後とします。0・負の倍率、逆再生、区間の0幅への圧縮には対応しません。
- 保存区間が1時刻のclipに長さ・両端を指定することはできません。正の倍率指定は許可し、
  チャンネルは1時刻のまま配置します。layer設定に他の時刻のキーがあれば、同じ基準で拡縮します。
- 倍率1や元と同じ長さ・区間でも通常の復元を行います。精度の限界でキーや区間が重なる指定は予約前に拒否します。

全node・全属性のキー、layerとrootの設定キーを同じ倍率で拡縮します。
保存区間外にあるlayer設定キーも同じ基準で変換し、定数設定は維持します。
接線のX（秒）も倍率に合わせて変換し、キーの値と接線Yは維持します。
接線の種類・lock・breakdown・weighted・infinityは既存の復元規則に従います。
auto等の接線はMayaが再計算するため、特にmerge・部分置換では隣接キーの影響を受けます。
旧来の`fast` / `slow`はMaya標準と同様に決まった傾きへ再計算されるため、全置換でも
元の形状をそのまま時間方向へ伸縮した結果にはなりません。接線の種類を維持する方針を優先します。
layer設定の比較でも、この2種類の接線はキー時刻・値・種類等から決まる再計算結果を許容します。

合成保存のサンプルもそのまま時間を拡縮し、キーの追加サンプリング・削減・整数時刻への丸めは行いません。
復元先のlayer合成値は、変換後のサンプル時刻で解決・検証します。
レイヤー保持では変換後の設定を既存layerと比較し、不一致時の`restore_layer_settings`の扱いは上記と同じです。
部分置換は拡縮・配置後の区間、全置換は対象カーブ全体を置換します。
元のclip・JSONを変更せず、予約時の独立コピー、Undo / Redo・rollbackにも対応します。

## 復元先と置換方法

- 既定: 保存したnode名へ復元します。DAG nodeはfull pathを保存し、曖昧な短縮名照合をしません。
- `namespace="new:character"`: 各DAG経路要素・node・layerの名前空間を指定値へ置き換えます。
  `namespace=""`なら取り除きます。必要な名前空間と復元先nodeは事前に用意してください。
- `targets=[dstA, dstB]`: 保存node順に対応させます。個数不一致・対応先の重複はエラーです。
  属性名は保存時のまま、layer名も保存時のままです。`namespace`との同時指定はできません。
- 予約時に存在する復元先nodeは同一性を保持し、改名に追従します。同名nodeへのすり替えはしません。
  作成待ちnodeも、先行するDG作成と同じmanagerで復元できます。

| mode | 呼称 | キーの扱い |
| --- | --- | --- |
| `merge`（既定） | 追加・上書き | 同時刻だけ上書きし、他のキーを残す |
| `replace_all` | 全置換 | 対象カーブの全キーを置換する |
| `replace_range` | 部分置換 | 移動指定後の保存区間の既存キーを両端込みで削除して復元し、外側のキーを残す |

保存データに含まれない属性・チャンネルは置換対象にしません。
部分置換はキー保持の契約で、境界をまたぐ補間やauto接線の再計算は影響を受け得ます。
全置換ではweighted / infinityも復元します。合成保存のデータはnonweighted / constantです。
merge / 部分置換では既存カーブの
weighted / infinityを維持するため、nonweightedへの復元では接線の重みが失われます。
新規カーブでは保存したweighted / infinityを使用します。

## 保存データのキー削減

`reduce_keys()`は全nodeの属性チャンネルを対象に、削減済みの新しい`AnimationClip`を即時に返します。
flatten / preserveの両方に対応し、元clip・scene・MayaのUndo履歴・保留中modifierは変更しません。
削減自体に`ModifierManager`は不要です。戻り値を受け取って保存・復元してください。

```python
reduced_clip = clip.reduce_keys(-50, 50, tolerance=0.01)

# 全体・片側の範囲も指定できます。
reduced_clip = clip.reduce_keys(tolerance=0.01)
reduced_clip = clip.reduce_keys(10, None, tolerance=0.01)

reduced_clip.restore(mod, targets=targets, mode="replace_all")
mod.do_it_dg()
text = reduced_clip.to_json()
```

- 範囲は両端包含で、`None`側は無制限です。時間は**clipに保存されたフレーム単位**を使います。
  24fpsで保存したclipの10〜20は、sceneを30fpsへ変更しても保存時の10〜20を指します。
  負の時刻・subframeにも対応します。保存範囲そのもの、`seconds_per_frame`、`sample_by`は変更しません。
- 範囲内の最初・最後の実在キーを残し、境界キーは追加しません。3キー未満・対象なしは同内容の独立コピーです。
  定数カーブも範囲内の両端を保持し、チャンネル・空node・node順を削除しません。
- `tolerance`は必須の非負・有限数です。各保存カーブの削減前後の絶対誤差を、
  TAはdegree、TLはcm、TUはunitlessで指定します。sceneの表示単位には依存しません。
- 既存の[キー削減](attributes.md#手動接線を維持してキーを削減する)と同じ判定を使います。
  キー時刻だけでなくキー間の形状も確認し、削減途中ではなく削減開始前のカーブと比較します。
  `tolerance=0`でも浮動小数点の丸めは許容します。キー数の最小化は保証しません。
- 残すキーの時刻・値・接線type・lock・breakdownを維持し、fixed接線の方向・重みを調整しません。
  auto・linear等のMayaによる再計算も誤差判定に含めます。nonweighted接線の保存XYは、
  削減後の隣接キー間隔に合わせて再取得するため長さが変わる場合がありますが、手動接線の方向変更ではありません。
- `preserve_breakdowns=True`ではbreakdownを残します。`False`でも範囲内の両端とstep系の値の切り替わりは保護します。
  範囲外の実在キー間の形状・linear infinityの傾きも維持します。周期infinityでは変更が他の周期にも反映されます。
- layerとrootの設定カーブ（weight・mute等）は削減しません。設定の変更は共有layerの他属性にも影響し、
  等価な間引きでも既存layerとの設定一致判定が変わるためです。layer構造・順序も維持します。
- JSONから読み込んだclipや、元nodeが既にないclipも削減できます。内部評価にはMaya実行環境が必要です。
  全チャンネルの処理が成功した場合だけ結果を返し、失敗時も元clipを保持します。JSONは引き続きschema 2です。

### 許容誤差と復元先のレイヤー

許容誤差は保存データのカーブに対する値であり、復元先の最終合成値の誤差を保証しません。
preserveでは各layerの生カーブごとに判定するため、合成すると誤差が加算・増幅される場合があります。

flattenの復元は残っているキー時刻だけで値を逆算・検証します。例えば0・1・2フレームで
保存値がすべて5のclipを両端だけに削減すると、保存カーブの誤差は0です。しかし復元先の加算layerが
同時刻で0・10・0なら、元clipはベースを5・-5・5として合成値5・5・5を再現できても、
削減後のclipではベースに両端の5だけを設定し、中間の合成値が15になる場合があります。
削除した時刻を自動的に再サンプリングしたり、補償キーを追加したりする機能は含めません。

`restore(tolerance=...)`は残ったサンプル時刻の値解決を検証する別の許容誤差です。
復元先の既存キーや隣接接線も結果へ影響するため、削減前後の保存カーブの比較と復元後の結果を区別してください。

## データとJSON

```python
text = clip.to_json()
clip = bdu.AnimationClip.from_json(text)
data = clip.to_dict()
clip = bdu.AnimationClip.from_dict(data)
```

ファイルI/Oは呼び出し側で行います。JSONはschema 2のみ対応し、旧形式変換は行いません。
`nodes`・`layers`は型付きtupleです。詳細型は`bd_util.maya.node.animation_clip`からimportできます。
各カーブの`KeyData`は編集可能ですが、復元予約時に再検証・独立コピーするため、予約後の編集は
予約内容を変えません。`clipped`は範囲切り出しの有無を記録し、設定カーブの比較にも使用します。

時間は`seconds_per_frame`を保存し、移植時に秒としての位置・長さを保ちます。
例えば24fpsの24フレームは、30fpsのsceneでは30フレームへ復元されます。
復元時刻の移動・正の時間拡縮は`restore()`で指定できます。逆再生、リグ固有の属性対応、
ワールド空間への変換はこのAPIに含みません。
