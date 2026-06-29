# coding: utf-8

# self
from ._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)
from .......std.at.numeric_scalar_range.double import DoubleField


class QuatPlugOperator(Double4CompoundBasePlugOperator["Quat4AttrOperator"]):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()
    w = DoubleField()


class Quat4AttrOperator(Double4CompoundBaseAttrOperator[QuatPlugOperator]):
    __slots__ = ()

    def __init__(self, *args, default_value=None, **kwargs):
        if default_value is None:
            default_value = (0.0, 0.0, 0.0, 1.0)
        super().__init__(*args, default_value=default_value, **kwargs)


class Quat4Field(
    Double4CompoundBaseField[Quat4AttrOperator, QuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Quat4AttrOperator
    PLUG_CLS = QuatPlugOperator
