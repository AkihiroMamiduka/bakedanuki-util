# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
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
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node.modifier_manager.dg_mod.newPlugValueMAngle(self.plug, value)

    def _to_anim_curve_value(self, value: float) -> float:
        return om.MAngle(value, om.MAngle.kDegrees).asRadians()

    def _from_anim_curve_value(self, value: float) -> float:
        return om.MAngle(value, om.MAngle.kRadians).asDegrees()

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
