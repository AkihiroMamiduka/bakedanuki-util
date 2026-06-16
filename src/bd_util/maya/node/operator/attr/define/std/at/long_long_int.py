# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ........py.error import UnsupportedOperationError
from .base.numeric_single_range_base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class LongLongIntPlugOperator(
    NumericRangeBasePlugOperator["LongLongIntAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> int:
        return self.plug.asInt64()

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueInt64(self.plug, value)

    def set_min(self, value: int):
        raise UnsupportedOperationError(
            "Setting min value is not supported for LongLongInt attributes."
        )

    def set_max(self, value: int):
        raise UnsupportedOperationError(
            "Setting max value is not supported for LongLongInt attributes."
        )

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kInt64)


class LongLongIntAttrOperator(
    NumericRangeBaseAttrOperator[LongLongIntPlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "long long int"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class LongLongIntField(
    NumericRangeBaseField[LongLongIntAttrOperator, LongLongIntPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LongLongIntAttrOperator
    PLUG_CLS = LongLongIntPlugOperator
