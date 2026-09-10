# Python属性の浮動小数点binding

Python objectやdataclassの数値属性を正本として、既存の`FloatSpinBox`で編集します。
リグ構築前の設定値など、Maya nodeへ保存しないツール内のパラメーターに使用します。
役割分担は[MVVM](mvvm_roles.md)と同じで、`PythonFloatAttributeStore`がPython属性を
読み書きし、既存の`FloatViewModel`とViewへ接続します。

## 最小の組み込み

```python
from dataclasses import dataclass

from bd_util.ui import FloatBinding, FloatSpinBox, qt


@dataclass
class Settings:
    weight: float = 0.5


class WeightWidget(qt.QWidget):
    def __init__(self, data: Settings, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        self.binding = FloatBinding.from_attribute(data, "weight", parent=self)
        self.spin_box = FloatSpinBox(self.binding, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
```

`FloatBinding.from_attribute()`は`PythonFloatAttributeStore`と専用ViewModelを組み立てます。
初期値はPython属性から読み取り、生成時に属性を書き換えたり作成したりしません。
`binding.store.instance`は`Settings`など入力objectの具体型を維持し、IDEで属性を辿れます。

## 公開APIと同期

| 入口 | 内容 |
| --- | --- |
| `PythonFloatAttributeStore(instance, attribute_name, presentation=None)` | 単一のPython属性を読み書きするStore。`presentation`はkeyword引数 |
| `FloatBinding.from_attribute(instance, attribute_name, presentation=None, parent=None)` | StoreとBindingを生成する入口。後ろの2引数はkeyword引数 |
| `binding.store.instance` / `attribute_name` | 正本のobjectと属性名 |
| `binding.value` / `changed(float)` | 最後に同期した確定値と変更通知 |
| `binding.set_value(value)` | 公開単位で変更を要求し、実値が変わったか返す |
| `binding.refresh()` | 正本の実値と編集可否を再取得する |
| `binding.dispose()` | 入力・同期を停止してQt objectの破棄を予約する |

同じBindingを複数の`FloatSpinBox`へ渡せます。Viewごとに`decimals`や`single_step`を
指定でき、表示の丸めでPython属性の精度を変更しません。入力確定の規則は
[scalar View](float_binding.md#入力精度範囲)と共通です。

Viewまたは`binding.set_value()`から変更すると、setter適用後の属性を読み直して
確定値として採用します。setterが丸めた値や変更を受け付けなかった結果も表示に反映し、
実値が変わった場合だけ`changed`を通知します。

Python属性への直接代入は明示的な`refresh()`で同期します。

```python
data = Settings()
binding = FloatBinding.from_attribute(data, "weight")
binding.set_value(0.75)  # data.weightと共有Viewへ反映する。

data.weight = 0.25
binding.refresh()  # 直接代入後の値を共有Viewへ反映する。
binding.dispose()
```

`store.write()`を直接呼ぶ場合も、Viewへの反映には`binding.refresh()`を使用します。
Python属性の自動監視やMaya nodeへの同期は行いません。

## 型、単位、範囲

有限のfloatとintを読み取り、公開値をfloatへ正規化します。
bool、文字列、None、NaN、無限大は拒否し、文字列からの暗黙変換は行いません。
初期値がintでも読み取りでobjectを書き換えず、Storeからの書き込みにはfloatを渡します。
属性名は単一の名前です。ドットによる入れ子アクセスや配列要素の解決は行いません。

Pythonのfloatには距離・角度の情報がないため、既定では単位なし・範囲なしです。
必要な表示倍率・suffix・範囲はimmutableな`FloatPresentation`で生成時に指定します。

```python
from bd_util.ui import FloatBinding, FloatPresentation

binding = FloatBinding.from_attribute(
    data,
    "weight",
    presentation=FloatPresentation(
        scale=100.0, suffix=" %", minimum=0.0, maximum=1.0
    ),
)
```

この設定では、Pythonの`0.5`をViewで`50 %`と表示します。
`binding.set_value(0.75)`や`binding.value`はPython側の公開単位で、Viewで入力した`75`は
`0.75`へ変換して正本へ渡します。Mayaの距離・角度の設定から単位を推測しません。

`minimum`／`maximum`は公開単位での入力範囲です。Storeは範囲外の要求をsetterの
実行前に拒否します。単位変換と範囲の表示は既存の`FloatSpinBox`へ委ねます。
小数桁数や刻み幅は`FloatSpinBox`側に指定し、Python属性やStoreでは丸めません。

範囲はこのStoreを経由する変更要求に適用します。初期値、直接代入された値、setterが
補正した結果にはPython objectの実値を優先し、自動clampや復元を行いません。
正本が範囲外の場合、Viewの表示はSpinBoxの範囲内に制限されても`binding.value`は実値を保持します。
object全体の不変条件が必要な場合は、Modelのsetterでも検証します。

## 編集可否、例外、寿命

通常属性、dataclass、slots、property、書き込み可能なdescriptorを扱います。
frozen dataclassとsetterのないpropertyは表示専用です。
`is_available`／`is_writable`はgetterを実行せず、静的な属性構造を確認します。
`__getattr__()`だけで提供する動的属性は対象外です。

構造上書き込み可能でも、setterや`__setattr__()`が要求を拒否する場合があります。
例外は隠さず呼び出し元へ返し、ViewModelは可能なら書き込み後の実値を読み直します。
読み直せない場合はCommandを無効化します。属性を修復した後に`binding.refresh()`を呼ぶと、
利用・編集可否を再確認します。GUI入力時の例外処理は既存の`FloatSpinBox`と共通です。

属性がなくなった場合も、`refresh()`や変更要求の際に検出して入力を無効化します。
Python本来の属性検索に従うため、instance属性を削除してもクラスdefaultが残っていれば
その値を読み取ります。

Bindingは専用ViewModelをQtの子として所有します。複数Windowで共有する場合は、
各Windowから独立したownerを指定します。1つのViewを閉じてもBindingは終了せず、
Bindingの`dispose()`やownerの破棄で残ったViewの入力を停止します。
渡したPython objectや外部Storeの所有権は移さず、値を削除・復元しません。

Pythonデータの変更はMayaのUndoへ登録しません。これは既存のPython bool版と同じ扱いです。
Python属性の3成分版と、Pythonを正本としてMaya plugへ同期する構成は後続対応です。

## サンプルと検証

```python
from bd_util._sample.maya.ui.float_sample import minimal

window = minimal.show()
```

1つの`WeightData.weight`を3桁と6桁のSpinBoxで共有します。
`Data value`はPythonの実値を表示します。

1. 一方のSpinBoxを編集し、もう一方と`Data value`が更新されることを確認する。
2. `Set data to 0.25`でPython属性だけを変更し、Viewの表示がそのままであることを確認する。
3. `Refresh views`で両Viewへ現在値が反映されることを確認する。
4. close後に`minimal.show()`を呼び、新しいデータとWindowで再表示できることを確認する。

表示中の`show()`は同じWindowを前面へ出します。`minimal.dispose()`で明示終了できます。
サンプルはMaya nodeやcallbackを作成せず、Channel Boxの表示設定にも依存しません。

- `tests/ui/test_python_float_attribute_store.py`: 属性の構造、有限値、範囲、setter、利用可否。
- `tests/ui/test_python_float_binding.py`: 共有View、外部変更、失敗復旧、寿命、サンプル。
- `tests/typecheck/python_float_binding_contract.py`: Store・Binding・正本の型とIDE補完。

最終確認は`scripts/verify.cmd`を使用します。
3 versionの結果は[UI README](README.md#maya-2025--2026--2027-ui互換性確認)に記載します。
