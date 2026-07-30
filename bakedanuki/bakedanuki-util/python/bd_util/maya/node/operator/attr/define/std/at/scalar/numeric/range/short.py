# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class ShortPlugOperator(NumericRangeBasePlugOperator["ShortAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asShort()

    # set
    def set(self, value: int):
        self._node.modifier_manager.dg_mod.newPlugValueShort(self.plug, value)

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
