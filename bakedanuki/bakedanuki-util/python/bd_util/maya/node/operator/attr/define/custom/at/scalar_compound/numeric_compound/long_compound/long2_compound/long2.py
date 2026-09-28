# coding: utf-8

from ._base import (
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseAttrOperator,
    Long2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.long import LongField


class Long2PlugOperator(Long2CompoundBasePlugOperator["Long2AttrOperator"]):
    """2 成分の long 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = LongField()
    y = LongField()


class Long2AttrOperator(Long2CompoundBaseAttrOperator[Long2PlugOperator]):
    """2 成分の long 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Long2Field(Long2CompoundBaseField[Long2AttrOperator, Long2PlugOperator]):
    """2 成分の long 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Long2AttrOperator
    PLUG_CLS = Long2PlugOperator
