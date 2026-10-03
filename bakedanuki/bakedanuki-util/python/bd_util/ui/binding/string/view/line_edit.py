# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from .... import qt
from .._connection import connect_queued_qt_signal
from ..binding import StringBinding
from ..store import StringValueStore
from ..view_model import StringViewModel
from ._source import resolve_string_view_source


class StringLineEdit(qt.QLineEdit):
    """文字列を編集中は保持し、確定時だけCommandへ渡す一行View。

    UI操作の失敗は最新の確定値へ表示を戻し、`edit_failed`で理由を通知する。
    """

    conflict_changed = qt.Signal(bool)
    edit_failed = qt.Signal(str)

    def __init__(
        self,
        view_model: StringViewModel | StringBinding[StringValueStore],
        parent: qt.QWidget | None = None,
        *,
        follow_source_during_edit: bool = False,
    ) -> None:
        """同じBindingを共有し、外部値変更時の入力保持方針を指定する。

        Args:
            view_model: 表示するViewModelまたはBinding。
            parent: 親Widget。
            follow_source_during_edit: 編集中も確定値の変更を優先する場合はTrue。
        """
        if type(follow_source_during_edit) is not bool:
            raise TypeError(
                "follow_source_during_editにはboolを指定してください"
            )
        view_model, binding = resolve_string_view_source(view_model)
        super().__init__(parent)
        self._view_model = view_model
        self._binding = binding
        self._input_enabled = True
        self._dirty = False
        self._conflicted = False
        self._follow_source_during_edit = follow_source_during_edit
        self._value_request_handler: Callable[[str], bool] | None = None
        # Qtの既定32767文字による正本の黙った切り詰めを防ぐ
        self.setMaxLength(2_147_483_647)
        self._render()
        self._update_enabled()
        self.textEdited.connect(self._on_text_edited)
        self.returnPressed.connect(self._commit_explicit)
        self.editingFinished.connect(self._commit_on_focus_loss)
        view_model.value.changed.connect(self._on_value_changed)
        view_model.source_changed.connect(self._on_source_changed)
        view_model.source_values_changed.connect(
            self._on_source_values_changed
        )
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

    def setValueRequestHandler(
        self, handler: Callable[[str], bool] | None
    ) -> None:
        """確定した文字列を先に処理する任意のhandlerを設定する。

        `handler` が`True`を返す場合は、このViewのCommandを実行しない。
        """
        if handler is not None and not callable(handler):
            raise TypeError(
                "handlerには呼出し可能な関数またはNoneを指定してください"
            )
        self._value_request_handler = handler

    def event(self, arg__1: qt.QEvent) -> bool:
        """Enterのshortcutを入力欄内で扱い、Mayaへ伝播させない。"""
        if (
            arg__1.type() == qt.QEvent.Type.ShortcutOverride
            and isinstance(arg__1, qt.QtGui.QKeyEvent)
            and arg__1.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter)
        ):
            arg__1.accept()
            return True
        return super().event(arg__1)

    def focusInEvent(self, arg__1: qt.QtGui.QFocusEvent) -> None:
        """入力開始時に正本の値と編集可否を再確認する。"""
        self._refresh_source()
        if qt.isValid(self):
            super().focusInEvent(arg__1)

    def keyPressEvent(self, arg__1: qt.QtGui.QKeyEvent) -> None:
        """Escapeで入力を破棄し、EnterはQtの確定処理後に受理する。"""
        if arg__1.key() == qt.Qt.Key.Key_Escape and self._dirty:
            self._render()
            arg__1.accept()
            return
        super().keyPressEvent(arg__1)
        if arg__1.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            arg__1.accept()

    def keyReleaseEvent(self, arg__1: qt.QtGui.QKeyEvent) -> None:
        """確定キーを離した通知も入力欄内で受理する。"""
        super().keyReleaseEvent(arg__1)
        if arg__1.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            arg__1.accept()

    def _on_text_edited(self, _text: str) -> None:
        """ユーザー編集だけを未確定入力として記録する。"""
        self._dirty = True
        if self.text() == self._view_model.value.value:
            self._set_conflicted(False)

    def _on_value_changed(self, _value: str) -> None:
        """選択した入力方針に従い、代表の最新値を表示する。"""
        if self._dirty:
            if (
                self._follow_source_during_edit
                or self.text() == self._view_model.value.value
            ):
                self._render()
            else:
                self._set_conflicted(True)
            return
        self._render()

    def _on_source_changed(self) -> None:
        """入力保持方針では後続対象の状態変化も競合として知らせる。"""
        if self._dirty and not self._follow_source_during_edit:
            self._set_conflicted(True)

    def _on_source_values_changed(self) -> None:
        """確定値優先のViewでは後続対象だけの値変更でも入力を破棄する。"""
        if self._dirty and self._follow_source_during_edit:
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
        view_model = self._view_model
        if view_model.is_disposed or not self._input_enabled:
            self._render()
            return
        # 通知されなかった外部変更を、書込み可否や競合の判定前に読む
        if not self._refresh_source() or not self._dirty:
            return
        if self._conflicted and not explicit:
            return
        if not view_model.set_value_command.can_execute:
            self._render()
            return
        requested = self.text()
        self._dirty = False
        try:
            handler = self._value_request_handler
            handled = handler is not None and handler(requested)
            if not handled:
                view_model.set_value_command.execute(requested)
        except Exception as error:
            # handlerが正本を変更してから失敗した場合も実値を優先する
            self._refresh_source(report_failure=False)
            if qt.isValid(self):
                self._render()
                self.edit_failed.emit(str(error))
        finally:
            if qt.isValid(self):
                self._render()

    def _refresh_source(self, *, report_failure: bool = True) -> bool:
        """操作前に正本を読み、UI境界の読込み失敗をsignalへ変換する。"""
        view_model = self._view_model
        if view_model.is_disposed:
            return False
        store = view_model.store
        if store is None:
            return True
        try:
            view_model.refresh_from_store(store, notify_confirmation=False)
            return qt.isValid(self) and not view_model.is_disposed
        except Exception as error:
            if qt.isValid(self):
                self._render()
                if report_failure:
                    self.edit_failed.emit(str(error))
            return False

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
