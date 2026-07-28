# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class OutputPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleAngleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleAngleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleAngleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleAngleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleAngleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleAngleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    DoubleAngle3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleAngleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleAngleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleAngleField(default_value=0.0, writable=False)
    oz = outputZ
