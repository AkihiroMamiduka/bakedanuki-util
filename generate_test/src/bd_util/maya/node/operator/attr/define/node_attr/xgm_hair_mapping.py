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

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField()
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField()
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField()
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    fsy = uvFilterSizeY


class CoveragePlugOperator(
    Float2CompoundBasePlugOperator["CoverageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coverageU", "cu"),
        ("coverageV", "cv"),
    )

    coverageU = FloatField()
    cu = coverageU

    coverageV = FloatField()
    cv = coverageV


class CoverageAttrOperator(
    Float2CompoundBaseAttrOperator[CoveragePlugOperator]
):
    __slots__ = ()

    coverageU = FloatField()
    cu = coverageU

    coverageV = FloatField()
    cv = coverageV


class CoverageField(
    Float2CompoundBaseField[CoverageAttrOperator, CoveragePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoverageAttrOperator
    PLUG_CLS = CoveragePlugOperator

    coverageU = FloatField()
    cu = coverageU

    coverageV = FloatField()
    cv = coverageV


class TranslateFramePlugOperator(
    Float2CompoundBasePlugOperator["TranslateFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateFrameU", "tfu"),
        ("translateFrameV", "tfv"),
    )

    translateFrameU = FloatField()
    tfu = translateFrameU

    translateFrameV = FloatField()
    tfv = translateFrameV


class TranslateFrameAttrOperator(
    Float2CompoundBaseAttrOperator[TranslateFramePlugOperator]
):
    __slots__ = ()

    translateFrameU = FloatField()
    tfu = translateFrameU

    translateFrameV = FloatField()
    tfv = translateFrameV


class TranslateFrameField(
    Float2CompoundBaseField[TranslateFrameAttrOperator, TranslateFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateFrameAttrOperator
    PLUG_CLS = TranslateFramePlugOperator

    translateFrameU = FloatField()
    tfu = translateFrameU

    translateFrameV = FloatField()
    tfv = translateFrameV


class RepeatUVPlugOperator(
    Float2CompoundBasePlugOperator["RepeatUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("repeatU", "reu"),
        ("repeatV", "rev"),
    )

    repeatU = FloatField()
    reu = repeatU

    repeatV = FloatField()
    rev = repeatV


class RepeatUVAttrOperator(
    Float2CompoundBaseAttrOperator[RepeatUVPlugOperator]
):
    __slots__ = ()

    repeatU = FloatField()
    reu = repeatU

    repeatV = FloatField()
    rev = repeatV


class RepeatUVField(
    Float2CompoundBaseField[RepeatUVAttrOperator, RepeatUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepeatUVAttrOperator
    PLUG_CLS = RepeatUVPlugOperator

    repeatU = FloatField()
    reu = repeatU

    repeatV = FloatField()
    rev = repeatV


class OffsetPlugOperator(
    Float2CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetU", "ofu"),
        ("offsetV", "ofv"),
    )

    offsetU = FloatField()
    ofu = offsetU

    offsetV = FloatField()
    ofv = offsetV


class OffsetAttrOperator(
    Float2CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetU = FloatField()
    ofu = offsetU

    offsetV = FloatField()
    ofv = offsetV


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetU = FloatField()
    ofu = offsetU

    offsetV = FloatField()
    ofv = offsetV


class OutUVPlugOperator(
    Float2CompoundBasePlugOperator["OutUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outU", "ou"),
        ("outV", "ov"),
    )

    outU = FloatField()
    ou = outU

    outV = FloatField()
    ov = outV


class OutUVAttrOperator(
    Float2CompoundBaseAttrOperator[OutUVPlugOperator]
):
    __slots__ = ()

    outU = FloatField()
    ou = outU

    outV = FloatField()
    ov = outV


class OutUVField(
    Float2CompoundBaseField[OutUVAttrOperator, OutUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUVAttrOperator
    PLUG_CLS = OutUVPlugOperator

    outU = FloatField()
    ou = outU

    outV = FloatField()
    ov = outV


class OutUvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["OutUvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outUvFilterSizeX", "ofsx"),
        ("outUvFilterSizeY", "ofsy"),
    )

    outUvFilterSizeX = FloatField()
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField()
    ofsy = outUvFilterSizeY


class OutUvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[OutUvFilterSizePlugOperator]
):
    __slots__ = ()

    outUvFilterSizeX = FloatField()
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField()
    ofsy = outUvFilterSizeY


class OutUvFilterSizeField(
    Float2CompoundBaseField[OutUvFilterSizeAttrOperator, OutUvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUvFilterSizeAttrOperator
    PLUG_CLS = OutUvFilterSizePlugOperator

    outUvFilterSizeX = FloatField()
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField()
    ofsy = outUvFilterSizeY
