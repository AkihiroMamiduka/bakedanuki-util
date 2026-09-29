# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued_qt_signal
from ..binding import StringBinding
from ..store import StringValueStore
from ..view_model import StringViewModel
from ._source import resolve_string_view_source


class StringLabel(qt.QLabel):
    """確定文字列をplain textで選択・コピーできる表示View。"""

    def __init__(
        self,
        view_model: StringViewModel | StringBinding[StringValueStore],
        parent: qt.QWidget | None = None,
    ) -> None:
        """BindingまたはViewModelと接続し、文字列を表示する。"""
        view_model, binding = resolve_string_view_source(view_model)
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
        view_model.disposed.connect(self._on_disposed)
        connect_queued_qt_signal(view_model.destroyed, self._on_disposed)

    @property
    def view_model(self) -> StringViewModel:
        """生存中のViewModelを返す。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のStringViewModelは終了しています")
        return self._view_model

    def _render(self, *_args: object) -> None:
        """同じ表示なら選択を維持し、変更時だけ更新する。"""
        if self._view_model.is_disposed:
            return
        value = self._view_model.value.value
        if self.text() != value:
            self.setText(value)

    @qt.Slot()
    def _on_disposed(self) -> None:
        """終了後は最後の表示を残す。"""
        if qt.isValid(self):
            self.setEnabled(False)
