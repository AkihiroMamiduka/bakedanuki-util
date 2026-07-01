# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class RotationPlugOperator(
    Float3CompoundBasePlugOperator["RotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationX", "rotationx"),
        ("rotationY", "rotationy"),
        ("rotationZ", "rotationz"),
    )

    rotationX = FloatField()
    rotationx = rotationX

    rotationY = FloatField()
    rotationy = rotationY

    rotationZ = FloatField()
    rotationz = rotationZ


class RotationAttrOperator(
    Float3CompoundBaseAttrOperator[RotationPlugOperator]
):
    __slots__ = ()

    rotationX = FloatField()
    rotationx = rotationX

    rotationY = FloatField()
    rotationy = rotationY

    rotationZ = FloatField()
    rotationz = rotationZ


class RotationField(
    Float3CompoundBaseField[RotationAttrOperator, RotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationAttrOperator
    PLUG_CLS = RotationPlugOperator

    rotationX = FloatField()
    rotationx = rotationX

    rotationY = FloatField()
    rotationy = rotationY

    rotationZ = FloatField()
    rotationz = rotationZ


class AxisPlugOperator(
    Float3CompoundBasePlugOperator["AxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisX", "axisx"),
        ("axisY", "axisy"),
        ("axisZ", "axisz"),
    )

    axisX = FloatField()
    axisx = axisX

    axisY = FloatField()
    axisy = axisY

    axisZ = FloatField()
    axisz = axisZ


class AxisAttrOperator(
    Float3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = FloatField()
    axisx = axisX

    axisY = FloatField()
    axisy = axisY

    axisZ = FloatField()
    axisz = axisZ


class AxisField(
    Float3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = FloatField()
    axisx = axisX

    axisY = FloatField()
    axisy = axisY

    axisZ = FloatField()
    axisz = axisZ


class TranslatePlugOperator(
    Float3CompoundBasePlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "translatex"),
        ("translateY", "translatey"),
        ("translateZ", "translatez"),
    )

    translateX = FloatField()
    translatex = translateX

    translateY = FloatField()
    translatey = translateY

    translateZ = FloatField()
    translatez = translateZ


class TranslateAttrOperator(
    Float3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = FloatField()
    translatex = translateX

    translateY = FloatField()
    translatey = translateY

    translateZ = FloatField()
    translatez = translateZ


class TranslateField(
    Float3CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateX = FloatField()
    translatex = translateX

    translateY = FloatField()
    translatey = translateY

    translateZ = FloatField()
    translatez = translateZ


class ScalePlugOperator(
    Float3CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "scalex"),
        ("scaleY", "scaley"),
        ("scaleZ", "scalez"),
    )

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class ScaleAttrOperator(
    Float3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class ScaleField(
    Float3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class PivotPlugOperator(
    Float3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "pivotx"),
        ("pivotY", "pivoty"),
        ("pivotZ", "pivotz"),
    )

    pivotX = FloatField()
    pivotx = pivotX

    pivotY = FloatField()
    pivoty = pivotY

    pivotZ = FloatField()
    pivotz = pivotZ


class PivotAttrOperator(
    Float3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = FloatField()
    pivotx = pivotX

    pivotY = FloatField()
    pivoty = pivotY

    pivotZ = FloatField()
    pivotz = pivotZ


class PivotField(
    Float3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = FloatField()
    pivotx = pivotX

    pivotY = FloatField()
    pivoty = pivotY

    pivotZ = FloatField()
    pivotz = pivotZ
