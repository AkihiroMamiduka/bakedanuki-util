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
        return self.plug.asMDistance()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)

    @property
    def keyframe(self):
        return self._get_keyframe_manager()

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
