# coding: utf-8
from typing import Any

# maya
from maya.api import OpenMaya as om

# self
from ...........py.error import UnsupportedOperationError
from ._base import (
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
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asInt64()

    # set
    def set(self, value: int):
        self._node.modifier_manager.dg_mod.newPlugValueInt64(self.plug, value)

    def set_min(self, value: int | float) -> None:
        raise UnsupportedOperationError(
            "Setting min value is not supported for LongLongInt attributes."
        )

    def set_max(self, value: int | float) -> None:
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


class LongLongIntField(
    NumericRangeBaseField[LongLongIntAttrOperator, LongLongIntPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LongLongIntAttrOperator
    PLUG_CLS = LongLongIntPlugOperator
