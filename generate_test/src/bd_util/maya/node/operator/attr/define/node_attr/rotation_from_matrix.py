# coding: utf-8

from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
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

    outputX = DoubleAngleField()
    ox = outputX

    outputY = DoubleAngleField()
    oy = outputY

    outputZ = DoubleAngleField()
    oz = outputZ


class OutputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleAngleField()
    ox = outputX

    outputY = DoubleAngleField()
    oy = outputY

    outputZ = DoubleAngleField()
    oz = outputZ


class OutputField(
    DoubleAngle3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleAngleField()
    ox = outputX

    outputY = DoubleAngleField()
    oy = outputY

    outputZ = DoubleAngleField()
    oz = outputZ
