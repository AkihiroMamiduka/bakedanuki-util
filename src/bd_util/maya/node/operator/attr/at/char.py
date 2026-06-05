# coding: utf-8
from .._core import AttrOperator, PlugOperator, AttributeField


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


class CharField(AttributeField[CharAttrOperator, CharPlugOperator]):
    __slots__ = ()

    ATTR_CLS = CharAttrOperator
    PLUG_CLS = CharPlugOperator
