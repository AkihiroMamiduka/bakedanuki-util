# coding: utf-8
from __future__ import annotations

from ....ui import EnumBinding, EnumViewModel, qt
from .enum_plug_resolver import MayaEnumPlug
from .enum_plug import MayaEnumPlugStore


class MayaEnumPlugBinding(EnumBinding[MayaEnumPlugStore]):
    """Mayaenumplugを正本とするStoreとViewModelを所有する。"""

    def __init__(
        self,
        plug: MayaEnumPlug,
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """Mayaの現在値を読み取り、書き戻さずに初期同期する。"""
        self._owned_store: MayaEnumPlugStore | None = None

        def create_store(view_model: EnumViewModel) -> MayaEnumPlugStore:
            store = MayaEnumPlugStore(view_model, plug, self)
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
