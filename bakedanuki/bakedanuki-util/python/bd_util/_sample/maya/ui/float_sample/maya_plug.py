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
from .....ui import FloatLabel, FloatRangeSliderSpinBox, qt

_TransformPlugs: TypeAlias = tuple[MayaFloatPlug, MayaFloatPlug, MayaFloatPlug]


class TransformFloatWidget(qt.QWidget):
    """translateX・rotateX・scaleXを独立したBindingで編集する。"""

    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        """各BindingをSlider・SpinBox・コピー可能な数値ラベルで共有する。"""
        super().__init__(parent)
        decimals = get_channel_box_precision()
        self.translate_x_binding = MayaFloatPlugBinding(plugs[0], parent=self)
        self.rotate_x_binding = MayaFloatPlugBinding(plugs[1], parent=self)
        self.scale_x_binding = MayaFloatPlugBinding(plugs[2], parent=self)
        # 操作範囲は公開単位で指定し、数値欄を固定幅・ボタンなしで省スペースにする。
        width_min_max = 40
        width_value = 100
        enabled_min_max = False
        enabled_value = True
        decimals_min_max = 0
        self.translate_x_editor = FloatRangeSliderSpinBox(
            self.translate_x_binding,
            self,
            minimum=-100,
            maximum=100,
            steps=2000,
            decimals=decimals,
            single_step=0.1,
            minimum_width=width_min_max,
            maximum_width=width_min_max,
            minimum_enabled=enabled_min_max,
            maximum_enabled=enabled_min_max,
            value_width=width_value,
            value_enabled=enabled_value,
            minimum_show_buttons=False,
            maximum_show_buttons=False,
            minimum_decimals=decimals_min_max,
            maximum_decimals=decimals_min_max,
            value_show_buttons=False,
        )
        self.rotate_x_editor = FloatRangeSliderSpinBox(
            self.rotate_x_binding,
            self,
            minimum=-180,
            maximum=180,
            steps=3600,
            decimals=decimals,
            single_step=1.0,
            minimum_width=width_min_max,
            maximum_width=width_min_max,
            minimum_enabled=enabled_min_max,
            maximum_enabled=enabled_min_max,
            value_width=width_value,
            value_enabled=enabled_value,
            minimum_show_buttons=False,
            maximum_show_buttons=False,
            minimum_decimals=decimals_min_max,
            maximum_decimals=decimals_min_max,
            value_show_buttons=False,
        )
        self.scale_x_editor = FloatRangeSliderSpinBox(
            self.scale_x_binding,
            self,
            minimum=0,
            maximum=3,
            steps=3000,
            decimals=decimals,
            single_step=0.01,
            minimum_width=width_min_max,
            maximum_width=width_min_max,
            minimum_enabled=enabled_min_max,
            maximum_enabled=enabled_min_max,
            value_width=width_value,
            value_enabled=enabled_value,
            minimum_show_buttons=False,
            maximum_show_buttons=False,
            minimum_decimals=decimals_min_max,
            maximum_decimals=decimals_min_max,
            value_show_buttons=False,
        )
        self.translate_x = self.translate_x_editor.spin_box
        self.rotate_x = self.rotate_x_editor.spin_box
        self.scale_x = self.scale_x_editor.spin_box
        self.translate_x_slider = self.translate_x_editor.slider
        self.rotate_x_slider = self.rotate_x_editor.slider
        self.scale_x_slider = self.scale_x_editor.slider
        self.translate_x_label = FloatLabel(
            self.translate_x_binding, self, decimals=decimals
        )
        self.rotate_x_label = FloatLabel(
            self.rotate_x_binding, self, decimals=decimals
        )
        self.scale_x_label = FloatLabel(
            self.scale_x_binding, self, decimals=decimals
        )
        # 同じ確定値を編集用と表示用で共有し、lock中もラベルからコピーできる。
        layout = qt.QFormLayout(self)
        for title, editor, label in (
            (
                "Translate X",
                self.translate_x_editor,
                self.translate_x_label,
            ),
            (
                "Rotate X",
                self.rotate_x_editor,
                self.rotate_x_label,
            ),
            ("Scale X", self.scale_x_editor, self.scale_x_label),
        ):
            row = qt.QHBoxLayout()
            # 伸縮するSliderだけ初期表示の操作幅を確保し、固定幅の指定は維持する。
            if editor.slider.minimumWidth() != editor.slider.maximumWidth():
                editor.slider.setMinimumWidth(160)
            row.addWidget(editor, 1)
            row.addWidget(label, 1)
            layout.addRow(title, row)


class TransformFloatWindow(qt.QDialog):
    """Maya属性の編集・表示を共有するWidgetを所有するWindow。"""

    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        """指定plugの共有表示WidgetをWindowへ配置する。"""
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
        """解決済みの既存plugを使ってWindowを生成する。"""
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
