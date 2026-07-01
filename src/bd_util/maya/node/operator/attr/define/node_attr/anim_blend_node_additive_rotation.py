# coding: utf-8

from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputAPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputAAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputAX", "iax"),
        ("inputAY", "iay"),
        ("inputAZ", "iaz"),
    )

    inputAX = DoubleAngleField()
    iax = inputAX

    inputAY = DoubleAngleField()
    iay = inputAY

    inputAZ = DoubleAngleField()
    iaz = inputAZ


class InputAAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputAPlugOperator]
):
    __slots__ = ()

    inputAX = DoubleAngleField()
    iax = inputAX

    inputAY = DoubleAngleField()
    iay = inputAY

    inputAZ = DoubleAngleField()
    iaz = inputAZ


class InputAField(
    DoubleAngle3CompoundBaseField[InputAAttrOperator, InputAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAAttrOperator
    PLUG_CLS = InputAPlugOperator

    inputAX = DoubleAngleField()
    iax = inputAX

    inputAY = DoubleAngleField()
    iay = inputAY

    inputAZ = DoubleAngleField()
    iaz = inputAZ


class InputBPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputBX", "ibx"),
        ("inputBY", "iby"),
        ("inputBZ", "ibz"),
    )

    inputBX = DoubleAngleField()
    ibx = inputBX

    inputBY = DoubleAngleField()
    iby = inputBY

    inputBZ = DoubleAngleField()
    ibz = inputBZ


class InputBAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputBPlugOperator]
):
    __slots__ = ()

    inputBX = DoubleAngleField()
    ibx = inputBX

    inputBY = DoubleAngleField()
    iby = inputBY

    inputBZ = DoubleAngleField()
    ibz = inputBZ


class InputBField(
    DoubleAngle3CompoundBaseField[InputBAttrOperator, InputBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputBAttrOperator
    PLUG_CLS = InputBPlugOperator

    inputBX = DoubleAngleField()
    ibx = inputBX

    inputBY = DoubleAngleField()
    iby = inputBY

    inputBZ = DoubleAngleField()
    ibz = inputBZ


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
