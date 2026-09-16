# coding: utf-8
from collections.abc import Callable

from .....ui import EnumBinding, EnumComboBox, EnumLabel, EnumValueStore, qt


class EnumSampleWindow(qt.QDialog):
    """2つの選択Viewとラベルで同じBindingを共有する。"""

    def __init__(
        self,
        create_binding: Callable[[qt.QObject], EnumBinding[EnumValueStore]],
        title: str,
        parent: qt.QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("bdUtilEnumSampleWindow")
        self.setWindowTitle(title)
        try:
            self.binding = create_binding(self)
        except Exception:
            self.deleteLater()
            raise
        self.combo_box = EnumComboBox(self.binding, self)
        self.linked_combo_box = EnumComboBox(self.binding, self)
        self.label = EnumLabel(self.binding, self)
        self.value_label = qt.QLabel(self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self._refresh)
        self.binding.changed.connect(self._render_value)
        self.binding.definition_changed.connect(self._render_value)
        layout = qt.QFormLayout(self)
        layout.addRow("選択", self.combo_box)
        layout.addRow("共有View", self.linked_combo_box)
        layout.addRow("項目名", self.label)
        layout.addRow("整数値", self.value_label)
        layout.addRow(self.refresh_button)
        self._render_value()

    def _render_value(self, *_args: object) -> None:
        self.value_label.setText(str(self.binding.value))

    @qt.Slot()
    def _refresh(self) -> None:
        self.binding.refresh()
        self._render_value()
