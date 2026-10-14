# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import cast

from ... import qt
from ._connection import connect_queued, disconnect
from ._validation import require_int
from .command import SetIntCommand
from .presentation import IntPresentation, require_presentation
from .store import IntValueStore
from .value import IntValue


class _MutableIntValue(IntValue):
    """ViewModelだけが更新する確定整数。"""

    def replace_silently(self, value: int) -> None:
        """再入時の通知順を制御するため、値だけを置き換える。"""
        self._value = value


class _MutableSetIntCommand(SetIntCommand):
    """ViewModelだけが実行可否を変更するCommand。"""

    def set_can_execute(self, value: bool) -> None:
        """実行可否が変わった場合だけ通知する。"""
        if type(value) is not bool:
            raise TypeError("can_executeにはboolを指定してください")
        if value != self._can_execute:
            self._can_execute = value
            self.can_execute_changed.emit(value)


class IntViewModel(qt.QObject):
    """単一整数の確定値とStoreへの変更要求を仲介する。"""

    store_refreshed = qt.Signal(object)
    presentation_changed = qt.Signal(object)
    disposed = qt.Signal()

    def __init__(
        self,
        value: int = 0,
        parent: qt.QObject | None = None,
        *,
        presentation: IntPresentation | None = None,
    ) -> None:
        """Store未接続でも使用できる初期値で生成する。"""
        super().__init__(parent)
        self._is_disposed = False
        self._presentation = require_presentation(
            presentation if presentation is not None else IntPresentation()
        )
        self._value = _MutableIntValue(value, self)
        self._notified_value = self._value.value
        self._set_value_command = _MutableSetIntCommand(
            self._request_value, self
        )
        self._store: IntValueStore | None = None
        self._store_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None

    @property
    def value(self) -> IntValue:
        """Viewが読む確定整数を返す。"""
        return self._value

    @property
    def set_value_command(self) -> SetIntCommand:
        """値変更を要求するCommandを返す。"""
        return self._set_value_command

    @property
    def presentation(self) -> IntPresentation:
        """現在の入力範囲を返す。"""
        return self._presentation

    @property
    def store(self) -> IntValueStore | None:
        """接続中のStoreを返す。"""
        return self._store

    @property
    def is_disposed(self) -> bool:
        """終了またはQt object破棄済みならTrueを返す。"""
        return self._is_disposed or not qt.isValid(self)

    def dispose(self) -> None:
        """変更要求を止め、Viewへ終了を通知する。"""
        if self.is_disposed:
            return
        self._is_disposed = True
        self._set_value_command.set_can_execute(False)
        self.disposed.emit()

    def attach_store(self, store: IntValueStore) -> None:
        """一つのStoreを接続して現在の実値を読む。"""
        if self.is_disposed:
            raise RuntimeError("IntViewModelは終了しています")
        if self._store is store:
            return
        if self._store is not None:
            raise RuntimeError("IntViewModelへ複数のStoreを接続できません")
        validator = cast(
            Callable[[IntViewModel], None] | None,
            getattr(store, "_validate_attached_view_model", None),
        )
        if validator is not None:
            validator(self)
        self._store = store
        try:
            if isinstance(store, qt.QObject):
                self._store_destroyed_connection = connect_queued(
                    store.destroyed, self._on_store_destroyed
                )
            self.refresh_from_store(store)
        except Exception:
            disconnect(self._store_destroyed_connection)
            self._store_destroyed_connection = None
            self._store = None
            self._set_value_command.set_can_execute(False)
            raise

    def refresh_from_store(self, store: IntValueStore) -> bool:
        """正本の実値、入力範囲と書込み可否を再同期する。"""
        self._require_attached_store(store)
        if self.is_disposed:
            return False
        try:
            available = store.is_available
            if type(available) is not bool:
                raise TypeError("store.is_availableにはboolが必要です")
            if not available:
                self.store_became_unavailable(store)
                return False
            value = require_int(store.read(), "store.read()")
            presentation = require_presentation(store.presentation)
            writable = store.is_writable
            if type(writable) is not bool:
                raise TypeError("store.is_writableにはboolが必要です")
        except Exception:
            self._set_value_command.set_can_execute(False)
            raise
        if presentation != self._presentation:
            self._presentation = presentation
            self.presentation_changed.emit(presentation)
            if self.is_disposed:
                return False
        changed = self._publish(value, writable)
        if not self.is_disposed:
            self.store_refreshed.emit(self._value.value)
        return changed

    def store_became_unavailable(self, store: IntValueStore) -> None:
        """正本が利用不能になったら変更要求を止める。"""
        self._require_attached_store(store)
        self._set_value_command.set_can_execute(False)

    def _request_value(self, value: int) -> bool:
        """変更要求を正本へ適用し、setter後の実値を確定する。"""
        value = require_int(value)
        if self.is_disposed:
            return False
        store = self._store
        if store is None:
            return self._publish(value, True)
        try:
            if not store.is_available or not store.is_writable:
                self._set_value_command.set_can_execute(False)
                return False
            previous = require_int(store.read(), "store.read()")
            if value != previous:
                require_int(store.write(value), "store.write()")
            if self.is_disposed:
                return value != previous
            self.refresh_from_store(store)
            return self._value.value != previous
        except Exception:
            try:
                self.refresh_from_store(store)
            except Exception:
                self._set_value_command.set_can_execute(False)
            raise

    def _publish(self, value: int, writable: bool) -> bool:
        """再入通知でも最新の確定値を公開する。"""
        if self.is_disposed:
            return False
        changed = value != self._value.value
        self._value.replace_silently(value)
        self._set_value_command.set_can_execute(writable)
        if not self.is_disposed and self._value.value != self._notified_value:
            self._notified_value = self._value.value
            self._value.changed.emit(self._notified_value)
        return changed

    def _require_attached_store(self, store: IntValueStore) -> None:
        """通知元が接続済みのStoreか検証する。"""
        if store is not self._store:
            raise ValueError("通知元はこのIntViewModelへ接続されていません")

    @qt.Slot()
    def _on_store_destroyed(self) -> None:
        """StoreのQt破棄後はCommandを停止する。"""
        self._store_destroyed_connection = None
        self._set_value_command.set_can_execute(False)
