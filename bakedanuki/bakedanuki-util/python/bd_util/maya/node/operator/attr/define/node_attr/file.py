# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.string import DataStringField
from ..custom import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float2Field,
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


class ColorGainPlugOperator(
    Float3CompoundBasePlugOperator["ColorGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorGainR", "cgr"),
        ("colorGainG", "cgg"),
        ("colorGainB", "cgb"),
    )

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
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

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
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

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
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

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
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

    explicitUvTilePosition = Float2Field(default_value=(0.0, 0.0))
    eutp = explicitUvTilePosition


class ExplicitUvTilesAttrOperator(
    CompoundAttrOperator[ExplicitUvTilesPlugOperator]
):
    __slots__ = ()

    explicitUvTileName = DataStringField()
    eutn = explicitUvTileName

    explicitUvTilePosition = Float2Field(default_value=(0.0, 0.0))
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

    baseExplicitUvTilePositionU = FloatField(default_value=0.0)
    bupu = baseExplicitUvTilePositionU

    baseExplicitUvTilePositionV = FloatField(default_value=0.0)
    bupv = baseExplicitUvTilePositionV


class BaseExplicitUvTilePositionAttrOperator(
    Float2CompoundBaseAttrOperator[BaseExplicitUvTilePositionPlugOperator]
):
    __slots__ = ()

    baseExplicitUvTilePositionU = FloatField(default_value=0.0)
    bupu = baseExplicitUvTilePositionU

    baseExplicitUvTilePositionV = FloatField(default_value=0.0)
    bupv = baseExplicitUvTilePositionV


class BaseExplicitUvTilePositionField(
    Float2CompoundBaseField[
        BaseExplicitUvTilePositionAttrOperator,
        BaseExplicitUvTilePositionPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = BaseExplicitUvTilePositionAttrOperator
    PLUG_CLS = BaseExplicitUvTilePositionPlugOperator

    baseExplicitUvTilePositionU = FloatField(default_value=0.0)
    bupu = baseExplicitUvTilePositionU

    baseExplicitUvTilePositionV = FloatField(default_value=0.0)
    bupv = baseExplicitUvTilePositionV


class CoveragePlugOperator(
    Float2CompoundBasePlugOperator["CoverageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coverageU", "cu"),
        ("coverageV", "cv"),
    )

    coverageU = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cu = coverageU

    coverageV = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cv = coverageV


class CoverageAttrOperator(
    Float2CompoundBaseAttrOperator[CoveragePlugOperator]
):
    __slots__ = ()

    coverageU = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cu = coverageU

    coverageV = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cv = coverageV


class CoverageField(
    Float2CompoundBaseField[CoverageAttrOperator, CoveragePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoverageAttrOperator
    PLUG_CLS = CoveragePlugOperator

    coverageU = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cu = coverageU

    coverageV = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cv = coverageV


class TranslateFramePlugOperator(
    Float2CompoundBasePlugOperator["TranslateFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateFrameU", "tfu"),
        ("translateFrameV", "tfv"),
    )

    translateFrameU = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    tfu = translateFrameU

    translateFrameV = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    tfv = translateFrameV


class TranslateFrameAttrOperator(
    Float2CompoundBaseAttrOperator[TranslateFramePlugOperator]
):
    __slots__ = ()

    translateFrameU = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    tfu = translateFrameU

    translateFrameV = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    tfv = translateFrameV


class TranslateFrameField(
    Float2CompoundBaseField[
        TranslateFrameAttrOperator, TranslateFramePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TranslateFrameAttrOperator
    PLUG_CLS = TranslateFramePlugOperator

    translateFrameU = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    tfu = translateFrameU

    translateFrameV = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    tfv = translateFrameV


class RepeatUVPlugOperator(
    Float2CompoundBasePlugOperator["RepeatUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("repeatU", "reu"),
        ("repeatV", "rev"),
    )

    repeatU = FloatField(default_value=1.0, min_value=0.0)
    reu = repeatU

    repeatV = FloatField(default_value=1.0, min_value=0.0)
    rev = repeatV


class RepeatUVAttrOperator(
    Float2CompoundBaseAttrOperator[RepeatUVPlugOperator]
):
    __slots__ = ()

    repeatU = FloatField(default_value=1.0, min_value=0.0)
    reu = repeatU

    repeatV = FloatField(default_value=1.0, min_value=0.0)
    rev = repeatV


class RepeatUVField(
    Float2CompoundBaseField[RepeatUVAttrOperator, RepeatUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepeatUVAttrOperator
    PLUG_CLS = RepeatUVPlugOperator

    repeatU = FloatField(default_value=1.0, min_value=0.0)
    reu = repeatU

    repeatV = FloatField(default_value=1.0, min_value=0.0)
    rev = repeatV


class OffsetPlugOperator(Float2CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetU", "ofu"),
        ("offsetV", "ofv"),
    )

    offsetU = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ofv = offsetV


class OffsetAttrOperator(Float2CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetU = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ofv = offsetV


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetU = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ofu = offsetU

    offsetV = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
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


class VertexCameraTwoPlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraTwoX", "c2x"),
        ("vertexCameraTwoY", "c2y"),
        ("vertexCameraTwoZ", "c2z"),
    )

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ


class VertexCameraTwoAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ


class VertexCameraTwoField(
    Float3CompoundBaseField[
        VertexCameraTwoAttrOperator, VertexCameraTwoPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraTwoAttrOperator
    PLUG_CLS = VertexCameraTwoPlugOperator

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
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

    vertexCameraThreeX = FloatField(default_value=0.0)
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField(default_value=0.0)
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField(default_value=0.0)
    c3z = vertexCameraThreeZ


class VertexCameraThreeAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraThreePlugOperator]
):
    __slots__ = ()

    vertexCameraThreeX = FloatField(default_value=0.0)
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField(default_value=0.0)
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField(default_value=0.0)
    c3z = vertexCameraThreeZ


class VertexCameraThreeField(
    Float3CompoundBaseField[
        VertexCameraThreeAttrOperator, VertexCameraThreePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraThreeAttrOperator
    PLUG_CLS = VertexCameraThreePlugOperator

    vertexCameraThreeX = FloatField(default_value=0.0)
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField(default_value=0.0)
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField(default_value=0.0)
    c3z = vertexCameraThreeZ


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


class PixelCenterPlugOperator(
    Float2CompoundBasePlugOperator["PixelCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pixelCenterX", "pcx"),
        ("pixelCenterY", "pcy"),
    )

    pixelCenterX = FloatField(default_value=0.0)
    pcx = pixelCenterX

    pixelCenterY = FloatField(default_value=0.0)
    pcy = pixelCenterY


class PixelCenterAttrOperator(
    Float2CompoundBaseAttrOperator[PixelCenterPlugOperator]
):
    __slots__ = ()

    pixelCenterX = FloatField(default_value=0.0)
    pcx = pixelCenterX

    pixelCenterY = FloatField(default_value=0.0)
    pcy = pixelCenterY


class PixelCenterField(
    Float2CompoundBaseField[PixelCenterAttrOperator, PixelCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PixelCenterAttrOperator
    PLUG_CLS = PixelCenterPlugOperator

    pixelCenterX = FloatField(default_value=0.0)
    pcx = pixelCenterX

    pixelCenterY = FloatField(default_value=0.0)
    pcy = pixelCenterY


class OutSizePlugOperator(
    Float2CompoundBasePlugOperator["OutSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSizeX", "osx"),
        ("outSizeY", "osy"),
    )

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutSizeAttrOperator(Float2CompoundBaseAttrOperator[OutSizePlugOperator]):
    __slots__ = ()

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutSizeField(
    Float2CompoundBaseField[OutSizeAttrOperator, OutSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSizeAttrOperator
    PLUG_CLS = OutSizePlugOperator

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
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
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
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
