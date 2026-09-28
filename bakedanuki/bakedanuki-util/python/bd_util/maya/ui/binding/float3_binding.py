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
        """Store 接続後に Maya へ初期同期し、失敗時は callback を解放する。

        Args:
            store: Python 側の正本となる3成分 Store。
            maya_plug: 同期先の Maya 3成分 plug。`None` なら Maya View を作らない。
            parent: この `MayaFloat3Binding` を所有する `QObject`。
        """
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
        """Python 属性の tuple を正本とし、任意の Maya compound を接続する。

        Args:
            instance: 正本の属性を持つ Python object。
            attribute_name: 正本として扱う既存属性の名前。
            maya_plug: 同期先の Maya 3成分 plug。`None` なら Maya View を作らない。
            presentation: 全軸共通、または XYZ 別の表示設定。`None` なら既定の `FloatPresentation` を全軸に使う。
            parent: この `MayaFloat3Binding` を所有する `QObject`。

        Returns:
            Python 属性 Store を持つ `MayaFloat3Binding`。
        """
        return MayaFloat3Binding(
            PythonFloat3AttributeStore(
                instance, attribute_name, presentation=presentation
            ),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaFloat3PlugView[MayaFloat3Plug] | None:
        """Maya 同期状態、失敗理由、明示再同期の窓口を返す。`maya_plug` 未指定なら `None`。"""
        return self._maya_view

    def dispose(self) -> None:
        """全軸のMaya callbackを即座に解放してBindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
