# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class UpPlugOperator(
    Double3CompoundBasePlugOperator["UpAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upX", "ux"),
        ("upY", "uy"),
        ("upZ", "uz"),
    )

    upX = DoubleField()
    ux = upX

    upY = DoubleField()
    uy = upY

    upZ = DoubleField()
    uz = upZ


class UpAttrOperator(
    Double3CompoundBaseAttrOperator[UpPlugOperator]
):
    __slots__ = ()

    upX = DoubleField()
    ux = upX

    upY = DoubleField()
    uy = upY

    upZ = DoubleField()
    uz = upZ


class UpField(
    Double3CompoundBaseField[UpAttrOperator, UpPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpAttrOperator
    PLUG_CLS = UpPlugOperator

    upX = DoubleField()
    ux = upX

    upY = DoubleField()
    uy = upY

    upZ = DoubleField()
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

    forwardX = DoubleField()
    fx = forwardX

    forwardY = DoubleField()
    fy = forwardY

    forwardZ = DoubleField()
    fz = forwardZ


class ForwardAttrOperator(
    Double3CompoundBaseAttrOperator[ForwardPlugOperator]
):
    __slots__ = ()

    forwardX = DoubleField()
    fx = forwardX

    forwardY = DoubleField()
    fy = forwardY

    forwardZ = DoubleField()
    fz = forwardZ


class ForwardField(
    Double3CompoundBaseField[ForwardAttrOperator, ForwardPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForwardAttrOperator
    PLUG_CLS = ForwardPlugOperator

    forwardX = DoubleField()
    fx = forwardX

    forwardY = DoubleField()
    fy = forwardY

    forwardZ = DoubleField()
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

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ
