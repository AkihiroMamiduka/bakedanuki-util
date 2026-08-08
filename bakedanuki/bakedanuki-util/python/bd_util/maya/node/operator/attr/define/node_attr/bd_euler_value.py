# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class ValuePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = DoubleAngleField(default_value=0.0)
    vx = valueX

    valueY = DoubleAngleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleAngleField(default_value=0.0)
    vz = valueZ


class ValueAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueX = DoubleAngleField(default_value=0.0)
    vx = valueX

    valueY = DoubleAngleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleAngleField(default_value=0.0)
    vz = valueZ


class ValueField(
    DoubleAngle3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = DoubleAngleField(default_value=0.0)
    vx = valueX

    valueY = DoubleAngleField(default_value=0.0)
    vy = valueY

    valueZ = DoubleAngleField(default_value=0.0)
    vz = valueZ
