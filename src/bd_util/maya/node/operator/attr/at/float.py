# coding: utf-8
from .._core import Attr, Plug


class FloatPlug(Plug["FloatAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asFloat()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueFloat(self.plug, value)


class FloatAttr(Attr[FloatPlug]):
    __slots__ = ()

    ATTR_TYPE = "float"
    PLUG_CLS = FloatPlug
