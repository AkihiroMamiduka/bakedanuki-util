# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import (
    Float3Binding,
    Float3ValueStore,
    FloatPresentation,
    PythonFloat3AttributeStore,
    qt,
)
from .float3_plug_resolver import MayaFloat3Plug
from .float3_plug_view import MayaFloat3PlugView

_StoreT = TypeVar("_StoreT", bound=Float3ValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaFloat3Binding(Float3Binding[_StoreT]):
    """Python正本の3成分Storeと任意のMaya Viewを所有する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: MayaFloat3Plug | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """Store接続後にMayaへ初期同期し、失敗時はcallbackを解放する。"""
        self._maya_view: MayaFloat3PlugView[MayaFloat3Plug] | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaFloat3PlugView(
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
        maya_plug: MayaFloat3Plug | None = None,
        presentation: (
            FloatPresentation
            | tuple[FloatPresentation, FloatPresentation, FloatPresentation]
            | None
        ) = None,
        parent: qt.QObject | None = None,
    ) -> MayaFloat3Binding[PythonFloat3AttributeStore[_InstanceT]]:
        """Python属性のtupleを正本とし、任意のMaya compoundを接続する。"""
        return MayaFloat3Binding(
            PythonFloat3AttributeStore(
                instance, attribute_name, presentation=presentation
            ),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaFloat3PlugView[MayaFloat3Plug] | None:
        """Maya同期状態、失敗理由、明示再同期の窓口を返す。"""
        return self._maya_view

    def dispose(self) -> None:
        """全軸のMaya callbackを即座に解放してBindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
