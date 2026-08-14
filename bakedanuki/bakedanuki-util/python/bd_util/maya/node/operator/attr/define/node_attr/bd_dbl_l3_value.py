# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class ValuePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = DoubleLinearField(default_value=0.0)
    vx = valueX

    valueY = DoubleLinearField(default_value=0.0)
    vy = valueY

    valueZ = DoubleLinearField(default_value=0.0)
    vz = valueZ


class ValueAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueX = DoubleLinearField(default_value=0.0)
    vx = valueX

    valueY = DoubleLinearField(default_value=0.0)
    vy = valueY

    valueZ = DoubleLinearField(default_value=0.0)
    vz = valueZ


class ValueField(
    DoubleLinear3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = DoubleLinearField(default_value=0.0)
    vx = valueX

    valueY = DoubleLinearField(default_value=0.0)
    vy = valueY

    valueZ = DoubleLinearField(default_value=0.0)
    vz = valueZ
