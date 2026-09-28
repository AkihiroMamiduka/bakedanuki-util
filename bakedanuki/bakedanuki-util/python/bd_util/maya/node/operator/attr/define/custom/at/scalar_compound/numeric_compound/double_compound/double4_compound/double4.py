# coding: utf-8

from ...........value import Double4
from ._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)
from ...._round import RoundCompoundPlugOperatorMixin
from .......std.at.scalar.numeric.range.double import DoubleField


class Double4PlugOperator(
    RoundCompoundPlugOperatorMixin,
    Double4CompoundBasePlugOperator["Double4AttrOperator", Double4],
):
    """4 成分の double 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    VALUE_TYPE = Double4

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()
    w = DoubleField()


class Double4AttrOperator(
    Double4CompoundBaseAttrOperator[Double4PlugOperator]
):
    """4 成分の double 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Double4Field(
    Double4CompoundBaseField[Double4AttrOperator, Double4PlugOperator]
):
    """4 成分の double 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Double4AttrOperator
    PLUG_CLS = Double4PlugOperator
