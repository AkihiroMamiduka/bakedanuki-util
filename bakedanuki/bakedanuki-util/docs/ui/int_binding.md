# 整数binding

## 現在の範囲

`IntBinding`は単一の符号付き32-bit整数を`IntValueStore`へ接続します。
`IntSpinBox`と`IntLabel`は同じ`IntViewModel`を共有します。
この段階の正本は`PythonIntAttributeStore`です。Maya属性への接続、複数属性の
一括編集、bdChannelBoxへの組込みは後続段階で扱います。

`QSpinBox`はQtの`int`を使うため、公開値の範囲は
`-2147483648`から`2147483647`までです。`bool`、`float`、文字列、
この範囲を超えるPython整数は明示的に拒否します。値を`float`へ変換しないので、
境界付近でも整数の精度を失いません。

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
Mayaの`int64`とは別型です。Maya側の型ごとの検証、Undo、
接続状態の扱いはMaya binding段階で追加します。

## Mayaで操作するサンプル

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
