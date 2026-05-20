# coding: utf-8
from .._core import Attr, Plug


class LongPlug(Plug["LongAttr"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asInt()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueInt(self.plug, value)


class LongAttr(Attr[LongPlug]):
    __slots__ = ()

    ATTR_TYPE = "long"
    PLUG_CLS = LongPlug
