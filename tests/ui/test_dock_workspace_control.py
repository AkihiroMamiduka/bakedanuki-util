# coding: utf-8
from PySide6 import QtCore, QtWidgets

from bd_util.maya.ui import DockArea
from bd_util.maya.ui.dock import workspace_control


def test_apply_allowed_area_updates_parent_dock_widget(
    qt_application,
) -> None:
    # MayaのworkspaceControl hostに相当するQDockWidgetを用意する。
    dock_widget = QtWidgets.QDockWidget()
    window = QtWidgets.QWidget()
    dock_widget.setWidget(window)

    # 公開enumがQtのallowedAreasへ変換されることを確認する。
    assert workspace_control.apply_allowed_area(window, DockArea.LEFT)
    assert dock_widget.allowedAreas() == (
        QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
    )

    # testで生成したWidgetの削除をQt event loopへ予約する。
    dock_widget.deleteLater()
    qt_application.processEvents()


def test_apply_allowed_area_ignores_unattached_widget(
    qt_application,
) -> None:
    # workspaceControlへ格納されていないWidgetを作成する。
    window = QtWidgets.QWidget()

    # 親DockWidgetがなければ設定を適用せず終了することを確認する。
    assert not workspace_control.apply_allowed_area(window, DockArea.ALL)

    # testで生成したWidgetの削除をQt event loopへ予約する。
    window.deleteLater()
    qt_application.processEvents()


def test_ensure_on_screen_updates_floating_dock_host(
    qt_application,
    monkeypatch,
) -> None:
    # Mayaのfloating workspaceControlに相当する外枠と内容を用意する。
    control_name = "testWorkspaceControl"
    dock_widget = QtWidgets.QDockWidget()
    dock_widget.setObjectName(control_name)
    window = QtWidgets.QWidget()
    dock_widget.setWidget(window)
    checked_hosts: list[QtWidgets.QWidget] = []
    monkeypatch.setattr(workspace_control, "exists", lambda _name: True)
    monkeypatch.setattr(
        workspace_control,
        "is_floating",
        lambda _name: True,
    )

    def record_host(host: QtWidgets.QWidget) -> bool:
        """画面外補正へ渡された外枠を記録する。"""
        checked_hosts.append(host)
        return True

    monkeypatch.setattr(
        workspace_control,
        "ensure_qt_window_on_screen",
        record_host,
    )

    # 内容WidgetではなくMayaが位置管理に使うfloating最上位外枠を補正する。
    assert workspace_control.ensure_on_screen(control_name, window)
    assert checked_hosts == [dock_widget]

    # testで生成したWidgetの削除をQt event loopへ予約する。
    dock_widget.deleteLater()
    qt_application.processEvents()


def test_ensure_on_screen_finds_maya_qwidget_wrapper(
    qt_application,
    monkeypatch,
) -> None:
    # Maya 2025で確認した最上位外枠、同名QWidget、内容Widgetの階層を再現する。
    control_name = "testWorkspaceControl"
    floating_host = QtWidgets.QWidget()
    workspace_widget = QtWidgets.QWidget(floating_host)
    workspace_widget.setObjectName(control_name)
    window = QtWidgets.QWidget(workspace_widget)
    checked_hosts: list[QtWidgets.QWidget] = []
    monkeypatch.setattr(workspace_control, "exists", lambda _name: True)
    monkeypatch.setattr(
        workspace_control,
        "is_floating",
        lambda _name: True,
    )
    monkeypatch.setattr(
        workspace_control,
        "_is_maya_main_window",
        lambda _widget: False,
    )
    monkeypatch.setattr(
        workspace_control,
        "ensure_qt_window_on_screen",
        lambda host: checked_hosts.append(host) or True,
    )

    # 直接の親がQDockWidgetでなくても、親階層の最上位外枠を補正する。
    assert workspace_control.ensure_on_screen(control_name, window)
    assert checked_hosts == [floating_host]

    # testで生成したWidgetの削除をQt event loopへ予約する。
    floating_host.deleteLater()
    qt_application.processEvents()


def test_ensure_on_screen_never_updates_maya_main_window(
    qt_application,
    monkeypatch,
) -> None:
    # docked時と同様にMaya main window配下となるWidget階層を用意する。
    control_name = "testWorkspaceControl"
    maya_main_window = QtWidgets.QWidget()
    workspace_widget = QtWidgets.QWidget(maya_main_window)
    workspace_widget.setObjectName(control_name)
    window = QtWidgets.QWidget(workspace_widget)
    checked_hosts: list[QtWidgets.QWidget] = []
    monkeypatch.setattr(workspace_control, "exists", lambda _name: True)
    monkeypatch.setattr(
        workspace_control,
        "is_floating",
        lambda _name: True,
    )
    monkeypatch.setattr(
        workspace_control,
        "_is_maya_main_window",
        lambda widget: widget is maya_main_window,
    )
    monkeypatch.setattr(
        workspace_control,
        "ensure_qt_window_on_screen",
        lambda host: checked_hosts.append(host) or True,
    )

    # Maya main windowをfloating外枠として誤って移動しないことを確認する。
    assert not workspace_control.ensure_on_screen(control_name, window)
    assert checked_hosts == []

    # testで生成したWidgetの削除をQt event loopへ予約する。
    maya_main_window.deleteLater()
    qt_application.processEvents()


def test_ensure_on_screen_leaves_docked_control_to_maya(
    qt_application,
    monkeypatch,
) -> None:
    # docked workspaceControlに相当する外枠と内容を用意する。
    control_name = "testWorkspaceControl"
    dock_widget = QtWidgets.QDockWidget()
    dock_widget.setObjectName(control_name)
    window = QtWidgets.QWidget()
    dock_widget.setWidget(window)
    monkeypatch.setattr(workspace_control, "exists", lambda _name: True)
    monkeypatch.setattr(
        workspace_control,
        "is_floating",
        lambda _name: False,
    )

    # docked状態ではQt geometryを変更せずMayaのlayout管理へ委ねる。
    assert not workspace_control.ensure_on_screen(control_name, window)

    # testで生成したWidgetの削除をQt event loopへ予約する。
    dock_widget.deleteLater()
    qt_application.processEvents()


def test_schedule_ensure_on_screen_waits_for_next_event_loop(
    monkeypatch,
) -> None:
    # 遅延実行されるcallbackと補正呼び出しを記録する。
    scheduled_callbacks: list[object] = []
    calls: list[tuple[str, object]] = []
    window = object()
    monkeypatch.setattr(
        workspace_control,
        "_run_later",
        scheduled_callbacks.append,
    )
    monkeypatch.setattr(
        workspace_control,
        "ensure_on_screen",
        lambda name, target: calls.append((name, target)),
    )

    # 予約時点では実行せず、Mayaのlayout計算後に補正する。
    workspace_control.schedule_ensure_on_screen(
        "testWorkspaceControl",
        window,
    )
    assert len(scheduled_callbacks) == 1
    assert calls == []
    callback = scheduled_callbacks[0]
    assert callable(callback)
    callback()
    assert calls == [("testWorkspaceControl", window)]
