# coding: utf-8
from .._core import Attr, Plug


class BytePlug(Plug["ByteAttr"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asChar()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueChar(self.plug, value)


class ByteAttr(Attr[BytePlug]):
    __slots__ = ()

    ATTR_TYPE = "byte"
    PLUG_CLS = BytePlug
