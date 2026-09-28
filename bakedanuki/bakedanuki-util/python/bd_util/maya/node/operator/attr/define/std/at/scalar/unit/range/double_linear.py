# coding: utf-8
from typing import Any

from maya.api import OpenMaya as om

from ._base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


class DoubleLinearPlugOperator(
    UnitRangeBasePlugOperator["DoubleLinearAttrOperator"]
):
    """`doubleLinear` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> float:
        """doubleLinearプラグの現在値をcentimeter単位で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMDistance().asCentimeters()

    def set(self, value: float) -> None:
        """doubleLinearプラグへcentimeter値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する距離。単位はcentimeter。
        """
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node.modifier_manager.dg_mod.newPlugValueMDistance(
            self.plug, value
        )

    def add_attr(self):
        """doubleLinear 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnUnitAttribute.kDistance)


class DoubleLinearAttrOperator(
    UnitRangeBaseAttrOperator[DoubleLinearPlugOperator]
):
    """`doubleLinear` 属性の定義を保持する。"""

    __slots__ = ()

    ATTR_TYPE = "doubleLinear"

    def __init__(
        self,
        *args: Any,
        default_value: float | None = None,
        **kwargs: Any,
    ) -> None:
        # デフォルト値
        if default_value is None:
            default_value = 0.0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class DoubleLinearField(
    UnitRangeBaseField[DoubleLinearAttrOperator, DoubleLinearPlugOperator]
):
    """`doubleLinear` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DoubleLinearAttrOperator
    PLUG_CLS = DoubleLinearPlugOperator
