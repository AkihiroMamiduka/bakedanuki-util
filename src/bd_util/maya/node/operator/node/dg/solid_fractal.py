# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.solid_fractal import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    DepthField,
    FilterSizeField,
    OutColorField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
    RipplesField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SolidFractal(DG):
    __slots__ = ()

    NODE_TYPE = "solidFractal"

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

    ripples = RipplesField()
    r = ripples
    ripplesX = ripples.ripplesX
    rx = ripplesX
    ripplesY = ripples.ripplesY
    ry = ripplesY
    ripplesZ = ripples.ripplesZ
    rz = ripplesZ

    depth = DepthField()
    d = depth
    depthMin = depth.depthMin
    dmn = depthMin
    depthMax = depth.depthMax
    dmx = depthMax

    frequencyRatio = FloatField()
    fr = frequencyRatio

    bias = FloatField()
    bs = bias

    inflection = BoolField()
    in_ = inflection

    animated = BoolField()
    an = animated

    timeRatio = FloatField()
    tr = timeRatio

    time = FloatField()
    ti = time
