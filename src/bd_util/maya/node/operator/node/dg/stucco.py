# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.stucco import (
    Channel1Field,
    Channel2Field,
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
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Stucco(DG):
    __slots__ = ()

    NODE_TYPE = "stucco"

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

    shaker = FloatField()
    sh = shaker

    channel1 = Channel1Field()
    c1 = channel1
    channel1R = channel1.channel1R
    c1r = channel1R
    channel1G = channel1.channel1G
    c1g = channel1G
    channel1B = channel1.channel1B
    c1b = channel1B

    channel2 = Channel2Field()
    c2 = channel2
    channel2R = channel2.channel2R
    c2r = channel2R
    channel2G = channel2.channel2G
    c2g = channel2G
    channel2B = channel2.channel2B
    c2b = channel2B

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    normalMelt = FloatField()
    nm = normalMelt

    normalDepth = FloatField()
    nd = normalDepth

    outNormal = OutNormalField()
    on = outNormal
    outNormalX = outNormal.outNormalX
    onx = outNormalX
    outNormalY = outNormal.outNormalY
    ony = outNormalY
    outNormalZ = outNormal.outNormalZ
    onz = outNormalZ
