# 整数binding

## 現在の範囲

`IntBinding`は単一の符号付き32-bit整数を`IntValueStore`へ接続します。
`IntSpinBox`・`IntLabel`・`IntSlider`は同じ`IntViewModel`を共有します。
正本には`PythonIntAttributeStore`、またはMayaのbyte・short・long属性を接続できます。
整数Step・Sliderの拡張とbdChannelBoxへの組込みまで、合意した開発範囲の
利用者確認・pushが完了しています（2026-10-16）。
Python正本をQtとMaya属性へ同期する場合は
[`MayaIntBinding`／`MayaIntPlugView`](python_int_maya_binding.md)を使用します。

`QSpinBox`はQtの`int`を使うため、公開値の範囲は
`-2147483648`から`2147483647`までです。`bool`、`float`、文字列、
この範囲を超えるPython整数は明示的に拒否します。ViewとBindingの公開値を`int`で保ち、
Mayaのdoubleカーブとの境界でも32-bit整数は正確に表現できます。

```python
from dataclasses import dataclass

from bd_util.ui import IntBinding, IntLabel, IntPresentation, IntSpinBox


@dataclass
class Settings:
    count: int = 3


settings = Settings()
binding = IntBinding.from_attribute(
    settings,
    "count",
    presentation=IntPresentation(minimum=0, maximum=100),
)
spin = IntSpinBox(binding, single_step=1)
label = IntLabel(binding)

binding.set_value(8)  # settings.countも8になる
settings.count = 12
binding.refresh()  # 外部変更をViewへ同期する
```

`IntPresentation`の`minimum`と`maximum`は正本に対する入力制約です。
省略した側は32-bitの全域を使用します。setter実行前に要求値を検証しますが、
既存値や外部変更を勝手に補正しません。外部変更後の実値が制約外でも
`IntSpinBox`はその値を表示できるよう、一時的にQt側の表示範囲を広げます。
`IntLabel`は小数化や桁区切りなしの十進文字列を表示します。

`IntBinding.dispose()`は変更要求を停止し、所有するQt objectの破棄を予約します。
渡されたStoreやPython objectは破棄しません。ViewだけがBindingを受け取る構成でも
Bindingへの参照を維持します。`IntSpinBox.setInputEnabled(False)`は、そのViewだけの
操作を止め、正本からの表示更新を続けます。

Mayaの整数属性では`byte`が0～255、`short`が符号付き16-bit、
`long`が符号付き32-bitです。`long`はC++の`int`に相当し、
Mayaの`int64`とは別型です。

`IntSpinBox`の通常Enter・テンキーEnterは、値を確定した後も親Windowへ伝播しません。
`select_all_on_mouse_focus=True`を指定すると、初回の文字クリックだけ全選択します。
再クリックのカーソル移動とドラッグ選択は維持します。既定値は`False`で、
取得・変更には`select_all_on_mouse_focus()`と`set_select_all_on_mouse_focus()`を使います。
bdChannelBoxではこの設定を有効にします。

## Maya属性を正本にする

`resolve_int_plug(node_name, attribute_name)`は既存のbyte・short・long属性を
型付きPlugOperatorとして解決します。単一属性は`MayaIntPlugBinding`、
複数属性は`MayaIntPlugsBinding`へ渡します。単一属性とcompoundの子属性が対象です。
配列、compound親、enum、bool、float、int64は受け付けません。

```python
from bd_util.maya.ui import MayaIntPlugBinding, resolve_int_plug
from bd_util.ui import IntLabel, IntSpinBox

plug = resolve_int_plug("myNode", "myLongAttribute")
binding = MayaIntPlugBinding(plug)
spin = IntSpinBox(binding)
label = IntLabel(binding)
```

初期化時はMaya属性へ書き込まず、現在値を表示します。
byteは0～255、shortは-32768～32767、longはsigned 32-bitの範囲を使い、
属性のhard limitとの共通部分を入力範囲にします。各対象の範囲は一括入力前に
検証し、失敗時は対象を変更しません。通常の未接続属性の入力はMaya Undoで一操作です。
複数属性では先頭を代表値とし、`is_mixed`と`target_states`で対象の状態を確認できます。
`apply_representative_value()`は代表の実値を編集可能な後続対象へ適用します。
異なる整数属性群を一操作で編集する場合は、
`apply_plugs_values()`へ`MayaIntValueEdit(binding, value)`または
`MayaIntOffsetEdit(binding, offset)`を渡します。後者は各対象の現在値へ差分を加えます。
両者とも全対象の範囲を先に検証し、変更を一回のUndoにまとめます。

ロック、入力接続、ノードや属性の削除に追従します。入力接続中は既定で読み取り専用です。
`edit_connected=True`を指定すると、時間カーブはAuto Key OFFで一時値、ONで現在時刻の
キーを変更します。SDKはキーを変更せず一時値を入力し、Animation LayerはMayaが選ぶ
編集先と合成結果に従います。Maya標準ではbyte属性をLayerに登録できないため、
整数Layerの対象はshort・longです。一般接続、constraint、unitConversion、共有カーブなどの
対象外条件は[複数属性Binding](plugs_binding.md#maya標準に合わせた接続属性への入力)と共通です。
bdChannelBoxはこの入力方針を使用し、上下・整列・値Pasteも同じ規則で処理します。

`key_animated=True`はAuto Keyの状態によらず既存時間カーブへキーを設定する入口です。
`edit_connected=True`との併用は拒否します。新しいキーの接線はMayaの設定に従い、
整数だからという理由でstepへ固定しません。利用側の移行は引数の明示指定だけで、
既存scene・設定・clipboard schemaの変換は不要です。

表示と同値判定にはMaya属性の整数評価値を使います。既存カーブに小数キーがあっても
自動で丸め直さず、Undoや失敗復旧では元のキー値と接線を保持します。
入力接続表示のKey Altered判定はDGの整数変換後の値で比較し、
小数補間や32-bit端の1だけの変更を誤判定しません。

## 開発完了と拡張時の確認

今回の合意範囲に未完了の実装予定はありません。整数Sliderの第三段階とbyte判定の修正も、
利用者による操作確認・pushが完了しました（2026-10-16、確認したMaya versionは未申告）。
完了時点のcommitはutilが`233f2b47`、利用側toolsが`3aee7c3`です。

| 完了した範囲 | 主なAPI・仕様 |
| --- | --- |
| Python整数の正本と共有View | `IntBinding.from_attribute()`、`IntSpinBox`、`IntLabel` |
| Maya整数属性の正本 | `resolve_int_plug()`、`MayaIntPlugBinding`、`MayaIntPlugsBinding` |
| Python正本とMayaの同期 | `MayaIntBinding`、`MayaIntPlugView` |
| 接続属性の入力 | 時間カーブ・SDK、short／longのAnimation Layer、Auto Keyと整数評価 |
| Step編集と保存 | `IntStepSpinBox`、`IntValueStepSpinBox`、`IntStepProfile` |
| Sliderと複合View | `IntSlider`、`IntSliderSpinBox`、`IntRangeSliderSpinBox`、範囲・Stepの保存復元 |
| bdChannelBoxへの組込み | 複数選択、一括入力、整列、状態操作、Copy／Paste、連続Undo、入力中断 |

### 段階ごとの完了記録

初回の基盤・サンプル・Maya属性連携・bdChannelBox組込みは利用者確認とpushが完了しています。
接続属性編集と入力操作の統一も利用者によるMaya本体確認とpushが完了しました。
Python正本とMaya属性の同期も利用者確認とpushが完了しました。
整数Step欄の加算・10倍方式、設定保存とbdChannelBoxへの組込みも利用者確認とpushが完了しました。
詳細と操作サンプルは[整数Stepの入力と保存](int_step.md)を参照してください。
整数Slider拡張は次の三段階に分け、各段階で利用者が確認・commitしました。

1. `IntSlider`単体・連続編集・Maya Undo・操作サンプル（利用者確認・push完了）
2. Sliderと数値欄・範囲設定付きSlider、範囲・Stepの保存復元（利用者確認・push完了）
3. bdChannelBoxへのSlider組込みと複数選択・中断・配置の確認（利用者確認・push完了）

第一段階の仕様とサンプルは[整数Sliderと連続編集](int_slider.md)を参照してください。
第二段階は[整数Slider複合Viewと設定保存](int_range_slider_spin_box.md)を参照してください。

`MayaIntPlugBinding`／`MayaIntPlugsBinding.hard_limits`は代表属性に明示された
`(下限, 上限)`を返し、未指定の側は`None`です。型固有範囲とsoft limitを含めません。
byteの下限・上限の組が型既定の0～255に一致する場合だけ、両側を未指定扱いとします。
同じ全範囲を明示指定した場合も同様です。0～31や10～255など、狭い範囲の両端は保持します。
Maya上で実際に片側のhard limitが未指定なら、その側だけ`None`です。
複数対象でも代表の定義を返し、値の書込みでは全対象の制限を別途検証します。
Binding終了後や代表属性が利用不能の場合は`RuntimeError`です。
bdChannelBoxはこの情報で整数Sliderを選び、型範囲を常に持つ`IntPresentation`と区別します。

第三段階の初回util検証は`scripts/verify.cmd`が終了code 0で完了しました。
Black・3 versionの型契約・Maya 2025 full pytestに加え、Maya 2025／2026／2027の
Qt UI各1092件、Maya UI各816件が成功しています。
明示hard limitの新規12件を含む整数Binding testは各versionで20件成功しました。

利用者確認で見つかったbyte判定の不備を修正しました。transform標準の
`objectColor`（short、0～7）と`overrideColor`（byte、0～31）はSlider対象です。
byteの各境界を個別に除外せず、全範囲0～255の組だけを除外します。
修正後の`scripts/verify.cmd`も終了code 0で完了しました（2026-10-16）。
Black・3 versionの型契約・Maya 2025 full pytestに加え、
Maya 2025／2026／2027のQt UI各1092件・Maya UI各826件が成功しました。
整数Binding testは各30件で、標準色属性、狭いbyte範囲、片側制限を追加確認しています。

接続編集は`tests/maya/ui/test_connected_int_binding.py`の105件で、時間カーブ・SDK・Layer、
小数キー復旧・範囲検証・整数評価・三つの値Paste APIを検証します。
Enterとマウス選択は`tests/ui/test_int_spin_box_interaction.py`の7件と既存floatの回帰テストで
確認します。`verify.cmd`を通じてMaya 2025／2026／2027ですべて通過しました。

### 拡張時に維持する仕様

- 公開値は符号付き32-bitの`int`を保ち、`bool`・小数・文字列・範囲外のPython整数を暗黙変換しません。
  Sliderの写像とStepの演算にもfloatを使わず、数値欄では32-bit両端と隣り合う整数を正確に扱います。
- Maya属性を正本にするBindingは生成時に書き込みません。Python正本の`MayaIntBinding`は
  Python初期値をMayaへ適用します。正本の選択に応じて入口を使い分けます。
- 入力制約の`IntPresentation`とSlider選別用の`hard_limits`を区別します。
  byteの0～255だけを組として除外し、0～31の下限0や10～255の上限255を失わないようにします。
- Step欄の10倍操作と、値欄へStepを加減する操作を区別します。
  Stepは1以上で、下方向は整数除算、上限超過では現在値を維持します。
  Sliderの分割数はStepから独立し、大きな範囲では全整数をSlider位置へ一対一に割り当てません。
- 範囲・StepはView設定です。変更・保存・復元で正本・scene・hard limit・Undoを変更しません。
  Slider範囲外の現在値も保持し、bdChannelBoxでSlider表示へ切り替えても保存済みStepを残します。
- 連続編集は一操作一回のUndoへまとめます。時刻・選択・範囲変更やcloseで操作を確定終了し、
  一括入力は全対象の制限を先に検証します。不正な更新で既に成功した更新まで取り消しません。
- 接続編集はMayaのAuto Keyと編集先に従います。属性の整数評価とカーブの小数キーを区別し、
  Undoや失敗復旧では元のキー値と接線を保持します。
- Viewだけの破棄では共有Bindingを終了しません。Bindingの終了では入力を止め、
  callbackを解放します。util更新時は`bd_tools.reload_package(reload_util=True)`で反映します。

### 対象外と今後の再開判断

整数2／3成分を一つの正本として扱うMVVMは、利用者の方針により今回の対象外です。
対応するcompound子を単独の整数属性として編集する機能は実装済みです。
32-bitを超えるPython整数とMayaの`int64`、time、配列・compound親も対象外です。
一般接続・constraintなどの未対応経路を一律に編集可能にはしません。

これらとbdChannelBox側のSlider範囲カスタマイズは、実装予定として確定していません。
必要な用途ができた時点で正本・入力範囲・Maya標準挙動・保存形式を確認して検討します。
Maya標準でbyteをAnimation Layerへ登録できない制約も、未完了の実装として扱いません。

### 回帰検証の入口

| 変更対象 | 主なtest |
| --- | --- |
| 整数正本・共有View・入力操作 | `tests/ui/test_int_binding.py`、`test_int_spin_box_interaction.py` |
| Maya属性とhard limit | `tests/maya/ui/test_int_plugs_binding.py`、`test_int_plug_view.py` |
| Python正本とMaya同期 | `tests/ui/test_python_int_maya_view.py` |
| 時間カーブ・SDK・Layer・値転送 | `tests/maya/ui/test_connected_int_binding.py`、`test_int_scalar_value_transfer.py` |
| Step・保存・復元・サンプル | `tests/ui/test_int_step.py` |
| Slider・複合View・連続Undo | `tests/ui/test_int_slider.py`、`test_int_slider_maya.py`、`test_int_range_slider_spin_box.py`、`test_int_range_slider_spin_box_maya.py` |
| bdChannelBoxでの一括入力・中断・Step保持 | toolsの`tests/maya/test_bd_channel_box_int.py`、`test_bd_channel_box_int_slider.py` |

公開APIを変更するときは`tests/typecheck`の整数・Python整数同期contractも更新します。
utilの実装変更後は最終入口の`scripts/verify.cmd`を使い、利用側はtoolsの
`scripts/check.cmd`と関連Maya testを確認します。Maya本体の表示・操作確認と利用者報告は、
自動テストや全対応versionでの確認とは分けて記録します。

## Python属性のサンプル

Maya Script EditorのPythonタブで次を実行します。

```python
from bd_util._sample.maya.ui.int_sample import minimal

window = minimal.show()
```

Windowには、同じ`signed_value`を共有するstep 1とstep 10の入力欄、
確定値ラベル、0～255に制限した`limited_value`入力欄があります。
「int32 最小値／最大値」で境界値を確認できます。
「先頭の入力欄を有効にする」を外しても、共有Viewからの値更新は表示されます。
「Python値を直接変更」は正本だけを変更し、「Refresh」で全Viewへ反映します。
Windowを閉じて再実行すると、新しいデータで開きます。Mayaシーンの属性は変更しません。

明示的にWindowを破棄する場合は次を実行します。

```python
minimal.dispose()
```

## Maya属性のサンプル

開発中に`bd_util`の変更を反映し、bdChannelBoxなど`bd_tools`のWindowも
開いている場合は、先にMaya Script Editorで次を実行します。
依存するWindowを破棄してからutil・toolsの順に再読込します。

```python
import bd_tools

bd_tools.reload_package(reload_util=True)
```

`bd_util.reload_package()`だけを実行すると、開いているtoolsのWindowに
古いclass参照が残り、次のノード作成や選択変更でエラーになることがあります。
その状態になった場合も上記のまとめた再読込を実行するか、Mayaを再起動します。

次をMaya Script EditorのPythonタブで実行すると、現在のシーンに二つの
検証用transformとbyte・short・long属性を作り、Windowを開きます。

```python
from bd_util._sample.maya.ui.int_sample import maya_plug

window = maya_plug.show_demo()
```

このサンプルは`edit_connected=True`を明示し、初回クリックの全選択も有効にしています。
Windowに表示されたノードの整数属性へMayaでキーやSDKを設定した後も、同じ欄から編集できます。
short・longをLayerへ登録した場合も、MayaのAuto Keyと編集先の選択に従います。

byte・shortは単一属性、longは二ノードの一括編集です。
二つのlongの初期値は異なり、「代表値に揃える」で混在解除とUndoを試せます。
MayaのChannel Boxから値やロック状態を変更すると、Windowへ同期します。
Windowを閉じても検証用ノードはシーンに残ります。
既存ノードの同名属性を試す場合は`maya_plug.show(first_name, second_name)`を使います。
`maya_plug.dispose()`はWindowとcallbackだけを破棄します。
