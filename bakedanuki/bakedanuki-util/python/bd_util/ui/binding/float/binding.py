# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Generic, TypeVar

from ... import qt
from .store import FloatValueStore
from .view_model import FloatViewModel

_StoreT = TypeVar("_StoreT", bound=FloatValueStore, covariant=True)


class FloatBinding(qt.QObject, Generic[_StoreT]):
    """1つのStoreとViewModelの組み立て、操作、寿命をまとめる。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """外部Storeを参照し、専用ViewModelをこのbindingの子として作る。"""
        self._initialize(lambda _view_model: store, parent=parent)

    def _initialize(
        self,
        create_store: Callable[[FloatViewModel], _StoreT],
        *,
        parent: qt.QObject | None,
    ) -> None:
        """constructorから一度だけ呼び、専用ViewModelに対応するStoreを作る。"""
        super().__init__(parent)
        self._is_disposed = False
        self._view_model = FloatViewModel(parent=self)
        try:
            self._store = create_store(self._view_model)
            self._view_model.attach_store(self._store)
        except Exception:
            self.dispose()
            raise

    @property
    def store(self) -> _StoreT:
        """正本へのアクセスを担うStoreを具体型のまま返す。"""
        return self._store

    @property
    def view_model(self) -> FloatViewModel:
        """各Viewへ渡す共通ViewModelを返す。"""
        self._require_active()
        return self._view_model

    @property
    def value(self) -> float:
        """最後に同期した確定値を返す。"""
        return self.view_model.value.value

    @property
    def changed(self) -> qt.QtCore.SignalInstance:
        """確定値の変更をfloatで通知する既存signalを返す。"""
        return self.view_model.value.changed

    @property
    def is_disposed(self) -> bool:
        """明示終了またはQt ownerの破棄によって終了したか返す。"""
        return (
            self._is_disposed
            or not qt.isValid(self)
            or self._view_model.is_disposed
        )

    def set_value(self, value: float) -> bool:
        """Viewと同じCommandへ要求し、正本の実値が変わったか返す。"""
        return self.view_model.set_value_command.execute(value)

    def refresh(self) -> bool:
        """正本を読み直し、公開値が変わったか返す。"""
        return self.view_model.refresh_from_store(self._store)

    def dispose(self) -> None:
        """入力を停止してQt objectを遅延破棄する。正本は破棄しない。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        view_model = self._view_model
        if qt.isValid(view_model):
            view_model.dispose()
        if qt.isValid(self):
            self.deleteLater()

    def _require_active(self) -> None:
        """終了後の操作と破棄済みQObjectへのアクセスを拒否する。"""
        if self.is_disposed:
            raise RuntimeError("FloatBindingは終了しています")
