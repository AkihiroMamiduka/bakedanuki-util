# coding: utf-8
"""translate・rotate・scaleをそれぞれ3成分で編集するサンプル。"""

from __future__ import annotations

from typing import TypeAlias

from .....maya.ui import (
    MayaFloat3Plug,
    MayaFloat3PlugBinding,
    MayaWindowController,
    get_channel_box_precision,
    resolve_float3_plug,
)
from .....ui import Float3SpinBox, qt

_TransformPlugs: TypeAlias = tuple[
    MayaFloat3Plug, MayaFloat3Plug, MayaFloat3Plug
]


class TransformFloat3Widget(qt.QWidget):
    """3つの親属性に独立した3成分Bindingを所有する。"""

    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        """起動時の桁数を使い、各属性をXYZの行として表示する。"""
        super().__init__(parent)
        decimals = get_channel_box_precision()

        # Mayaの正本ごとにBindingを作り、単位変換と各軸の編集可否を任せる。
        self.translate_binding = MayaFloat3PlugBinding(plugs[0], parent=self)
        self.rotate_binding = MayaFloat3PlugBinding(plugs[1], parent=self)
        self.scale_binding = MayaFloat3PlugBinding(plugs[2], parent=self)
        self.translate = Float3SpinBox(
            self.translate_binding, self, decimals=decimals, single_step=0.1
        )
        self.rotate = Float3SpinBox(
            self.rotate_binding, self, decimals=decimals, single_step=1.0
        )
        self.scale = Float3SpinBox(
            self.scale_binding, self, decimals=decimals, single_step=0.01
        )
        layout = qt.QFormLayout(self)
        layout.addRow("Translate", self.translate)
        layout.addRow("Rotate", self.rotate)
        layout.addRow("Scale", self.scale)


class TransformFloat3Window(qt.QDialog):
    """transformの3成分編集Widgetを表示するWindow。"""

    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        """Windowの識別子を設定し、編集Widgetを配置する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilTransformFloat3SampleWindow")
        self.setWindowTitle("bakedanuki-util Transform XYZ")
        self.widget = TransformFloat3Widget(plugs, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller: MayaWindowController[TransformFloat3Window] | None = None


def show(node_name: str) -> TransformFloat3Window:
    """対象の3属性を検証してから既存Windowを置き換える。"""
    global _controller
    plugs = (
        resolve_float3_plug(node_name, "translate"),
        resolve_float3_plug(node_name, "rotate"),
        resolve_float3_plug(node_name, "scale"),
    )
    dispose()

    def create_window(
        parent: qt.QWidget | None = None,
    ) -> TransformFloat3Window:
        """検証済みの親plugを使ってWindowを作る。"""
        return TransformFloat3Window(plugs, parent)

    _controller = MayaWindowController(create_window)
    try:
        return _controller.show()
    except Exception:
        dispose()
        raise


def dispose() -> None:
    """Maya属性を残してWindowと全callbackを終了する。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
