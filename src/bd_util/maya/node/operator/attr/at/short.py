# coding: utf-8
from .._core import Attr, Plug


class ShortPlug(Plug["ShortAttr"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asShort()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueShort(self.plug, value)


class ShortAttr(Attr[ShortPlug]):
    __slots__ = ()

    ATTR_TYPE = "short"
    PLUG_CLS = ShortPlug
