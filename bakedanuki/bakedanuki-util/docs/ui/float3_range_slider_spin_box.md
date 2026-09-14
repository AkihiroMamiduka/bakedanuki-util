# XYZの範囲とstepを編集するFloat3RangeSliderSpinBox

`Float3RangeSliderSpinBox`は、各軸の`FloatRangeSliderSpinBox`を縦3行に並べるViewです。
Min・スライダー・Max・現在値・stepを軸ごとに操作でき、値は同じBindingの他Viewと共有します。
範囲とstepはそのView・その軸だけの設定です。正本や他View、MayaのUndo履歴を変更しません。

```text
X  [ -100 ]  ───●────  [ 100 ]  [ 1.235 ]  [ 0.1 ↕ ]
Y  [ -100 ]  ────●───  [ 100 ]  [ 2.346 ]  [ 0.1 ↕ ]
Z  [ -100 ]  ─────●──  [ 100 ]  [ 3.457 ]  [ 0.1 ↕ ]
```

## 最小の組み込み

```python
import bd_util as bdu
from bd_util.maya.ui import MayaFloat3PlugBinding, get_channel_box_precision
from bd_util.ui import Float3RangeSliderSpinBox, qt

window = qt.QWidget()
nodes = bdu.Nodes()
node = nodes.existing.transform("pCube1")
binding = MayaFloat3PlugBinding(node.translate, parent=window)
editor = Float3RangeSliderSpinBox(
    binding, window,
    minimum=(-100, -50, -10), maximum=(100, 50, 10),
    decimals=get_channel_box_precision(),
    single_step=0.1, step_mode="multiplicative",
    minimum_width=60, maximum_width=60, value_width=180, step_width=80,
    minimum_show_buttons=False, maximum_show_buttons=False, value_show_buttons=False,
)
layout = qt.QVBoxLayout(window)
layout.addWidget(editor)
window.resize(720, window.sizeHint().height())
window.show()
```

QApplicationが存在するMaya上で実行し、対象transformを先に用意してください。
`Float3Binding.from_attribute()`、`MayaFloat3Binding.from_attribute()`、
Store接続済みの`Float3ViewModel`も同じViewへ渡せます。
`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float3`、`bd_util.ui.binding.float3.view`からimportできます。

## 生成時の設定

`minimum`・`maximum`は必須で、全軸共通の数値またはXYZ順の3成分Sequenceを受け取ります。
公開単位はtranslateならcm、rotateならdegree、scaleなら単位なしです。
すべての軸で有限の`minimum < maximum`を必要とし、子Widget生成前に全軸の範囲を検証します。

その他は[単一値版](float_range_slider_spin_box.md)と同名・同じ既定値で、生成時に全軸へ適用します。

| 引数 | 既定値 | 内容 |
| --- | --- | --- |
| `steps` | `1000` | 各軸のスライダー分割数 |
| `decimals` / `single_step` | `6` / `0.1` | 現在値の表示桁数・表示単位での刻み幅 |
| `step_mode` / `step_increment` | `"additive"` / `1.0` | step欄を加算、または10倍／1/10倍で操作する設定 |
| `slider_width` / `minimum_width` / `maximum_width` / `value_width` / `step_width` | `None` | 指定時は固定幅、未指定の欄は余白に応じて伸縮 |
| `minimum_enabled` / `maximum_enabled` / `value_enabled` / `step_enabled` | `True` | 各数値欄の入力可否 |
| `minimum_show_buttons` / `maximum_show_buttons` / `value_show_buttons` / `step_show_buttons` | `True` | 各数値欄の上下ボタン表示 |
| `minimum_decimals` / `maximum_decimals` | `0` | 範囲入力欄の表示桁数 |
| `minimum_show_unit` / `maximum_show_unit` / `value_show_unit` / `step_show_unit` | `False` | 各数値欄の単位文字表示 |

単位文字を隠しても入力値の単位変換は有効です。Preferences変更時は範囲の物理量を保ち、
Min・Max・現在値を新しい表示単位へ変換します。stepの数値は保ち、新しい表示単位の刻み幅として扱います。
`step_mode="multiplicative"`では15を直接入力した後も150／1.5へ操作できます。
角度用には`single_step=15, step_increment=15`で15ずつ増減する設定を使えます。

## 軸ごとの操作

`x_editor`・`y_editor`・`z_editor`は具体型が追える`FloatRangeSliderSpinBox`です。
各行に`minimum_spin_box`・`slider`・`maximum_spin_box`・`spin_box`・`step_spin_box`があります。
`x_spin_box`・`y_spin_box`・`z_spin_box`は現在値欄への短いアクセスです。

```python
editor.y_editor.setFloatRange(-20, 20)
editor.z_editor.setSingleStep(0.25)
editor.x_editor.setMinimumDecimals(2)
editor.z_editor.rangeEditRejected.connect(print)
```

範囲やstepの同期処理も含めて変更する場合は、行の`setFloatRange()`・`setSingleStep()`を使います。
Min／Max欄の不正入力はその軸だけを元の範囲へ戻し、`rangeEditRejected`と状態表示で通知します。
hard limitとの共通範囲がなければその軸のスライダーだけを無効化し、範囲を再編集できます。
数値欄からはhard limit内でスライダー範囲外の値も入力できます。

Tabは各行のMin・スライダー・Max・現在値・stepから次の軸へ進みます。
View全体へのフォーカスはXの現在値へ入り、`value_enabled=False`ならXのスライダーへ入ります。

## 同期・Undo・寿命

各成分の同期は既存のscalar Viewと`Float3ViewModel`を使います。ViewはMaya callbackを追加しません。
ドラッグ中もMayaと他Viewへ即時反映し、他2軸の未丸めの値を保持します。
Maya連携時は各軸のドラッグをUndo 1回へまとめます。別軸の操作開始や操作中の軸の範囲変更で連続編集を終了します。
他の軸・他Viewの範囲変更や、他Viewを閉じる操作では、操作中のドラッグを終了しません。

Maya正本のlock・接続時は該当軸のスライダーと現在値を無効化します。
Min・Max・stepはローカル設定として引き続き編集できます。Python正本では既存の同期保留仕様を使います。
Viewだけの破棄は共有Bindingを終了せず、BindingのdisposeやViewModelの破棄は全入力欄を停止します。
構築途中で失敗した場合も、生成途中のViewだけを片付けます。

## サンプルと確認

```python
from bd_util._sample.maya.ui.float3_sample import maya_plug

window = maya_plug.show("pCube1")
```

`maya_plug`・`maya_view`・`minimal`はこのViewと`Float3Label`を並べます。
初期範囲はtranslateが±100 cm、rotateが±180 degree、scaleが0～3で、分割数は2000・3600・3000です。
初期stepは順に0.1・15・0.01、translateとscaleは10倍／1/10倍、rotateは15ずつ増減します。
`maya_view`の共有translateは±10 cm、`minimal`の共有Viewは±10と±100です。
現在値欄は起動時のChannel Box桁数、共有translateは6桁、minimalは3桁と6桁です。
数値欄の単位文字は非表示、共有ラベルには表示します。

Min／Max・stepを変更して他軸・他Viewの設定が保たれること、ドラッグの即時同期とUndo、
単位変更、lock・接続、close後の再表示を確認してください。
範囲・stepは[UiStateManagerへの明示登録](float_view_settings.md)で軸ごとに保存・復元できます。
既存の3サンプルは保存を有効にしており、close後の再生成でも各軸の設定を保持します。
初期設定へ戻す専用操作は[今後の拡張候補](float_roadmap.md)です。

`tests/ui/test_float3_range_slider_spin_box.py`は軸別設定・範囲・入力・寿命を検証します。
`tests/ui/test_float3_slider_spin_box_maya.py`は両方の3成分スライダーでMaya同期・Undo・callback・
読込回数を確認し、範囲・step編集の単位変更とUndoからの独立性も検証します。
`tests/typecheck/float3_range_slider_spin_box_contract.py`は子Widgetまでの型・IDE補完を検証します。
最終検証は`scripts/verify.cmd`で行い、結果は[UI README](README.md)へ記載します。
