# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class FloatPlugOperator(NumericRangeBasePlugOperator["FloatAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asFloat()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueFloat(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kFloat)


class FloatAttrOperator(NumericRangeBaseAttrOperator[FloatPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "float"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = 0.0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class FloatField(NumericRangeBaseField[FloatAttrOperator, FloatPlugOperator]):
    __slots__ = ()

    ATTR_CLS = FloatAttrOperator
    PLUG_CLS = FloatPlugOperator
