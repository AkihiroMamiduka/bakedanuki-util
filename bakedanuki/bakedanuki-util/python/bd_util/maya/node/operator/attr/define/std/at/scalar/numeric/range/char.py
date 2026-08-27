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


class CharPlugOperator(NumericRangeBasePlugOperator["CharAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        """charプラグの現在値を1文字の文字列で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asChar()

    # set
    def set(self, value: str) -> None:
        """charプラグへ1文字の文字列をModifierManager経由で設定する。

        Args:
            value: 設定する1文字の文字列。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        self._node.modifier_manager.dg_mod.newPlugValueChar(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kChar)


class CharAttrOperator(NumericRangeBaseAttrOperator[CharPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "char"

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


class CharField(NumericRangeBaseField[CharAttrOperator, CharPlugOperator]):
    __slots__ = ()

    ATTR_CLS = CharAttrOperator
    PLUG_CLS = CharPlugOperator
