# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ocean import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
    WaveHeightField,
    WavePeakingField,
    WaveTurbulenceField,
    WindUVField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ColorModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WAVEHEIGHT = 0
    FOAM = 1
    FOAMONWAVES = 2


class ColorModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WAVEHEIGHT = 0
    FOAM = 1
    FOAMONWAVES = 2

    NAME_MAP = {
        WAVEHEIGHT: "WaveHeight",
        FOAM: "Foam",
        FOAMONWAVES: "FoamOnWaves",
    }


class ColorModeEnumField(
    EnumField[ColorModeEnumAttrOperator, ColorModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorModeEnumAttrOperator
    PLUG_CLS = ColorModeEnumPlugOperator


class Ocean(DG):
    __slots__ = ()

    NODE_TYPE = "ocean"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

    invert = BoolField()
    i = invert

    alphaIsLuminance = BoolField()
    ail = alphaIsLuminance

    colorGain = ColorGainField()
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField()
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField()
    ag = alphaGain

    alphaOffset = FloatField()
    ao = alphaOffset

    defaultColor = DefaultColorField()
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField()
    oa = outAlpha

    time = FloatField()
    ti = time

    scale = FloatField()
    sc = scale

    windUV = WindUVField()
    wi = windUV
    windU = windUV.windU
    wiu = windU
    windV = windUV.windV
    wiv = windV

    observerSpeed = FloatField()
    os = observerSpeed

    waveDirSpread = FloatField()
    wd = waveDirSpread

    numFrequencies = FloatField()
    nf = numFrequencies

    waveLengthMin = FloatField()
    wlm = waveLengthMin

    waveLengthMax = FloatField()
    wlx = waveLengthMax

    waveHeight = WaveHeightField(multi=True)
    wh = waveHeight

    waveTurbulence = WaveTurbulenceField(multi=True)
    wtb = waveTurbulence

    wavePeaking = WavePeakingField(multi=True)
    wp = wavePeaking

    foamEmission = FloatField()
    fme = foamEmission

    foamThreshold = FloatField()
    fmt = foamThreshold

    colorMode = ColorModeEnumField()
    cmd = colorMode

    outFoam = FloatField()
    ofm = outFoam
