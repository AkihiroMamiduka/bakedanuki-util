# coding: utf-8

from ._base import (
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBaseField,
)
from .......std.at.scalar.numeric.range.double import DoubleField


class Double3PlugOperator(
    Double3CompoundBasePlugOperator["Double3AttrOperator"]
):
    """3 成分の double 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()


class Double3AttrOperator(
    Double3CompoundBaseAttrOperator[Double3PlugOperator]
):
    """3 成分の double 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Double3Field(
    Double3CompoundBaseField[Double3AttrOperator, Double3PlugOperator]
):
    """3 成分の double 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Double3AttrOperator
    PLUG_CLS = Double3PlugOperator
