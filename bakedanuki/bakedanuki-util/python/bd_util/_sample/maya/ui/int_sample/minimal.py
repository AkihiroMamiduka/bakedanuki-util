# coding: utf-8
"""Python整数属性を複数のViewで編集するMaya Windowサンプル。"""

from __future__ import annotations

from .....maya.ui import MayaWindowController
from .....ui import (
    IntBinding,
    IntLabel,
    IntPresentation,
    IntSpinBox,
    qt,
)
from .data import IntSampleData


class MinimalIntWidget(qt.QWidget):
    """整数Viewの共有、境界値、外部変更と入力制約を操作する。"""

    def __init__(
        self,
        data: IntSampleData,
        parent: qt.QWidget | None = None,
    ) -> None:
        """符号付き32-bitと0～255のPython属性をBindingへ接続する。"""
        super().__init__(parent)
        self.signed_binding = IntBinding.from_attribute(
            data, "signed_value", parent=self
        )
        self.limited_binding = IntBinding.from_attribute(
            data,
            "limited_value",
            presentation=IntPresentation(minimum=0, maximum=255),
            parent=self,
        )

        # 一つの正本を刻み幅の異なる二つの入力欄とラベルで共有する。
        self.spin_box = IntSpinBox(self.signed_binding, self)
        self.linked_spin_box = IntSpinBox(
            self.signed_binding, self, single_step=10
        )
        self.value_label = IntLabel(self.signed_binding, self)
        self.limited_spin_box = IntSpinBox(self.limited_binding, self)
        self.limited_label = IntLabel(self.limited_binding, self)
        self.data_label = qt.QLabel(self)
        self.input_check_box = qt.QCheckBox("先頭の入力欄を有効にする", self)
        self.input_check_box.setChecked(True)
        self.input_check_box.toggled.connect(self.spin_box.setInputEnabled)

        self.minimum_button = qt.QPushButton("int32 最小値", self)
        self.maximum_button = qt.QPushButton("int32 最大値", self)
        self.set_data_button = qt.QPushButton("Python値を直接変更", self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.minimum_button.clicked.connect(self._set_minimum)
        self.maximum_button.clicked.connect(self._set_maximum)
        self.set_data_button.clicked.connect(self._set_data_values)
        self.refresh_button.clicked.connect(self._refresh_views)
        self.signed_binding.changed.connect(self._on_value_changed)
        self.limited_binding.changed.connect(self._on_value_changed)

        # rawなPython値と、最後に同期したViewの値を同時に見せる。
        form = qt.QFormLayout()
        form.addRow("signed int32（step 1）", self.spin_box)
        form.addRow("共有View（step 10）", self.linked_spin_box)
        form.addRow("確定値ラベル", self.value_label)
        form.addRow("0～255", self.limited_spin_box)
        form.addRow("制約付きラベル", self.limited_label)
        buttons = qt.QHBoxLayout()
        buttons.addWidget(self.minimum_button)
        buttons.addWidget(self.maximum_button)
        buttons.addWidget(self.set_data_button)
        buttons.addWidget(self.refresh_button)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.input_check_box)
        layout.addWidget(self.data_label)
        layout.addLayout(buttons)
        self._update_data_label()

    @qt.Slot()
    def _set_minimum(self) -> None:
        """Commandからsigned int32の最小値を設定する。"""
        self.signed_binding.set_value(-(2**31))

    @qt.Slot()
    def _set_maximum(self) -> None:
        """Commandからsigned int32の最大値を設定する。"""
        self.signed_binding.set_value(2**31 - 1)

    @qt.Slot()
    def _set_data_values(self) -> None:
        """Python正本だけを変更し、View同期をRefresh操作へ委ねる。"""
        data = self.signed_binding.store.instance
        data.signed_value = -123456789
        data.limited_value = 200
        self._update_data_label()

    @qt.Slot()
    def _refresh_views(self) -> None:
        """直接変更された両属性の実値をViewへ同期する。"""
        self.signed_binding.refresh()
        self.limited_binding.refresh()
        self._update_data_label()

    @qt.Slot(object)
    def _on_value_changed(self, _value: object) -> None:
        """ViewまたはCommandの編集後、正本の現在値を表示する。"""
        self._update_data_label()

    def _update_data_label(self) -> None:
        """表示用の型変換をせず二つのPython整数を表示する。"""
        data = self.signed_binding.store.instance
        self.data_label.setText(
            f"Python values: signed={data.signed_value}, "
            f"limited={data.limited_value}"
        )


class MinimalIntWindow(qt.QDialog):
    """Python属性の整数MVVM操作WidgetをMaya Windowへ置く。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        """新しい正本とWidgetでWindowを生成する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilMinimalIntSampleWindow")
        self.setWindowTitle("bakedanuki-util int")
        self.widget = MinimalIntWidget(IntSampleData(), self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller = MayaWindowController(MinimalIntWindow)


def show() -> MinimalIntWindow:
    """サンプルを表示し、表示中なら同じWindowを前面へ出す。"""
    return _controller.show()


def dispose() -> None:
    """サンプルWindowと所有するBindingを終了する。"""
    _controller.dispose()
