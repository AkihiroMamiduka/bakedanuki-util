# coding: utf-8
from .._core import AttrOperator, PlugOperator


class CharPlugOperator(PlugOperator["CharAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        return self.plug.asChar()

    # set
    def set(self, value: str):
        self._node._dg_mod.newPlugValueChar(self.plug, value)


class CharAttrOperator(AttrOperator[CharPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "char"
    PLUG_CLS = CharPlugOperator
