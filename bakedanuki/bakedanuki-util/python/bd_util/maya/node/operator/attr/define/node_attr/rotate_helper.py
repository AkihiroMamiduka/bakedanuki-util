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


class UpPlugOperator(Double3CompoundBasePlugOperator["UpAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upX", "ux"),
        ("upY", "uy"),
        ("upZ", "uz"),
    )

    upX = DoubleField(default_value=0.0)
    ux = upX

    upY = DoubleField(default_value=1.0)
    uy = upY

    upZ = DoubleField(default_value=0.0)
    uz = upZ


class UpAttrOperator(Double3CompoundBaseAttrOperator[UpPlugOperator]):
    __slots__ = ()

    upX = DoubleField(default_value=0.0)
    ux = upX

    upY = DoubleField(default_value=1.0)
    uy = upY

    upZ = DoubleField(default_value=0.0)
    uz = upZ


class UpField(Double3CompoundBaseField[UpAttrOperator, UpPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UpAttrOperator
    PLUG_CLS = UpPlugOperator

    upX = DoubleField(default_value=0.0)
    ux = upX

    upY = DoubleField(default_value=1.0)
    uy = upY

    upZ = DoubleField(default_value=0.0)
    uz = upZ


class ForwardPlugOperator(
    Double3CompoundBasePlugOperator["ForwardAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forwardX", "fx"),
        ("forwardY", "fy"),
        ("forwardZ", "fz"),
    )

    forwardX = DoubleField(default_value=0.0)
    fx = forwardX

    forwardY = DoubleField(default_value=0.0)
    fy = forwardY

    forwardZ = DoubleField(default_value=1.0)
    fz = forwardZ


class ForwardAttrOperator(
    Double3CompoundBaseAttrOperator[ForwardPlugOperator]
):
    __slots__ = ()

    forwardX = DoubleField(default_value=0.0)
    fx = forwardX

    forwardY = DoubleField(default_value=0.0)
    fy = forwardY

    forwardZ = DoubleField(default_value=1.0)
    fz = forwardZ


class ForwardField(
    Double3CompoundBaseField[ForwardAttrOperator, ForwardPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForwardAttrOperator
    PLUG_CLS = ForwardPlugOperator

    forwardX = DoubleField(default_value=0.0)
    fx = forwardX

    forwardY = DoubleField(default_value=0.0)
    fy = forwardY

    forwardZ = DoubleField(default_value=1.0)
    fz = forwardZ


class RotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rx"),
        ("rotateY", "ry"),
        ("rotateZ", "rz"),
    )

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ
