# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .numeric_single_range_base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class CharPlugOperator(NumericRangeBasePlugOperator["CharAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        return self.plug.asChar()

    # set
    def set(self, value: str):
        self._node._dg_mod.newPlugValueChar(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kChar)


class CharAttrOperator(NumericRangeBaseAttrOperator[CharPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "char"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class CharField(NumericRangeBaseField[CharAttrOperator, CharPlugOperator]):
    __slots__ = ()

    ATTR_CLS = CharAttrOperator
    PLUG_CLS = CharPlugOperator
