# coding: utf-8


from ._base import (
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBaseField,
)

from .......std.at.scalar.unit.range.float_linear import FloatLinearField


class FloatLinear3PlugOperator(
    FloatLinear3CompoundBasePlugOperator["FloatLinear3AttrOperator"]
):
    """3 成分の float 型の距離 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = FloatLinearField()
    y = FloatLinearField()
    z = FloatLinearField()


class FloatLinear3AttrOperator(
    FloatLinear3CompoundBaseAttrOperator[FloatLinear3PlugOperator]
):
    """3 成分の float 型の距離 compound 属性の定義を保持する。"""

    __slots__ = ()


class FloatLinear3Field(
    FloatLinear3CompoundBaseField[
        FloatLinear3AttrOperator, FloatLinear3PlugOperator
    ]
):
    """3 成分の float 型の距離 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = FloatLinear3AttrOperator
    PLUG_CLS = FloatLinear3PlugOperator
