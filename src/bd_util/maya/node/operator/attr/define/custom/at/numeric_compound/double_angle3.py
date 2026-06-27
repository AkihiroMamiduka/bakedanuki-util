# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._core import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)
from ....std.at.double_angle import DoubleAngleField


class DoubleAngle3PlugOperator(
    NumericCompoundBasePlugOperator["DoubleAngle3AttrOperator"]
):
    __slots__ = ()

    CHILD_M_FN = om.MFnUnitAttribute
    CHILD_M_ATTR_TYPE: int = om.MFnUnitAttribute.kAngle

    x = DoubleAngleField()
    y = DoubleAngleField()
    z = DoubleAngleField()

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asMAngle().asDegrees()

    # set
    def _set_child_value(self, child_plug, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            child_plug, om.MAngle(value, om.MAngle.kDegrees)
        )


class DoubleAngle3AttrOperator(
    NumericCompoundBaseAttrOperator[DoubleAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleAngle3Field(
    NumericCompoundBaseField[
        DoubleAngle3AttrOperator, DoubleAngle3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngle3AttrOperator
    PLUG_CLS = DoubleAngle3PlugOperator
