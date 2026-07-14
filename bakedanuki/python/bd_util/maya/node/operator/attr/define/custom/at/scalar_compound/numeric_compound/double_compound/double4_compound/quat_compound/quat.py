# coding: utf-8

# self
from ._base import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)
from ........std.at.numeric_scalar_range.double import DoubleField


class QuatPlugOperator(QuatCompoundBasePlugOperator["Quat4AttrOperator"]):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()
    w = DoubleField()


class Quat4AttrOperator(QuatCompoundBaseAttrOperator[QuatPlugOperator]):
    __slots__ = ()

    def __init__(self, *args, default_value=None, **kwargs):
        if default_value is None:
            default_value = (0.0, 0.0, 0.0, 1.0)
        super().__init__(*args, default_value=default_value, **kwargs)


class Quat4Field(QuatCompoundBaseField[Quat4AttrOperator, QuatPlugOperator]):
    __slots__ = ()

    ATTR_CLS = Quat4AttrOperator
    PLUG_CLS = QuatPlugOperator
