# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class ValuePlugOperator(Double3CompoundBasePlugOperator["ValueAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = DoubleField(default_value=0.0)
    vx = valueX

    valueY = DoubleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleField(default_value=0.0)
    vz = valueZ


class ValueAttrOperator(Double3CompoundBaseAttrOperator[ValuePlugOperator]):
    __slots__ = ()

    valueX = DoubleField(default_value=0.0)
    vx = valueX

    valueY = DoubleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleField(default_value=0.0)
    vz = valueZ


class ValueField(
    Double3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = DoubleField(default_value=0.0)
    vx = valueX

    valueY = DoubleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleField(default_value=0.0)
    vz = valueZ
