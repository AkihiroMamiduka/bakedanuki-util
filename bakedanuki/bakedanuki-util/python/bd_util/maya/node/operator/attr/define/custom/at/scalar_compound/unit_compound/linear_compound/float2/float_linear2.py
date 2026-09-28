# coding: utf-8


from ._base import (
    FloatLinear2CompoundBasePlugOperator,
    FloatLinear2CompoundBaseAttrOperator,
    FloatLinear2CompoundBaseField,
)

from .......std.at.scalar.unit.range.float_linear import FloatLinearField


class FloatLinear2PlugOperator(
    FloatLinear2CompoundBasePlugOperator["FloatLinear2AttrOperator"]
):
    """2 成分の float 型の距離 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = FloatLinearField()
    y = FloatLinearField()


class FloatLinear2AttrOperator(
    FloatLinear2CompoundBaseAttrOperator[FloatLinear2PlugOperator]
):
    """2 成分の float 型の距離 compound 属性の定義を保持する。"""

    __slots__ = ()


class FloatLinear2Field(
    FloatLinear2CompoundBaseField[
        FloatLinear2AttrOperator, FloatLinear2PlugOperator
    ]
):
    """2 成分の float 型の距離 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = FloatLinear2AttrOperator
    PLUG_CLS = FloatLinear2PlugOperator
