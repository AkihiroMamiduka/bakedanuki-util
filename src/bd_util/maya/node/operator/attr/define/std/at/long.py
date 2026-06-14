# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_range_base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class LongPlugOperator(NumericRangeBasePlugOperator["LongAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asInt()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueInt(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kLong)


class LongAttrOperator(NumericRangeBaseAttrOperator[LongPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "long"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class LongField(NumericRangeBaseField[LongAttrOperator, LongPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LongAttrOperator
    PLUG_CLS = LongPlugOperator
