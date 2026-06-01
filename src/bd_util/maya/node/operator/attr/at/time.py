# coding: utf-8
from .._core import AttrOperator, PlugOperator


class TimePlug(PlugOperator["TimeAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMTime()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMTime(self.plug, value)


class TimeAttr(AttrOperator[TimePlug]):
    __slots__ = ()

    ATTR_TYPE = "time"
    PLUG_CLS = TimePlug
