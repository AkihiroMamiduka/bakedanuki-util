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


class LongPlugOperator(NumericRangeBasePlugOperator["LongAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> int:
        """longプラグの現在値を整数で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asInt()

    # set
    def set(self, value: int) -> None:
        """longプラグへ整数値をModifierManager経由で設定する。

        Args:
            value: 設定する整数値。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        self._node.modifier_manager.dg_mod.newPlugValueInt(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kLong)


class LongAttrOperator(NumericRangeBaseAttrOperator[LongPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "long"

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


class LongField(NumericRangeBaseField[LongAttrOperator, LongPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LongAttrOperator
    PLUG_CLS = LongPlugOperator
