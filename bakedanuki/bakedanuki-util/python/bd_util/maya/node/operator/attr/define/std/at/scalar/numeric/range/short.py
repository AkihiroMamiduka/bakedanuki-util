# coding: utf-8
from typing import Any

from maya.api import OpenMaya as om

from ._base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)


class ShortPlugOperator(NumericRangeBasePlugOperator["ShortAttrOperator"]):
    """`short` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> int:
        """shortプラグの現在値を整数で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asShort()

    def set(self, value: int) -> None:
        """shortプラグへ整数値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する整数値。
        """
        self._node.modifier_manager.dg_mod.newPlugValueShort(self.plug, value)

    def add_attr(self):
        """short 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnNumericData.kShort)


class ShortAttrOperator(NumericRangeBaseAttrOperator[ShortPlugOperator]):
    """`short` 属性の定義を保持する。"""

    __slots__ = ()

    ATTR_TYPE = "short"

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


class ShortField(NumericRangeBaseField[ShortAttrOperator, ShortPlugOperator]):
    """`short` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = ShortAttrOperator
    PLUG_CLS = ShortPlugOperator
