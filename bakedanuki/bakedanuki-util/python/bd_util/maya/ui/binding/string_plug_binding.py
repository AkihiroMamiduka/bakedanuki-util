# coding: utf-8
from __future__ import annotations

from ....ui import StringBinding, StringViewModel, qt
from .string_plug import MayaStringPlugStore
from .string_plug_resolver import MayaStringPlug


class MayaStringPlugBinding(StringBinding[MayaStringPlugStore]):
    """Maya string属性を正本とするStoreとViewModelを所有する。"""

    def __init__(
        self, plug: MayaStringPlug, *, parent: qt.QObject | None = None
    ) -> None:
        """Mayaの現在値を初期読込みし、書き戻さずに接続する。"""
        self._owned_store: MayaStringPlugStore | None = None

        def create_store(view_model: StringViewModel) -> MayaStringPlugStore:
            """BindingをownerとしてMaya Storeを生成する。"""
            store = MayaStringPlugStore(view_model, plug, self)
            self._owned_store = store
            return store

        self._initialize(create_store, parent=parent)

    def dispose(self) -> None:
        """所有するMaya callbackを解除してからBindingを終了する。"""
        try:
            store = self._owned_store
            if store is not None and qt.isValid(store):
                store.dispose()
        finally:
            super().dispose()
