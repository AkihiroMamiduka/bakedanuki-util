# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.noise import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    ImplodeCenterField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class NoiseTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    WAVE = 2
    WISPY = 3
    SPACETIME = 4


class NoiseTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    WAVE = 2
    WISPY = 3
    SPACETIME = 4

    NAME_MAP = {
        PERLIN_NOISE: "Perlin Noise",
        BILLOW: "Billow",
        WAVE: "Wave",
        WISPY: "Wispy",
        SPACETIME: "SpaceTime",
    }


class NoiseTypeEnumField(
    EnumField[NoiseTypeEnumAttrOperator, NoiseTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseTypeEnumAttrOperator
    PLUG_CLS = NoiseTypeEnumPlugOperator


class FalloffEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 1
    FAST = 2
    BUBBLE = 3


class FalloffEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 1
    FAST = 2
    BUBBLE = 3

    NAME_MAP = {
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        FAST: "Fast",
        BUBBLE: "Bubble",
    }


class FalloffEnumField(
    EnumField[FalloffEnumAttrOperator, FalloffEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffEnumAttrOperator
    PLUG_CLS = FalloffEnumPlugOperator


class Noise(DG):
    __slots__ = ()

    NODE_TYPE = "noise"

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

    amplitude = FloatField()
    a = amplitude

    ratio = FloatField()
    ra = ratio

    threshold = FloatField()
    th = threshold

    depthMax = ShortField()
    dm = depthMax

    frequency = FloatField()
    fq = frequency

    frequencyRatio = FloatField()
    fr = frequencyRatio

    inflection = BoolField()
    in_ = inflection

    time = FloatField()
    ti = time

    noiseType = NoiseTypeEnumField()
    nty = noiseType

    density = FloatField()
    d = density

    spottyness = FloatField()
    sp = spottyness

    sizeRand = FloatField()
    sr = sizeRand

    randomness = FloatField()
    rn = randomness

    falloff = FalloffEnumField()
    fof = falloff

    numWaves = ShortField()
    nw = numWaves

    implode = FloatField()
    imp = implode

    implodeCenter = ImplodeCenterField()
    imc = implodeCenter
    implodeCenterU = implodeCenter.implodeCenterU
    imu = implodeCenterU
    implodeCenterV = implodeCenter.implodeCenterV
    imv = implodeCenterV
