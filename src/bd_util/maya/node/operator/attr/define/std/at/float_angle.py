# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.unit_range_base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


class FloatAnglePlugOperator(
    UnitRangeBasePlugOperator["FloatAngleAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(self.plug, value)

    @property
    def keyframe(self):
        return self._get_keyframe_manager()

    def _to_anim_curve_value(self, value: float) -> float:
        return om.MAngle(value, om.MAngle.kDegrees).asRadians()

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnUnitAttribute.kAngle)


class FloatAngleAttrOperator(
    UnitRangeBaseAttrOperator[FloatAnglePlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "floatAngle"


class FloatAngleField(
    UnitRangeBaseField[FloatAngleAttrOperator, FloatAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatAngleAttrOperator
    PLUG_CLS = FloatAnglePlugOperator
