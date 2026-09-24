# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued_qt_signal
from ..binding import EnumBinding
from ..store import EnumValueStore
from ..view_model import EnumViewModel
from ._source import resolve_enum_view_source


class EnumLabel(qt.QLabel):
    """確定した項目名、または未定義の整数値を表示する。"""

    def __init__(
        self,
        view_model: EnumViewModel | EnumBinding[EnumValueStore],
        parent: qt.QWidget | None = None,
    ) -> None:
        """確定した項目名を選択・コピー可能なラベルで表示する。

        未定義の整数値は ``未定義 (値)`` と表示する。

        Args:
            view_model: 表示するViewModelまたはそのBinding。
            parent: Qtの親Widget。
        """
        view_model, binding = resolve_enum_view_source(view_model)
        super().__init__(parent)
        self._view_model = view_model
        self._binding = binding
        self.setTextFormat(qt.Qt.TextFormat.PlainText)
        self.setTextInteractionFlags(
            qt.Qt.TextInteractionFlag.TextSelectableByMouse
            | qt.Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
        self._render()
        view_model.value.changed.connect(self._render)
        view_model.definition_changed.connect(self._render)
        view_model.disposed.connect(self._disable_binding)
        connect_queued_qt_signal(view_model.destroyed, self._disable_binding)

    @property
    def view_model(self) -> EnumViewModel:
        """表示対象を返す。終了済みの場合は ``RuntimeError`` を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のEnumViewModelは終了しています")
        return self._view_model

    def _render(self, *_args: object) -> None:
        if self._view_model.is_disposed:
            self._disable_binding()
            return
        vm = self._view_model
        item = vm.definition.item_for_value(vm.value.value)
        text = item.name if item is not None else f"未定義 ({vm.value.value})"
        if self.text() != text:
            self.setText(text)

    @qt.Slot()
    def _disable_binding(self) -> None:
        if qt.isValid(self):
            self.setEnabled(False)
