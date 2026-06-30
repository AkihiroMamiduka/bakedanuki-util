# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class LightPositionPlugOperator(
    Float3CompoundBasePlugOperator["LightPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightPositionX", "lpx"),
        ("lightPositionY", "lpy"),
        ("lightPositionZ", "lpz"),
    )

    lightPositionX = FloatField()
    lpx = lightPositionX

    lightPositionY = FloatField()
    lpy = lightPositionY

    lightPositionZ = FloatField()
    lpz = lightPositionZ


class LightPositionAttrOperator(
    Float3CompoundBaseAttrOperator[LightPositionPlugOperator]
):
    __slots__ = ()

    lightPositionX = FloatField()
    lpx = lightPositionX

    lightPositionY = FloatField()
    lpy = lightPositionY

    lightPositionZ = FloatField()
    lpz = lightPositionZ


class LightPositionField(
    Float3CompoundBaseField[LightPositionAttrOperator, LightPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightPositionAttrOperator
    PLUG_CLS = LightPositionPlugOperator

    lightPositionX = FloatField()
    lpx = lightPositionX

    lightPositionY = FloatField()
    lpy = lightPositionY

    lightPositionZ = FloatField()
    lpz = lightPositionZ


class LightDirectionPlugOperator(
    Float3CompoundBasePlugOperator["LightDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionX", "ldx"),
        ("lightDirectionY", "ldy"),
        ("lightDirectionZ", "ldz"),
    )

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ


class LightDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[LightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ


class LightDirectionField(
    Float3CompoundBaseField[LightDirectionAttrOperator, LightDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDirectionAttrOperator
    PLUG_CLS = LightDirectionPlugOperator

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ
