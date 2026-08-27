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


class FloatPlugOperator(
    RoundScalarPlugOperatorMixin,
    NumericRangeBasePlugOperator["FloatAttrOperator"],
):
    __slots__ = ()

    # get
    def get(self) -> float:
        """floatプラグの現在値を浮動小数点数で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asFloat()

    # set
    def set(self, value: float) -> None:
        """floatプラグへ値をModifierManager経由で設定する。

        Args:
            value: 設定する浮動小数点値。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        self._node.modifier_manager.dg_mod.newPlugValueFloat(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kFloat)


class FloatAttrOperator(NumericRangeBaseAttrOperator[FloatPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "float"

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


class FloatField(NumericRangeBaseField[FloatAttrOperator, FloatPlugOperator]):
    __slots__ = ()

    ATTR_CLS = FloatAttrOperator
    PLUG_CLS = FloatPlugOperator
