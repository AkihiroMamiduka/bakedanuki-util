# 整数binding

## 現在の範囲

`IntBinding`は単一の符号付き32-bit整数を`IntValueStore`へ接続します。
`IntSpinBox`と`IntLabel`は同じ`IntViewModel`を共有します。
正本には`PythonIntAttributeStore`、またはMayaのbyte・short・long属性を接続できます。
bdChannelBoxへの組込みは後続段階で扱います。

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
Mayaの`int64`とは別型です。

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

ロック、入力接続、ノードや属性の削除に追従します。入力接続中の整数属性は
現在読み取り専用です。時間カーブ・SDK・Animation Layerへの値入力は、
各対応Mayaで実挙動を確認した後に別段階で設計します。

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

byte・shortは単一属性、longは二ノードの一括編集です。
二つのlongの初期値は異なり、「代表値に揃える」で混在解除とUndoを試せます。
MayaのChannel Boxから値やロック状態を変更すると、Windowへ同期します。
Windowを閉じても検証用ノードはシーンに残ります。
既存ノードの同名属性を試す場合は`maya_plug.show(first_name, second_name)`を使います。
`maya_plug.dispose()`はWindowとcallbackだけを破棄します。
