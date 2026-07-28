# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.noise import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    ImplodeCenterField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField


class NoiseTypeEnumPlugOperator(EnumPlugOperator["NoiseTypeEnumAttrOperator"]):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    WAVE = 2
    WISPY = 3
    SPACETIME = 4


class NoiseTypeEnumAttrOperator(EnumAttrOperator[NoiseTypeEnumPlugOperator]):
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


class FalloffEnumPlugOperator(EnumPlugOperator["FalloffEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 1
    FAST = 2
    BUBBLE = 3


class FalloffEnumAttrOperator(EnumAttrOperator[FalloffEnumPlugOperator]):
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


class GeneratedNoise(DG):
    __slots__ = ()

    NODE_TYPE = "noise"

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

    filter = FloatField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    f = filter

    filterOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(
        default_value=(1.0, 1.0, 1.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 2.0, 2.0),
    )
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 2.0, 2.0),
    )
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=2.0
    )
    ag = alphaGain

    alphaOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    ao = alphaOffset

    defaultColor = DefaultColorField(
        default_value=(0.5, 0.5, 0.5),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
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

    amplitude = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    a = amplitude

    ratio = FloatField(
        default_value=0.7070000171661377, min_value=0.0, soft_max_value=1.0
    )
    ra = ratio

    threshold = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    th = threshold

    depthMax = ShortField(
        default_value=3, min_value=1, max_value=80, soft_max_value=8
    )
    dm = depthMax

    frequency = FloatField(
        default_value=8.0, soft_min_value=0.0, soft_max_value=100.0
    )
    fq = frequency

    frequencyRatio = FloatField(
        default_value=2.0, soft_min_value=1.0, soft_max_value=10.0
    )
    fr = frequencyRatio

    inflection = BoolField(default_value=False)
    in_ = inflection

    time = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ti = time

    noiseType = NoiseTypeEnumField(default_value=1)
    nty = noiseType

    density = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    d = density

    spottyness = FloatField(
        default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0
    )
    sp = spottyness

    sizeRand = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    sr = sizeRand

    randomness = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    rn = randomness

    falloff = FalloffEnumField(default_value=2)
    fof = falloff

    numWaves = ShortField(default_value=5, min_value=1, soft_max_value=20)
    nw = numWaves

    implode = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    imp = implode

    implodeCenter = ImplodeCenterField(default_value=(0.5, 0.5))
    imc = implodeCenter
    implodeCenterU = implodeCenter.implodeCenterU
    imu = implodeCenterU
    implodeCenterV = implodeCenter.implodeCenterV
    imv = implodeCenterV
