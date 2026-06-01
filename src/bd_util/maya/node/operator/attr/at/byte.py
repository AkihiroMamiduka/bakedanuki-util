# coding: utf-8
from .._core import AttrOperator, PlugOperator


class BytePlugOperator(PlugOperator["ByteAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asChar()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueChar(self.plug, value)


class ByteAttrOperator(AttrOperator[BytePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "byte"
    PLUG_CLS = BytePlugOperator
