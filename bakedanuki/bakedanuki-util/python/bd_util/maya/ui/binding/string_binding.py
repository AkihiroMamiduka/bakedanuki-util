# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import (
    PythonStringAttributeStore,
    StringBinding,
    StringValueStore,
    qt,
)
from .string_plug import MayaStringPlugView
from .string_plug_resolver import MayaStringPlug

_StoreT = TypeVar("_StoreT", bound=StringValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaStringBinding(StringBinding[_StoreT]):
    """Python正本と任意のMaya string Viewを所有する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: MayaStringPlug | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """Python Storeを接続し、指定したMaya plugへ初期同期する。"""
        self._maya_view: MayaStringPlugView | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaStringPlugView(
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
        maya_plug: MayaStringPlug | None = None,
        parent: qt.QObject | None = None,
    ) -> MayaStringBinding[PythonStringAttributeStore[_InstanceT]]:
        """Python文字列属性を正本とし、任意のMaya plugへ同期する。"""
        return MayaStringBinding(
            PythonStringAttributeStore(instance, attribute_name),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaStringPlugView | None:
        """Maya同期状態の窓口を返す。未指定なら`None`。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを解除してからPython側Bindingを終了する。"""
        try:
            view = self._maya_view
            if view is not None and qt.isValid(view):
                view.dispose()
        finally:
            super().dispose()
