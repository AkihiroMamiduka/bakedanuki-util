# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputRotateX", "irx"),
        ("inputRotateY", "iry"),
        ("inputRotateZ", "irz"),
    )

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputRotatePlugOperator]
):
    __slots__ = ()

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputRotateField(
    DoubleAngle3CompoundBaseField[
        InputRotateAttrOperator, InputRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputRotateAttrOperator
    PLUG_CLS = InputRotatePlugOperator

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class AxisRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["AxisRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisRotateX", "arx"),
        ("axisRotateY", "ary"),
        ("axisRotateZ", "arz"),
    )

    axisRotateX = DoubleAngleField(default_value=0.0)
    arx = axisRotateX

    axisRotateY = DoubleAngleField(default_value=0.0)
    ary = axisRotateY

    axisRotateZ = DoubleAngleField(default_value=0.0)
    arz = axisRotateZ


class AxisRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[AxisRotatePlugOperator]
):
    __slots__ = ()

    axisRotateX = DoubleAngleField(default_value=0.0)
    arx = axisRotateX

    axisRotateY = DoubleAngleField(default_value=0.0)
    ary = axisRotateY

    axisRotateZ = DoubleAngleField(default_value=0.0)
    arz = axisRotateZ


class AxisRotateField(
    DoubleAngle3CompoundBaseField[
        AxisRotateAttrOperator, AxisRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AxisRotateAttrOperator
    PLUG_CLS = AxisRotatePlugOperator

    axisRotateX = DoubleAngleField(default_value=0.0)
    arx = axisRotateX

    axisRotateY = DoubleAngleField(default_value=0.0)
    ary = axisRotateY

    axisRotateZ = DoubleAngleField(default_value=0.0)
    arz = axisRotateZ


class OutputPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputTwist", "otw"),
        ("outputBendH", "obh"),
        ("outputBendV", "obv"),
    )

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist

    outputBendH = DoubleAngleField(default_value=0.0, writable=False)
    obh = outputBendH

    outputBendV = DoubleAngleField(default_value=0.0, writable=False)
    obv = outputBendV


class OutputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist

    outputBendH = DoubleAngleField(default_value=0.0, writable=False)
    obh = outputBendH

    outputBendV = DoubleAngleField(default_value=0.0, writable=False)
    obv = outputBendV


class OutputField(
    DoubleAngle3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist

    outputBendH = DoubleAngleField(default_value=0.0, writable=False)
    obh = outputBendH

    outputBendV = DoubleAngleField(default_value=0.0, writable=False)
    obv = outputBendV
