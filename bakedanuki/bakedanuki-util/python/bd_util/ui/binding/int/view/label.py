# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel
from ._source import resolve_int_view_source


class IntLabel(qt.QLabel):
    """整数の確定値をコピー可能なテキストで表示する。"""

    def __init__(
        self,
        view_model: IntViewModel | IntBinding[IntValueStore],
        parent: qt.QWidget | None = None,
    ) -> None:
        """BindingまたはViewModelを共有する読み取り専用Viewを作る。"""
        view_model, binding = resolve_int_view_source(view_model)
        if view_model.is_disposed:
            raise RuntimeError("表示対象のIntViewModelは終了しています")
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self.setTextFormat(qt.Qt.TextFormat.PlainText)
        self.setTextInteractionFlags(
            qt.Qt.TextInteractionFlag.TextSelectableByMouse
            | qt.Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
        self.setAlignment(
            qt.Qt.AlignmentFlag.AlignRight | qt.Qt.AlignmentFlag.AlignVCenter
        )
        self._render()
        view_model.value.changed.connect(self._update_value)
        view_model.disposed.connect(self._on_view_model_disposed)
        connect_queued(view_model.destroyed, self._on_view_model_disposed)

    @property
    def view_model(self) -> IntViewModel:
        """生存中のViewModelを返す。"""
        view_model = self._view_model
        if view_model.is_disposed:
            raise RuntimeError("表示対象のIntViewModelは終了しています")
        return view_model

    def _render(self) -> None:
        """精度変換なしの確定整数を表示する。"""
        value = self.view_model.value.value
        text = str(value)
        if text != self.text():
            self.setText(text)

    def _update_value(self, _value: object) -> None:
        """通知先の再入変更後も最新値を表示する。"""
        if not self._view_model.is_disposed:
            self._render()

    @qt.Slot()
    def _on_view_model_disposed(self) -> None:
        """最後の表示文字列を残してViewを無効にする。"""
        if qt.isValid(self):
            self.setEnabled(False)
