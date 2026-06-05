# coding: utf-8
from ..._core import AttrOperator, PlugOperator, AttributeField


class LongPlugOperator(PlugOperator["LongAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asInt()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueInt(self.plug, value)


class LongAttrOperator(AttrOperator[LongPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "long"


class LongField(AttributeField[LongAttrOperator, LongPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LongAttrOperator
    PLUG_CLS = LongPlugOperator
