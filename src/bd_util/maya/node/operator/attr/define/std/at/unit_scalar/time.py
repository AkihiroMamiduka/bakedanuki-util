# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .unit_base import (
    UnitBaseAttrOperator,
    UnitBasePlugOperator,
    UnitBaseField,
)


class TimePlugOperator(UnitBasePlugOperator["TimeAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMTime()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMTime(self.plug, value)

    def _to_anim_curve_value(self, value: float) -> om.MTime:
        return om.MTime(value, om.MTime.uiUnit())

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnUnitAttribute.kTime)


class TimeAttrOperator(UnitBaseAttrOperator[TimePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "time"


class TimeField(UnitBaseField[TimeAttrOperator, TimePlugOperator]):
    __slots__ = ()

    ATTR_CLS = TimeAttrOperator
    PLUG_CLS = TimePlugOperator
