# coding: utf-8
from .._core import Attr, Plug


class DoubleLinearPlug(Plug["DoubleLinearAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMDistance()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)


class DoubleLinearAttr(Attr[DoubleLinearPlug]):
    __slots__ = ()

    ATTR_TYPE = "doubleLinear"
    PLUG_CLS = DoubleLinearPlug
