# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import (
    FloatBinding,
    FloatPresentation,
    FloatValueStore,
    PythonFloatAttributeStore,
    qt,
)
from .float_plug_resolver import MayaFloatPlug
from .float_plug import MayaFloatPlugView

_StoreT = TypeVar("_StoreT", bound=FloatValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaFloatBinding(FloatBinding[_StoreT]):
    """Python正本のStoreと任意のMaya float Viewを1組だけ所有する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: MayaFloatPlug | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """Store接続後にMayaへ初期同期し、失敗時はcallbackを解放する。"""
        self._maya_view: MayaFloatPlugView | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaFloatPlugView(
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
        maya_plug: MayaFloatPlug | None = None,
        presentation: FloatPresentation | None = None,
        parent: qt.QObject | None = None,
    ) -> MayaFloatBinding[PythonFloatAttributeStore[_InstanceT]]:
        """Python属性を正本とし、任意のMaya plugと単位追従Viewを接続する。"""
        return MayaFloatBinding(
            PythonFloatAttributeStore(
                instance, attribute_name, presentation=presentation
            ),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaFloatPlugView | None:
        """Maya同期状態、失敗理由、明示再同期の窓口を返す。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを即座に解放してからBindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
