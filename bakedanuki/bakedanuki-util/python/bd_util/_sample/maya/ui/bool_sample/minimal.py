# coding: utf-8
"""Pythonのbool属性とCheckBoxを接続する最小sample。"""

from __future__ import annotations

from .....maya.ui import MayaWindowController
from .....ui import BoolBinding, BoolCheckBox, qt
from .data import VisibilityData


class MinimalBoolWidget(qt.QWidget):
    """1つのbool属性を1つのCheckBoxで編集する。"""

    def __init__(
        self,
        data: VisibilityData,
        parent: qt.QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.binding = BoolBinding.from_attribute(
            data, "visible_by_default", parent=self
        )
        self.check_box = BoolCheckBox(self.binding.view_model, "Visible", self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.check_box)


class MinimalBoolWindow(qt.QDialog):
    """最小WidgetをMaya Windowへ配置する。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("bdUtilMinimalBoolSampleWindow")
        self.setWindowTitle("bakedanuki-util bool")
        self.widget = MinimalBoolWidget(VisibilityData(), self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller = MayaWindowController(MinimalBoolWindow)


def show() -> MinimalBoolWindow:
    """最小sampleを表示する。"""
    return _controller.show()


def dispose() -> None:
    """sample Windowを終了する。"""
    _controller.dispose()
