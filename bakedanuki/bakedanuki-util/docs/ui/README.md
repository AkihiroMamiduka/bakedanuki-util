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
