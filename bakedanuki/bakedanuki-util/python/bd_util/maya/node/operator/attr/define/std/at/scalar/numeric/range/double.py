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
from ..._round import RoundScalarPlugOperatorMixin


class DoublePlugOperator(
    RoundScalarPlugOperatorMixin,
    NumericRangeBasePlugOperator["DoubleAttrOperator"],
):
    __slots__ = ()

    # get
    def get(self) -> float:
        """doubleプラグの現在値を浮動小数点数で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asDouble()

    # set
    def set(self, value: float) -> None:
        """doubleプラグへ値をModifierManager経由で設定する。

        Args:
            value: 設定する浮動小数点値。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
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
