# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.volume_noise import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    FilterSizeField,
    ImplodeCenterField,
    OriginField,
    OutColorField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
    ScaleField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField


class NoiseTypeEnumPlugOperator(EnumPlugOperator["NoiseTypeEnumAttrOperator"]):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    VOLUME_WAVE = 2
    WISPY = 3
    SPACETIME = 4


class NoiseTypeEnumAttrOperator(EnumAttrOperator[NoiseTypeEnumPlugOperator]):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    VOLUME_WAVE = 2
    WISPY = 3
    SPACETIME = 4

    NAME_MAP = {
        PERLIN_NOISE: "Perlin Noise",
        BILLOW: "Billow",
        VOLUME_WAVE: "Volume Wave",
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


class GeneratedVolumeNoise(DG):
    __slots__ = ()

    NODE_TYPE = "volumeNoise"

    pointObj = PointObjField(default_value=(0.0, 0.0, 0.0))
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    filterSize = FilterSizeField(default_value=(0.0, 0.0, 0.0))
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    placementMatrix = FltMatrixField()
    pm = placementMatrix

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    filter = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    f = filter

    filterOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    fo = filterOffset

    blend = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    b = blend

    local = BoolField(default_value=False)
    lo = local

    wrap = BoolField(default_value=True)
    w = wrap

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

    xPixelAngle = FloatField(
        default_value=0.002053000032901764, readable=False
    )
    xpa = xPixelAngle

    refPointObj = RefPointObjField(default_value=(0.0, 0.0, 0.0))
    rpo = refPointObj
    refPointObjX = refPointObj.refPointObjX
    rox = refPointObjX
    refPointObjY = refPointObj.refPointObjY
    roy = refPointObjY
    refPointObjZ = refPointObj.refPointObjZ
    roz = refPointObjZ

    refPointCamera = RefPointCameraField(default_value=(0.0, 0.0, 0.0))
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    amplitude = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    a = amplitude

    ratio = FloatField(
        default_value=0.7070000171661377, min_value=0.0, max_value=1.0
    )
    ra = ratio

    threshold = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    th = threshold

    scale = ScaleField(
        default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0)
    )
    sc = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    origin = OriginField(default_value=(0.0, 0.0, 0.0))
    orr = origin
    originX = origin.originX
    orx = originX
    originY = origin.originY
    ory = originY
    originZ = origin.originZ
    orz = originZ

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
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
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

    implodeCenter = ImplodeCenterField(default_value=(0.0, 0.0, 0.0))
    imc = implodeCenter
    implodeCenterX = implodeCenter.implodeCenterX
    imx = implodeCenterX
    implodeCenterY = implodeCenter.implodeCenterY
    imy = implodeCenterY
    implodeCenterZ = implodeCenter.implodeCenterZ
    imz = implodeCenterZ
