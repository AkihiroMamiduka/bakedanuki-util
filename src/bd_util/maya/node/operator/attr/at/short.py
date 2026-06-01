# coding: utf-8
from .._core import AttrOperator, PlugOperator


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
    PLUG_CLS = ShortPlugOperator
