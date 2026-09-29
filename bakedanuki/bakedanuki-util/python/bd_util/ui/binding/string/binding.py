# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Generic, TypeVar

from ... import qt
from .store import PythonStringAttributeStore, StringValueStore
from .view_model import StringViewModel

_StoreT = TypeVar("_StoreT", bound=StringValueStore, covariant=True)
_InstanceT = TypeVar("_InstanceT")


class StringBinding(qt.QObject, Generic[_StoreT]):
    """一つの文字列Storeと専用ViewModelの同期・寿命を管理する。"""

    def __init__(
        self, store: _StoreT, *, parent: qt.QObject | None = None
    ) -> None:
        """外部Storeを接続する。終了時にStoreは破棄しない。"""
        self._initialize(lambda _view_model: store, parent=parent)

    def _initialize(
        self,
        create_store: Callable[[StringViewModel], _StoreT],
        *,
        parent: qt.QObject | None,
    ) -> None:
        """専用ViewModelとStoreを一度だけ組み立てる。"""
        super().__init__(parent)
        self._is_disposed = False
        self._view_model = self._create_view_model()
        try:
            self._store = create_store(self._view_model)
            self._view_model.attach_store(self._store)
        except Exception:
            self.dispose()
            raise

    @staticmethod
    def from_attribute(
        instance: _InstanceT,
        attribute_name: str,
        *,
        parent: qt.QObject | None = None,
    ) -> StringBinding[PythonStringAttributeStore[_InstanceT]]:
        """既存のPython文字列属性を正本とするBindingを作る。"""
        return StringBinding(
            PythonStringAttributeStore(instance, attribute_name), parent=parent
        )

    @property
    def store(self) -> _StoreT:
        """接続中のStoreを具体型のまま返す。"""
        return self._store

    @property
    def view_model(self) -> StringViewModel:
        """共有するViewModelを返す。"""
        self._require_active()
        return self._view_model

    @property
    def value(self) -> str:
        """最後に同期した確定文字列を返す。"""
        return self.view_model.value.value

    @property
    def changed(self) -> qt.QtCore.SignalInstance:
        """確定値の変更を通知するsignalを返す。"""
        return self.view_model.value.changed

    @property
    def is_disposed(self) -> bool:
        """Bindingまたは専用ViewModelが終了済みか返す。"""
        return (
            self._is_disposed
            or not qt.isValid(self)
            or self._view_model.is_disposed
        )

    def set_value(self, value: str) -> bool:
        """Commandを通して変更を要求し、正本が変わったか返す。"""
        return self.view_model.set_value_command.execute(value)

    def refresh(self) -> bool:
        """正本を再読込みし、公開値が変わったか返す。"""
        return self.view_model.refresh_from_store(self._store)

    def dispose(self) -> None:
        """同期を停止し、Qt objectの遅延破棄を予約する。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        if qt.isValid(self._view_model):
            self._view_model.dispose()
        if qt.isValid(self):
            self.deleteLater()

    def _require_active(self) -> None:
        """終了後の公開操作を拒否する。"""
        if self.is_disposed:
            raise RuntimeError("StringBindingは終了しています")

    def _create_view_model(self) -> StringViewModel:
        """派生Bindingが入力規則を差し替えられるViewModelを作る。"""
        return StringViewModel(parent=self)
