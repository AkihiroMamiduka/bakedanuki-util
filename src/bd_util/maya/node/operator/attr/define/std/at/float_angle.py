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

    @property
    def keyframe(self):
        return self._get_keyframe_manager()

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
