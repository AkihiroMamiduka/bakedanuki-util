# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


class FloatLinearPlugOperator(
    UnitRangeBasePlugOperator["FloatLinearAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> float:
        """floatLinearプラグの現在値をcentimeter単位で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMDistance().asCentimeters()

    # set
    def set(self, value: float) -> None:
        """floatLinearプラグへcentimeter値をModifierManager経由で設定する。

        Args:
            value: 設定する距離。単位はcentimeter。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        distance = om.MDistance(value, om.MDistance.kCentimeters)
        self._node.modifier_manager.dg_mod.newPlugValueMDistance(
            self.plug, distance
        )

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnUnitAttribute.kDistance)


class FloatLinearAttrOperator(
    UnitRangeBaseAttrOperator[FloatLinearPlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "floatLinear"


class FloatLinearField(
    UnitRangeBaseField[FloatLinearAttrOperator, FloatLinearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatLinearAttrOperator
    PLUG_CLS = FloatLinearPlugOperator
