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

## Mayaへドッキング可能なWindow

`MayaDockableWindow`と`MayaDockableWindowController`は、Mayaの`workspaceControl`を
利用して1つのdockable Widgetを管理します。通常windowとはMaya側のlifecycleが異なるため、
`MayaWindowController`とは別のcontrollerとして提供します。

```python
from PySide6 import QtWidgets

from bd_util.maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
)


class MyWindow(MayaDockableWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Maya tool")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Dockable content"))


controller = MayaDockableWindowController(
    MyWindow,
    control_id="myMayaTool",
    restore=DockRestoreSpec(
        module="my_tool.ui.main_window",
        function="restore",
    ),
    dock_options=DockOptions(
        area=DockArea.RIGHT,
        floating=False,
        initial_width=420,
        retain=True,
    ),
)


def show() -> MyWindow:
    return controller.show()


def restore() -> MyWindow:
    return controller.restore()
```

`control_id`はQtの`objectName`として使われ、上の例ではMaya側に
`myMayaToolWorkspaceControl`が作成されます。Mayaの保存状態と対応付けるため、release後は
同じIDを維持してください。1つのIDにつき1つのWidgetを管理します。

`DockRestoreSpec`には、Maya再起動時にもimportできるmoduleと復元関数を指定します。
controllerが生成した`uiScript`からその関数が呼ばれ、`restore()`がMayaの復元中のlayoutへ
Widgetを接続します。lambdaやlocal関数は復元先に指定できません。

`controller.close()`は`retain`設定に従ってworkspaceControlを閉じ、Widgetの参照を保持します。
`controller.dispose()`はworkspaceControlとWidgetを完全に削除するため、開発中のmodule reload
前にも利用できます。`controller.reset_workspace_state()`は完全破棄に加えてMayaが保存した
配置も削除し、次回表示で`DockOptions`の初期値を適用します。

`DockOptions.allowed_area`は移動を許可する領域を制限し、既定値の`DockArea.ALL`では全領域を
許可します。`MayaDockableWindow.dock_closed`と`floating_changed`を使うと、Maya側で閉じた
ときとドッキング状態が変わったときをtool固有処理へ通知できます。

同梱sampleはMayaのScript Editorから開けます。

```python
from bd_util._sample.maya.ui import dockable_window

dockable_window.show()
```

### 状態保存の責務

ドッキング位置、タブ構成、ドック幅、フローティング状態はMayaのworkspaceControlへ委ねます。
内側のWidgetへ`WindowStateStore.restoreGeometry()`を適用するとMaya側の復元と競合するため、
dockable Widgetのgeometry保存には使用しません。

tool固有のSplitter幅、選択タブ、Viewの列幅などは、従来どおりtool単位の`ui.ini`へ保存する
想定です。これらの内部状態を扱う共通基盤は、dockable Windowとは分離して追加できます。
