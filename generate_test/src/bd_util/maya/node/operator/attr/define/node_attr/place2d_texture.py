# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
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


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvThreeU", "t3u"),
        ("vertexUvThreeV", "t3v"),
    )

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvThreePlugOperator]
):
    __slots__ = ()

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexUvThreeField(
    Float2CompoundBaseField[VertexUvThreeAttrOperator, VertexUvThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvThreeAttrOperator
    PLUG_CLS = VertexUvThreePlugOperator

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexCameraOnePlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraOneX", "c1x"),
        ("vertexCameraOneY", "c1y"),
        ("vertexCameraOneZ", "c1z"),
    )

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraOnePlugOperator]
):
    __slots__ = ()

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraOneField(
    Float3CompoundBaseField[VertexCameraOneAttrOperator, VertexCameraOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraOneAttrOperator
    PLUG_CLS = VertexCameraOnePlugOperator

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


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


class NoiseUVPlugOperator(
    Float2CompoundBasePlugOperator["NoiseUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("noiseU", "nu"),
        ("noiseV", "nv"),
    )

    noiseU = FloatField()
    nu = noiseU

    noiseV = FloatField()
    nv = noiseV


class NoiseUVAttrOperator(
    Float2CompoundBaseAttrOperator[NoiseUVPlugOperator]
):
    __slots__ = ()

    noiseU = FloatField()
    nu = noiseU

    noiseV = FloatField()
    nv = noiseV


class NoiseUVField(
    Float2CompoundBaseField[NoiseUVAttrOperator, NoiseUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseUVAttrOperator
    PLUG_CLS = NoiseUVPlugOperator

    noiseU = FloatField()
    nu = noiseU

    noiseV = FloatField()
    nv = noiseV


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
