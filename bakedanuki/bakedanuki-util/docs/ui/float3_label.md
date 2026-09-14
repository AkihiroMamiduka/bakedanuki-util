# XYZを表示するFloat3Label

`Float3Label`は、X・Y・Zの`FloatLabel`を横に並べる読み取り専用の複合Viewです。
同じ`Float3Binding`／`Float3ViewModel`を`Float3SpinBox`と共有し、各軸の確定値を表示します。
数値を選択してコピーでき、ラベル自体は正本への書き込みやMaya callbackの追加を行いません。

```text
X 1.235 cm   Y 2.346 cm   Z 3.457 cm
```

## 最小の組み込み

```python
from dataclasses import dataclass
from bd_util.ui import Float3Binding, Float3Label, Float3SpinBox, qt


@dataclass
class Data:
    offset: tuple[float, float, float] = (1.23456789, 2.34567891, 3.45678912)


window = qt.QWidget()
data = Data()
binding = Float3Binding.from_attribute(data, "offset", parent=window)
spin_box = Float3SpinBox(binding, window, decimals=3)
label = Float3Label(binding, window, decimals=3)
layout = qt.QVBoxLayout(window)
layout.addWidget(spin_box)
layout.addWidget(label)
window.show()

label.setDecimals(6)  # 全軸の表示だけを変更し、data.offsetの精度は維持する。
```

この例はQApplicationが存在するMaya上で実行します。
Maya属性を正本とする場合は`MayaFloat3PlugBinding`、Python正本とMaya同期は`MayaFloat3Binding`を渡します。
Store接続済みの`Float3ViewModel`も直接渡せます。入力元の検証は`Float3SpinBox`と共有します。

## 公開API

| API | 内容 |
| --- | --- |
| `Float3Label(source, parent=None, *, decimals=6)` | XYZの値を全軸共通の桁数で表示する |
| `label.view_model` | 共有する`Float3ViewModel`。終了後は例外を送出する |
| `label.x_label` / `y_label` / `z_label` | 各軸の`FloatLabel` |
| `label.decimals()` / `setDecimals(decimals)` | 全軸共通の表示桁数設定を取得・変更する |
| `label.x_label.text()` | Xの表示単位・表示精度による文字列を取得する |
| `label.x_label.setSelection(start, length)` | Xの表示文字列を選択する |

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float3`、`bd_util.ui.binding.float3.view`からimportできます。
外側余白は0で、配置先のlayoutで管理します。Widgetの`x()`／`y()`はQtの座標取得APIとして維持します。

全軸共通の桁数は0～323の整数です。各軸へ直接`setDecimals()`して異なる桁数にすることもできますが、
複合Viewの`decimals()`は最後に指定した共通設定を返します。複合Viewの`setDecimals()`で全軸を再び揃えられます。
`Float3SpinBox`や別のラベルの表示桁数には影響しません。

## 表示・単位・コピー

- 各軸の表示は[FloatLabel](float_label.md)へ委譲し、単位・locale・表示丸めの規則を共有します。
- 表示桁数を減らしても正本の精度は保持し、桁数を増やすと確定値から再表示します。
- hard limitの範囲外にある正本の値も、ラベルではclampせず表示します。
- 表示単位への換算でoverflowした軸だけを`—`と単位文字で表示します。他の軸は表示を継続します。
- 単位文字は各軸に表示します。Mayaのtranslateは現在の距離単位、rotateは角度単位、scaleは単位なしです。
- MayaのChannel Box桁数に合わせる場合は、生成時に`get_channel_box_precision()`を`decimals`へ渡します。

コピーは**軸ごと**に表示文字列を選択してCtrl+Cで行います。コピーする内容は、表示桁数と単位文字を含む文字列です。
3成分を1つのtuple文字列としてコピーする専用操作は追加していません。
正本の未丸めの数値が必要な場合は`binding.value`または`label.view_model.value.value`を参照してください。
同じ表示文字列へのrefreshでは選択を維持し、値・単位・桁数の変更で表示が変わると選択は解除されます。

## 同期と寿命

各軸の編集、一括Command、Mayaの外部変更・Undo／Redoに追従します。
Python属性への直接代入後は、既存仕様どおり`binding.refresh()`が必要です。
Python正本とMayaの同期がlockなどで保留されている場合は、Python側の確定値を表示します。

属性がlock・入力接続中・Pythonの読み取り専用属性でも、各数値ラベルの表示・選択・コピーは継続します。
Bindingの明示終了やViewModelのQObject破棄後は、各数値ラベルに最後の表示を残して無効化します。
終了後の桁数・locale変更では、終了前のデータを再描画しません。
`MayaFloat3Binding`の終了時はMaya Viewの表示変換を解除するため、Python側の単位へ戻ってから表示を保持します。

Viewは渡されたBindingとViewModelを参照保持します。ラベルだけを破棄しても、共有Bindingや他のViewを終了しません。
構築途中で失敗した場合も、共有Bindingを維持して生成途中の子Widgetを片付けます。

## サンプルと確認

```python
from bd_util._sample.maya.ui.float3_sample import maya_plug

window = maya_plug.show("pCube1")
window.widget.translate_label.setDecimals(6)
```

`maya_plug`と`maya_view`では`translate_label`・`rotate_label`・`scale_label`を既存のXYZ SpinBoxへ並べています。
`maya_view`の`linked_translate_label`は6桁、その他は起動時のChannel Box桁数を使います。
`minimal`の`value_label`は3桁、`linked_value_label`は6桁で、同じPython tupleを表示します。

1. 各軸のSpinBoxとMayaのChannel Boxで編集し、対応する値と他Viewの表示が揃うことを確認する。
2. XYZそれぞれのラベルを選択し、Ctrl+Cで表示文字列をコピーする。
3. 表示単位とラベルの桁数を変更し、元の値の精度が保たれることを確認する。
4. Maya属性をlock・接続し、編集欄が無効でもラベルの表示・コピーが継続することを確認する。
5. 一括変更・Undo／Redo・Pythonへの直接代入後のrefreshで、全軸の表示が追従することを確認する。
6. Windowを閉じて再表示し、callbackが解放され、新しいラベルが表示されることを確認する。

`tests/ui/test_float3_label.py`は表示・コピー・精度・共有・寿命、
`tests/ui/test_float3_label_maya.py`はMaya同期・単位・Undo・lock・callback・サンプル、
`tests/typecheck/float3_label_contract.py`は公開APIの型補完を検証します。
最終検証は`scripts/verify.cmd`を使用し、[UI README](README.md)へ確認結果を記載します。
