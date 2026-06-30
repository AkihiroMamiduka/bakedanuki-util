# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InBoxMinPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InBoxMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inBoxMinX", "bmix"),
        ("inBoxMinY", "bmiy"),
        ("inBoxMinZ", "bmiz"),
    )

    inBoxMinX = DoubleLinearField()
    bmix = inBoxMinX

    inBoxMinY = DoubleLinearField()
    bmiy = inBoxMinY

    inBoxMinZ = DoubleLinearField()
    bmiz = inBoxMinZ


class InBoxMinAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InBoxMinPlugOperator]
):
    __slots__ = ()

    inBoxMinX = DoubleLinearField()
    bmix = inBoxMinX

    inBoxMinY = DoubleLinearField()
    bmiy = inBoxMinY

    inBoxMinZ = DoubleLinearField()
    bmiz = inBoxMinZ


class InBoxMinField(
    DoubleLinear3CompoundBaseField[InBoxMinAttrOperator, InBoxMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InBoxMinAttrOperator
    PLUG_CLS = InBoxMinPlugOperator

    inBoxMinX = DoubleLinearField()
    bmix = inBoxMinX

    inBoxMinY = DoubleLinearField()
    bmiy = inBoxMinY

    inBoxMinZ = DoubleLinearField()
    bmiz = inBoxMinZ


class InBoxMaxPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InBoxMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inBoxMaxX", "bmax"),
        ("inBoxMaxY", "bmay"),
        ("inBoxMaxZ", "bmaz"),
    )

    inBoxMaxX = DoubleLinearField()
    bmax = inBoxMaxX

    inBoxMaxY = DoubleLinearField()
    bmay = inBoxMaxY

    inBoxMaxZ = DoubleLinearField()
    bmaz = inBoxMaxZ


class InBoxMaxAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InBoxMaxPlugOperator]
):
    __slots__ = ()

    inBoxMaxX = DoubleLinearField()
    bmax = inBoxMaxX

    inBoxMaxY = DoubleLinearField()
    bmay = inBoxMaxY

    inBoxMaxZ = DoubleLinearField()
    bmaz = inBoxMaxZ


class InBoxMaxField(
    DoubleLinear3CompoundBaseField[InBoxMaxAttrOperator, InBoxMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InBoxMaxAttrOperator
    PLUG_CLS = InBoxMaxPlugOperator

    inBoxMaxX = DoubleLinearField()
    bmax = inBoxMaxX

    inBoxMaxY = DoubleLinearField()
    bmay = inBoxMaxY

    inBoxMaxZ = DoubleLinearField()
    bmaz = inBoxMaxZ


class CameraPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cameraX", "cax"),
        ("cameraY", "cay"),
        ("cameraZ", "caz"),
    )

    cameraX = DoubleLinearField()
    cax = cameraX

    cameraY = DoubleLinearField()
    cay = cameraY

    cameraZ = DoubleLinearField()
    caz = cameraZ


class CameraAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CameraPlugOperator]
):
    __slots__ = ()

    cameraX = DoubleLinearField()
    cax = cameraX

    cameraY = DoubleLinearField()
    cay = cameraY

    cameraZ = DoubleLinearField()
    caz = cameraZ


class CameraField(
    DoubleLinear3CompoundBaseField[CameraAttrOperator, CameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraAttrOperator
    PLUG_CLS = CameraPlugOperator

    cameraX = DoubleLinearField()
    cax = cameraX

    cameraY = DoubleLinearField()
    cay = cameraY

    cameraZ = DoubleLinearField()
    caz = cameraZ
