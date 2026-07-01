# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.leather import (
    CellColorField,
    ColorGainField,
    ColorOffsetField,
    CreaseColorField,
    DefaultColorField,
    FilterSizeField,
    OutColorField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Leather(DG):
    __slots__ = ()

    NODE_TYPE = "leather"

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

    cellColor = CellColorField()
    ce = cellColor
    cellColorR = cellColor.cellColorR
    cer = cellColorR
    cellColorG = cellColor.cellColorG
    ceg = cellColorG
    cellColorB = cellColor.cellColorB
    ceb = cellColorB

    creaseColor = CreaseColorField()
    cr = creaseColor
    creaseColorR = creaseColor.creaseColorR
    crr = creaseColorR
    creaseColorG = creaseColor.creaseColorG
    crg = creaseColorG
    creaseColorB = creaseColor.creaseColorB
    crb = creaseColorB

    cellSize = FloatField()
    cs = cellSize

    density = FloatField()
    d = density

    spottyness = FloatField()
    s = spottyness

    randomness = FloatField()
    r = randomness

    threshold = FloatField()
    th = threshold

    creases = BoolField()
    c = creases
