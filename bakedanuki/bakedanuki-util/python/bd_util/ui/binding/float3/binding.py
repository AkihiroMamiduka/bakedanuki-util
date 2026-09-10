# coding: utf-8
from collections.abc import Callable, Sequence
from typing import Generic, TypeVar

from ... import qt
from .store import Float3ValueStore
from .value import Float3
from .view_model import Float3ViewModel

_StoreT = TypeVar("_StoreT", bound=Float3ValueStore, covariant=True)


class Float3Binding(qt.QObject, Generic[_StoreT]):
    """3成分Storeと専用ViewModelの組み立て・操作・寿命をまとめる。"""

    def __init__(
        self, store: _StoreT, *, parent: qt.QObject | None = None
    ) -> None:
        """外部Storeの所有権を変更せずViewModelへ接続する。"""
        self._initialize(lambda _view_model: store, parent=parent)

    def _initialize(
        self,
        create_store: Callable[[Float3ViewModel], _StoreT],
        *,
        parent: qt.QObject | None,
    ) -> None:
        """constructorから一度だけStoreとViewModelを組み立てる。"""
        super().__init__(parent)
        self._is_disposed = False
        self._view_model = Float3ViewModel(self)
        try:
            self._store = create_store(self._view_model)
            self._view_model.attach_store(self._store)
        except Exception:
            self.dispose()
            raise

    @property
    def store(self) -> _StoreT:
        """具体型を維持した3成分Storeを返す。"""
        return self._store

    @property
    def view_model(self) -> Float3ViewModel:
        """各Viewで共有するViewModelを返す。"""
        if self.is_disposed:
            raise RuntimeError("Float3Bindingは終了しています")
        return self._view_model

    @property
    def value(self) -> Float3:
        """最後に同期した3成分値を返す。"""
        return self.view_model.value.value

    @property
    def changed(self) -> qt.QtCore.SignalInstance:
        """3成分tupleの変更を通知する既存signalを返す。"""
        return self.view_model.value.changed

    @property
    def is_disposed(self) -> bool:
        """明示終了またはQt ownerの破棄によって終了したか返す。"""
        return (
            self._is_disposed
            or not qt.isValid(self)
            or self._view_model.is_disposed
        )

    def set_value(self, value: Sequence[float]) -> bool:
        """公開単位の3成分を一括設定し、実値が変わったか返す。"""
        return self.view_model.set_value_command.execute(value)

    def refresh(self) -> bool:
        """正本の現在値・表示情報・編集可否を読み直す。"""
        return self.view_model.refresh()

    def dispose(self) -> None:
        """入力と同期を停止してQt objectの破棄を予約する。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        if qt.isValid(self._view_model):
            self._view_model.dispose()
        if qt.isValid(self):
            self.deleteLater()
