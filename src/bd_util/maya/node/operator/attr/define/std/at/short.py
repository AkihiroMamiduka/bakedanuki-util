# coding: utf-8
from ...._core import AttrOperator, PlugOperator, AttributeField


class ShortPlugOperator(PlugOperator["ShortAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asShort()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueShort(self.plug, value)


class ShortAttrOperator(AttrOperator[ShortPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "short"


class ShortField(AttributeField[ShortAttrOperator, ShortPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ShortAttrOperator
    PLUG_CLS = ShortPlugOperator
