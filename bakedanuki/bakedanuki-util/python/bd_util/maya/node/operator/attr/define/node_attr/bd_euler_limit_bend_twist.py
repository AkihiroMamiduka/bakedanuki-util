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


class MinPlugOperator(DoubleAngle3CompoundBasePlugOperator["MinAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minTwist", "mntw"),
        ("minBendH", "mnbh"),
        ("minBendV", "mnbv"),
    )

    minTwist = DoubleAngleField(default_value=-180.0)
    mntw = minTwist

    minBendH = DoubleAngleField(default_value=-180.0)
    mnbh = minBendH

    minBendV = DoubleAngleField(default_value=-180.0)
    mnbv = minBendV


class MinAttrOperator(DoubleAngle3CompoundBaseAttrOperator[MinPlugOperator]):
    __slots__ = ()

    minTwist = DoubleAngleField(default_value=-180.0)
    mntw = minTwist

    minBendH = DoubleAngleField(default_value=-180.0)
    mnbh = minBendH

    minBendV = DoubleAngleField(default_value=-180.0)
    mnbv = minBendV


class MinField(
    DoubleAngle3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minTwist = DoubleAngleField(default_value=-180.0)
    mntw = minTwist

    minBendH = DoubleAngleField(default_value=-180.0)
    mnbh = minBendH

    minBendV = DoubleAngleField(default_value=-180.0)
    mnbv = minBendV


class MaxPlugOperator(DoubleAngle3CompoundBasePlugOperator["MaxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxTwist", "mxtw"),
        ("maxBendH", "mxbh"),
        ("maxBendV", "mxbv"),
    )

    maxTwist = DoubleAngleField(default_value=180.0)
    mxtw = maxTwist

    maxBendH = DoubleAngleField(default_value=180.0)
    mxbh = maxBendH

    maxBendV = DoubleAngleField(default_value=180.0)
    mxbv = maxBendV


class MaxAttrOperator(DoubleAngle3CompoundBaseAttrOperator[MaxPlugOperator]):
    __slots__ = ()

    maxTwist = DoubleAngleField(default_value=180.0)
    mxtw = maxTwist

    maxBendH = DoubleAngleField(default_value=180.0)
    mxbh = maxBendH

    maxBendV = DoubleAngleField(default_value=180.0)
    mxbv = maxBendV


class MaxField(
    DoubleAngle3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxTwist = DoubleAngleField(default_value=180.0)
    mxtw = maxTwist

    maxBendH = DoubleAngleField(default_value=180.0)
    mxbh = maxBendH

    maxBendV = DoubleAngleField(default_value=180.0)
    mxbv = maxBendV


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


class OutputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputRotateX", "orx"),
        ("outputRotateY", "ory"),
        ("outputRotateZ", "orz"),
    )

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputRotatePlugOperator]
):
    __slots__ = ()

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateField(
    DoubleAngle3CompoundBaseField[
        OutputRotateAttrOperator, OutputRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateAttrOperator
    PLUG_CLS = OutputRotatePlugOperator

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ
