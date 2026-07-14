# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class TranslatePlugOperator(
    Float3CompoundBasePlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "translatex"),
        ("translateY", "translatey"),
        ("translateZ", "translatez"),
    )

    translateX = FloatField(default_value=0.0)
    translatex = translateX

    translateY = FloatField(default_value=0.0)
    translatey = translateY

    translateZ = FloatField(default_value=0.0)
    translatez = translateZ


class TranslateAttrOperator(
    Float3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = FloatField(default_value=0.0)
    translatex = translateX

    translateY = FloatField(default_value=0.0)
    translatey = translateY

    translateZ = FloatField(default_value=0.0)
    translatez = translateZ


class TranslateField(
    Float3CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateX = FloatField(default_value=0.0)
    translatex = translateX

    translateY = FloatField(default_value=0.0)
    translatey = translateY

    translateZ = FloatField(default_value=0.0)
    translatez = translateZ


class RotatePlugOperator(
    Float3CompoundBasePlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rotatex"),
        ("rotateY", "rotatey"),
        ("rotateZ", "rotatez"),
    )

    rotateX = FloatField(default_value=0.0)
    rotatex = rotateX

    rotateY = FloatField(default_value=0.0)
    rotatey = rotateY

    rotateZ = FloatField(default_value=0.0)
    rotatez = rotateZ


class RotateAttrOperator(
    Float3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = FloatField(default_value=0.0)
    rotatex = rotateX

    rotateY = FloatField(default_value=0.0)
    rotatey = rotateY

    rotateZ = FloatField(default_value=0.0)
    rotatez = rotateZ


class RotateField(
    Float3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = FloatField(default_value=0.0)
    rotatex = rotateX

    rotateY = FloatField(default_value=0.0)
    rotatey = rotateY

    rotateZ = FloatField(default_value=0.0)
    rotatez = rotateZ


class ScalePlugOperator(
    Float3CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "scalex"),
        ("scaleY", "scaley"),
        ("scaleZ", "scalez"),
    )

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class ScaleAttrOperator(
    Float3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class ScaleField(
    Float3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ
