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
        """Store 接続後に Maya へ初期同期し、失敗時は生成途中でも終了する。

        Args:
            store: Python 側の正本となる bool Store。
            maya_plug: 同期先の Maya bool plug。`None` なら Maya View を作らない。
            parent: この `MayaBoolBinding` を所有する `QObject`。
        """
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
        """Python の bool 属性を正本として、任意の Maya plug と同期する。

        Args:
            instance: 正本の属性を持つ Python object。
            attribute_name: 正本として扱う既存属性の名前。
            maya_plug: 同期先の Maya bool plug。`None` なら Maya View を作らない。
            parent: この `MayaBoolBinding` を所有する `QObject`。

        Returns:
            Python 属性 Store を持つ `MayaBoolBinding`。
        """
        return MayaBoolBinding(
            PythonBoolAttributeStore(instance, attribute_name),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaBoolPlugView | None:
        """Maya View を返す。同期状態、失敗理由、再試行はここから操作する。`maya_plug` 未指定なら `None`。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを即座に解除してからbindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
