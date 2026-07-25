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
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMDistance()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)

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
