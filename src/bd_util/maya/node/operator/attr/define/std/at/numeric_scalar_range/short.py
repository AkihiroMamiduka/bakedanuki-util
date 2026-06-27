# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .numeric_single_range_base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class ShortPlugOperator(NumericRangeBasePlugOperator["ShortAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asShort()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueShort(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kShort)


class ShortAttrOperator(NumericRangeBaseAttrOperator[ShortPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "short"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class ShortField(NumericRangeBaseField[ShortAttrOperator, ShortPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ShortAttrOperator
    PLUG_CLS = ShortPlugOperator
