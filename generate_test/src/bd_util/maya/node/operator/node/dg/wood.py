# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.wood import (
    CenterField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    DepthField,
    FillerColorField,
    FilterSizeField,
    GrainColorField,
    NormalCameraField,
    OutColorField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
    RipplesField,
    VeinColorField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Wood(DG):
    __slots__ = ()

    NODE_TYPE = "wood"

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

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

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

    fillerColor = FillerColorField()
    fc = fillerColor
    fillerColorR = fillerColor.fillerColorR
    fcr = fillerColorR
    fillerColorG = fillerColor.fillerColorG
    fcg = fillerColorG
    fillerColorB = fillerColor.fillerColorB
    fcb = fillerColorB

    veinColor = VeinColorField()
    vc = veinColor
    veinColorR = veinColor.veinColorR
    vcr = veinColorR
    veinColorG = veinColor.veinColorG
    vcg = veinColorG
    veinColorB = veinColor.veinColorB
    vcb = veinColorB

    veinSpread = FloatField()
    v = veinSpread

    layerSize = FloatField()
    ls = layerSize

    randomness = FloatField()
    rd = randomness

    age = FloatField()
    a = age

    grainColor = GrainColorField()
    gc = grainColor
    grainColorR = grainColor.grainColorR
    gcr = grainColorR
    grainColorG = grainColor.grainColorG
    gcg = grainColorG
    grainColorB = grainColor.grainColorB
    gcb = grainColorB

    grainContrast = FloatField()
    gx = grainContrast

    grainSpacing = FloatField()
    gs = grainSpacing

    center = CenterField()
    c = center
    centerU = center.centerU
    cu = centerU
    centerV = center.centerV
    cv = centerV

    amplitudeX = FloatField()
    ax = amplitudeX

    amplitudeY = FloatField()
    ay = amplitudeY

    ratio = FloatField()
    ra = ratio

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
