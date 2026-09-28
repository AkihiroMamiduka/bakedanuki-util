# coding: utf-8

from ._base import (
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseAttrOperator,
    Double2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.double import DoubleField


class Double2PlugOperator(
    Double2CompoundBasePlugOperator["Double2AttrOperator"]
):
    """2 成分の double 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleField()
    y = DoubleField()


class Double2AttrOperator(
    Double2CompoundBaseAttrOperator[Double2PlugOperator]
):
    """2 成分の double 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Double2Field(
    Double2CompoundBaseField[Double2AttrOperator, Double2PlugOperator]
):
    """2 成分の double 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Double2AttrOperator
    PLUG_CLS = Double2PlugOperator
