# coding: utf-8
from .._core import AttrOperator, PlugOperator


class FloatLinearPlugOperator(PlugOperator["FloatLinearAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMDistance()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)


class FloatLinearAttrOperator(AttrOperator[FloatLinearPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "floatLinear"
    PLUG_CLS = FloatLinearPlugOperator
