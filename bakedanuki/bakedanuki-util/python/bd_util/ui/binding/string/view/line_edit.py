# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued_qt_signal
from ..binding import StringBinding
from ..store import StringValueStore
from ..view_model import StringViewModel
from ._source import resolve_string_view_source


class StringLineEdit(qt.QLineEdit):
    """文字列を編集中は保持し、確定時だけCommandへ渡す一行View。"""

    conflict_changed = qt.Signal(bool)

    def __init__(
        self,
        view_model: StringViewModel | StringBinding[StringValueStore],
        parent: qt.QWidget | None = None,
    ) -> None:
        """同じBindingを共有する複数Viewから編集できる入力欄を作る。"""
        view_model, binding = resolve_string_view_source(view_model)
        super().__init__(parent)
        self._view_model = view_model
        self._binding = binding
        self._input_enabled = True
        self._dirty = False
        self._conflicted = False
        # Qtの既定32767文字による正本の黙った切り詰めを防ぐ
        self.setMaxLength(2_147_483_647)
        self._render()
        self._update_enabled()
        self.textEdited.connect(self._on_text_edited)
        self.returnPressed.connect(self._commit_explicit)
        self.editingFinished.connect(self._commit_on_focus_loss)
        view_model.value.changed.connect(self._on_value_changed)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )
        view_model.disposed.connect(self._on_disposed)
        connect_queued_qt_signal(view_model.destroyed, self._on_disposed)

    @property
    def view_model(self) -> StringViewModel:
        """生存中のViewModelを返す。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のStringViewModelは終了しています")
        return self._view_model

    def isInputEnabled(self) -> bool:
        """このView固有の入力許可を返す。"""
        return self._input_enabled

    def setInputEnabled(self, enabled: bool) -> None:
        """コピーを保ったまま、このViewからの編集だけを切り替える。"""
        if type(enabled) is not bool:
            raise TypeError("enabledにはboolを指定してください")
        self._input_enabled = enabled
        if not enabled:
            self._render()
        self._update_enabled()

    def hasConflict(self) -> bool:
        """編集中に正本が外部更新された場合は`True`。"""
        return self._conflicted

    def keyPressEvent(self, arg__1: qt.QtGui.QKeyEvent) -> None:
        """Escapeで未確定入力を破棄し、最新の正本を表示する。"""
        if arg__1.key() == qt.Qt.Key.Key_Escape and self._dirty:
            self._render()
            arg__1.accept()
            return
        super().keyPressEvent(arg__1)

    def _on_text_edited(self, _text: str) -> None:
        """ユーザー編集だけを未確定入力として記録する。"""
        self._dirty = self.text() != self._view_model.value.value
        if not self._dirty:
            self._set_conflicted(False)

    def _on_value_changed(self, _value: str) -> None:
        """入力中の外部更新は保持し、それ以外は最新値を表示する。"""
        if self._dirty:
            self._set_conflicted(True)
            return
        self._render()

    def _commit_explicit(self) -> None:
        """Enterによる確定は競合中でも明示入力として扱う。"""
        self._commit(explicit=True)

    def _commit_on_focus_loss(self) -> None:
        """通常のフォーカス移動では競合した入力を書き込まない。"""
        self._commit(explicit=False)

    def _commit(self, *, explicit: bool) -> None:
        """未確定入力を一回だけ正本へ渡し、実値へ表示を戻す。"""
        if not self._dirty:
            return
        if self._conflicted and not explicit:
            return
        view_model = self._view_model
        if (
            view_model.is_disposed
            or not self._input_enabled
            or not view_model.set_value_command.can_execute
        ):
            self._render()
            return
        requested = self.text()
        self._dirty = False
        try:
            view_model.set_value_command.execute(requested)
        finally:
            if qt.isValid(self):
                self._render()

    def _render(self) -> None:
        """同値の`setText()`を避け、入力欄のUndo履歴を保持する。"""
        if self._view_model.is_disposed:
            return
        value = self._view_model.value.value
        if self.text() != value:
            self.setText(value)
        self._dirty = False
        self._set_conflicted(False)

    def _set_conflicted(self, value: bool) -> None:
        """競合状態が変わった場合だけ通知する。"""
        if value != self._conflicted:
            self._conflicted = value
            self.conflict_changed.emit(value)

    def _update_enabled(self, *_args: object) -> None:
        """正本とView固有の入力可否を反映し、コピーは許可する。"""
        view_model = self._view_model
        editable = (
            self._input_enabled
            and not view_model.is_disposed
            and view_model.set_value_command.can_execute
        )
        self.setReadOnly(not editable)
        if not editable and self._dirty:
            self._render()

    @qt.Slot()
    def _on_disposed(self) -> None:
        """終了後は値を残し、入力だけを停止する。"""
        if qt.isValid(self):
            self.setReadOnly(True)
