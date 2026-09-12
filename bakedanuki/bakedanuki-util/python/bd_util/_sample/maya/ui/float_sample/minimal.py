# coding: utf-8
"""Pythonのfloat属性をSlider・SpinBox・数値ラベルで共有する最小sample。"""

from __future__ import annotations

from .....maya.ui import MayaWindowController
from .....ui import (
    FloatBinding,
    FloatLabel,
    FloatSliderSpinBox,
    FloatPresentation,
    qt,
)
from .data import WeightData


class MinimalFloatWidget(qt.QWidget):
    """Python属性の編集と直接代入後のrefreshを確認するWidget。"""

    def __init__(
        self, data: WeightData, parent: qt.QWidget | None = None
    ) -> None:
        """1つのBindingを異なる桁数のViewで共有する。"""
        super().__init__(parent)
        self.binding = FloatBinding.from_attribute(
            data,
            "weight",
            presentation=FloatPresentation(minimum=0.0, maximum=1.0),
            parent=self,
        )

        # Viewの丸めが正本に戻らないことを、異なる表示桁数で確認する。
        self.editor = FloatSliderSpinBox(
            self.binding,
            self,
            minimum=0,
            maximum=1,
            decimals=3,
            single_step=0.01,
        )
        self.linked_editor = FloatSliderSpinBox(
            self.binding,
            self,
            minimum=0,
            maximum=1,
            decimals=6,
            single_step=0.01,
        )
        self.spin_box = self.editor.spin_box
        self.linked_spin_box = self.linked_editor.spin_box
        self.slider = self.editor.slider
        self.linked_slider = self.linked_editor.slider
        self.value_label = FloatLabel(self.binding, self, decimals=3)
        self.linked_value_label = FloatLabel(self.binding, self, decimals=6)
        self.data_label = qt.QLabel(self)
        self.set_data_button = qt.QPushButton("Set data to 0.25", self)
        self.refresh_button = qt.QPushButton("Refresh views", self)
        self.set_data_button.clicked.connect(self._set_data_value)
        self.refresh_button.clicked.connect(self._refresh_views)
        self.binding.changed.connect(self._on_value_changed)

        # Pythonの実値とViewを並べ、直接代入と同期の違いを確認できるようにする。
        form = qt.QFormLayout()
        for title, editor, label in (
            (
                "Weight (3 decimals)",
                self.editor,
                self.value_label,
            ),
            (
                "Weight (6 decimals)",
                self.linked_editor,
                self.linked_value_label,
            ),
        ):
            row = qt.QHBoxLayout()
            editor.slider.setMinimumWidth(160)
            row.addWidget(editor, 1)
            row.addWidget(label, 1)
            form.addRow(title, row)
        buttons = qt.QHBoxLayout()
        buttons.addWidget(self.set_data_button)
        buttons.addWidget(self.refresh_button)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.data_label)
        layout.addLayout(buttons)
        self._update_data_label()

    @qt.Slot()
    def _set_data_value(self) -> None:
        """正本だけを直接変更し、Viewの同期はrefresh操作へ委ねる。"""
        self.binding.store.instance.weight = 0.25
        self._update_data_label()

    @qt.Slot()
    def _refresh_views(self) -> None:
        """Python属性の現在値を読み直して両Viewへ反映する。"""
        self.binding.refresh()
        self._update_data_label()

    @qt.Slot(float)
    def _on_value_changed(self, _value: float) -> None:
        """CommandやViewから編集された正本の値を表示する。"""
        self._update_data_label()

    def _update_data_label(self) -> None:
        """表示用の丸めを加えずPython属性の実値を表示する。"""
        self.data_label.setText(
            f"Data value: {self.binding.store.instance.weight!r}"
        )


class MinimalFloatWindow(qt.QDialog):
    """Python属性を編集するWidgetをMayaのWindowへ配置する。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        """新しいサンプルデータと専用Widgetを生成する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilMinimalFloatSampleWindow")
        self.setWindowTitle("bakedanuki-util float")
        self.widget = MinimalFloatWidget(WeightData(), self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller = MayaWindowController(MinimalFloatWindow)


def show() -> MinimalFloatWindow:
    """Python属性のsampleを表示し、表示中なら同じWindowを前面へ出す。"""
    return _controller.show()


def dispose() -> None:
    """sample WindowとBindingを終了する。"""
    _controller.dispose()
