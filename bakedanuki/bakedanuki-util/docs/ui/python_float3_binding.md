# Python属性の浮動小数点3成分binding

Python objectやdataclassの1属性にあるXYZのtupleを正本として、既存の`Float3SpinBox`で
編集します。[単一float版](python_float_binding.md)と同じ属性の存在・編集可否判定を使い、
各軸と全体の編集を1つの属性のsetterへまとめます。

## 最小の組み込み

```python
from dataclasses import dataclass

from bd_util.ui import Float3Binding, Float3SpinBox, qt


@dataclass
class Settings:
    offset: tuple[float, float, float] = (1.0, 2.0, 3.0)


class OffsetWidget(qt.QWidget):
    def __init__(self, data: Settings, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        self.binding = Float3Binding.from_attribute(data, "offset", parent=self)
        self.spin_box = Float3SpinBox(self.binding, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
```

`Float3Binding.from_attribute()`は`PythonFloat3AttributeStore`と専用ViewModelを生成します。
初期値を書き換えずに読み取り、`binding.store.instance`には`Settings`などの具体型を維持します。
Python属性の名前は単一の名前です。3つの独立した属性や、ドットによる属性パスは扱いません。

## 各軸と一括編集

```python
data = Settings()
binding = Float3Binding.from_attribute(data, "offset")
binding.set_value((10.0, 20.0, 30.0))
binding.view_model.x.set_value_command.execute(5.0)
print(binding.value)  # (5.0, 20.0, 30.0)
binding.dispose()
```

Xの編集では、正本から最新のXYZを読み直し、Xだけを差し替えたtupleをsetterへ1回渡します。
表示用に丸めたY・Zや、ViewModelに残っている古いY・Zは書き戻しません。
setterがY・Zも補正した場合は、その確定値を全体と各軸へ反映します。
Xが元の値のままでも、Y・Zだけの補正を検出して同期します。

`binding.set_value()`は全成分を事前検証してsetterを1回呼びます。
通常の一括変更では、中間tupleを公開せず、確定したtupleを`binding.changed`へ1回通知します。
通知先からさらに編集された場合も、最新の正本を読み直します。
同じ値への要求はsetterを呼ばず、実値に変更がなければ`changed`も通知しません。
各軸Commandの戻り値はその軸の実値が変わったかを表すため、他軸だけの補正では`False`です。

## 値と表示情報

正本の属性は3成分tupleとします。要素は有限のfloatまたはintで、公開値とsetterに渡す値は
`tuple[float, float, float]`へ正規化します。生成・読み取りだけでは元の属性を変更しません。
bool、文字列、NaN、無限大、3成分以外の値は拒否します。

`binding.set_value()`への入力は既存の3成分Commandと同じSequenceで、listや既存の
`Double3`なども渡せます。正本自体がlistや`Double3`の場合は、初期化時に拒否して型の
暗黙な置き換えを避けます。その形式を正本にしたい場合は独自の`Float3ValueStore`で変換します。
setterが返す属性の実値も3成分tupleである必要があります。

`presentation`は全軸共通の`FloatPresentation`、またはXYZごとの3成分tupleを受け取ります。
省略時は全軸とも単位なし・範囲なしです。

```python
from bd_util.ui import Float3Binding, FloatPresentation

binding = Float3Binding.from_attribute(
    data,
    "offset",
    presentation=(
        FloatPresentation(scale=0.01, suffix=" m", minimum=-100, maximum=100),
        FloatPresentation(scale=0.01, suffix=" m", minimum=-200, maximum=200),
        FloatPresentation(scale=0.01, suffix=" m", minimum=-300, maximum=300),
    ),
)
```

この例ではPython側の公開値をcmと決め、Viewでmへ変換して表示します。
単位の意味はModel側が決め、Mayaの属性型やPreferencesからは推測しません。
`minimum`／`maximum`は公開単位で指定し、`binding.store.presentations`で各軸の設定を確認できます。
小数桁数・刻み幅は既存の`Float3SpinBox`へ指定します。

一括変更は全軸の入力範囲を検証し、1軸の編集はその軸の入力範囲だけを検証します。
初期値や外部変更によって他軸が範囲外でも、編集していない軸はその実値をsetterへ渡します。
正本全体の不変条件はModelのsetterで検証します。setter適用後の実値を自動clamp・復元せず、
表示範囲を超える値も`binding.value`ではそのまま保持します。

## 外部変更、読み取り専用、失敗時の扱い

Python属性へ直接代入した場合は、`binding.refresh()`で共有Viewへ反映します。
Storeまたは`store.components[index]`の`write()`を直接呼んだ場合も同じです。
Python属性の自動監視は行いません。

```python
data.offset = (7.0, 8.0, 9.0)
binding.refresh()
```

正本がfrozen dataclassやsetterのないpropertyなら、XYZと一括Commandをすべて無効にします。
Pythonの1属性を対象にしているため、編集可否は全軸共通です。
属性がなくなった場合も、refreshや変更要求の際に検出して入力を停止します。
静的な属性構造の判定、slots・descriptorの対応範囲は単一float版と共通です。

setterが拒否・補正した場合は実値を採用します。値を変更してから例外を送出した場合も、
可能ならXYZを読み直して同期し、元の例外を呼び出し元へ返します。
値が不正になった場合やgetterが失敗する場合は全軸を無効にし、最後に同期した値を保持します。
正本を修復した後に`binding.refresh()`を呼ぶと編集可否を再確認します。
任意のsetterによる副作用を巻き戻すtransactionは提供しません。

## 共有と寿命

同じBindingを複数の`Float3SpinBox`で共有できます。
`FloatSpinBox(binding.view_model.x)`で1軸だけを別の場所に表示することもできます。
1つのViewを破棄してもBindingは終了せず、Bindingの`dispose()`やQt ownerの破棄で
残ったViewの入力を停止します。Python objectの値を削除・復元しません。
複数Windowで共有する場合は、Windowから独立したownerでBindingを管理します。

Pythonだけの変更はMayaのUndoへ登録しません。Pythonを正本としてMaya plugへも同期する場合は
[MayaFloat3Binding](python_float3_maya_binding.md)を使います。
Maya属性を正本とする場合は既存の`MayaFloat3PlugBinding`を使います。

## サンプルと検証

```python
from bd_util._sample.maya.ui.float3_sample import minimal

window = minimal.show()
```

1つの`OffsetData.offset`を3桁と6桁のXYZ Viewで共有します。

1. Xだけを編集し、他軸の実値の精度が維持されることを確認する。
2. `Set XYZ to (4, 5, 6)`で一括変更し、両Viewが同期することを確認する。
3. `Set data to (7, 8, 9)`でPython属性だけを変更する。
4. `Refresh views`で最新のtupleが両Viewへ反映されることを確認する。
5. close後に`minimal.show()`を呼び、新しいデータとWindowで再表示する。

`Data value`はPythonの実値を表示します。表示中の`show()`は同じWindowを前面へ出し、
`minimal.dispose()`はWindowとBindingを終了します。サンプルはMaya nodeを作成・変更しません。

- `tests/ui/test_python_float3_attribute_store.py`: tuple、各軸、入力範囲、読み取り専用、属性の寿命。
- `tests/ui/test_python_float3_binding.py`: 共有View、setterの全軸補正・失敗、再入、サンプル。
- `tests/typecheck/python_float3_binding_contract.py`: 正本・Store・各軸・サンプルの型とIDE補完。

最終確認は`scripts/verify.cmd`を使用し、単一float版・Maya版の回帰テストも実行します。
3 versionの結果は[UI README](README.md#maya-2025--2026--2027-ui互換性確認)に記載します。
