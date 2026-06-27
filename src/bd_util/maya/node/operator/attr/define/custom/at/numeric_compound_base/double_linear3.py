# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._core import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)
from ....std.at.double_linear import DoubleLinearField


class DoubleLinear3PlugOperator(
    NumericCompoundBasePlugOperator["DoubleLinear3AttrOperator"]
):
    __slots__ = ()

    CHILD_M_FN = om.MFnUnitAttribute
    CHILD_M_ATTR_TYPE: int = om.MFnUnitAttribute.kDistance

    x = DoubleLinearField()
    y = DoubleLinearField()
    z = DoubleLinearField()

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asMDistance().asCentimeters()

    # set
    def _set_child_value(self, child_plug, value: float):
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node._dg_mod.newPlugValueMDistance(child_plug, value)


class DoubleLinear3AttrOperator(
    NumericCompoundBaseAttrOperator[DoubleLinear3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleLinear3Field(
    NumericCompoundBaseField[
        DoubleLinear3AttrOperator, DoubleLinear3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleLinear3AttrOperator
    PLUG_CLS = DoubleLinear3PlugOperator
