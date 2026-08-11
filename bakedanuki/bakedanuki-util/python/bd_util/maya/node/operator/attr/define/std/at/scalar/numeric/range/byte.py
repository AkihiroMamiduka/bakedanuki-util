# coding: utf-8
from typing import Any

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class BytePlugOperator(NumericRangeBasePlugOperator["ByteAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asChar()

    # set
    def set(self, value: int):
        self._node.modifier_manager.dg_mod.newPlugValueChar(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kByte)


class ByteAttrOperator(NumericRangeBaseAttrOperator[BytePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "byte"

    def __init__(
        self,
        *args: Any,
        default_value: int | None = None,
        **kwargs: Any,
    ) -> None:
        # デフォルト値
        if default_value is None:
            default_value = 0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class ByteField(NumericRangeBaseField[ByteAttrOperator, BytePlugOperator]):
    __slots__ = ()

    ATTR_CLS = ByteAttrOperator
    PLUG_CLS = BytePlugOperator
