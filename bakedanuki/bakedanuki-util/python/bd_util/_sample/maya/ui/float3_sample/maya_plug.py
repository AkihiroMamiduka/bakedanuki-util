# coding: utf-8
"""translate・rotate・scaleをそれぞれ3成分で編集するサンプル。"""

from __future__ import annotations

from typing import TypeAlias

from .....maya.ui import (
    MayaFloat3Plug,
    MayaFloat3PlugBinding,
    MayaWindowController,
    MayaUiStateTracker,
    create_ui_state_manager,
    get_channel_box_precision,
    resolve_float3_plug,
)
from .....ui import Float3Label, Float3RangeSliderSpinBox, qt

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
        self.translate = Float3RangeSliderSpinBox(
            self.translate_binding,
            self,
            minimum=-100,
            maximum=100,
            steps=2000,
            decimals=decimals,
            single_step=0.1,
            step_mode="multiplicative",
            minimum_width=60,
            maximum_width=60,
            value_width=max(130, 55 + 8 * decimals),
            step_width=80,
            minimum_show_buttons=False,
            maximum_show_buttons=False,
            value_show_buttons=False,
        )
        self.rotate = Float3RangeSliderSpinBox(
            self.rotate_binding,
            self,
            minimum=-180,
            maximum=180,
            steps=3600,
            decimals=decimals,
            single_step=15.0,
            step_increment=15.0,
            minimum_width=60,
            maximum_width=60,
            value_width=max(130, 55 + 8 * decimals),
            step_width=80,
            minimum_show_buttons=False,
            maximum_show_buttons=False,
            value_show_buttons=False,
        )
        self.scale = Float3RangeSliderSpinBox(
            self.scale_binding,
            self,
            minimum=0,
            maximum=3,
            steps=3000,
            decimals=decimals,
            single_step=0.01,
            step_mode="multiplicative",
            minimum_width=60,
            maximum_width=60,
            value_width=max(130, 55 + 8 * decimals),
            step_width=80,
            minimum_show_buttons=False,
            maximum_show_buttons=False,
            value_show_buttons=False,
        )
        self.translate_label = Float3Label(
            self.translate_binding, self, decimals=decimals
        )
        self.rotate_label = Float3Label(
            self.rotate_binding, self, decimals=decimals
        )
        self.scale_label = Float3Label(
            self.scale_binding, self, decimals=decimals
        )

        # 属性ごとにXYZ編集欄をまとめ、その下に共有ラベルを並べる。
        layout = qt.QVBoxLayout(self)
        for name, editor, label in (
            ("Translate", self.translate, self.translate_label),
            ("Rotate", self.rotate, self.rotate_label),
            ("Scale", self.scale, self.scale_label),
        ):
            group = qt.QGroupBox(name, self)
            column = qt.QVBoxLayout(group)
            column.addWidget(editor)
            column.addWidget(label)
            layout.addWidget(group)


class TransformFloat3Window(qt.QDialog):
    """transformの3成分編集Widgetを表示するWindow。"""

    def __init__(
        self, plugs: _TransformPlugs, parent: qt.QWidget | None = None
    ) -> None:
        """Windowの識別子を設定し、編集Widgetを配置する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilTransformFloat3SampleWindow")
        self.setWindowTitle("bakedanuki-util Transform XYZ")
        self.setMinimumWidth(720)
        # 保存先を先に準備し、失敗時にMayaのBindingを残さない。
        self.editor_settings = create_ui_state_manager(
            "float3_sample/editor_settings/maya_plug"
        )
        self.widget = TransformFloat3Widget(plugs, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)

        # 各ViewのXYZ設定を、Window配置とは別の保存先へ登録する。
        for key, editor in (
            ("translate", self.widget.translate),
            ("rotate", self.widget.rotate),
            ("scale", self.widget.scale),
        ):
            self.editor_settings.register_float3_range_slider_spin_box(
                key, editor
            )
        self.editor_settings_tracker = MayaUiStateTracker.for_window(
            self.editor_settings, self
        )


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
