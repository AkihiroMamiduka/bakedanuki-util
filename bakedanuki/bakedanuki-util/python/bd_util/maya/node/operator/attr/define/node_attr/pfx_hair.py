# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class CameraPointPlugOperator(
    Double3CompoundBasePlugOperator["CameraPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cameraPointX", "cpx"),
        ("cameraPointY", "cpy"),
        ("cameraPointZ", "cpz"),
    )

    cameraPointX = DoubleField(default_value=0.0)
    cpx = cameraPointX

    cameraPointY = DoubleField(default_value=0.0)
    cpy = cameraPointY

    cameraPointZ = DoubleField(default_value=0.0)
    cpz = cameraPointZ


class CameraPointAttrOperator(
    Double3CompoundBaseAttrOperator[CameraPointPlugOperator]
):
    __slots__ = ()

    cameraPointX = DoubleField(default_value=0.0)
    cpx = cameraPointX

    cameraPointY = DoubleField(default_value=0.0)
    cpy = cameraPointY

    cameraPointZ = DoubleField(default_value=0.0)
    cpz = cameraPointZ


class CameraPointField(
    Double3CompoundBaseField[CameraPointAttrOperator, CameraPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraPointAttrOperator
    PLUG_CLS = CameraPointPlugOperator

    cameraPointX = DoubleField(default_value=0.0)
    cpx = cameraPointX

    cameraPointY = DoubleField(default_value=0.0)
    cpy = cameraPointY

    cameraPointZ = DoubleField(default_value=0.0)
    cpz = cameraPointZ
