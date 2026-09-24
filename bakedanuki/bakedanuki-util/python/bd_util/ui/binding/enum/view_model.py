# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import cast

from ... import qt
from ._connection import (
    connect_queued_qt_signal,
    disconnect_qt_connection,
)
from .command import SetEnumCommand
from .definition import EnumDefinition, require_definition, require_enum_value
from .store import EnumValueStore
from .value import EnumValue


class _MutableEnumValue(EnumValue):
    def replace_silently(self, value: int) -> None:
        """通知順を制御できるよう、signalなしで確定値を置き換える。"""
        self._value = value


class _MutableSetEnumCommand(SetEnumCommand):
    def set_can_execute(self, value: bool) -> None:
        """入力可否が変わった場合だけ変更signalを通知する。"""
        if value != self._can_execute:
            self._can_execute = value
            self.can_execute_changed.emit(value)


class EnumViewModel(qt.QObject):
    """Storeの確定値、選択肢、変更要求をViewへ届ける。

    Attributes:
        definition_changed: 選択肢が変わると`EnumDefinition`を通知する。
        store_refreshed: Storeの再読込後に確定した`int`値を通知する。
        disposed: 終了時に通知する。
    """

    definition_changed = qt.Signal(object)
    store_refreshed = qt.Signal(object)
    disposed = qt.Signal()

    def __init__(
        self,
        value: int = 0,
        parent: qt.QObject | None = None,
        *,
        definition: EnumDefinition | None = None,
    ) -> None:
        """初期値と選択肢を指定してViewModelを作る。

        Args:
            value: Storeを接続する前の整数値。
            parent: このViewModelを所有するQObject。
            definition: 選択肢。`None`なら空の定義。
        """
        super().__init__(parent)
        self._is_disposed = False
        self._revision = 0
        self._definition = require_definition(
            definition if definition is not None else EnumDefinition()
        )
        self._value = _MutableEnumValue(value, self)
        self._notified_value = self._value.value
        self._set_value_command = _MutableSetEnumCommand(
            self._request_value, self
        )
        self._set_value_command.set_can_execute(bool(self._definition.items))
        self._store: EnumValueStore | None = None
        self._store_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None

    @property
    def value(self) -> EnumValue:
        """現在の確定値と変更signalを保持する値objectを返す。"""
        return self._value

    @property
    def definition(self) -> EnumDefinition:
        """最後に同期した選択肢を返す。"""
        return self._definition

    @property
    def is_value_defined(self) -> bool:
        """現在値が選択肢に含まれている場合は`True`。"""
        return self._definition.item_for_value(self._value.value) is not None

    @property
    def set_value_command(self) -> SetEnumCommand:
        """選択肢を検証して変更を要求するCommandを返す。"""
        return self._set_value_command

    @property
    def store(self) -> EnumValueStore | None:
        """接続中のStoreを返す。未接続なら`None`。"""
        return self._store

    @property
    def is_disposed(self) -> bool:
        """終了済み、またはQt objectが破棄済みなら`True`。"""
        return self._is_disposed or not qt.isValid(self)

    def dispose(self) -> None:
        """変更要求を止め、終了を通知する。"""
        if self.is_disposed:
            return
        self._is_disposed = True
        self._set_value_command.set_can_execute(False)
        self.disposed.emit()

    def attach_store(self, store: EnumValueStore) -> None:
        """一つのStoreを接続し、その確定値と選択肢を読み込む。

        Args:
            store: 接続するenum Store。

        Raises:
            RuntimeError: 終了済み、または別のStoreが接続済みの場合。
        """
        if self.is_disposed:
            raise RuntimeError("EnumViewModelは終了しています")
        if self._store is store:
            return
        if self._store is not None:
            raise RuntimeError("EnumViewModelへ複数のStoreを接続できません")
        validator = cast(
            Callable[[EnumViewModel], None] | None,
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

    def refresh_from_store(self, store: EnumValueStore) -> bool:
        """接続中のStoreから確定値と選択肢を再取得する。

        Args:
            store: 接続中のStore。

        Returns:
            公開値が変わった場合は`True`。

        Raises:
            ValueError: 接続中のStoreと異なる場合。
        """
        self._require_attached_store(store)
        if self.is_disposed:
            return False
        try:
            if not store.is_available:
                self.store_became_unavailable(store)
                return False
            definition = require_definition(store.definition)
            value = require_enum_value(store.read())
            writable = store.is_writable
        except Exception:
            self._set_value_command.set_can_execute(False)
            raise
        changed = self._publish(value, definition, writable)
        if not self.is_disposed:
            self.store_refreshed.emit(self._value.value)
        return changed

    def store_became_unavailable(self, store: EnumValueStore) -> None:
        """接続中のStoreを編集できない状態にする。

        Args:
            store: 接続中のStore。

        Raises:
            ValueError: 接続中のStoreと異なる場合。
        """
        self._require_attached_store(store)
        self._set_value_command.set_can_execute(False)

    def _request_value(self, value: int) -> bool:
        value = require_enum_value(value)
        if self.is_disposed:
            return False
        store = self._store
        if store is None:
            self._definition.require_value(value)
            return self._publish(value, self._definition, True)
        try:
            if not store.is_available or not store.is_writable:
                self._set_value_command.set_can_execute(False)
                return False
            # staleなViewからの入力も正本の最新定義で検証する。
            definition = require_definition(store.definition)
            definition.require_value(value)
            previous = require_enum_value(store.read())
            actual = previous
            if value != previous:
                actual = require_enum_value(store.write(value))
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

    def _publish(
        self, value: int, definition: EnumDefinition, writable: bool
    ) -> bool:
        if self.is_disposed:
            return False
        changed = value != self._value.value
        definition_changed = definition != self._definition
        if changed or definition_changed:
            self._revision += 1
        revision = self._revision
        # 通知中の読み取りでも整合するよう、値と定義を両方更新してからsignalを出す。
        self._value.replace_silently(value)
        self._definition = definition
        self._set_value_command.set_can_execute(
            writable and bool(definition.items)
        )
        if self.is_disposed or self._revision != revision:
            return changed
        if definition_changed:
            self.definition_changed.emit(definition)
        # 定義通知中の再入で値を維持したまま定義だけ再更新されても、
        # 未通知の値変更は最新状態で一度だけ届ける。
        if not self.is_disposed and self._value.value != self._notified_value:
            self._notified_value = self._value.value
            self._value.changed.emit(self._notified_value)
        return changed

    def _require_attached_store(self, store: EnumValueStore) -> None:
        if store is not self._store:
            raise ValueError("通知元はこのEnumViewModelへ接続されていません")

    @qt.Slot()
    def _on_store_destroyed(self) -> None:
        self._store_destroyed_connection = None
        self._set_value_command.set_can_execute(False)
