# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class InputPlugOperator(Double3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(Double3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputField(
    Double3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ
