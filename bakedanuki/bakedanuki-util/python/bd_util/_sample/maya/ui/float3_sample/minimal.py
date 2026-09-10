# coding: utf-8
"""Python属性の3成分tupleを2つのXYZ Viewで共有するsample。"""

from __future__ import annotations

from .....maya.ui import MayaWindowController
from .....ui import Float3Binding, Float3SpinBox, FloatPresentation, qt
from .data import OffsetData


class MinimalFloat3Widget(qt.QWidget):
    """各軸・一括編集と直接代入後のrefreshを確認するWidget。"""

    def __init__(
        self, data: OffsetData, parent: qt.QWidget | None = None
    ) -> None:
        """1つのPython属性を異なる桁数のXYZ Viewで共有する。"""
        super().__init__(parent)
        self.binding = Float3Binding.from_attribute(
            data,
            "offset",
            presentation=FloatPresentation(minimum=-1000, maximum=1000),
            parent=self,
        )

        # 正本の精度を保持したまま、表示桁数の違う2つのViewを作る。
        self.spin_box = Float3SpinBox(self.binding, self, decimals=3)
        self.linked_spin_box = Float3SpinBox(self.binding, self, decimals=6)
        self.data_label = qt.QLabel(self)
        self.set_value_button = qt.QPushButton("Set XYZ to (4, 5, 6)", self)
        self.set_data_button = qt.QPushButton("Set data to (7, 8, 9)", self)
        self.refresh_button = qt.QPushButton("Refresh views", self)
        self.set_value_button.clicked.connect(self._set_value)
        self.set_data_button.clicked.connect(self._set_data)
        self.refresh_button.clicked.connect(self._refresh_views)
        self.binding.changed.connect(self._on_value_changed)

        # 同期済みの表示とPythonの実値を並べ、各入力経路を試せるようにする。
        form = qt.QFormLayout()
        form.addRow("Offset (3 decimals)", self.spin_box)
        form.addRow("Offset (6 decimals)", self.linked_spin_box)
        buttons = qt.QHBoxLayout()
        for button in (
            self.set_value_button,
            self.set_data_button,
            self.refresh_button,
        ):
            buttons.addWidget(button)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.data_label)
        layout.addLayout(buttons)
        self._update_data_label()

    @qt.Slot()
    def _set_value(self) -> None:
        """Commandを通じて3成分を一括変更し、共有Viewへ反映する。"""
        self.binding.set_value((4.0, 5.0, 6.0))

    @qt.Slot()
    def _set_data(self) -> None:
        """Python属性だけを直接変更し、表示の同期を次の操作へ委ねる。"""
        self.binding.store.instance.offset = (7.0, 8.0, 9.0)
        self._update_data_label()

    @qt.Slot()
    def _refresh_views(self) -> None:
        """Python属性の最新値を両Viewへ反映する。"""
        self.binding.refresh()
        self._update_data_label()

    @qt.Slot(object)
    def _on_value_changed(self, _value: object) -> None:
        """確定した3成分の実値表示を更新する。"""
        self._update_data_label()

    def _update_data_label(self) -> None:
        """表示用の丸めを加えずPythonのtupleを表示する。"""
        self.data_label.setText(
            f"Data value: {self.binding.store.instance.offset!r}"
        )


class MinimalFloat3Window(qt.QDialog):
    """Pythonの3成分属性を編集するMaya Window。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        """新しいデータと編集Widgetを生成する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilMinimalFloat3SampleWindow")
        self.setWindowTitle("bakedanuki-util float3")
        self.widget = MinimalFloat3Widget(OffsetData(), self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller = MayaWindowController(MinimalFloat3Window)


def show() -> MinimalFloat3Window:
    """表示中なら同じWindowを前面へ出し、終了後なら新しく生成する。"""
    return _controller.show()


def dispose() -> None:
    """sample WindowとBindingを終了する。"""
    _controller.dispose()
