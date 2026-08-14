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


class DoublePlugOperator(NumericRangeBasePlugOperator["DoubleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asDouble()

    # set
    def set(self, value: float):
        self._node.modifier_manager.dg_mod.newPlugValueDouble(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kDouble)


class DoubleAttrOperator(NumericRangeBaseAttrOperator[DoublePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double"

    def __init__(
        self,
        *args: Any,
        default_value: float | None = None,
        **kwargs: Any,
    ) -> None:
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
