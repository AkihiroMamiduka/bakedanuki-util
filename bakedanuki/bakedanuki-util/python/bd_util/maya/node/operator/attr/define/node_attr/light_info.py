# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
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

    lightPositionX = FloatField(default_value=0.0, writable=False)
    lpx = lightPositionX

    lightPositionY = FloatField(default_value=0.0, writable=False)
    lpy = lightPositionY

    lightPositionZ = FloatField(default_value=0.0, writable=False)
    lpz = lightPositionZ


class LightPositionAttrOperator(
    Float3CompoundBaseAttrOperator[LightPositionPlugOperator]
):
    __slots__ = ()

    lightPositionX = FloatField(default_value=0.0, writable=False)
    lpx = lightPositionX

    lightPositionY = FloatField(default_value=0.0, writable=False)
    lpy = lightPositionY

    lightPositionZ = FloatField(default_value=0.0, writable=False)
    lpz = lightPositionZ


class LightPositionField(
    Float3CompoundBaseField[
        LightPositionAttrOperator, LightPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LightPositionAttrOperator
    PLUG_CLS = LightPositionPlugOperator

    lightPositionX = FloatField(default_value=0.0, writable=False)
    lpx = lightPositionX

    lightPositionY = FloatField(default_value=0.0, writable=False)
    lpy = lightPositionY

    lightPositionZ = FloatField(default_value=0.0, writable=False)
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

    lightDirectionX = FloatField(default_value=0.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=1.0, writable=False)
    ldz = lightDirectionZ


class LightDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[LightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = FloatField(default_value=0.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=1.0, writable=False)
    ldz = lightDirectionZ


class LightDirectionField(
    Float3CompoundBaseField[
        LightDirectionAttrOperator, LightDirectionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LightDirectionAttrOperator
    PLUG_CLS = LightDirectionPlugOperator

    lightDirectionX = FloatField(default_value=0.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=1.0, writable=False)
    ldz = lightDirectionZ
