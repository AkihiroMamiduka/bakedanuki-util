# coding: utf-8
from typing import Any

from maya.api import OpenMaya as om

from ._base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class BytePlugOperator(NumericRangeBasePlugOperator["ByteAttrOperator"]):
    """`byte` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> int:
        """byteプラグの現在値を整数で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asChar()

    def set(self, value: int) -> None:
        """byteプラグへ整数値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する整数値。
        """
        self._node.modifier_manager.dg_mod.newPlugValueChar(self.plug, value)

    def add_attr(self):
        """byte 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnNumericData.kByte)


class ByteAttrOperator(NumericRangeBaseAttrOperator[BytePlugOperator]):
    """`byte` 属性の定義を保持する。"""

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
    """`byte` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = ByteAttrOperator
    PLUG_CLS = BytePlugOperator
