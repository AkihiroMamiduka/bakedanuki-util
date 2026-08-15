# UI utilities

UI utilityは、利用場所ではなく依存関係で分けます。

- `bd_util.ui`には、Mayaを直接importしない汎用PySide6処理を置きます。
- `bd_util.maya.ui`には、Maya main windowやUI lifecycleへのadapterを置きます。
- 依存は`bd_util.maya.ui`から`bd_util.ui`への一方向とし、逆方向には依存させません。

## WindowController

`WindowController`は、factoryが生成したwidgetを1つ保持します。`show()`を繰り返しても
同じwidgetを再利用するため、意図しないtool windowの重複を防げます。

`close()`は再表示に備えてinstanceを保持します。`dispose()`はwindowを閉じ、Qt event
loopへ削除を予約します。`WA_DeleteOnClose`などにより外部からwidgetが破棄された場合も、
次の`show()`で新しいwidgetを生成します。

`MayaWindowController`は同じlifecycle管理にMaya main windowのparentingを加えます。
factoryはMaya main windowを引数として受け取ります。

```python
from PySide6 import QtWidgets

from bd_util.maya.ui import MayaWindowController


class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("My Maya tool")


controller = MayaWindowController(MyWindow)


def show() -> MyWindow:
    return controller.show()
```

同梱sampleはMayaのScript Editorから開けます。

```python
from bd_util._sample.maya.ui import simple_window

simple_window.show()
```

`get_main_window()`はbatch MayaとMaya初期化前には`None`を返します。そのため、これらの
環境でmoduleをimportしてもMaya UIを取得しに行きません。

## Window stateの保存

`settings_path`を指定すると、windowの位置、サイズ、最大化状態をMayaのuser
preferencesへ保存します。`QMainWindow`の場合は、dockとtoolbarのstateもgeometryと
分離して保存します。

```python
controller = MayaWindowController(
    MyWindow,
    settings_path="tool_name/widget_a/func_a/my_window",
)
```

先頭segmentはtool名、それ以降はtoolのINIファイル内のgroupとして扱います。

```text
<Maya userPrefDir>/
└─ bakedanuki/
   └─ tools/
      └─ tool_name/
         └─ ui.ini
```

`ui.ini`内では次のgroupとkeyに分かれます。

```text
widget_a/func_a/my_window/geometry
widget_a/func_a/my_window/window_state
widget_a/func_a/my_window/schema_version
```

window stateはclose eventで保存されます。タイトルバーのclose、`controller.close()`、
`controller.dispose()`のいずれも同じ保存処理を通ります。`settings_path`を省略した場合は
永続化を行いません。

`settings_path`はplatformにかかわらず`/`で区切ります。絶対path、`.`、`..`、空segment、
Windows予約名や使用できない文字は拒否されます。
