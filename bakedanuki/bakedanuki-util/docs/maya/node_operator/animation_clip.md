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
    start_frame=None,
    end_frame=None,
    layer_mode="flatten",
    layers=None,
    sample_by=1.0,
) -> AnimationClip

clip.restore(
    modifier_manager,
    *,
    targets=None,
    namespace=None,
    mode="merge",
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

## 合成保存（既定）

`layer_mode="flatten"`では`sample_values()`と共通の評価処理を使い、最終的なplug値を保存します。
レイヤー構造は保存データに含めません。保存元のレイヤー、現在時刻、選択状態は変更しません。

`sample_by`は取得時のMaya UI時間単位で、既定は1フレームです。開始時刻から等間隔に採取し、
刻みが割り切れない場合も終了時刻を含めます。数値はlinear、bool / 整数 / enumはstepで復元します。
キー削減は自動実行しません。元カーブのキー数・接線を保持する方式ではありません。

キーのない属性も保存区間を通して評価し、一定値ならその値を持つサンプルとして保存します。
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
| `replace_range` | 部分置換 | 保存区間の既存キーを両端込みで削除して復元し、外側のキーを残す |

保存データに含まれない属性・チャンネルは置換対象にしません。
部分置換はキー保持の契約で、境界をまたぐ補間やauto接線の再計算は影響を受け得ます。
全置換ではweighted / infinityも復元します。合成保存のデータはnonweighted / constantです。
merge / 部分置換では既存カーブの
weighted / infinityを維持するため、nonweightedへの復元では接線の重みが失われます。
新規カーブでは保存したweighted / infinityを使用します。

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
時刻の移動・拡縮、リグ固有の属性対応、ワールド空間への変換はこのAPIに含みません。
