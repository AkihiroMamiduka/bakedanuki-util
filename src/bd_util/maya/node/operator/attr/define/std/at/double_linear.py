# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.unit_range_base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)

M_ATTR_KIND = om.MFnUnitAttribute.kDistance


class DoubleLinearPlugOperator(
    UnitRangeBasePlugOperator["DoubleLinearAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMDistance().asCentimeters()

    # set
    def set(self, value: float):
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(M_ATTR_KIND)


class DoubleLinearAttrOperator(
    UnitRangeBaseAttrOperator[DoubleLinearPlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "doubleLinear"

    def __init__(self, *args, default_value=None, **kwargs):
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
    __slots__ = ()

    ATTR_CLS = DoubleLinearAttrOperator
    PLUG_CLS = DoubleLinearPlugOperator

    M_ATTR_TYPE = M_ATTR_KIND
    M_FN = om.MFnUnitAttribute
