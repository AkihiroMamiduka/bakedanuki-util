# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued_qt_signal
from ..binding import EnumBinding
from ..definition import EnumDefinition, require_enum_value
from ..store import EnumValueStore
from ..view_model import EnumViewModel
from ._source import resolve_enum_view_source


def _require_enabled(value: object) -> bool:
    if not isinstance(value, bool):
        raise TypeError("enabledにはboolを指定してください")
    return value


class EnumRadioButtonGroup(qt.QWidget):
    """enumの整数値を排他的なRadioButtonで選択するView。"""

    def __init__(
        self,
        view_model: EnumViewModel | EnumBinding[EnumValueStore],
        parent: qt.QWidget | None = None,
        *,
        orientation: qt.Qt.Orientation = qt.Qt.Orientation.Horizontal,
    ) -> None:
        """定義中の各項目に対応するラジオボタンを生成する。

        Args:
            view_model: 表示する ViewModel またはその Binding。
            parent: Qt の親 Widget。
            orientation: ボタンの横並びまたは縦並び。

        Raises:
            ValueError: ``orientation`` が水平・垂直以外の場合。
        """
        if orientation not in (
            qt.Qt.Orientation.Horizontal,
            qt.Qt.Orientation.Vertical,
        ):
            raise ValueError(
                "orientationにはHorizontalまたはVerticalを指定してください"
            )
        view_model, binding = resolve_enum_view_source(view_model)
        super().__init__(parent)
        self._view_model = view_model
        self._binding = binding
        self._orientation = orientation
        self._input_enabled = True
        self._definition: EnumDefinition | None = None
        self._buttons: dict[int, qt.QRadioButton] = {}
        self._button_values: dict[qt.QtWidgets.QAbstractButton, int] = {}
        self._button_group = qt.QtWidgets.QButtonGroup(self)
        self._button_group.setExclusive(True)
        self._layout = (
            qt.QHBoxLayout(self)
            if orientation == qt.Qt.Orientation.Horizontal
            else qt.QVBoxLayout(self)
        )
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addStretch()
        self._render()
        self._button_group.buttonClicked.connect(self._request_button)
        view_model.value.changed.connect(self._render)
        view_model.definition_changed.connect(self._render)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )
        view_model.disposed.connect(self._disable_binding)
        connect_queued_qt_signal(view_model.destroyed, self._disable_binding)

    @property
    def view_model(self) -> EnumViewModel:
        """表示対象を返す。終了済みの場合は ``RuntimeError`` を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のEnumViewModelは終了しています")
        return self._view_model

    @property
    def buttons(self) -> tuple[qt.QRadioButton, ...]:
        """現在の定義順でボタンを返す。定義変更時には作り直される。"""
        return tuple(self._buttons.values())

    def button_for_value(self, value: int) -> qt.QRadioButton | None:
        """整数値に対応するボタンを返す。未定義ならNoneを返す。"""
        return self._buttons.get(require_enum_value(value))

    def orientation(self) -> qt.Qt.Orientation:
        """構築時に指定したボタンの配置方向を返す。"""
        return self._orientation

    def isInputEnabled(self) -> bool:
        """この View 固有の入力許可設定を返す。"""
        return self._input_enabled

    def setInputEnabled(self, enabled: bool) -> None:
        """この View からの入力を許可または停止する。

        Args:
            enabled: 入力を許可する場合は ``True``。

        Raises:
            TypeError: ``enabled`` が ``bool`` でない場合。
        """
        self._input_enabled = _require_enabled(enabled)
        self._update_enabled()

    def _update_enabled(self, *_args: object) -> None:
        self.setEnabled(
            self._input_enabled
            and not self._view_model.is_disposed
            and self._view_model.set_value_command.can_execute
        )

    def _replace_buttons(self, definition: EnumDefinition) -> None:
        # 公開済みの buttons は定義変更後に無効となるため、古い Widget を破棄する。
        for button in self._buttons.values():
            self._button_group.removeButton(button)
            self._layout.removeWidget(button)
            button.setEnabled(False)
            button.hide()
            button.deleteLater()
        self._buttons.clear()
        self._button_values.clear()
        # 項目名の & は Qt のニーモニックにせず、表示文字として扱う。
        for index, item in enumerate(definition.items):
            button = qt.QRadioButton(item.name.replace("&", "&&"), self)
            button.setAccessibleName(item.name)
            button.setAutoExclusive(False)
            self._button_group.addButton(button)
            self._layout.insertWidget(index, button)
            self._buttons[item.value] = button
            self._button_values[button] = item.value
        self._definition = definition

    def _render(self, *_args: object) -> None:
        if self._view_model.is_disposed:
            self._disable_binding()
            return
        vm = self._view_model
        if self._definition != vm.definition:
            self._replace_buttons(vm.definition)
        blockers = [qt.QtCore.QSignalBlocker(self._button_group)]
        blockers.extend(
            qt.QtCore.QSignalBlocker(button) for button in self.buttons
        )
        # 排他状態のままでは現在の選択を解除できないため、一時的に解除する。
        self._button_group.setExclusive(False)
        try:
            for value, button in self._buttons.items():
                button.setChecked(value == vm.value.value)
        finally:
            self._button_group.setExclusive(True)
            blockers.clear()
        self._update_enabled()

    def _request_button(self, button: qt.QtWidgets.QAbstractButton) -> None:
        vm = self._view_model
        if vm.is_disposed:
            self._disable_binding()
            return
        if not self._input_enabled or button not in self._button_values:
            self._render()
            return
        try:
            vm.set_value_command.execute(self._button_values[button])
        finally:
            if qt.isValid(self):
                self._render()

    @qt.Slot()
    def _disable_binding(self) -> None:
        if qt.isValid(self):
            self.setEnabled(False)
