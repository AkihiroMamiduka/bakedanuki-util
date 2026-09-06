# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputPlugOperator(Double3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleField(default_value=0.0, readable=False)
    ix = inputX

    inputY = DoubleField(default_value=0.0, readable=False)
    iy = inputY

    inputZ = DoubleField(default_value=0.0, readable=False)
    iz = inputZ


class InputAttrOperator(Double3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputX = DoubleField(default_value=0.0, readable=False)
    ix = inputX

    inputY = DoubleField(default_value=0.0, readable=False)
    iy = inputY

    inputZ = DoubleField(default_value=0.0, readable=False)
    iz = inputZ


class InputField(
    Double3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleField(default_value=0.0, readable=False)
    ix = inputX

    inputY = DoubleField(default_value=0.0, readable=False)
    iy = inputY

    inputZ = DoubleField(default_value=0.0, readable=False)
    iz = inputZ


class RotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rx"),
        ("rotateY", "ry"),
        ("rotateZ", "rz"),
    )

    rotateX = DoubleAngleField(default_value=0.0, readable=False)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0, readable=False)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0, readable=False)
    rz = rotateZ


class RotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField(default_value=0.0, readable=False)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0, readable=False)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0, readable=False)
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField(default_value=0.0, readable=False)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0, readable=False)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0, readable=False)
    rz = rotateZ


class OutputPlugOperator(
    Double3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(Double3CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    Double3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ
