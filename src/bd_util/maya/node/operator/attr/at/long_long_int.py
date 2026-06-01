# coding: utf-8
from .._core import AttrOperator, PlugOperator


class LongLongIntPlug(PlugOperator["LongLongIntAttr"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asInt64()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueInt64(self.plug, value)


class LongLongIntAttr(AttrOperator[LongLongIntPlug]):
    __slots__ = ()

    ATTR_TYPE = "long long int"
    PLUG_CLS = LongLongIntPlug
