# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.unit_range_base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


def _float_to_angle(value: float) -> om.MAngle:
    return om.MAngle(value, om.MAngle.kDegrees)


def _float_to_radians(value: float) -> float:
    return _float_to_angle(value).asRadians()


M_ATTR_KIND = om.MFnUnitAttribute.kAngle


class DoubleAnglePlugOperator(
    UnitRangeBasePlugOperator["DoubleAngleAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            self.plug, _float_to_angle(value)
        )

    def set_min(self, value):
        super().set_min(_float_to_angle(value))

    def set_max(self, value):
        super().set_max(_float_to_angle(value))

    def set_soft_min(self, value):
        super().set_soft_min(_float_to_angle(value))

    def set_soft_max(self, value):
        super().set_soft_max(_float_to_angle(value))

    # add
    def add_attr(self):
        self._add_attr_base(M_ATTR_KIND)


class DoubleAngleAttrOperator(
    UnitRangeBaseAttrOperator[DoubleAnglePlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "doubleAngle"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0.0
        else:
            default_value = _float_to_radians(default_value)
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class DoubleAngleField(
    UnitRangeBaseField[DoubleAngleAttrOperator, DoubleAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngleAttrOperator
    PLUG_CLS = DoubleAnglePlugOperator

    M_ATTR_TYPE = M_ATTR_KIND
    M_FN = om.MFnUnitAttribute()
