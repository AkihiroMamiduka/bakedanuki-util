# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class ValuePlugOperator(QuatCompoundBasePlugOperator["ValueAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
        ("valueW", "vw"),
    )

    valueX = DoubleField(default_value=0.0)
    vx = valueX

    valueY = DoubleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleField(default_value=0.0)
    vz = valueZ

    valueW = DoubleField(default_value=1.0)
    vw = valueW


class ValueAttrOperator(QuatCompoundBaseAttrOperator[ValuePlugOperator]):
    __slots__ = ()

    valueX = DoubleField(default_value=0.0)
    vx = valueX

    valueY = DoubleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleField(default_value=0.0)
    vz = valueZ

    valueW = DoubleField(default_value=1.0)
    vw = valueW


class ValueField(QuatCompoundBaseField[ValueAttrOperator, ValuePlugOperator]):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = DoubleField(default_value=0.0)
    vx = valueX

    valueY = DoubleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleField(default_value=0.0)
    vz = valueZ

    valueW = DoubleField(default_value=1.0)
    vw = valueW
