# coding: utf-8

from ._base import (
    Short3CompoundBasePlugOperator,
    Short3CompoundBaseAttrOperator,
    Short3CompoundBaseField,
)
from .......std.at.scalar.numeric.range.short import ShortField


class Short3PlugOperator(Short3CompoundBasePlugOperator["Short3AttrOperator"]):
    """3 成分の short 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = ShortField()
    y = ShortField()
    z = ShortField()


class Short3AttrOperator(Short3CompoundBaseAttrOperator[Short3PlugOperator]):
    """3 成分の short 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Short3Field(
    Short3CompoundBaseField[Short3AttrOperator, Short3PlugOperator]
):
    """3 成分の short 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Short3AttrOperator
    PLUG_CLS = Short3PlugOperator
