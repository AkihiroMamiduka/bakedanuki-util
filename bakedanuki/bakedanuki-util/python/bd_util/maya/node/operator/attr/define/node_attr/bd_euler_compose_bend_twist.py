# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputTwist", "itw"),
        ("inputBendH", "ibh"),
        ("inputBendV", "ibv"),
    )

    inputTwist = DoubleAngleField(default_value=0.0)
    itw = inputTwist

    inputBendH = DoubleAngleField(default_value=0.0)
    ibh = inputBendH

    inputBendV = DoubleAngleField(default_value=0.0)
    ibv = inputBendV


class InputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputTwist = DoubleAngleField(default_value=0.0)
    itw = inputTwist

    inputBendH = DoubleAngleField(default_value=0.0)
    ibh = inputBendH

    inputBendV = DoubleAngleField(default_value=0.0)
    ibv = inputBendV


class InputField(
    DoubleAngle3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputTwist = DoubleAngleField(default_value=0.0)
    itw = inputTwist

    inputBendH = DoubleAngleField(default_value=0.0)
    ibh = inputBendH

    inputBendV = DoubleAngleField(default_value=0.0)
    ibv = inputBendV


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
