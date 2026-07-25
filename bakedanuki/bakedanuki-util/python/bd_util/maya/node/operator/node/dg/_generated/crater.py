# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.crater import (
    Channel1Field,
    Channel2Field,
    Channel3Field,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    FilterSizeField,
    NormalCameraField,
    OutColorField,
    OutNormalField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedCrater(DG):
    __slots__ = ()

    NODE_TYPE = "crater"

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

    filter = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    f = filter

    filterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = filterOffset

    blend = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    b = blend

    local = BoolField(default_value=False)
    lo = local

    wrap = BoolField(default_value=True)
    w = wrap

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

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

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

    shaker = FloatField(default_value=1.5, min_value=0.0, soft_max_value=20.0)
    sh = shaker

    channel1 = Channel1Field(default_value=(1.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    c1 = channel1
    channel1R = channel1.channel1R
    c1r = channel1R
    channel1G = channel1.channel1G
    c1g = channel1G
    channel1B = channel1.channel1B
    c1b = channel1B

    channel2 = Channel2Field(default_value=(0.0, 1.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    c2 = channel2
    channel2R = channel2.channel2R
    c2r = channel2R
    channel2G = channel2.channel2G
    c2g = channel2G
    channel2B = channel2.channel2B
    c2b = channel2B

    channel3 = Channel3Field(default_value=(0.0, 0.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    c3 = channel3
    channel3R = channel3.channel3R
    c3r = channel3R
    channel3G = channel3.channel3G
    c3g = channel3G
    channel3B = channel3.channel3B
    c3b = channel3B

    melt = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    m = melt

    balance = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    ba = balance

    frequency = FloatField(default_value=2.0, min_value=0.0, soft_max_value=10.0)
    fr = frequency

    normDepth = FloatField(default_value=5.0, soft_min_value=0.0, soft_max_value=10.0)
    nd = normDepth

    normMelt = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    nm = normMelt

    normBalance = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    nb = normBalance

    normFrequency = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    nf = normFrequency

    outNormal = OutNormalField(default_value=(0.0, 0.0, 1.0), writable=False)
    o = outNormal
    outNormalX = outNormal.outNormalX
    ox = outNormalX
    outNormalY = outNormal.outNormalY
    oy = outNormalY
    outNormalZ = outNormal.outNormalZ
    oz = outNormalZ
