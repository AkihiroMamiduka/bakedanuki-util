# coding: utf-8
"""Mayaのtransform属性を編集する浮動小数点bindingのサンプル。"""

from __future__ import annotations

from typing import TypeAlias

from .....maya.ui import (
    MayaFloatPlug,
    MayaFloatPlugBinding,
    MayaWindowController,
    get_channel_box_precision,
    resolve_float_plug,
)
from .....ui import FloatSpinBox, qt

_TransformPlugs: TypeAlias = tuple[MayaFloatPlug, MayaFloatPlug, MayaFloatPlug]


class TransformFloatWidget(qt.QWidget):
    """translateX・rotateX・scaleXを独立したBindingで編集する。"""

    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        super().__init__(parent)
        decimals = get_channel_box_precision()
        self.translate_x_binding = MayaFloatPlugBinding(plugs[0], parent=self)
        self.rotate_x_binding = MayaFloatPlugBinding(plugs[1], parent=self)
        self.scale_x_binding = MayaFloatPlugBinding(plugs[2], parent=self)
        self.translate_x = FloatSpinBox(
            self.translate_x_binding, self, decimals=decimals, single_step=0.1
        )
        self.rotate_x = FloatSpinBox(
            self.rotate_x_binding, self, decimals=decimals, single_step=1.0
        )
        self.scale_x = FloatSpinBox(
            self.scale_x_binding, self, decimals=decimals, single_step=0.01
        )
        layout = qt.QFormLayout(self)
        layout.addRow("Translate X", self.translate_x)
        layout.addRow("Rotate X", self.rotate_x)
        layout.addRow("Scale X", self.scale_x)


class TransformFloatWindow(qt.QDialog):
    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.setObjectName("bdUtilTransformFloatSampleWindow")
        self.setWindowTitle("bakedanuki-util Transform")
        self.widget = TransformFloatWidget(plugs, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller: MayaWindowController[TransformFloatWindow] | None = None


def show(node_name: str) -> TransformFloatWindow:
    """既存transformの現在値を読み取り、サンプルWindowを表示する。"""
    global _controller
    plugs = (
        resolve_float_plug(node_name, "translateX"),
        resolve_float_plug(node_name, "rotateX"),
        resolve_float_plug(node_name, "scaleX"),
    )
    dispose()

    def create_window(
        parent: qt.QWidget | None = None,
    ) -> TransformFloatWindow:
        return TransformFloatWindow(plugs, parent)

    controller = MayaWindowController(create_window)
    _controller = controller
    try:
        return controller.show()
    except Exception:
        dispose()
        raise


def dispose() -> None:
    """UIとcallbackを終了する。Maya nodeや属性は残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
