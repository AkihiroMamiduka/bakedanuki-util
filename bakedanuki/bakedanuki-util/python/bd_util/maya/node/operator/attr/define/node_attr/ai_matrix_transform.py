# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
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

    rotationX = FloatField(default_value=0.0)
    rotationx = rotationX

    rotationY = FloatField(default_value=0.0)
    rotationy = rotationY

    rotationZ = FloatField(default_value=0.0)
    rotationz = rotationZ


class RotationAttrOperator(
    Float3CompoundBaseAttrOperator[RotationPlugOperator]
):
    __slots__ = ()

    rotationX = FloatField(default_value=0.0)
    rotationx = rotationX

    rotationY = FloatField(default_value=0.0)
    rotationy = rotationY

    rotationZ = FloatField(default_value=0.0)
    rotationz = rotationZ


class RotationField(
    Float3CompoundBaseField[RotationAttrOperator, RotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationAttrOperator
    PLUG_CLS = RotationPlugOperator

    rotationX = FloatField(default_value=0.0)
    rotationx = rotationX

    rotationY = FloatField(default_value=0.0)
    rotationy = rotationY

    rotationZ = FloatField(default_value=0.0)
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

    axisX = FloatField(default_value=1.0)
    axisx = axisX

    axisY = FloatField(default_value=0.0)
    axisy = axisY

    axisZ = FloatField(default_value=0.0)
    axisz = axisZ


class AxisAttrOperator(
    Float3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = FloatField(default_value=1.0)
    axisx = axisX

    axisY = FloatField(default_value=0.0)
    axisy = axisY

    axisZ = FloatField(default_value=0.0)
    axisz = axisZ


class AxisField(
    Float3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = FloatField(default_value=1.0)
    axisx = axisX

    axisY = FloatField(default_value=0.0)
    axisy = axisY

    axisZ = FloatField(default_value=0.0)
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


class PivotPlugOperator(
    Float3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "pivotx"),
        ("pivotY", "pivoty"),
        ("pivotZ", "pivotz"),
    )

    pivotX = FloatField(default_value=0.0)
    pivotx = pivotX

    pivotY = FloatField(default_value=0.0)
    pivoty = pivotY

    pivotZ = FloatField(default_value=0.0)
    pivotz = pivotZ


class PivotAttrOperator(
    Float3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = FloatField(default_value=0.0)
    pivotx = pivotX

    pivotY = FloatField(default_value=0.0)
    pivoty = pivotY

    pivotZ = FloatField(default_value=0.0)
    pivotz = pivotZ


class PivotField(
    Float3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = FloatField(default_value=0.0)
    pivotx = pivotX

    pivotY = FloatField(default_value=0.0)
    pivoty = pivotY

    pivotZ = FloatField(default_value=0.0)
    pivotz = pivotZ
