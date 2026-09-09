# coding: utf-8
from __future__ import annotations

from ....ui import FloatBinding, FloatViewModel, qt
from .float_plug_resolver import MayaFloatPlug
from .float_plug import MayaFloatPlugStore


class MayaFloatPlugBinding(FloatBinding[MayaFloatPlugStore]):
    """Maya浮動小数点plugを正本とするStoreとViewModelを所有する。"""

    def __init__(
        self,
        plug: MayaFloatPlug,
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """Mayaの現在値を読み取り、書き戻さずに初期同期する。"""
        self._owned_store: MayaFloatPlugStore | None = None

        def create_store(view_model: FloatViewModel) -> MayaFloatPlugStore:
            store = MayaFloatPlugStore(view_model, plug, self)
            self._owned_store = store
            return store

        self._initialize(create_store, parent=parent)

    def dispose(self) -> None:
        """所有するStoreのcallbackを即座に解除し、入力と同期を終了する。"""
        try:
            store = self._owned_store
            if store is not None and qt.isValid(store):
                store.dispose()
        finally:
            super().dispose()
