# coding: utf-8

from ._base import (
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.float import FloatField


class Float2PlugOperator(Float2CompoundBasePlugOperator["Float2AttrOperator"]):
    """2 成分の float 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = FloatField()
    y = FloatField()


class Float2AttrOperator(Float2CompoundBaseAttrOperator[Float2PlugOperator]):
    """2 成分の float 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Float2Field(
    Float2CompoundBaseField[Float2AttrOperator, Float2PlugOperator]
):
    """2 成分の float 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Float2AttrOperator
    PLUG_CLS = Float2PlugOperator
