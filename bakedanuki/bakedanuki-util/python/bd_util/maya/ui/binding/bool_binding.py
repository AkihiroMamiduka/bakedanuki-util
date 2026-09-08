# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import BoolBinding, BoolValueStore, PythonBoolAttributeStore, qt
from ...node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
from .bool_plug import MayaBoolPlugView

_StoreT = TypeVar("_StoreT", bound=BoolValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaBoolBinding(BoolBinding[_StoreT]):
    """Python側の正本と任意のMaya bool Viewを1組だけ所有する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: BoolPlugOperator | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """Store接続後にMayaへ初期同期し、失敗時は生成途中でも終了する。"""
        self._maya_view: MayaBoolPlugView | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaBoolPlugView(
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
        maya_plug: BoolPlugOperator | None = None,
        parent: qt.QObject | None = None,
    ) -> MayaBoolBinding[PythonBoolAttributeStore[_InstanceT]]:
        """Pythonのbool属性を正本として、任意のMaya plugと同期する。"""
        return MayaBoolBinding(
            PythonBoolAttributeStore(instance, attribute_name),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaBoolPlugView | None:
        """Maya Viewを返す。同期状態、失敗理由、再試行はここから操作する。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを即座に解除してからbindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
