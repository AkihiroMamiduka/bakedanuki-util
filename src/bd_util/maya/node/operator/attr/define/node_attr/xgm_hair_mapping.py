# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "u"),
        ("vCoord", "v"),
    )

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class CoveragePlugOperator(
    Float2CompoundBasePlugOperator["CoverageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coverageU", "cu"),
        ("coverageV", "cv"),
    )

    coverageU = FloatField(default_value=1.0, min_value=0.0)
    cu = coverageU

    coverageV = FloatField(default_value=1.0, min_value=0.0)
    cv = coverageV


class CoverageAttrOperator(
    Float2CompoundBaseAttrOperator[CoveragePlugOperator]
):
    __slots__ = ()

    coverageU = FloatField(default_value=1.0, min_value=0.0)
    cu = coverageU

    coverageV = FloatField(default_value=1.0, min_value=0.0)
    cv = coverageV


class CoverageField(
    Float2CompoundBaseField[CoverageAttrOperator, CoveragePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoverageAttrOperator
    PLUG_CLS = CoveragePlugOperator

    coverageU = FloatField(default_value=1.0, min_value=0.0)
    cu = coverageU

    coverageV = FloatField(default_value=1.0, min_value=0.0)
    cv = coverageV


class TranslateFramePlugOperator(
    Float2CompoundBasePlugOperator["TranslateFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateFrameU", "tfu"),
        ("translateFrameV", "tfv"),
    )

    translateFrameU = FloatField(default_value=0.0)
    tfu = translateFrameU

    translateFrameV = FloatField(default_value=0.0)
    tfv = translateFrameV


class TranslateFrameAttrOperator(
    Float2CompoundBaseAttrOperator[TranslateFramePlugOperator]
):
    __slots__ = ()

    translateFrameU = FloatField(default_value=0.0)
    tfu = translateFrameU

    translateFrameV = FloatField(default_value=0.0)
    tfv = translateFrameV


class TranslateFrameField(
    Float2CompoundBaseField[TranslateFrameAttrOperator, TranslateFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateFrameAttrOperator
    PLUG_CLS = TranslateFramePlugOperator

    translateFrameU = FloatField(default_value=0.0)
    tfu = translateFrameU

    translateFrameV = FloatField(default_value=0.0)
    tfv = translateFrameV


class RepeatUVPlugOperator(
    Float2CompoundBasePlugOperator["RepeatUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("repeatU", "reu"),
        ("repeatV", "rev"),
    )

    repeatU = FloatField(default_value=1.0)
    reu = repeatU

    repeatV = FloatField(default_value=1.0)
    rev = repeatV


class RepeatUVAttrOperator(
    Float2CompoundBaseAttrOperator[RepeatUVPlugOperator]
):
    __slots__ = ()

    repeatU = FloatField(default_value=1.0)
    reu = repeatU

    repeatV = FloatField(default_value=1.0)
    rev = repeatV


class RepeatUVField(
    Float2CompoundBaseField[RepeatUVAttrOperator, RepeatUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepeatUVAttrOperator
    PLUG_CLS = RepeatUVPlugOperator

    repeatU = FloatField(default_value=1.0)
    reu = repeatU

    repeatV = FloatField(default_value=1.0)
    rev = repeatV


class OffsetPlugOperator(
    Float2CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetU", "ofu"),
        ("offsetV", "ofv"),
    )

    offsetU = FloatField(default_value=0.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0)
    ofv = offsetV


class OffsetAttrOperator(
    Float2CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetU = FloatField(default_value=0.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0)
    ofv = offsetV


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetU = FloatField(default_value=0.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0)
    ofv = offsetV


class OutUVPlugOperator(
    Float2CompoundBasePlugOperator["OutUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outU", "ou"),
        ("outV", "ov"),
    )

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class OutUVAttrOperator(
    Float2CompoundBaseAttrOperator[OutUVPlugOperator]
):
    __slots__ = ()

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class OutUVField(
    Float2CompoundBaseField[OutUVAttrOperator, OutUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUVAttrOperator
    PLUG_CLS = OutUVPlugOperator

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class OutUvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["OutUvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outUvFilterSizeX", "ofsx"),
        ("outUvFilterSizeY", "ofsy"),
    )

    outUvFilterSizeX = FloatField(default_value=0.0, writable=False)
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField(default_value=0.0, writable=False)
    ofsy = outUvFilterSizeY


class OutUvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[OutUvFilterSizePlugOperator]
):
    __slots__ = ()

    outUvFilterSizeX = FloatField(default_value=0.0, writable=False)
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField(default_value=0.0, writable=False)
    ofsy = outUvFilterSizeY


class OutUvFilterSizeField(
    Float2CompoundBaseField[OutUvFilterSizeAttrOperator, OutUvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUvFilterSizeAttrOperator
    PLUG_CLS = OutUvFilterSizePlugOperator

    outUvFilterSizeX = FloatField(default_value=0.0, writable=False)
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField(default_value=0.0, writable=False)
    ofsy = outUvFilterSizeY
