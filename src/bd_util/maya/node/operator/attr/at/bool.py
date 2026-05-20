# coding: utf-8
from .._core import Attr, Plug


class BoolPlug(Plug["BoolAttr"]):
    __slots__ = ()

    # get
    def get(self) -> bool:
        return self.plug.asBool()

    # set
    def set(self, value: bool):
        self._node._dg_mod.newPlugValueBool(self.plug, value)


class BoolAttr(Attr[BoolPlug]):
    __slots__ = ()

    ATTR_TYPE = "bool"
    PLUG_CLS = BoolPlug
