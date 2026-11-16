# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from .... import qt
from ..._view_source import ViewSourceConnections
from ..binding import BoolBinding
from ..store import BoolValueStore
from ..view_model import BoolViewModel
from ._connection import disconnect_qt_connection
from ._source import resolve_bool_view_source


class BoolCheckBox(qt.QCheckBox):
    """`BoolViewModel` を表示・操作する二値チェックボックス。"""

    def __init__(
        self,
        view_model: BoolViewModel | BoolBinding[BoolValueStore],
        text: str = "",
        parent: qt.QWidget | None = None,
    ) -> None:
        """確定したbool値に追従する二値チェックボックスを生成する。

        Args:
            view_model: 操作するViewModelまたはそのBinding。
            text: チェックボックスの表示文字列。
            parent: Qtの親Widget。
        """
        view_model, binding = resolve_bool_view_source(view_model)
        super().__init__(text, parent)
        self._binding = binding
        self._source_connections = ViewSourceConnections(self)
        self._value_request_handler: Callable[[bool], bool] | None = None
        # Viewだけを保持するfactory構成でもbinding先を存続させる。
        self._view_model = view_model
        self.setTristate(False)
        self._toggled_connection: qt.QtCore.QMetaObject.Connection | None = (
            self.toggled.connect(self._request_value)
        )
        self.set_source(binding if binding is not None else view_model)

    def set_source(
        self, source: BoolViewModel | BoolBinding[BoolValueStore]
    ) -> None:
        """入力handlerを保ち、正本へ書き込まずに表示先を交換する。

        旧Bindingの終了処理は呼出し側が所有する。交換後の旧通知は無視する。

        Args:
            source: 生存中のViewModelまたはBinding。
        """
        view_model, binding = resolve_bool_view_source(source)
        if view_model.is_disposed:
            raise RuntimeError("表示対象のBoolViewModelは終了しています")
        self._source_connections.clear()
        self._view_model = view_model
        self._binding = binding
        if self._toggled_connection is None:
            self._toggled_connection = self.toggled.connect(
                self._request_value
            )
        self._source_connections.connect(
            view_model.value.changed, self._update_checked
        )
        self._source_connections.connect(
            view_model.set_value_command.can_execute_changed,
            self._update_enabled,
            discard_args=True,
        )
        self._source_connections.connect(
            view_model.destroyed,
            self._on_view_model_destroyed,
            queued=True,
            discard_args=True,
        )
        self._update_checked(view_model.value.value)
        self.setEnabled(view_model.set_value_command.can_execute)

    @property
    def view_model(self) -> BoolViewModel:
        """表示・操作対象のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("表示対象のBoolViewModelは破棄されています")
        return view_model

    def setValueRequestHandler(
        self, handler: Callable[[bool], bool] | None
    ) -> None:
        """チェック操作時の入力 `handler` を設定する。

        Args:
            handler: 入力を処理したら ``True`` を返す関数。``False`` または
                ``None`` の場合はViewModelのCommandが値を設定する。

        Raises:
            TypeError: ``handler`` が呼び出し可能でも ``None`` でもない場合。
        """
        if handler is not None and not callable(handler):
            raise TypeError(
                "handlerには呼出し可能な関数またはNoneを指定してください"
            )
        self._value_request_handler = handler

    def _request_value(self, value: bool) -> None:
        """ユーザー入力をCommandへ渡し、拒否時は実値へ戻す。"""
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            self._disable_binding()
            return
        handled = False
        generation = self._source_connections.generation
        try:
            handler = self._value_request_handler
            handled = handler is not None and handler(value)
            if generation != self._source_connections.generation:
                return
            changed = handled or view_model.set_value_command.execute(value)
        except Exception:
            current = self._valid_view_model()
            if current is not None:
                self._update_checked(current.value.value)
            raise
        if generation == self._source_connections.generation and (
            handled or not changed
        ):
            self._update_checked(view_model.value.value)

    def _update_checked(self, value: bool) -> None:
        """Commandを再実行せずViewModelの実値を表示する。"""
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.setChecked(value)
        finally:
            del blocker

    def _update_enabled(self) -> None:
        """現在の表示先だけを参照して入力可否を同期する。"""
        view_model = self._valid_view_model()
        self.setEnabled(
            view_model is not None
            and not view_model.is_disposed
            and view_model.set_value_command.can_execute
        )

    def _valid_view_model(self) -> BoolViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        view_model = self._view_model
        if not qt.isValid(view_model):
            return None
        return view_model

    def _disable_binding(self) -> None:
        """入力接続を解除してチェックボックスを無効にする。"""
        disconnect_qt_connection(self._toggled_connection)
        self._toggled_connection = None
        if qt.isValid(self):
            self.setEnabled(False)

    @qt.Slot()
    def _on_view_model_destroyed(self) -> None:
        """次のevent loopでViewModel破棄後のUI入力を停止する。"""
        self._disable_binding()
