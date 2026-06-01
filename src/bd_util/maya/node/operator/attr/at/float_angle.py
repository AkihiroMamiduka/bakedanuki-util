# coding: utf-8
from .._core import AttrOperator, PlugOperator


class FloatAnglePlugOperator(PlugOperator["FloatAngleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(self.plug, value)


class FloatAngleAttrOperator(AttrOperator[FloatAnglePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "floatAngle"
    PLUG_CLS = FloatAnglePlugOperator
