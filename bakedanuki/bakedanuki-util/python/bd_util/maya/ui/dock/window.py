# coding: utf-8
from typing import TYPE_CHECKING

from PySide6 import QtCore, QtWidgets

if TYPE_CHECKING:

    class _MayaQWidgetDockableMixin:
        """型検査時にMaya mixinの初期化境界だけを表す。"""

        def __init__(
            self,
            parent: QtWidgets.QWidget | None = None,
            *args: object,
            **kwargs: object,
        ) -> None: ...

else:
    from maya.app.general.mayaMixin import (
        MayaQWidgetDockableMixin as _MayaQWidgetDockableMixin,
    )


class MayaDockableWindow(_MayaQWidgetDockableMixin, QtWidgets.QWidget):
    """MayaのworkspaceControlへ格納できるWidgetの基底クラス。"""

    dock_closed = QtCore.Signal()
    floating_changed = QtCore.Signal(bool)

    def __init__(
        self,
        parent: QtWidgets.QWidget | None = None,
    ) -> None:
        """Mayaのdockable mixinとQWidgetを初期化する。"""
        # MayaのMixinを先頭にしたMROを通してQt Widgetを初期化する。
        super().__init__(parent=parent)

    def dockCloseEventTriggered(self) -> None:
        """workspaceControlが閉じられたことをsignalで通知する。"""
        # 子WidgetのcloseEventに依存せず、Maya側のclose通知を公開する。
        self.dock_closed.emit()

    def floatingChanged(self, isFloating: bool) -> None:
        """フローティング状態の変更をsignalで通知する。"""
        # Mayaから渡された現在の状態を利用者向けsignalへ変換する。
        self.floating_changed.emit(isFloating)
