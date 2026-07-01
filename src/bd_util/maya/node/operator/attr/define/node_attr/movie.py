# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound.float2 import Float2Field
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


class ColorGainPlugOperator(
    Float3CompoundBasePlugOperator["ColorGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorGainR", "cgr"),
        ("colorGainG", "cgg"),
        ("colorGainB", "cgb"),
    )

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorOffsetPlugOperator(
    Float3CompoundBasePlugOperator["ColorOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorOffsetR", "cor"),
        ("colorOffsetG", "cog"),
        ("colorOffsetB", "cob"),
    )

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class DefaultColorPlugOperator(
    Float3CompoundBasePlugOperator["DefaultColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultColorR", "dcr"),
        ("defaultColorG", "dcg"),
        ("defaultColorB", "dcb"),
    )

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class ExplicitUvTilesPlugOperator(
    CompoundPlugOperator["ExplicitUvTilesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("explicitUvTileName", "eutn"),
        ("explicitUvTilePosition", "eutp"),
    )

    explicitUvTileName = DataStringField()
    eutn = explicitUvTileName

    explicitUvTilePosition = Float2Field()
    eutp = explicitUvTilePosition


class ExplicitUvTilesAttrOperator(
    CompoundAttrOperator[ExplicitUvTilesPlugOperator]
):
    __slots__ = ()

    explicitUvTileName = DataStringField()
    eutn = explicitUvTileName

    explicitUvTilePosition = Float2Field()
    eutp = explicitUvTilePosition


class ExplicitUvTilesField(
    CompoundField[ExplicitUvTilesAttrOperator, ExplicitUvTilesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExplicitUvTilesAttrOperator
    PLUG_CLS = ExplicitUvTilesPlugOperator


class BaseExplicitUvTilePositionPlugOperator(
    Float2CompoundBasePlugOperator["BaseExplicitUvTilePositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseExplicitUvTilePositionU", "bupu"),
        ("baseExplicitUvTilePositionV", "bupv"),
    )

    baseExplicitUvTilePositionU = FloatField()
    bupu = baseExplicitUvTilePositionU

    baseExplicitUvTilePositionV = FloatField()
    bupv = baseExplicitUvTilePositionV


class BaseExplicitUvTilePositionAttrOperator(
    Float2CompoundBaseAttrOperator[BaseExplicitUvTilePositionPlugOperator]
):
    __slots__ = ()

    baseExplicitUvTilePositionU = FloatField()
    bupu = baseExplicitUvTilePositionU

    baseExplicitUvTilePositionV = FloatField()
    bupv = baseExplicitUvTilePositionV


class BaseExplicitUvTilePositionField(
    Float2CompoundBaseField[BaseExplicitUvTilePositionAttrOperator, BaseExplicitUvTilePositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseExplicitUvTilePositionAttrOperator
    PLUG_CLS = BaseExplicitUvTilePositionPlugOperator

    baseExplicitUvTilePositionU = FloatField()
    bupu = baseExplicitUvTilePositionU

    baseExplicitUvTilePositionV = FloatField()
    bupv = baseExplicitUvTilePositionV


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


class VertexCameraTwoPlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraTwoX", "c2x"),
        ("vertexCameraTwoY", "c2y"),
        ("vertexCameraTwoZ", "c2z"),
    )

    vertexCameraTwoX = FloatField()
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField()
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField()
    c2z = vertexCameraTwoZ


class VertexCameraTwoAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    vertexCameraTwoX = FloatField()
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField()
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField()
    c2z = vertexCameraTwoZ


class VertexCameraTwoField(
    Float3CompoundBaseField[VertexCameraTwoAttrOperator, VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraTwoAttrOperator
    PLUG_CLS = VertexCameraTwoPlugOperator

    vertexCameraTwoX = FloatField()
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField()
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField()
    c2z = vertexCameraTwoZ


class VertexCameraThreePlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraThreeX", "c3x"),
        ("vertexCameraThreeY", "c3y"),
        ("vertexCameraThreeZ", "c3z"),
    )

    vertexCameraThreeX = FloatField()
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField()
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField()
    c3z = vertexCameraThreeZ


class VertexCameraThreeAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraThreePlugOperator]
):
    __slots__ = ()

    vertexCameraThreeX = FloatField()
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField()
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField()
    c3z = vertexCameraThreeZ


class VertexCameraThreeField(
    Float3CompoundBaseField[VertexCameraThreeAttrOperator, VertexCameraThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraThreeAttrOperator
    PLUG_CLS = VertexCameraThreePlugOperator

    vertexCameraThreeX = FloatField()
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField()
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField()
    c3z = vertexCameraThreeZ


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


class PixelCenterPlugOperator(
    Float2CompoundBasePlugOperator["PixelCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pixelCenterX", "pcx"),
        ("pixelCenterY", "pcy"),
    )

    pixelCenterX = FloatField()
    pcx = pixelCenterX

    pixelCenterY = FloatField()
    pcy = pixelCenterY


class PixelCenterAttrOperator(
    Float2CompoundBaseAttrOperator[PixelCenterPlugOperator]
):
    __slots__ = ()

    pixelCenterX = FloatField()
    pcx = pixelCenterX

    pixelCenterY = FloatField()
    pcy = pixelCenterY


class PixelCenterField(
    Float2CompoundBaseField[PixelCenterAttrOperator, PixelCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PixelCenterAttrOperator
    PLUG_CLS = PixelCenterPlugOperator

    pixelCenterX = FloatField()
    pcx = pixelCenterX

    pixelCenterY = FloatField()
    pcy = pixelCenterY


class OutSizePlugOperator(
    Float2CompoundBasePlugOperator["OutSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSizeX", "osx"),
        ("outSizeY", "osy"),
    )

    outSizeX = FloatField()
    osx = outSizeX

    outSizeY = FloatField()
    osy = outSizeY


class OutSizeAttrOperator(
    Float2CompoundBaseAttrOperator[OutSizePlugOperator]
):
    __slots__ = ()

    outSizeX = FloatField()
    osx = outSizeX

    outSizeY = FloatField()
    osy = outSizeY


class OutSizeField(
    Float2CompoundBaseField[OutSizeAttrOperator, OutSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSizeAttrOperator
    PLUG_CLS = OutSizePlugOperator

    outSizeX = FloatField()
    osx = outSizeX

    outSizeY = FloatField()
    osy = outSizeY


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
