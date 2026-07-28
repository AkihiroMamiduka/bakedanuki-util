# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
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

    inputAX = DoubleAngleField(default_value=0.0)
    iax = inputAX

    inputAY = DoubleAngleField(default_value=0.0)
    iay = inputAY

    inputAZ = DoubleAngleField(default_value=0.0)
    iaz = inputAZ


class InputAAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputAPlugOperator]
):
    __slots__ = ()

    inputAX = DoubleAngleField(default_value=0.0)
    iax = inputAX

    inputAY = DoubleAngleField(default_value=0.0)
    iay = inputAY

    inputAZ = DoubleAngleField(default_value=0.0)
    iaz = inputAZ


class InputAField(
    DoubleAngle3CompoundBaseField[InputAAttrOperator, InputAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAAttrOperator
    PLUG_CLS = InputAPlugOperator

    inputAX = DoubleAngleField(default_value=0.0)
    iax = inputAX

    inputAY = DoubleAngleField(default_value=0.0)
    iay = inputAY

    inputAZ = DoubleAngleField(default_value=0.0)
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

    inputBX = DoubleAngleField(default_value=0.0)
    ibx = inputBX

    inputBY = DoubleAngleField(default_value=0.0)
    iby = inputBY

    inputBZ = DoubleAngleField(default_value=0.0)
    ibz = inputBZ


class InputBAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputBPlugOperator]
):
    __slots__ = ()

    inputBX = DoubleAngleField(default_value=0.0)
    ibx = inputBX

    inputBY = DoubleAngleField(default_value=0.0)
    iby = inputBY

    inputBZ = DoubleAngleField(default_value=0.0)
    ibz = inputBZ


class InputBField(
    DoubleAngle3CompoundBaseField[InputBAttrOperator, InputBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputBAttrOperator
    PLUG_CLS = InputBPlugOperator

    inputBX = DoubleAngleField(default_value=0.0)
    ibx = inputBX

    inputBY = DoubleAngleField(default_value=0.0)
    iby = inputBY

    inputBZ = DoubleAngleField(default_value=0.0)
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

    outputX = DoubleAngleField(default_value=0.0)
    ox = outputX

    outputY = DoubleAngleField(default_value=0.0)
    oy = outputY

    outputZ = DoubleAngleField(default_value=0.0)
    oz = outputZ


class OutputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleAngleField(default_value=0.0)
    ox = outputX

    outputY = DoubleAngleField(default_value=0.0)
    oy = outputY

    outputZ = DoubleAngleField(default_value=0.0)
    oz = outputZ


class OutputField(
    DoubleAngle3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleAngleField(default_value=0.0)
    ox = outputX

    outputY = DoubleAngleField(default_value=0.0)
    oy = outputY

    outputZ = DoubleAngleField(default_value=0.0)
    oz = outputZ
