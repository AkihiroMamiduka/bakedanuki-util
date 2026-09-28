# coding: utf-8

from ._base import (
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBaseField,
)
from .......std.at.scalar.unit.range.double_linear import DoubleLinearField


class DoubleLinear3PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["DoubleLinear3AttrOperator"]
):
    """3 成分の double 型の距離 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleLinearField()
    y = DoubleLinearField()
    z = DoubleLinearField()


class DoubleLinear3AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[DoubleLinear3PlugOperator]
):
    """3 成分の double 型の距離 compound 属性の定義を保持する。"""

    __slots__ = ()


class DoubleLinear3Field(
    DoubleLinear3CompoundBaseField[
        DoubleLinear3AttrOperator, DoubleLinear3PlugOperator
    ]
):
    """3 成分の double 型の距離 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DoubleLinear3AttrOperator
    PLUG_CLS = DoubleLinear3PlugOperator
