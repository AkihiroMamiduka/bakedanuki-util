# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)
from ....std.at.unit_scalar_range.float_linear import FloatLinearField


class FloatLinear3PlugOperator(
    NumericCompoundBasePlugOperator["FloatLinear3AttrOperator"]
):
    __slots__ = ()

    CHILD_M_FN = om.MFnUnitAttribute
    CHILD_M_ATTR_TYPE: int = om.MFnUnitAttribute.kDistance

    x = FloatLinearField()
    y = FloatLinearField()
    z = FloatLinearField()

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asMDistance().asCentimeters()

    # set
    def _set_child_value(self, child_plug, value: float):
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node._dg_mod.newPlugValueMDistance(child_plug, value)


class FloatLinear3AttrOperator(
    NumericCompoundBaseAttrOperator[FloatLinear3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatLinear3Field(
    NumericCompoundBaseField[
        FloatLinear3AttrOperator, FloatLinear3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FloatLinear3AttrOperator
    PLUG_CLS = FloatLinear3PlugOperator
