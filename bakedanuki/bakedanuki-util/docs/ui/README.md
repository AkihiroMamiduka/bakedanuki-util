# UI utilities

UI utilityは、利用場所ではなく依存関係で分けます。

- `bd_util.ui`には、Mayaを直接importしない汎用Qt処理を置きます。
- `bd_util.maya.ui`には、Maya main windowやUI lifecycleへのadapterを置きます。
- 依存は`bd_util.maya.ui`から`bd_util.ui`への一方向とし、逆方向には依存させません。

## Qt binding facade

`bd_util.ui.qt`は、Maya同梱Qt bindingのimport先を集約します。toolやパッケージ内部では
`PySide`や`shiboken`を直接importせず、このmoduleを入口として使用します。

```python
from bd_util.ui import qt


class MyWidget(qt.QWidget):
    changed = qt.Signal()

    def __init__(self) -> None:
        super().__init__()

        label = qt.QLabel("My tool")
        layout = qt.QVBoxLayout(self)
        layout.addWidget(label)
```

頻出classは`qt.QLabel`のような短いaliasで公開します。公開aliasへ含まれないAPIも、元module
から利用できます。

```python
painter_path = qt.QtGui.QPainterPath()
```

`QtCore`、`QtGui`、`QtWidgets`に加えて、`wrapInstance()`、`getCppPointer()`、`isValid()`も
同じ入口から利用できます。診断用に現在のbinding情報も公開します。

```python
qt.QT_BINDING
qt.QT_BINDING_VERSION
qt.QT_BINDING_MAJOR_VERSION
```

実行時は新しいbinding候補から順に確認し、root packageが存在しない場合だけ次の候補へ
切り替えます。発見したbinding内部のimport errorやDLLの読み込み失敗はfallbackで隠さず、
そのまま送出します。PySideとshibokenは同じversionの組み合わせで読み込みます。

現在の対応MayaはすべてPySide6です。将来bindingのimport先が変わった場合は`qt.py`の候補へ
PySideとshibokenの組み合わせを追加します。module、頻出alias、利用側のimport方法は変更
しません。公開aliasはversion間の互換性を維持する小さな集合に限定し、利用頻度の低いclassを
網羅的に列挙しません。

## WindowController

`WindowController`は、factoryが生成したwidgetを1つ保持します。`show()`を繰り返しても
同じwidgetを再利用するため、意図しないtool windowの重複を防げます。

`close()`は再表示に備えてinstanceを保持します。`dispose()`はwindowを閉じ、Qt event
loopへ削除を予約します。`WA_DeleteOnClose`などにより外部からwidgetが破棄された場合も、
次の`show()`で新しいwidgetを生成します。

`MayaWindowController`は同じlifecycle管理にMaya main windowのparentingを加えます。
factoryはMaya main windowを引数として受け取ります。

```python
from bd_util.maya.ui import MayaWindowController
from bd_util.ui import qt


class MyWindow(qt.QDialog):
    def __init__(self, parent: qt.QWidget | None = None) -> None:
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

## Widget内部状態の保存

`UiStateManager`は、明示登録したWidgetの内部状態を同じtool単位の`ui.ini`へ保存します。
第一弾では次のWidgetに対応しています。

- `QSplitter`: 分割位置
- `QHeaderView`: 列幅、表示順などQtが管理するheader state
- `QTabWidget`: 現在選択されているタブ

Mayaでは`create_ui_state_manager()`から生成します。

```python
from bd_util.maya.ui import create_ui_state_manager


self.ui_state = create_ui_state_manager(
    "rig_editor/windows/main",
)
self.ui_state.register_splitter(
    "main_splitter",
    self.main_splitter,
)
self.ui_state.register_header(
    "node_header",
    self.node_view.header(),
)
self.ui_state.register_tab_widget(
    "main_tabs",
    self.main_tabs,
)

# 全Widgetの構築と登録が完了してから復元する。
self.ui_state.restore()
```

保存時は登録したWidgetの現在値をまとめて取得します。dockable WindowではMaya側のclose通知へ
接続できます。

```python
self.dock_closed.connect(self.ui_state.save)
```

通常Windowでは`closeEvent()`などtoolの終了処理から`save()`を呼び出します。
`clear()`はWidget内部状態だけを削除し、同じgroupに保存されたgeometryや他のtool設定は
変更しません。

state keyは`main_splitter`のような固定識別子を指定します。異なるWidgetへの重複登録や、
`/`を含むkeyは拒否されます。保存時のWidget種類と登録時の種類が異なる場合や、Qtが復元
できない値は適用せず、そのWidgetの状態だけを削除します。

`save()`はそのmanagerへ登録されているkeyだけを更新します。同じsettings pathを複数の
UI componentで共有しても、別managerが保存したWidget状態は維持されます。`clear()`は
settings path配下の`ui_state`全体を削除するため、toolの「UI配置をリセット」に利用できます。

上記の例はINI内で次のように分離されます。

```text
windows/main/geometry
windows/main/ui_state/schema_version
windows/main/ui_state/widgets/main_splitter/type
windows/main/ui_state/widgets/main_splitter/state
windows/main/ui_state/widgets/node_header/type
windows/main/ui_state/widgets/node_header/state
windows/main/ui_state/widgets/main_tabs/type
windows/main/ui_state/widgets/main_tabs/state
```

## Mayaへドッキング可能なWindow

`MayaDockableWindow`と`MayaDockableWindowController`は、Mayaの`workspaceControl`を
利用して1つのdockable Widgetを管理します。通常windowとはMaya側のlifecycleが異なるため、
`MayaWindowController`とは別のcontrollerとして提供します。

```python
from bd_util.maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
)
from bd_util.ui import qt


class MyWindow(MayaDockableWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Maya tool")

        layout = qt.QVBoxLayout(self)
        layout.addWidget(qt.QLabel("Dockable content"))


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

tool固有のSplitter幅、選択タブ、Viewの列幅などは`UiStateManager`でtool単位の`ui.ini`へ
保存します。Window geometryとは別の`ui_state` groupで管理するため、dockable Windowでも
同じ仕組みを利用できます。
