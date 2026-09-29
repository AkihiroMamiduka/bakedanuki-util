# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import cast

from ... import qt
from ._connection import connect_queued_qt_signal, disconnect_qt_connection
from ._validation import require_string
from .command import SetStringCommand
from .store import StringValueStore
from .value import StringValue


class _MutableStringValue(StringValue):
    """ViewModelだけが更新する確定文字列。"""

    def replace_silently(self, value: str) -> None:
        """再入時の通知順を制御するため値だけを置き換える。"""
        self._value = value


class _MutableSetStringCommand(SetStringCommand):
    """ViewModelだけが実行可否を更新するCommand。"""

    def set_can_execute(self, value: bool) -> None:
        """実行可否が変わった場合だけ通知する。"""
        if type(value) is not bool:
            raise TypeError("can_executeにはboolを指定してください")
        if value != self._can_execute:
            self._can_execute = value
            self.can_execute_changed.emit(value)


class StringViewModel(qt.QObject):
    """一つの確定文字列と変更要求をStoreへ仲介する。"""

    store_refreshed = qt.Signal(str)
    disposed = qt.Signal()

    def __init__(
        self, value: str = "", parent: qt.QObject | None = None
    ) -> None:
        """Store未接続でも使える初期値で生成する。"""
        super().__init__(parent)
        self._is_disposed = False
        self._value = _MutableStringValue(value, self)
        self._notified_value = self._value.value
        self._set_value_command = _MutableSetStringCommand(
            self._request_value, self
        )
        self._store: StringValueStore | None = None
        self._store_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None

    @property
    def value(self) -> StringValue:
        """Viewが読む確定値を返す。"""
        return self._value

    @property
    def set_value_command(self) -> SetStringCommand:
        """値の変更要求を受け付けるCommandを返す。"""
        return self._set_value_command

    @property
    def store(self) -> StringValueStore | None:
        """接続中のStoreを返す。"""
        return self._store

    @property
    def is_disposed(self) -> bool:
        """終了またはQt object破棄済みなら`True`。"""
        return self._is_disposed or not qt.isValid(self)

    def dispose(self) -> None:
        """変更要求を止め、Viewへ終了を通知する。"""
        if self.is_disposed:
            return
        self._is_disposed = True
        self._set_value_command.set_can_execute(False)
        self.disposed.emit()

    def attach_store(self, store: StringValueStore) -> None:
        """一つのStoreを接続し、現在の実値を読み込む。"""
        if self.is_disposed:
            raise RuntimeError("StringViewModelは終了しています")
        if self._store is store:
            return
        if self._store is not None:
            raise RuntimeError("StringViewModelへ複数のStoreを接続できません")
        validator = cast(
            Callable[[StringViewModel], None] | None,
            getattr(store, "_validate_attached_view_model", None),
        )
        if validator is not None:
            validator(self)
        self._store = store
        try:
            if isinstance(store, qt.QObject):
                self._store_destroyed_connection = connect_queued_qt_signal(
                    store.destroyed, self._on_store_destroyed
                )
            self.refresh_from_store(store)
        except Exception:
            disconnect_qt_connection(self._store_destroyed_connection)
            self._store_destroyed_connection = None
            self._store = None
            self._set_value_command.set_can_execute(False)
            raise

    def refresh_from_store(self, store: StringValueStore) -> bool:
        """正本の確定値と書込み可否を読み直す。"""
        self._require_attached_store(store)
        if self.is_disposed:
            return False
        try:
            if not store.is_available:
                self.store_became_unavailable(store)
                return False
            value = require_string(store.read(), "store.read()")
            writable = store.is_writable
            if type(writable) is not bool:
                raise TypeError("store.is_writableにはboolが必要です")
        except Exception:
            self._set_value_command.set_can_execute(False)
            raise
        changed = self._publish(value, writable)
        if not self.is_disposed:
            self.store_refreshed.emit(self._value.value)
        return changed

    def store_became_unavailable(self, store: StringValueStore) -> None:
        """正本の利用終了をCommandへ反映する。"""
        self._require_attached_store(store)
        self._set_value_command.set_can_execute(False)

    def _request_value(self, value: str) -> bool:
        """Commandの要求を適用し、正本の実値を確定する。"""
        value = require_string(value)
        if self.is_disposed:
            return False
        store = self._store
        if store is None:
            return self._publish(value, True)
        try:
            if not store.is_available or not store.is_writable:
                self._set_value_command.set_can_execute(False)
                return False
            previous = require_string(store.read(), "store.read()")
            actual = previous
            if value != previous:
                actual = require_string(store.write(value), "store.write()")
            if self.is_disposed:
                return actual != previous
            self.refresh_from_store(store)
            return self._value.value != previous
        except Exception:
            try:
                self.refresh_from_store(store)
            except Exception:
                self._set_value_command.set_can_execute(False)
            raise

    def _publish(self, value: str, writable: bool) -> bool:
        """通知先から再入しても最新の確定値を公開する。"""
        if self.is_disposed:
            return False
        changed = value != self._value.value
        self._value.replace_silently(value)
        self._set_value_command.set_can_execute(writable)
        if not self.is_disposed and self._value.value != self._notified_value:
            self._notified_value = self._value.value
            self._value.changed.emit(self._notified_value)
        return changed

    def _require_attached_store(self, store: StringValueStore) -> None:
        """再読込み元が接続中のStoreか検証する。"""
        if store is not self._store:
            raise ValueError("通知元はこのStringViewModelへ接続されていません")

    @qt.Slot()
    def _on_store_destroyed(self) -> None:
        """StoreのQt破棄後はCommandを停止する。"""
        self._store_destroyed_connection = None
        self._set_value_command.set_can_execute(False)
