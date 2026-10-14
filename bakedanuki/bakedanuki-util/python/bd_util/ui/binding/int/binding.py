# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Generic, TypeVar

from ... import qt
from .presentation import IntPresentation
from .store import IntValueStore, PythonIntAttributeStore
from .view_model import IntViewModel

_StoreT = TypeVar("_StoreT", bound=IntValueStore, covariant=True)
_InstanceT = TypeVar("_InstanceT")


class IntBinding(qt.QObject, Generic[_StoreT]):
    """単一整数Storeと専用ViewModelの同期と寿命を管理する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """外部Storeに対応する専用ViewModelを作る。"""
        self._initialize(lambda _view_model: store, parent=parent)

    def _initialize(
        self,
        create_store: Callable[[IntViewModel], _StoreT],
        *,
        parent: qt.QObject | None,
    ) -> None:
        """constructorから一度だけ呼び、専用Storeを作る。"""
        super().__init__(parent)
        self._is_disposed = False
        self._view_model = IntViewModel(parent=self)
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
        presentation: IntPresentation | None = None,
        parent: qt.QObject | None = None,
    ) -> IntBinding[PythonIntAttributeStore[_InstanceT]]:
        """Pythonの既存整数属性を正本にするBindingを作る。"""
        return IntBinding(
            PythonIntAttributeStore(
                instance, attribute_name, presentation=presentation
            ),
            parent=parent,
        )

    @property
    def store(self) -> _StoreT:
        """正本を具体Store型のまま返す。"""
        return self._store

    @property
    def view_model(self) -> IntViewModel:
        """各Viewへ渡すViewModelを返す。"""
        self._require_active()
        return self._view_model

    @property
    def value(self) -> int:
        """最後に同期した確定整数を返す。"""
        return self.view_model.value.value

    @property
    def changed(self) -> qt.QtCore.SignalInstance:
        """確定値の変更signalを返す。"""
        return self.view_model.value.changed

    @property
    def is_disposed(self) -> bool:
        """明示終了またはQt owner破棄で終了したか返す。"""
        return (
            self._is_disposed
            or not qt.isValid(self)
            or self._view_model.is_disposed
        )

    def set_value(self, value: int) -> bool:
        """共通Commandを通して正本の整数値を変更する。"""
        return self.view_model.set_value_command.execute(value)

    def refresh(self) -> bool:
        """正本を読み直し、値が変わったか返す。"""
        return self.view_model.refresh_from_store(self._store)

    def dispose(self) -> None:
        """入力を止めてQt objectを遅延破棄する。正本は破棄しない。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        if qt.isValid(self._view_model):
            self._view_model.dispose()
        if qt.isValid(self):
            self.deleteLater()

    def _require_active(self) -> None:
        """終了後の操作を拒否する。"""
        if self.is_disposed:
            raise RuntimeError("IntBindingは終了しています")
