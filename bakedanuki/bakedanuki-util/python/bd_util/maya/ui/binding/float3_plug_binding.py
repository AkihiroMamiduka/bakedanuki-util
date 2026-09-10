# coding: utf-8
from typing import Generic, TypeVar

from ....ui import qt
from ....ui.binding.float3 import Float3Binding, Float3ViewModel
from .float3_plug import MayaFloat3PlugStore
from .float3_plug_resolver import MayaFloat3Plug

_PlugT = TypeVar("_PlugT", bound=MayaFloat3Plug, covariant=True)


class MayaFloat3PlugBinding(
    Float3Binding[MayaFloat3PlugStore[_PlugT]], Generic[_PlugT]
):
    """Mayaの3成分属性を正本とするStoreとViewModelを所有する。"""

    def __init__(
        self, plug: _PlugT, *, parent: qt.QObject | None = None
    ) -> None:
        """Mayaの現在値から各軸と3成分の初期状態を同期する。"""
        self._owned_store: MayaFloat3PlugStore[_PlugT] | None = None

        def create_store(
            view_model: Float3ViewModel,
        ) -> MayaFloat3PlugStore[_PlugT]:
            """ViewModelに対応するMaya StoreをこのBindingの子として作る。"""
            store = MayaFloat3PlugStore(view_model, plug, self)
            self._owned_store = store
            return store

        self._initialize(create_store, parent=parent)

    def dispose(self) -> None:
        """Maya callbackを解除して、全成分の入力と同期を終了する。"""
        try:
            if self._owned_store is not None and qt.isValid(self._owned_store):
                self._owned_store.dispose()
        finally:
            super().dispose()
