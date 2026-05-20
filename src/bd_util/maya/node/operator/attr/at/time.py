# coding: utf-8
from .._core import Attr, Plug


class TimePlug(Plug["TimeAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMTime()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMTime(self.plug, value)


class TimeAttr(Attr[TimePlug]):
    __slots__ = ()

    ATTR_TYPE = "time"
    PLUG_CLS = TimePlug
