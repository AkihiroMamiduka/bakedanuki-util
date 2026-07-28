# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordAttrOperator(Float2CompoundBaseAttrOperator[UvCoordPlugOperator]):
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


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvThreeU", "t3u"),
        ("vertexUvThreeV", "t3v"),
    )

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class VertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvThreePlugOperator]
):
    __slots__ = ()

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class VertexUvThreeField(
    Float2CompoundBaseField[
        VertexUvThreeAttrOperator, VertexUvThreePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexUvThreeAttrOperator
    PLUG_CLS = VertexUvThreePlugOperator

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
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

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraOnePlugOperator]
):
    __slots__ = ()

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraOneField(
    Float3CompoundBaseField[
        VertexCameraOneAttrOperator, VertexCameraOnePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraOneAttrOperator
    PLUG_CLS = VertexCameraOnePlugOperator

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


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

    coverageU = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    cu = coverageU

    coverageV = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    cv = coverageV


class CoverageAttrOperator(
    Float2CompoundBaseAttrOperator[CoveragePlugOperator]
):
    __slots__ = ()

    coverageU = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    cu = coverageU

    coverageV = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    cv = coverageV


class CoverageField(
    Float2CompoundBaseField[CoverageAttrOperator, CoveragePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoverageAttrOperator
    PLUG_CLS = CoveragePlugOperator

    coverageU = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    cu = coverageU

    coverageV = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
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
    Float2CompoundBaseField[
        TranslateFrameAttrOperator, TranslateFramePlugOperator
    ]
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


class OffsetPlugOperator(Float2CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetU", "ofu"),
        ("offsetV", "ofv"),
    )

    offsetU = FloatField(default_value=0.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0)
    ofv = offsetV


class OffsetAttrOperator(Float2CompoundBaseAttrOperator[OffsetPlugOperator]):
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


class NoiseUVPlugOperator(
    Float2CompoundBasePlugOperator["NoiseUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("noiseU", "nu"),
        ("noiseV", "nv"),
    )

    noiseU = FloatField(default_value=0.0, min_value=0.0)
    nu = noiseU

    noiseV = FloatField(default_value=0.0, min_value=0.0)
    nv = noiseV


class NoiseUVAttrOperator(Float2CompoundBaseAttrOperator[NoiseUVPlugOperator]):
    __slots__ = ()

    noiseU = FloatField(default_value=0.0, min_value=0.0)
    nu = noiseU

    noiseV = FloatField(default_value=0.0, min_value=0.0)
    nv = noiseV


class NoiseUVField(
    Float2CompoundBaseField[NoiseUVAttrOperator, NoiseUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseUVAttrOperator
    PLUG_CLS = NoiseUVPlugOperator

    noiseU = FloatField(default_value=0.0, min_value=0.0)
    nu = noiseU

    noiseV = FloatField(default_value=0.0, min_value=0.0)
    nv = noiseV


class OutUVPlugOperator(Float2CompoundBasePlugOperator["OutUVAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outU", "ou"),
        ("outV", "ov"),
    )

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class OutUVAttrOperator(Float2CompoundBaseAttrOperator[OutUVPlugOperator]):
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
    Float2CompoundBaseField[
        OutUvFilterSizeAttrOperator, OutUvFilterSizePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutUvFilterSizeAttrOperator
    PLUG_CLS = OutUvFilterSizePlugOperator

    outUvFilterSizeX = FloatField(default_value=0.0, writable=False)
    ofsx = outUvFilterSizeX

    outUvFilterSizeY = FloatField(default_value=0.0, writable=False)
    ofsy = outUvFilterSizeY
