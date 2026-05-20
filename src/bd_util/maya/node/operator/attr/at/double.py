# coding: utf-8
from .._core import Attr, Plug


class DoublePlug(Plug["DoubleAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asDouble()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueDouble(self.plug, value)


class DoubleAttr(Attr[DoublePlug]):
    __slots__ = ()

    ATTR_TYPE = "double"
    PLUG_CLS = DoublePlug
