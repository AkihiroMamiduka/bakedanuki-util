# SliderとSpinBoxをまとめるFloatSliderSpinBox

`FloatSliderSpinBox`は、`FloatSlider`と`FloatSpinBox`を横に並べた単一値の複合Viewです。
1つのWidgetとしてlayoutへ追加し、内部の両Viewで同じBinding／ViewModelを共有します。
値の同期・単位変換・Undoは既存の基盤を使い、複合View独自の値やMaya callbackは追加しません。

## 最小の組み込み

```python
from dataclasses import dataclass

from bd_util.ui import FloatBinding, FloatSliderSpinBox, qt


@dataclass
class Data:
    weight: float = 0.123456789


window = qt.QWidget()
data = Data()
binding = FloatBinding.from_attribute(data, "weight", parent=window)
editor = FloatSliderSpinBox(
    binding, window, minimum=0, maximum=1, decimals=3, single_step=0.01
)
layout = qt.QVBoxLayout(window)
layout.addWidget(editor)
window.show()
```

この例はQApplicationが存在するMaya上で実行します。初期表示で小数3桁に丸めても、
`data.weight`は`0.123456789`を維持します。

Maya正本なら`MayaFloatPlugBinding`、Python正本とMaya同期なら`MayaFloatBinding`を渡します。
単体Viewと同じく、`FloatViewModel`を直接渡すこともできます。

## 公開API

| API | 内容 |
| --- | --- |
| `FloatSliderSpinBox(source, parent=None, *, minimum, maximum, steps=1000, decimals=6, single_step=0.1)` | 水平方向の複合Viewを生成する |
| `editor.view_model` | 共有ViewModelを返す。明示終了・Qt破棄後は例外を送出する |
| `editor.slider` | 内部の`FloatSlider`を具体型で返す |
| `editor.spin_box` | 内部の`FloatSpinBox`を具体型で返す |

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float`からimportできます。
レイアウトの外側余白は0で、追加した先のlayoutで余白を管理します。
Widgetへのフォーカス要求はSpinBoxへ渡します。各子Viewへ直接フォーカスを設定することもできます。

設定変更は、対象の子Viewへ明示的に行います。

```python
editor.slider.setFloatRange(-10, 10)
editor.spin_box.setDecimals(6)
editor.spin_box.setSingleStep(0.25)

# 正本の値の取得・変更は、共有するBindingから行う。
binding.set_value(3.125)
print(binding.value)
```

`editor.slider.value()`はQtの整数位置、`editor.spin_box.value()`は丸められた表示単位の値です。
正本の公開値を扱う場合は`binding.value`または`editor.view_model.value.value`を使用します。

## 範囲・精度・単位

- `minimum`／`maximum`はスライダーの操作範囲です。公開単位で指定し、Mayaの距離はcm、角度はdegreeです。
- `steps`はスライダーの分割数です。操作範囲と正本のhard limitの共通範囲を等分します。
- `decimals`はSpinBoxの表示・入力桁数です。
- `single_step`はSpinBoxの**表示単位**での刻み幅です。

スライダーの操作範囲をSpinBoxの入力範囲へ転用しません。例えばスライダーが0～1でも、
正本のhard limitが許せばSpinBoxから3.125を入力できます。この場合、正本とSpinBoxは3.125を保持し、
つまみだけを端へ寄せます。スライダーに有効な操作範囲がない場合も、SpinBoxは独立して入力できます。

単位・範囲・表示桁数の変更や位置への丸めは、正本へ書き戻しません。
Pythonのsetterが値を補正・拒否した場合も、両Viewは正本の確定値へ表示を揃えます。

Mayaの表示単位への追従とChannel Boxの表示桁数の扱いは、単体Viewと同じです。
Channel Boxの桁数を使用する場合は、生成時に`get_channel_box_precision()`を`decimals`へ渡します。

## 入力とUndo・寿命

Sliderのドラッグ中はMayaと他のViewへ即時反映し、一連のMaya書き込みをUndo 1回にまとめます。
SpinBoxの文字入力はEnter／フォーカス移動で確定し、各変更は従来どおり個別のUndo対象です。
詳細な操作単位、MayaのUndo chunk、Python正本の制約は[FloatSlider](float_slider.md)を参照してください。

SpinBoxで未確定の数値を入力してからSliderへフォーカスを移した場合は、その数値を先に確定します。
SliderからSpinBoxへフォーカスを戻すと、進行中のドラッグを確定終了します。

複合Widgetのclose・hide・非アクティブ化時は、その内部Sliderが開始した編集だけを終了します。
非表示の親の中にある場合も終了し、別の共有Viewによる編集には干渉しません。
子Viewと複合Viewを破棄しても、共有Bindingや正本は終了しません。
Bindingを渡した場合は複合Viewが参照保持し、Viewだけを保持する構成にも対応します。

正本が読み取り専用、lock・接続中などの場合、各子Viewが既存のCommandの実行可否へ追従します。
表示をコピーしたい場合は、同じBindingを使う`FloatLabel`を隣へ配置できます。
複合Viewの生成に失敗した場合は子Widgetを片付け、共有Bindingは保持します。

## サンプルと確認

既存の`maya_plug.py`・`minimal.py`・`maya_view.py`は、このクラスを継承する
[FloatRangeSliderSpinBox](float_range_slider_spin_box.md)を使用し、両端の範囲編集も確認できます。
共有ラベルと、各子Viewへの従来のサンプル変数も引き続き使用できます。

```python
from bd_util._sample.maya.ui.float_sample import maya_plug

window = maya_plug.show("pCube1")
editor = window.widget.translate_x_editor
```

`translate_x_editor`・`rotate_x_editor`・`scale_x_editor`が複合Viewです。
Python正本とMaya同期の`maya_view`には`linked_translate_x_editor`も配置しています。
Pythonだけの`minimal`では`editor`と`linked_editor`を使います。
入力範囲や初期値適用の方針は既存サンプルと同じです。

1. SliderとSpinBoxから編集し、相互の表示・共有Label・Mayaの値が揃うことを確認する。
2. Sliderの操作範囲外の値をSpinBoxから入力し、正本を保持することを確認する。
3. ドラッグを終了して数値入力し、Undoを2回実行してそれぞれの操作前へ戻ることを確認する。
4. 表示単位の追従を確認する。Channel Boxの表示桁数は、変更後にWindowを再表示して確認する。
5. Windowを閉じて再表示し、古いViewやcallbackが残らないことを確認する。

`tests/ui/test_float_slider_spin_box.py`は複合Viewの入力・設定・寿命、
`tests/ui/test_float_slider_spin_box_maya.py`はMaya同期・Undo・サンプル、
`tests/typecheck/float_slider_spin_box_contract.py`は型補完を検証します。
最終検証は`scripts/verify.cmd`を使い、結果は[UI README](README.md#maya-2025--2026--2027-ui互換性確認)へ記載します。
