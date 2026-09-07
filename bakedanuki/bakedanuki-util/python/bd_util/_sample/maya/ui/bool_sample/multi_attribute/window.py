# coding: utf-8
from __future__ import annotations

from ......maya.ui import MayaWindowController
from ......ui import qt
from .data import DisplayOptionsData
from .widget import DisplayOptionsWidget


class DisplayOptionsWindow(qt.QDialog):
    """複数bool属性の編集サンプルをMayaのWindowへ配置する。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("bdUtilMultiAttributeBoolSampleWindow")
        self.setWindowTitle("bakedanuki-util display options")
        self.widget = DisplayOptionsWidget(DisplayOptionsData(), self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller = MayaWindowController(DisplayOptionsWindow)


def show() -> DisplayOptionsWindow:
    """サンプルを表示する。閉じた後は初期設定のWindowを新しく作る。"""
    return _controller.show()


def dispose() -> None:
    """Windowと、その所有するBindingを終了する。"""
    _controller.dispose()
