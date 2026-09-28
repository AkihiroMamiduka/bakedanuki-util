# coding: utf-8

from ._base import (
    DoubleLinear2CompoundBasePlugOperator,
    DoubleLinear2CompoundBaseAttrOperator,
    DoubleLinear2CompoundBaseField,
)
from .......std.at.scalar.unit.range.double_linear import DoubleLinearField


class DoubleLinear2PlugOperator(
    DoubleLinear2CompoundBasePlugOperator["DoubleLinear2AttrOperator"]
):
    """2 成分の double 型の距離 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleLinearField()
    y = DoubleLinearField()


class DoubleLinear2AttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[DoubleLinear2PlugOperator]
):
    """2 成分の double 型の距離 compound 属性の定義を保持する。"""

    __slots__ = ()


class DoubleLinear2Field(
    DoubleLinear2CompoundBaseField[
        DoubleLinear2AttrOperator, DoubleLinear2PlugOperator
    ]
):
    """2 成分の double 型の距離 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DoubleLinear2AttrOperator
    PLUG_CLS = DoubleLinear2PlugOperator
