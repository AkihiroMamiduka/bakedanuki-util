# coding: utf-8
from collections.abc import Iterator

import pytest

from bd_util.maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindowController,
)
from bd_util.maya.ui.dock import controller as dock_controller


class RecordingSignal:
    """Qt signalのconnect操作だけを再現するtest用object。"""

    def __init__(self) -> None:
        """接続されたcallbackを保持できる状態で初期化する。"""
        # controllerが登録した破棄通知を確認できるようlistを用意する。
        self.callbacks: list[object] = []

    def connect(self, callback: object) -> None:
        """callbackを接続済みlistへ追加する。"""
        # Qt eventを発生させず接続処理だけを記録する。
        self.callbacks.append(callback)


class RecordingDockableWindow:
    """Dockable Widgetと同じ操作を記録するtest用object。"""

    def __init__(self) -> None:
        """表示回数を記録できる状態でWidgetを初期化する。"""
        # QWidgetを作れないbatch Mayaでもcontrollerだけを検証できるよう準備する。
        self.show_arguments: list[dict[str, object]] = []
        self.closed = False
        self.deleted_later = False
        self.destroyed = RecordingSignal()
        self._object_name = ""

    def setObjectName(self, name: str) -> None:
        """Maya UIの固定名を記録する。"""
        # controllerがshow前に設定したobjectNameを保持する。
        self._object_name = name

    def objectName(self) -> str:
        """記録済みのobjectNameを返す。"""
        # Maya側のcontrol名検証に利用できる固定名を公開する。
        return self._object_name

    def show(self, *args: object, **kwargs: object) -> None:
        """表示引数を記録する。"""
        # controllerからMixinへ渡されたkeyword引数を保存する。
        self.show_arguments.append(dict(kwargs))

    def raise_(self) -> None:
        """testでは前面化を何もせず完了する。"""

    def activateWindow(self) -> None:
        """testではactive window変更を何もせず完了する。"""

    def close(self) -> None:
        """closeが呼ばれたことを記録する。"""
        # workspaceControl作成前のclose経路を検証できる状態へ変更する。
        self.closed = True

    def deleteLater(self) -> None:
        """遅延削除が予約されたことを記録する。"""
        # Qt event loopを使わずdisposeの削除経路を確認できるようにする。
        self.deleted_later = True


@pytest.fixture
def workspace_spy(monkeypatch) -> Iterator[dict[str, object]]:
    """workspaceControl操作を記録する置き換えを提供する。"""
    # Maya UIを作らずcontrollerの分岐だけを確認できる関数群を用意する。
    state: dict[str, object] = {
        "exists": False,
        "state_exists": False,
        "calls": [],
    }
    calls = state["calls"]
    assert isinstance(calls, list)

    # test用objectを生存中のQt wrapperとしてcontrollerへ扱わせる。
    monkeypatch.setattr(dock_controller, "isValid", lambda _window: True)

    monkeypatch.setattr(
        dock_controller.workspace_control,
        "exists",
        lambda _name: state["exists"],
    )
    monkeypatch.setattr(
        dock_controller.workspace_control,
        "state_exists",
        lambda _name: state["state_exists"],
    )

    # 各操作名と引数を共通listへ記録する。
    for name in (
        "restore",
        "close",
        "delete",
        "remove_state",
        "unregister",
    ):
        monkeypatch.setattr(
            dock_controller.workspace_control,
            name,
            lambda control_name, operation=name: calls.append(
                (operation, control_name)
            ),
        )

    monkeypatch.setattr(
        dock_controller.workspace_control,
        "register",
        lambda control_name, window: calls.append(
            ("register", control_name, window)
        ),
    )
    monkeypatch.setattr(
        dock_controller.workspace_control,
        "current_parent",
        lambda: 101,
    )
    monkeypatch.setattr(
        dock_controller.workspace_control,
        "find_control",
        lambda control_name: 202,
    )
    monkeypatch.setattr(
        dock_controller.workspace_control,
        "attach",
        lambda window, parent: calls.append(("attach", window, parent)),
    )
    monkeypatch.setattr(
        dock_controller.workspace_control,
        "apply_allowed_area",
        lambda window, area: calls.append(
            ("apply_allowed_area", window, area)
        ),
    )
    monkeypatch.setattr(
        dock_controller.workspace_control,
        "tab_to",
        lambda control_name, target: calls.append(
            ("tab_to", control_name, target)
        ),
    )
    yield state


def _create_controller() -> MayaDockableWindowController:
    """test共通のdockable controllerを生成する。"""
    # 固定ID、復元関数、初期ドッキング設定をまとめて作成する。
    return MayaDockableWindowController(
        RecordingDockableWindow,
        control_id="sampleDock",
        restore=DockRestoreSpec("sample_tool.ui"),
        dock_options=DockOptions(
            area=DockArea.RIGHT,
            initial_width=360,
            tab_to_control="AttributeEditor",
        ),
    )


def test_show_creates_workspace_control(
    workspace_spy,
) -> None:
    # workspaceControlが存在しない状態で初回表示する。
    controller = _create_controller()
    window = controller.show()

    # 固定名とDockOptionsがMixinへ渡されることを確認する。
    assert window.objectName() == "sampleDock"
    assert window.show_arguments == [
        {
            "dockable": True,
            "floating": False,
            "area": "right",
            "allowedArea": "all",
            "retain": True,
            "uiScript": (
                "from bd_util.maya.ui import restore_dockable; "
                "restore_dockable('sample_tool.ui', 'restore')"
            ),
            "width": 360,
        }
    ]
    assert ("tab_to", "sampleDockWorkspaceControl", "AttributeEditor") in (
        workspace_spy["calls"]
    )
    assert (
        "apply_allowed_area",
        window,
        DockArea.ALL,
    ) in workspace_spy["calls"]


def test_restore_attaches_window_to_current_parent(
    workspace_spy,
) -> None:
    # MayaのuiScriptから呼ばれる復元経路を実行する。
    controller = _create_controller()
    window = controller.restore()

    # current parentへWidgetを接続しMixinへ登録することを確認する。
    assert ("attach", window, 101) in workspace_spy["calls"]
    assert (
        "register",
        "sampleDockWorkspaceControl",
        window,
    ) in workspace_spy["calls"]
    assert (
        "apply_allowed_area",
        window,
        DockArea.ALL,
    ) in workspace_spy["calls"]


def test_show_restores_existing_workspace_control(
    workspace_spy,
) -> None:
    # Maya側に保存済みcontrolだけが存在する状態を作る。
    workspace_spy["exists"] = True
    controller = _create_controller()

    # controlを復元して新しいWidgetを既存layoutへ接続する。
    window = controller.show()
    assert ("restore", "sampleDockWorkspaceControl") in workspace_spy["calls"]
    assert ("attach", window, 202) in workspace_spy["calls"]
    assert window.show_arguments == []


def test_close_and_dispose_have_different_lifecycle(
    workspace_spy,
) -> None:
    # 表示済みのworkspaceControlが存在する状態へ切り替える。
    controller = _create_controller()
    window = controller.show()
    workspace_spy["exists"] = True

    # closeはinstanceを保持し、disposeはcontrolごと完全破棄する。
    controller.close()
    assert controller.window is window
    assert ("close", "sampleDockWorkspaceControl") in workspace_spy["calls"]

    controller.dispose()
    assert controller.window is None
    assert ("delete", "sampleDockWorkspaceControl") in workspace_spy["calls"]


def test_reset_removes_saved_workspace_state(
    workspace_spy,
) -> None:
    # Maya側にcontrol本体と保存済みstateがある状態を作る。
    workspace_spy["exists"] = True
    workspace_spy["state_exists"] = True
    controller = _create_controller()

    # 実体の破棄後に保存済みstateも削除されることを確認する。
    controller.reset_workspace_state()
    calls = workspace_spy["calls"]
    assert ("delete", "sampleDockWorkspaceControl") in calls
    assert ("remove_state", "sampleDockWorkspaceControl") in calls


def test_controller_rejects_unstable_control_id() -> None:
    # Maya UI名として安定しない区切り文字を含むIDを拒否する。
    with pytest.raises(ValueError):
        MayaDockableWindowController(
            RecordingDockableWindow,
            control_id="sample/dock",
            restore=DockRestoreSpec("sample_tool.ui"),
        )
