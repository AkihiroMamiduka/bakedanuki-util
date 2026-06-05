# coding: utf-8
from ..._core import AttrOperator, PlugOperator, AttributeField


class LongLongIntPlugOperator(PlugOperator["LongLongIntAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asInt64()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueInt64(self.plug, value)


class LongLongIntAttrOperator(AttrOperator[LongLongIntPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "long long int"


class LongLongIntField(
    AttributeField[LongLongIntAttrOperator, LongLongIntPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LongLongIntAttrOperator
    PLUG_CLS = LongLongIntPlugOperator
