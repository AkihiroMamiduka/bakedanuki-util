# coding: utf-8
from collections.abc import Sequence

from .....maya.ui import (
    MayaEnumPlug,
    MayaEnumPlugsBinding,
    MayaWindowController,
    resolve_enum_plug,
)
from .....ui import EnumComboBox, EnumLabel, EnumRadioButtonGroup, qt


class EnumPlugsSampleWindow(qt.QDialog):
    """代表値・混在状態と、複数enum属性への一括入力を確認する。"""

    def __init__(
        self, plugs: Sequence[MayaEnumPlug], parent: qt.QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.setObjectName("bdUtilEnumPlugsSampleWindow")
        self.setWindowTitle("bakedanuki-util enum / Maya plugs")
        try:
            self.binding = MayaEnumPlugsBinding(plugs, parent=self)
        except Exception:
            self.deleteLater()
            raise
        self.combo_box = EnumComboBox(self.binding, self)
        self.radio_group = EnumRadioButtonGroup(self.binding, self)
        self.label = EnumLabel(self.binding, self)
        self.state_label = qt.QLabel(self)
        self.targets_label = qt.QLabel(self)
        self.error_label = qt.QLabel(self)
        for label in (self.state_label, self.targets_label, self.error_label):
            label.setTextFormat(qt.Qt.TextFormat.PlainText)
        self.apply_button = qt.QPushButton("代表値に揃える", self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.apply_button.clicked.connect(self._apply)
        self.refresh_button.clicked.connect(self._refresh)
        self.binding.changed.connect(self._render_state)
        self.binding.definition_changed.connect(self._render_state)
        self.binding.state_changed.connect(self._render_state)
        self.binding.view_model.set_value_command.can_execute_changed.connect(
            self._render_state
        )
        self.binding.edit_failed.connect(self.error_label.setText)
        layout = qt.QFormLayout(self)
        layout.addRow("代表の選択", self.combo_box)
        layout.addRow("共有View", self.radio_group)
        layout.addRow("代表の項目名", self.label)
        layout.addRow("状態", self.state_label)
        layout.addRow("対象", self.targets_label)
        layout.addRow(self.apply_button)
        layout.addRow(self.refresh_button)
        layout.addRow(self.error_label)
        self._render_state()

    def _render_state(self, *_args: object) -> None:
        if self.binding.is_disposed:
            self.apply_button.setEnabled(False)
            self.refresh_button.setEnabled(False)
            return
        binding = self.binding
        mixed = "混在" if binding.is_mixed else "一致"
        can_execute = binding.view_model.set_value_command.can_execute
        input_state = "入力可" if can_execute else "入力停止"
        self.state_label.setText(
            f"{mixed} / 編集可能 {binding.writable_count}/{binding.target_count} / {input_state}"
        )
        self.targets_label.setText(
            "\n".join(
                f"{state.name}: {state.reason or '編集可能'}"
                for state in binding.target_states
            )
        )
        self.apply_button.setEnabled(binding.is_value_defined and can_execute)

    @qt.Slot()
    def _apply(self) -> None:
        self.error_label.clear()
        try:
            self.binding.apply_representative_value()
        except Exception as error:
            self.error_label.setText(str(error))

    @qt.Slot()
    def _refresh(self) -> None:
        self.binding.refresh()


_controller: MayaWindowController[EnumPlugsSampleWindow] | None = None


def show(
    node_names: Sequence[str], attribute_name: str = "rotateOrder"
) -> EnumPlugsSampleWindow:
    """既存属性を指定順で表示する。先頭を代表とし、値は書き戻さない。"""
    global _controller
    if isinstance(node_names, str):
        raise TypeError("node_namesにはノード名のリストなどを指定してください")
    plugs = tuple(
        resolve_enum_plug(name, attribute_name) for name in node_names
    )
    dispose()
    _controller = MayaWindowController(
        lambda parent: EnumPlugsSampleWindow(plugs, parent)
    )
    return _controller.show()


def dispose() -> None:
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
