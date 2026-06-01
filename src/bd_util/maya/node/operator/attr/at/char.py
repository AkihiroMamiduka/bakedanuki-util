# coding: utf-8
from .._core import AttrOperator, PlugOperator


class CharPlug(PlugOperator["CharAttr"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        return self.plug.asChar()

    # set
    def set(self, value: str):
        self._node._dg_mod.newPlugValueChar(self.plug, value)


class CharAttr(AttrOperator[CharPlug]):
    __slots__ = ()

    ATTR_TYPE = "char"
    PLUG_CLS = CharPlug
