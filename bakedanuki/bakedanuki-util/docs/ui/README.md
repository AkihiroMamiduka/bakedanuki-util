# UI utilities

UI utilityは、利用場所ではなく依存関係で分けます。

- `bd_util.ui`には、Mayaを直接importしない汎用Qt処理を置きます。
- `bd_util.maya.ui`には、Maya main windowやUI lifecycleへのadapterを置きます。
- 依存は`bd_util.maya.ui`から`bd_util.ui`への一方向とし、逆方向には依存させません。

## 新しいtoolへの導入

新しいMaya toolでは、次の順にUI基盤を組み込みます。

1. Mayaの通常Windowには`MayaWindowController`、workspaceControlを使うUIには
   `MayaDockableWindowController`を選ぶ。
2. controllerをmodule単位で1つ生成し、dockable Windowでは`control_id`と
   `DockRestoreSpec`のmodule・functionをrelease後も維持する。
3. 永続化する場合は`tool_name/windows/main`のような固定`settings_path`を決める。
4. Widget内部状態は全Widgetを`UiStateManager`へ登録した後、通常Windowでは
   `MayaUiStateTracker.for_window()`、dockable Windowでは`for_dockable()`へ接続する。
5. tool固有のMaya callbackはWindowをownerとする`MayaCallbackRegistry`へ登録する。
6. UIのreset操作には`reset_and_show_ui_layout()`を使い、破棄、保存状態削除、再表示の
   順序をtool側で組み直さない。
7. module reload前は`dispose()`で古いWindow、workspaceControl、Maya callbackを完全に
   破棄してからreloadする。

controllerの`retain`は既定で`False`です。タイトルバーのcloseと`controller.close()`は
Windowを完全破棄し、Windowが所有するMaya callbackも解除します。close後の再表示でも同じ
instanceとcallbackを維持する必要があるtoolだけ、`retain=True`を明示します。`dispose()`は
設定にかかわらず完全破棄するため、module reload前とUI配置resetに使用します。

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

`WindowController`は、factoryが生成した表示中のwidgetを1つ管理します。表示中に`show()`を
繰り返しても同じwidgetを返すため、意図しないtool windowの重複を防げます。

既定の`retain=False`では`WA_DeleteOnClose`を有効にし、タイトルバーのcloseと
`controller.close()`でwindowを完全破棄します。次の`show()`ではfactoryから新しいwindowを
生成します。`retain=True`ではclose後もinstanceを保持し、次の`show()`で同じwindowを
再表示します。`dispose()`は`retain`にかかわらずwindowを閉じ、Qt event loopへ削除を
予約します。

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

非表示中も同じWindowとcallbackを維持するtoolでは保持を明示します。

```python
controller = MayaWindowController(
    MyWindow,
    retain=True,
)
```

同梱sampleはMayaのScript Editorから開けます。

```python
from bd_util._sample.maya.ui import simple_window

simple_window.show()
```

`get_main_window()`はbatch MayaとMaya初期化前には`None`を返します。そのため、これらの
環境でmoduleをimportしてもMaya UIを取得しに行きません。

## Maya callbackのlifecycle管理

`MayaCallbackRegistry`は、`MEventMessage`、`MSceneMessage`、`MNodeMessage`などが返す
Maya callback IDを1つのQt ownerへ関連付けます。callback種別ごとの登録方法はMaya APIへ
委ね、解除とlifecycleだけを共通化します。

```python
from maya.api import OpenMaya as om

from bd_util.maya.ui import MayaCallbackRegistry
from bd_util.ui import qt


class MyWindow(qt.QDialog):
    def __init__(self, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)

        # Window instanceが所有するMaya callbackをまとめて管理する。
        self.maya_callbacks = MayaCallbackRegistry(self)
        callback_id = om.MEventMessage.addEventCallback(
            "SelectionChanged",
            self._on_selection_changed,
        )
        self.maya_callbacks.register(int(callback_id))

    def _on_selection_changed(self, *_args: object) -> None:
        print("selection changed")
```

登録済みIDは`callback_ids`で確認でき、`remove()`では1件、`dispose()`では全件を解除します。
全件解除は登録と逆順に行い、二重disposeとMaya側で解除済みのIDを許容します。破棄済みregistry
への追加と、同じIDの重複登録はerrorにします。

Qt ownerの`destroyed`と`MSceneMessage.kMayaExiting`でも自動解除します。さらに
`MayaWindowController.dispose()`と`MayaDockableWindowController.dispose()`は、Qtの遅延破棄や
workspaceControl削除を待たず、owner直下のregistryを即座に解除します。既定の
`retain=False`では`close()`も完全破棄を通るためcallbackを解除します。`retain=True`の
closeだけはWindow instanceとcallbackを維持し、同じinstanceの再表示で再登録されません。

Maya終了前にtool固有処理が必要な場合は`on_maya_exiting`を指定できます。処理が例外を送出しても
registryのcallback解除は必ず実行されます。

```python
self.maya_callbacks = MayaCallbackRegistry(
    self,
    on_maya_exiting=self.save_cached_state,
)
```

`MayaUiStateTracker`のMaya終了callbackもこのregistryで管理します。tool側でtracker用callbackを
個別に解除する必要はありません。

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

保存済みgeometryの復元後は、Windowのタイトル領域が現在接続されているいずれかのscreenで
操作可能か確認します。モニター切断、解像度変更、配置変更によってタイトル領域が画面外へ
移動した場合は、現在のWindowと最も広く重なるscreen、Maya親Windowのscreen、Windowへ割り当て
済みのscreen、primary screenの順に補正先を選びます。元のサイズを可能な限り維持し、screenの
available geometryを超える場合は収まる大きさへ変更して中央へ配置します。

既に操作可能なWindowは変更しません。表示中のWindowを明示的に確認する場合は、汎用Qt APIの
`ensure_window_on_screen()`を使用できます。戻り値はgeometryを補正した場合だけ`True`です。

```python
from bd_util.ui import ensure_window_on_screen

ensure_window_on_screen(window)
```

`settings_path`はplatformにかかわらず`/`で区切ります。絶対path、`.`、`..`、空segment、
Windows予約名や使用できない文字は拒否されます。

## Widget内部状態の保存

`UiStateManager`は、明示登録したWidgetの内部状態を同じtool単位の`ui.ini`へ保存します。
第一弾では次のWidgetに対応しています。

- `QSplitter`: 分割位置
- `QTabWidget`: 現在選択されているタブ

`QHeaderView`の列幅・表示順は対応対象に含めません。MayaのworkspaceControlでは終了時の
layout変更とWidget破棄の順序により、利用中のheader stateを安定して取得・復元できなかった
ためです。必要なtoolでは`UiStateManager`へ含めず、tool側の要件に合わせて個別に管理します。
`bd_util.ui.qt.QHeaderView`は通常のUI構築用Qt facadeとして引き続き利用できます。

Mayaでは`create_ui_state_manager()`から生成し、`MayaUiStateTracker`でMaya終了前の保存を
管理します。

```python
from bd_util.maya.ui import MayaUiStateTracker, create_ui_state_manager


self.ui_state = create_ui_state_manager(
    "rig_editor/windows/main",
)
self.ui_state.register_splitter(
    "main_splitter",
    self.main_splitter,
)
self.ui_state.register_tab_widget(
    "main_tabs",
    self.main_tabs,
)

# 通常Windowでは全Widgetの登録後にlifecycle連携済みtrackerを生成する。
self.ui_state_tracker = MayaUiStateTracker.for_window(
    self.ui_state,
    self,
)
```

dockable Windowでは`for_dockable()`を使用します。

```python
self.ui_state_tracker = MayaUiStateTracker.for_dockable(
    self.ui_state,
    self,
)
```

Maya終了時はQtの`closeEvent()`や`destroyed`だけでは保存処理の実行順を保証できません。
`MayaUiStateTracker`は`MSceneMessage.kMayaExiting`を受け、Widgetから終了時に再取得せず、
変更signalで退避済みの状態を保存します。ownerの破棄時にはMaya callbackを解除します。

`MayaUiStateTracker.for_dockable()`は`MayaDockableWindow`のlifecycle signalへ次の処理を
接続します。

- `dock_attached`: workspaceControl接続後、次のQt event loopで一度だけ復元
- `dock_closed`: workspaceControlのclose時に退避済み状態を保存
- `dock_about_to_dispose`: 完全破棄前に保存してMaya callbackを解除
- `destroyed`: 外部から破棄された場合も退避済み状態を保存してcallbackを解除

controllerが接続完了と完全破棄前を通知するため、tool側の`show()`、`restore()`、`dispose()`で
trackerを個別に呼び出す必要はありません。

`MayaUiStateTracker.for_window()`は通常Windowへevent filterを設定し、次の処理を接続します。

- 初回`Show`: 次のQt event loopで一度だけ復元
- `Close`: 退避済み状態を保存
- `destroyed`: `Close`を通らない外部破棄では退避済み状態を保存し、callbackを解除
- Maya終了: 退避済み状態を保存し、callbackを解除

`MayaWindowController.dispose()`は`Close`後にQt event loopへ破棄を予約します。close時点で保存済みの
Windowは、遅れて`destroyed`が届いても二重保存しません。これによりUI配置リセットでINIを削除した
後に、古いWindowの状態が復活することを防ぎます。

```python
def show():
    return controller.show()


def restore():
    return controller.restore()
```

`MayaUiStateTracker.restore()`は次のQt event loopで一度だけ復元します。通常Windowの表示または
workspaceControl接続後のlayout計算を待って内部状態を適用し、同じWindowの再表示では保存済み状態を
再適用しません。`for_window()`と`for_dockable()`を使用する場合、tool側から`restore()`や`save()`を
個別に呼び出す必要はありません。

`clear()`はWidget内部状態だけを削除し、同じgroupに保存されたgeometryや他のtool設定は変更しません。

Splitter移動とTab選択変更はsignalでmemoryへ退避し、通常closeまたはMaya終了時にまとめて
永続化します。

`save()`は生存中のWidgetから現在状態を取得してQSettingsへ書き込みます。
`MayaUiStateTracker.save()`はMaya終了処理中のlayout状態で上書きせず、変更時に退避した状態を
`save_cached()`で永続化します。C++ objectが破棄済みの場合や、有効なまま初期状態へ戻った
場合でも、利用中の最新状態を維持できます。

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
windows/main/ui_state/widgets/main_tabs/type
windows/main/ui_state/widgets/main_tabs/state
```

### 通常Windowでのlifecycle統合確認

同梱sampleをMayaのScript Editorから表示できます。

```python
from bd_util._sample.maya.ui import simple_window

simple_window.show()
```

次の操作で、通常Windowの自動保存・復元とリセットを確認します。

1. Splitter幅と選択タブを変更する。
2. `Close`後に`simple_window.show()`を実行し、新しいWindowへ状態が復元されることを確認する。
3. 表示中に`simple_window.show()`を再実行し、同じWindowが前面へ移動することを確認する。
4. `Reset layout`でWindowが再生成され、初期geometry、Splitter幅、選択タブへ戻ることを確認する。
5. Mayaを終了・再起動して`simple_window.show()`を実行し、Splitter幅と選択タブが復元されることを確認する。

## UI配置の統合リセット

`reset_ui_layout()`は、controllerの完全破棄と保存済みUI配置の削除を正しい順序でまとめて
実行します。通常Windowとdockable Windowの両方に利用でき、reset後はWindowを閉じた状態に
します。

```python
from bd_util.maya.ui import reset_and_show_ui_layout, reset_ui_layout


def reset_layout() -> bool:
    return reset_ui_layout(
        controller,
        "tool_name/windows/main",
    )


def reset_and_show_layout():
    return reset_and_show_ui_layout(
        controller,
        "tool_name/windows/main",
    )
```

通常Windowでは`dispose()`後にgeometry、QMainWindow state、Widget内部状態を削除します。
dockable Windowでは`reset_workspace_state()`によってworkspaceControl本体とMayaの保存配置も
削除してから、同じINI stateを削除します。dispose時のclose eventやlifecycle trackerによる
最終保存より後にINIをclearするため、resetした値が直後に復活しません。

既定ではWindow stateとWidget内部状態の両方を削除します。片方を維持する場合は
`clear_window_state=False`または`clear_widget_state=False`を指定します。同じsettings pathに
保存されたtool固有設定や、別のsettings pathは削除しません。通常WindowのWindow stateを
削除する場合、settings pathは`MayaWindowController`へ指定した保存先と一致させます。

ユーザー操作からresetする場合は`reset_and_show_ui_layout()`を使うと、保存配置の削除後に
同じcontrollerから初期状態のWindowを再生成して返します。通常Windowとdockable Windowの
どちらでも具体的なWindow型が戻り値へ維持されます。QSettingsのclearが失敗した場合は、
古い配置を復元しないよう再表示せず`RuntimeError`を送出します。

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
        retain=False,
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

`DockOptions.retain`の既定値は`False`です。タイトルバーのcloseと`controller.close()`で
workspaceControlとWidgetを削除し、Windowが所有するMaya callbackも解除します。次の
`show()`では保存済みworkspace配置へ新しいWidgetを接続します。`retain=True`ではMaya標準の
closeでworkspaceControlを非表示にし、同じWidgetとcallbackを維持します。

`controller.dispose()`は`retain`にかかわらずworkspaceControlとWidgetを完全に削除するため、
開発中のmodule reload前にも利用できます。`controller.reset_workspace_state()`は完全破棄に
加えてMayaが保存した配置も削除し、次回表示で`DockOptions`の初期値を適用します。

floating workspaceControlは`show()`と`restore()`のlayout接続後、次のQt event loopで外枠の
タイトル領域を確認します。現在接続中のscreenから外れている場合だけ、Mayaが位置管理に使う
floating最上位Widgetへ`ensure_window_on_screen()`を適用します。Maya 2025では内容Widgetの
直接の親が同名の`QWidget`になるため、その親階層から最上位Windowを取得します。docked状態、
Maya main window、内側のWidget geometryは変更しないため、Mayaのworkspace layout管理とは
競合しません。

表示後に明示的な確認が必要な場合はcontrollerから実行できます。

```python
controller.ensure_on_screen()
```

Qtが接続中と認識しているscreenは補正対象外です。モニターの電源OFF後もOS上で接続中の場合は
そのscreenの保存配置を維持します。

`DockOptions.allowed_area`は移動を許可する領域を制限し、既定値の`DockArea.ALL`では全領域を
許可します。`MayaDockableWindow.dock_closed`と`floating_changed`を使うと、Maya側で閉じた
ときとドッキング状態が変わったときをtool固有処理へ通知できます。

同梱sampleはMayaのScript Editorから開けます。

```python
from bd_util._sample.maya.ui import dockable_window

dockable_window.show()
```

sampleは`retain=False`を使用します。close後の`show()`で新しいWidgetが生成され、Splitter幅と
選択タブが復元されることを確認できます。

### 実Mayaでのlifecycle統合確認

開発用ハーネスをMayaのScript Editorから表示できます。

```python
from bd_util._dev.maya.ui import dock_lifecycle

dock_lifecycle.show()
```

このハーネスは既定の破棄policyを検証するため`retain=False`を指定しています。

次の操作で、workspaceControlとWidget内部状態を実Maya上で確認します。

1. Splitter幅と選択タブを変更する。
2. `Close`後の`dock_lifecycle.diagnose()`でWindowとcallbackが残っていないことを確認する。
3. `dock_lifecycle.show()`を実行し、新しいWidgetへ状態が復元されることを確認する。
4. floatingとdockを切り替え、event logへ変更が記録されることを確認する。
5. Mayaを終了・再起動し、workspaceControl、Splitter幅、選択タブが復元されることを確認する。
6. `Reset`でWindowが再生成され、初期配置と初期Widget状態へ戻ることを確認する。

同じハーネスには`SelectionChanged` callbackも登録されています。次の操作でcallbackの寿命を
確認できます。

1. Maya上で選択を変更し、event logへ`selection_changed`が1行追加されることを確認する。
2. `Close`後に`dock_lifecycle.diagnose()`を実行し、`callback_ids`が空であることを確認する。
3. `dock_lifecycle.show()`で新しいWindowを生成し、選択変更ごとに1行だけ追加されることを確認する。
4. `dock_lifecycle.dispose()`後にmoduleをreloadし、古いcallbackによる二重記録がないことを確認する。

管理中の利用側callback IDは診断結果から確認できます。

```python
from pprint import pprint

pprint(dock_lifecycle.diagnose()["callback_ids"])
```

floating workspaceControlの画面外救済は、Script Editorから次の順に確認できます。

```python
from maya import cmds
from bd_util._dev.maya.ui import dock_lifecycle

dock_lifecycle.show()
cmds.workspaceControl(
    "bdUtilDockLifecycleHarnessWorkspaceControl",
    edit=True,
    floating=True,
)
```

floating表示へ切り替わった後、test用の画面外座標へ移動します。

```python
dock_lifecycle.move_offscreen_for_test()
```

明示APIまたは通常の`show()`で現在のscreenへ戻ることを確認します。

```python
dock_lifecycle.ensure_on_screen()

# 再度画面外へ移動した場合は、show後の遅延処理でも自動補正される。
dock_lifecycle.move_offscreen_for_test()
dock_lifecycle.show()
```

同名の直下workspace widget、実際に補正するfloating外枠、Qtが認識しているscreenは次で
確認できます。

```python
from pprint import pprint

pprint(dock_lifecycle.diagnose())
```

module reloadは古いcontrollerとMaya callbackを残さないよう、完全破棄後に実行します。

```python
from importlib import reload
from bd_util._dev.maya.ui import dock_lifecycle

dock_lifecycle.dispose()
reload(dock_lifecycle)
dock_lifecycle.show()
```

### 状態保存の責務

ドッキング位置、タブ構成、ドック幅、フローティング状態はMayaのworkspaceControlへ委ねます。
内側のWidgetへ`WindowStateStore.restoreGeometry()`を適用するとMaya側の復元と競合するため、
dockable Widgetのgeometry保存には使用しません。

tool固有のSplitter幅や選択タブは`UiStateManager`でtool単位の`ui.ini`へ
保存します。Window geometryとは別の`ui_state` groupで管理するため、dockable Windowでも
同じ仕組みを利用できます。

## Maya 2025 / 2026 / 2027 UI互換性確認

Qt facade、Window lifecycle、Maya UI adapterの自動テストは、対応する各Mayaの`mayapy`で
同じコマンドから実行できます。

```powershell
.\scripts\test-ui-maya2025.cmd
.\scripts\test-ui-maya2026.cmd
.\scripts\test-ui-maya2027.cmd

# 3 versionを順番に確認する。
.\scripts\test-ui-maya-all.cmd
```

各versionでは、Maya、Python、Qt bindingの実バージョンを表示した後、汎用Qt/UIテストと
Maya APIを使うUIテストを独立したmayapy processで実行します。pytestはrepository直下の
`.test`から読み込み、統一検証では`.\scripts\verify.cmd`が3 versionを実行します。

2026-08-22時点の確認結果です。

| Maya | Python | Qt binding | `tests/ui` | `tests/maya/ui` |
| --- | --- | --- | --- | --- |
| 2025 | 3.11.4 | PySide6 6.5.3 | 71 passed | 50 passed |
| 2026 | 3.11.9 | PySide6 6.5.3 | 71 passed | 50 passed |
| 2027 | 3.13.9 | PySide6 6.8.3 | 71 passed | 50 passed |

Maya 2027のPySide6 6.8では、bound methodを指定するsignal切断が`RuntimeWarning`になるため、
ownerの`destroyed`接続は`QMetaObject.Connection`を保持し、その接続オブジェクトを使って
解除します。この方法はMaya 2025 / 2026同梱のPySide6 6.5でも利用できます。

mayapyでは実際のworkspaceControl表示やMaya再起動後の復元までは確認できません。各versionの
Maya Script Editorで次を実行し、同じハーネスを表示します。

```python
from pprint import pprint

from bd_util._dev.maya.ui import dock_lifecycle

window = dock_lifecycle.show()
pprint(dock_lifecycle.diagnose())
```

各versionで、次の共通項目を確認します。

1. dockとfloatingの切り替え、`Close`後の再表示、`Dispose`後の再生成ができる。
2. Splitter幅、選択タブ、workspaceControlがMaya再起動後に復元される。
3. `SelectionChanged`が1操作につき1行だけ記録され、module reload後に重複しない。
4. `Reset`で初期配置と初期Widget状態へ戻り、新しいWindowが表示される。
5. floating時に`move_offscreen_for_test()`後の`ensure_on_screen()`で画面内へ戻る。

詳しい操作手順は前節の「実Mayaでのlifecycle統合確認」を参照してください。

## 保守時に維持する設計境界

UI基盤を変更・拡張するときは、次のcontractを維持します。

- `bd_util.ui`はMayaをimportせず、Maya固有処理は`bd_util.maya.ui`へ置く。
- PySideとshibokenは利用側から直接importせず、`bd_util.ui.qt`をbinding境界とする。
- dockable Windowの配置はworkspaceControlへ委ね、内側のWidgetへ通常Window用geometryを
  復元しない。
- Maya終了時にWidgetから状態を再取得せず、変更signalで退避済みの状態を保存する。
- ownerの`destroyed`接続は`QMetaObject.Connection`を保持して解除し、PySideのversion差を
  bound methodの再検索へ依存させない。
- closeの既定は`retain=False`とし、WindowとMaya callbackを完全破棄する。非表示中も処理を
  継続する明確な要件があるtoolだけ`retain=True`を指定する。
- QHeaderViewの列幅・表示順は共通保存へ追加せず、必要なtoolが個別に管理する。
- Qt facade、Window lifecycle、Maya UI adapterの変更中は`test-ui-maya-all.cmd`で
  切り分け、最終確認は`verify.cmd`を実行する。
  workspaceControl、再起動復元、実画面配置に関わる変更は各versionのMaya本体でも確認する。
