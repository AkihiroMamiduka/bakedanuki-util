# coding: utf-8
from typing import Any

from maya.api import OpenMaya as om

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
    """`double` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> float:
        """doubleプラグの現在値を浮動小数点数で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asDouble()

    def set(self, value: float) -> None:
        """doubleプラグへ値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する浮動小数点値。
        """
        self._node.modifier_manager.dg_mod.newPlugValueDouble(self.plug, value)

    def add_attr(self):
        """double 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnNumericData.kDouble)


class DoubleAttrOperator(NumericRangeBaseAttrOperator[DoublePlugOperator]):
    """`double` 属性の定義を保持する。"""

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
    """`double` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DoubleAttrOperator
    PLUG_CLS = DoublePlugOperator
