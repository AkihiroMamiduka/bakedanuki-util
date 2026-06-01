# coding: utf-8
from .._core import AttrOperator, PlugOperator


class FloatPlug(PlugOperator["FloatAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asFloat()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueFloat(self.plug, value)


class FloatAttr(AttrOperator[FloatPlug]):
    __slots__ = ()

    ATTR_TYPE = "float"
    PLUG_CLS = FloatPlug
