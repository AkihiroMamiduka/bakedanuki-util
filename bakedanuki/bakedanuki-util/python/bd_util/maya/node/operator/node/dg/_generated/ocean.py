# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ocean import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


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


class _GeneratedOcean(DG):
    __slots__ = ()

    NODE_TYPE = "ocean"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    f = filter

    filterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    ag = alphaGain

    alphaOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ao = alphaOffset

    defaultColor = DefaultColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    time = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    ti = time

    scale = FloatField(default_value=10.0, min_value=0.0, soft_max_value=1000.0)
    sc = scale

    windUV = WindUVField(default_value=(1.0, 0.0), min_value=(-1.0, -1.0), max_value=(1.0, 1.0))
    wi = windUV
    windU = windUV.windU
    wiu = windU
    windV = windUV.windV
    wiv = windV

    observerSpeed = FloatField(default_value=0.0, min_value=0.0, soft_max_value=2.0)
    os = observerSpeed

    waveDirSpread = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=1.0)
    wd = waveDirSpread

    numFrequencies = FloatField(default_value=3.0, min_value=0.0, soft_max_value=10.0)
    nf = numFrequencies

    waveLengthMin = FloatField(default_value=0.30000001192092896, min_value=0.0, soft_max_value=10.0)
    wlm = waveLengthMin

    waveLengthMax = FloatField(default_value=4.0, min_value=0.0, soft_max_value=10.0)
    wlx = waveLengthMax

    waveHeight = WaveHeightField(multi=True, default_value=(0.0, 0.0, 0.0))
    wh = waveHeight

    waveTurbulence = WaveTurbulenceField(multi=True, default_value=(0.0, 0.0, 0.0))
    wtb = waveTurbulence

    wavePeaking = WavePeakingField(multi=True, default_value=(0.0, 0.0, 0.0))
    wp = wavePeaking

    foamEmission = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fme = foamEmission

    foamThreshold = FloatField(default_value=0.5099999904632568, soft_min_value=0.0, soft_max_value=1.0)
    fmt = foamThreshold

    colorMode = ColorModeEnumField(default_value=0)
    cmd = colorMode

    outFoam = FloatField(default_value=0.0, writable=False)
    ofm = outFoam
