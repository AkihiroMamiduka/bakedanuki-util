# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import (
    EnumBinding,
    EnumDefinition,
    EnumValueStore,
    PythonEnumAttributeStore,
    qt,
)
from .enum_plug_resolver import MayaEnumPlug
from .enum_plug import MayaEnumPlugView

_StoreT = TypeVar("_StoreT", bound=EnumValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaEnumBinding(EnumBinding[_StoreT]):
    """Python正本のStoreと任意のMaya enum Viewを1組だけ所有する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: MayaEnumPlug | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """Store 接続後に Maya へ初期同期し、失敗時は callback を解放する。

        Args:
            store: Python 側の正本となる enum Store。
            maya_plug: 同期先の Maya enum plug。`None` なら Maya View を作らない。
            parent: この `MayaEnumBinding` を所有する `QObject`。
        """
        self._maya_view: MayaEnumPlugView | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaEnumPlugView(
                    self.view_model, maya_plug, self
                )
        except Exception:
            self.dispose()
            raise

    @staticmethod
    def from_attribute(
        instance: _InstanceT,
        attribute_name: str,
        *,
        maya_plug: MayaEnumPlug | None = None,
        definition: EnumDefinition,
        parent: qt.QObject | None = None,
    ) -> MayaEnumBinding[PythonEnumAttributeStore[_InstanceT]]:
        """Python 属性を正本とし、任意の Maya plug と enum View を接続する。

        Args:
            instance: 正本の属性を持つ Python object。
            attribute_name: 正本として扱う既存属性の名前。
            maya_plug: 同期先の Maya enum plug。`None` なら Maya View を作らない。
            definition: 値と表示名の対応を表す `EnumDefinition`。
            parent: この `MayaEnumBinding` を所有する `QObject`。

        Returns:
            Python 属性 Store を持つ `MayaEnumBinding`。
        """
        return MayaEnumBinding(
            PythonEnumAttributeStore(
                instance, attribute_name, definition=definition
            ),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaEnumPlugView | None:
        """Maya 同期状態、失敗理由、明示再同期の窓口を返す。`maya_plug` 未指定なら `None`。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを即座に解放してからBindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
