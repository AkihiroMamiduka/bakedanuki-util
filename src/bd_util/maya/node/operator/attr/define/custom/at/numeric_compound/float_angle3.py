# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._core import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)
from ....std.at.unit_scalar_range.float_angle import FloatAngleField


class FloatAngle3PlugOperator(
    NumericCompoundBasePlugOperator["FloatAngle3AttrOperator"]
):
    __slots__ = ()

    CHILD_M_FN = om.MFnUnitAttribute
    CHILD_M_ATTR_TYPE: int = om.MFnUnitAttribute.kAngle

    x = FloatAngleField()
    y = FloatAngleField()
    z = FloatAngleField()

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asMAngle().asDegrees()

    # set
    def _set_child_value(self, child_plug, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            child_plug, om.MAngle(value, om.MAngle.kDegrees)
        )


class FloatAngle3AttrOperator(
    NumericCompoundBaseAttrOperator[FloatAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatAngle3Field(
    NumericCompoundBaseField[FloatAngle3AttrOperator, FloatAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatAngle3AttrOperator
    PLUG_CLS = FloatAngle3PlugOperator
