# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from ... import qt
from .command import SetBoolCommand
from .store import BoolValueStore
from .value import BoolValue


class _StoreAttachmentValidator(Protocol):
    """Store固有のViewModel接続条件を検証する内部境界。"""

    def __call__(self, view_model: BoolViewModel) -> None:
        """接続可能なViewModelでなければ例外を送出する。"""
        raise NotImplementedError


def _require_bool(value: object, argument_name: str) -> bool:
    """値をboolとして検証して返す。"""
    if not isinstance(value, bool):
        raise TypeError(
            f"{argument_name}にはboolを指定してください: "
            f"{type(value).__name__}"
        )
    return value


def _disconnect_qt_connection(
    connection: qt.QtCore.QMetaObject.Connection | None,
) -> None:
    """保持しているQt signal接続を安全に解除する。"""
    if connection is None:
        return
    try:
        disconnect = cast(
            Callable[[qt.QtCore.QMetaObject.Connection], bool],
            getattr(qt.QtCore.QObject, "disconnect"),
        )
        disconnect(connection)
    except (RuntimeError, TypeError):
        pass


class _MutableBoolValue(BoolValue):
    """BoolViewModelだけが保持する更新可能なBoolValue。"""

    def replace(self, value: bool) -> bool:
        """ViewModelから値を確定し、変更された場合だけ通知する。"""
        value = _require_bool(value, "value")
        if value == self._value:
            return False
        self._value = value
        self.changed.emit(value)
        return True


class _MutableSetBoolCommand(SetBoolCommand):
    """BoolViewModelだけが保持する状態更新可能なCommand。"""

    def set_can_execute(self, can_execute: bool) -> None:
        """ViewModelから実行可否を更新する。"""
        can_execute = _require_bool(can_execute, "can_execute")
        if can_execute == self._can_execute:
            return
        self._can_execute = can_execute
        self.can_execute_changed.emit(can_execute)


class BoolViewModel(qt.QObject):
    """boolデータ、変更Command、任意のStoreを仲介するHub。"""

    store_refreshed = qt.Signal(bool)

    def __init__(
        self,
        value: bool = False,
        parent: qt.QObject | None = None,
    ) -> None:
        """メモリ上の初期値と任意のQt ownerで初期化する。"""
        super().__init__(parent)
        self._value = _MutableBoolValue(value, self)
        self._set_value_command = _MutableSetBoolCommand(
            self._request_value,
            self,
        )
        self._store: BoolValueStore | None = None
        self._store_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None

    @property
    def value(self) -> BoolValue:
        """Viewへ公開する読み取り専用データを返す。"""
        return self._value

    @property
    def set_value_command(self) -> SetBoolCommand:
        """UIとPythonから共有する値設定Commandを返す。"""
        return self._set_value_command

    @property
    def store(self) -> BoolValueStore | None:
        """現在接続されている値の正本を返す。"""
        return self._store

    def attach_store(self, store: BoolValueStore) -> None:
        """値の正本を接続し、その実値を初期同期する。"""
        current_store = self._store
        if current_store is store:
            return
        if current_store is not None:
            raise RuntimeError("BoolViewModelへ複数のStoreを接続できません")

        validator = cast(
            _StoreAttachmentValidator | None,
            getattr(store, "_validate_attached_view_model", None),
        )
        if validator is not None:
            validator(self)

        self._store = store
        try:
            if isinstance(store, qt.QObject):
                self._store_destroyed_connection = store.destroyed.connect(
                    self._on_store_destroyed
                )
            self.refresh_from_store(store)
        except Exception:
            _disconnect_qt_connection(self._store_destroyed_connection)
            self._store_destroyed_connection = None
            self._store = None
            self._set_value_command.set_can_execute(True)
            raise

    def refresh_from_store(self, store: BoolValueStore) -> bool:
        """接続Storeの実値と書き込み可否をViewModelへ同期する。"""
        self._require_attached_store(store)
        available = _require_bool(
            store.is_available,
            "store.is_available",
        )
        if not available:
            self._set_value_command.set_can_execute(False)
            return False

        value = _require_bool(store.read(), "store.read()")
        writable = _require_bool(
            store.is_writable,
            "store.is_writable",
        )
        # changed slotがStoreを破棄しても古い状態で再度enableしない。
        self._set_value_command.set_can_execute(writable)
        changed = self._commit_value(value)
        self.store_refreshed.emit(value)
        return changed

    def store_became_unavailable(self, store: BoolValueStore) -> None:
        """接続Storeが利用できなくなったことを反映する。"""
        self._require_attached_store(store)
        self._set_value_command.set_can_execute(False)

    def _request_value(self, value: bool) -> bool:
        """Commandからの変更要求を処理して実値を確定する。"""
        value = _require_bool(value, "value")
        store = self._store
        if store is None:
            return self._commit_value(value)

        available = _require_bool(
            store.is_available,
            "store.is_available",
        )
        if not available:
            self._set_value_command.set_can_execute(False)
            return False
        writable = _require_bool(
            store.is_writable,
            "store.is_writable",
        )
        if not writable:
            self._set_value_command.set_can_execute(False)
            return False

        current_value = _require_bool(store.read(), "store.read()")
        if value == current_value:
            self._commit_value(current_value)
            return False

        try:
            actual_value = _require_bool(
                store.write(value),
                "store.write()",
            )
        except Exception:
            # Storeが値変更後に失敗した場合も、可能なら実値へ復旧する。
            try:
                self.refresh_from_store(store)
            except Exception:
                self._set_value_command.set_can_execute(False)
            raise

        changed = actual_value != current_value
        self._commit_value(actual_value)
        try:
            available = _require_bool(
                store.is_available,
                "store.is_available",
            )
            writable = available and _require_bool(
                store.is_writable,
                "store.is_writable",
            )
        except Exception:
            self._set_value_command.set_can_execute(False)
            raise
        self._set_value_command.set_can_execute(writable)
        return changed

    def _commit_value(self, value: bool) -> bool:
        """すべての入力経路から到達する唯一のデータ確定処理。"""
        return self._value.replace(value)

    def _require_attached_store(self, store: BoolValueStore) -> None:
        """通知元が現在接続中のStoreか検証する。"""
        if store is not self._store:
            raise ValueError("通知元はこのBoolViewModelへ接続されていません")

    def _on_store_destroyed(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """QObject Storeの破棄をCommand状態へ反映する。"""
        self._store_destroyed_connection = None
        self._set_value_command.set_can_execute(False)
