# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.marble import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    DepthField,
    FillerColorField,
    FilterSizeField,
    NormalCameraField,
    OutColorField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
    RipplesField,
    VeinColorField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedMarble(DG):
    __slots__ = ()

    NODE_TYPE = "marble"

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

    xPixelAngle = FloatField(default_value=0.002053000032901764, readable=False)
    xpa = xPixelAngle

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

    fillerColor = FillerColorField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    fc = fillerColor
    fillerColorR = fillerColor.fillerColorR
    fcr = fillerColorR
    fillerColorG = fillerColor.fillerColorG
    fcg = fillerColorG
    fillerColorB = fillerColor.fillerColorB
    fcb = fillerColorB

    veinColor = VeinColorField(default_value=(0.2980000078678131, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    vc = veinColor
    veinColorR = veinColor.veinColorR
    vcr = veinColorR
    veinColorG = veinColor.veinColorG
    vcg = veinColorG
    veinColorB = veinColor.veinColorB
    vcb = veinColorB

    veinWidth = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)
    vw = veinWidth

    diffusion = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    di = diffusion

    contrast = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    c = contrast

    ripples = RipplesField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0))
    r = ripples
    ripplesX = ripples.ripplesX
    rx = ripplesX
    ripplesY = ripples.ripplesY
    ry = ripplesY
    ripplesZ = ripples.ripplesZ
    rz = ripplesZ

    depth = DepthField(default_value=(0.0, 20.0), min_value=(0.0, 0.0))
    d = depth
    depthMin = depth.depthMin
    dmn = depthMin
    depthMax = depth.depthMax
    dmx = depthMax

    amplitude = FloatField(default_value=1.5, min_value=0.0, soft_max_value=1.5)
    a = amplitude

    ratio = FloatField(default_value=0.7070000171661377, min_value=0.0, max_value=1.0)
    ra = ratio
