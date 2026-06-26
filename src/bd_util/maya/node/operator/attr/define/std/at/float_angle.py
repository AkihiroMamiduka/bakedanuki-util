# coding: utf-8
from maya.api import OpenMaya as om

from ...._core import AttrOperator, PlugOperator, AttributeField


class FloatAnglePlugOperator(PlugOperator["FloatAngleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(self.plug, value)

    def set_key_direct(self, value: float, frame: float):
        self._set_key_direct(value, frame)

    def insert_key_direct(self, frame: float, breakdown: bool = False) -> int:
        return self._insert_key_direct(frame, breakdown=breakdown)

    def delete_anim_curve(self) -> bool:
        return self._delete_anim_curve()

    def _to_anim_curve_value(self, value: float) -> float:
        return om.MAngle(value, om.MAngle.kDegrees).asRadians()


class FloatAngleAttrOperator(AttrOperator[FloatAnglePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "floatAngle"


class FloatAngleField(
    AttributeField[FloatAngleAttrOperator, FloatAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatAngleAttrOperator
    PLUG_CLS = FloatAnglePlugOperator
