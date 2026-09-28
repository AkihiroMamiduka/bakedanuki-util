# coding: utf-8

from ._base import (
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBaseField,
)
from .......std.at.scalar.numeric.range.float import FloatField


class Float3PlugOperator(Float3CompoundBasePlugOperator["Float3AttrOperator"]):
    """3 成分の float 型 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = FloatField()
    y = FloatField()
    z = FloatField()


class Float3AttrOperator(Float3CompoundBaseAttrOperator[Float3PlugOperator]):
    """3 成分の float 型 compound 属性の定義を保持する。"""

    __slots__ = ()


class Float3Field(
    Float3CompoundBaseField[Float3AttrOperator, Float3PlugOperator]
):
    """3 成分の float 型 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Float3AttrOperator
    PLUG_CLS = Float3PlugOperator
