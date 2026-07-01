# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class AllCoordinatesPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["AllCoordinatesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xCoordinate", "xc"),
        ("yCoordinate", "yc"),
        ("zCoordinate", "zc"),
    )

    xCoordinate = DoubleLinearField()
    xc = xCoordinate

    yCoordinate = DoubleLinearField()
    yc = yCoordinate

    zCoordinate = DoubleLinearField()
    zc = zCoordinate


class AllCoordinatesAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AllCoordinatesPlugOperator]
):
    __slots__ = ()

    xCoordinate = DoubleLinearField()
    xc = xCoordinate

    yCoordinate = DoubleLinearField()
    yc = yCoordinate

    zCoordinate = DoubleLinearField()
    zc = zCoordinate


class AllCoordinatesField(
    DoubleLinear3CompoundBaseField[AllCoordinatesAttrOperator, AllCoordinatesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AllCoordinatesAttrOperator
    PLUG_CLS = AllCoordinatesPlugOperator

    xCoordinate = DoubleLinearField()
    xc = xCoordinate

    yCoordinate = DoubleLinearField()
    yc = yCoordinate

    zCoordinate = DoubleLinearField()
    zc = zCoordinate


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


class WorldUpVectorPlugOperator(
    Double3CompoundBasePlugOperator["WorldUpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldUpVectorX", "wux"),
        ("worldUpVectorY", "wuy"),
        ("worldUpVectorZ", "wuz"),
    )

    worldUpVectorX = DoubleField()
    wux = worldUpVectorX

    worldUpVectorY = DoubleField()
    wuy = worldUpVectorY

    worldUpVectorZ = DoubleField()
    wuz = worldUpVectorZ


class WorldUpVectorAttrOperator(
    Double3CompoundBaseAttrOperator[WorldUpVectorPlugOperator]
):
    __slots__ = ()

    worldUpVectorX = DoubleField()
    wux = worldUpVectorX

    worldUpVectorY = DoubleField()
    wuy = worldUpVectorY

    worldUpVectorZ = DoubleField()
    wuz = worldUpVectorZ


class WorldUpVectorField(
    Double3CompoundBaseField[WorldUpVectorAttrOperator, WorldUpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldUpVectorAttrOperator
    PLUG_CLS = WorldUpVectorPlugOperator

    worldUpVectorX = DoubleField()
    wux = worldUpVectorX

    worldUpVectorY = DoubleField()
    wuy = worldUpVectorY

    worldUpVectorZ = DoubleField()
    wuz = worldUpVectorZ
