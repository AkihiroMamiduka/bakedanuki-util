# coding: utf-8

# self
from ._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)


class QuatPlugOperator(Double4CompoundBasePlugOperator["Quat4AttrOperator"]):
    __slots__ = ()


class Quat4AttrOperator(Double4CompoundBaseAttrOperator[QuatPlugOperator]):
    __slots__ = ()


class Quat4Field(
    Double4CompoundBaseField[Quat4AttrOperator, QuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Quat4AttrOperator
    PLUG_CLS = QuatPlugOperator
