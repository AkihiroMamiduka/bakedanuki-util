# coding: utf-8

from ._base import (
    Short2CompoundBasePlugOperator,
    Short2CompoundBaseAttrOperator,
    Short2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.short import ShortField


class Short2PlugOperator(Short2CompoundBasePlugOperator["Short2AttrOperator"]):
    """2 成分の short 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = ShortField()
    y = ShortField()


class Short2AttrOperator(Short2CompoundBaseAttrOperator[Short2PlugOperator]):
    """2 成分の short 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Short2Field(
    Short2CompoundBaseField[Short2AttrOperator, Short2PlugOperator]
):
    """2 成分の short 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Short2AttrOperator
    PLUG_CLS = Short2PlugOperator
