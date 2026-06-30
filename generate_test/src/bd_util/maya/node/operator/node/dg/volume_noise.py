# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.volume_noise import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class NoiseTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    VOLUME_WAVE = 2
    WISPY = 3
    SPACETIME = 4


class NoiseTypeEnumAttrOperator(EnumAttrOperator):
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


class VolumeNoise(DG):
    __slots__ = ()

    NODE_TYPE = "volumeNoise"

    pointObj = PointObjField()
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    pointCamera = PointCameraField()
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    filterSize = FilterSizeField()
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

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

    blend = FloatField()
    b = blend

    local = BoolField()
    lo = local

    wrap = BoolField()
    w = wrap

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

    xPixelAngle = FloatField()
    xpa = xPixelAngle

    refPointObj = RefPointObjField()
    rpo = refPointObj
    refPointObjX = refPointObj.refPointObjX
    rox = refPointObjX
    refPointObjY = refPointObj.refPointObjY
    roy = refPointObjY
    refPointObjZ = refPointObj.refPointObjZ
    roz = refPointObjZ

    refPointCamera = RefPointCameraField()
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    amplitude = FloatField()
    a = amplitude

    ratio = FloatField()
    ra = ratio

    threshold = FloatField()
    th = threshold

    scale = ScaleField()
    sc = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    origin = OriginField()
    orr = origin
    originX = origin.originX
    orx = originX
    originY = origin.originY
    ory = originY
    originZ = origin.originZ
    orz = originZ

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
    implodeCenterX = implodeCenter.implodeCenterX
    imx = implodeCenterX
    implodeCenterY = implodeCenter.implodeCenterY
    imy = implodeCenterY
    implodeCenterZ = implodeCenter.implodeCenterZ
    imz = implodeCenterZ
