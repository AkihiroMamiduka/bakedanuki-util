# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from ... import qt
from ._validation import require_float
from .presentation import FloatPresentation, require_presentation
from .command import SetFloatCommand
from .store import FloatValueStore
from .value import FloatValue


class _StoreAttachmentValidator(Protocol):
    """Store固有のViewModel接続条件を検証する内部境界。"""

    def __call__(self, view_model: FloatViewModel) -> None:
        """接続可能なViewModelでなければ例外を送出する。"""
        raise NotImplementedError


class _QueuedSignal(Protocol):
    """QueuedConnectionを指定できるQt signalの型境界。"""

    def connect(
        self,
        slot: Callable[[], None],
        connection_type: qt.Qt.ConnectionType,
    ) -> qt.QtCore.QMetaObject.Connection:
        """slotを指定した接続方式で接続する。"""
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


class _MutableFloatValue(FloatValue):
    """FloatViewModelだけが保持する更新可能なFloatValue。"""

    def replace(self, value: float) -> bool:
        """ViewModelから値を確定し、変更された場合だけ通知する。"""
        value = require_float(value)
        if value == self._value:
            return False
        self._value = value
        self.changed.emit(value)
        return True


class _MutableSetFloatCommand(SetFloatCommand):
    """FloatViewModelだけが保持する状態更新可能なCommand。"""

    def set_can_execute(self, can_execute: bool) -> None:
        """ViewModelから実行可否を更新する。"""
        can_execute = _require_bool(can_execute, "can_execute")
        if can_execute == self._can_execute:
            return
        self._can_execute = can_execute
        self.can_execute_changed.emit(can_execute)


class FloatViewModel(qt.QObject):
    """浮動小数点データ、変更Command、任意のStoreを仲介するHub。"""

    store_refreshed = qt.Signal(float)
    presentation_changed = qt.Signal(object)

    def __init__(
        self,
        value: float = 0.0,
        parent: qt.QObject | None = None,
        *,
        presentation: FloatPresentation | None = None,
    ) -> None:
        """メモリ上の初期値とbindingの寿命を管理するownerで初期化する。"""
        super().__init__(parent)
        self._is_disposed = False
        self._presentation = require_presentation(
            presentation if presentation is not None else FloatPresentation()
        )
        self._value = _MutableFloatValue(value, self)
        self._set_value_command = _MutableSetFloatCommand(
            self._request_value,
            self,
        )
        self._store: FloatValueStore | None = None
        self._store_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None

    @property
    def value(self) -> FloatValue:
        """Viewへ公開する読み取り専用データを返す。"""
        return self._value

    @property
    def set_value_command(self) -> SetFloatCommand:
        """UIとPythonから共有する値設定Commandを返す。"""
        return self._set_value_command

    @property
    def presentation(self) -> FloatPresentation:
        """現在の表示単位とhard limitを返す。"""
        return self._presentation

    @property
    def store(self) -> FloatValueStore | None:
        """現在接続されている値の正本を返す。"""
        return self._store

    @property
    def is_disposed(self) -> bool:
        """入力とStoreからの同期を終了したか返す。"""
        return self._is_disposed or not qt.isValid(self)

    def dispose(self) -> None:
        """入力と同期を停止する。QObjectの破棄はownerへ任せる。"""
        if self.is_disposed:
            return
        self._is_disposed = True
        self._set_value_command.set_can_execute(False)

    def attach_store(self, store: FloatValueStore) -> None:
        """値の正本を接続し、その実値を初期同期する。"""
        if self.is_disposed:
            raise RuntimeError("FloatViewModelは終了しています")
        current_store = self._store
        if current_store is store:
            return
        if current_store is not None:
            raise RuntimeError("FloatViewModelへ複数のStoreを接続できません")

        validator = cast(
            _StoreAttachmentValidator | None,
            getattr(store, "_validate_attached_view_model", None),
        )
        if validator is not None:
            validator(self)

        self._store = store
        try:
            if isinstance(store, qt.QObject):
                self._store_destroyed_connection = cast(
                    _QueuedSignal,
                    store.destroyed,
                ).connect(
                    self._on_store_destroyed,
                    qt.Qt.ConnectionType.QueuedConnection,
                )
            self.refresh_from_store(store)
        except Exception:
            _disconnect_qt_connection(self._store_destroyed_connection)
            self._store_destroyed_connection = None
            self._store = None
            self._set_value_command.set_can_execute(not self.is_disposed)
            raise

    def refresh_from_store(self, store: FloatValueStore) -> bool:
        """接続Storeの実値と書き込み可否をViewModelへ同期する。"""
        self._require_attached_store(store)
        if self.is_disposed:
            return False
        available = _require_bool(
            store.is_available,
            "store.is_available",
        )
        if not available:
            self._set_value_command.set_can_execute(False)
            return False

        value = require_float(store.read(), "store.read()")
        presentation = require_presentation(store.presentation)
        if presentation != self._presentation:
            self._presentation = presentation
            self.presentation_changed.emit(presentation)
            if self.is_disposed:
                return False
            if not _require_bool(store.is_available, "store.is_available"):
                self._set_value_command.set_can_execute(False)
                return False
            # 表示情報の通知slotが正本を変更した場合は新しい実値を使う。
            value = require_float(store.read(), "store.read()")
        if self.is_disposed:
            return False
        writable = _require_bool(
            store.is_writable,
            "store.is_writable",
        )
        # changed slotがStoreを破棄しても古い状態で再度enableしない。
        self._set_value_command.set_can_execute(
            writable and not self.is_disposed
        )
        changed = self._commit_value(value)
        if not self.is_disposed:
            self.store_refreshed.emit(value)
        return changed

    def store_became_unavailable(self, store: FloatValueStore) -> None:
        """接続Storeが利用できなくなったことを反映する。"""
        self._require_attached_store(store)
        self._set_value_command.set_can_execute(False)

    def _request_value(self, value: float) -> bool:
        """Commandからの変更要求を処理して実値を確定する。"""
        value = require_float(value)
        if self.is_disposed:
            return False
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

        current_value = require_float(store.read(), "store.read()")
        if self.is_disposed:
            return False
        if value == current_value:
            self._commit_value(current_value)
            return False

        try:
            actual_value = require_float(
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
        self._set_value_command.set_can_execute(
            writable and not self.is_disposed
        )
        return changed

    def _commit_value(self, value: float) -> bool:
        """すべての入力経路から到達する唯一のデータ確定処理。"""
        if self.is_disposed:
            return False
        return self._value.replace(value)

    def _require_attached_store(self, store: FloatValueStore) -> None:
        """通知元が現在接続中のStoreか検証する。"""
        if store is not self._store:
            raise ValueError("通知元はこのFloatViewModelへ接続されていません")

    @qt.Slot()
    def _on_store_destroyed(self) -> None:
        """QObject Store破棄後のCommand停止をevent loopで反映する。"""
        self._store_destroyed_connection = None
        self._set_value_command.set_can_execute(False)
