# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_range_base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class DoublePlugOperator(NumericRangeBasePlugOperator["DoubleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asDouble()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueDouble(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kDouble)


class DoubleAttrOperator(NumericRangeBaseAttrOperator[DoublePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0.0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class DoubleField(
    NumericRangeBaseField[DoubleAttrOperator, DoublePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DoubleAttrOperator
    PLUG_CLS = DoublePlugOperator
