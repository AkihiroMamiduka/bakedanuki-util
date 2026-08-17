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
