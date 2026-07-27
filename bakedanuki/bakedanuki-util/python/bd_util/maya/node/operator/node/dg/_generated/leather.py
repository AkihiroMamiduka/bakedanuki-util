# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.leather import (
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
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedLeather(DG):
    __slots__ = ()

    NODE_TYPE = "leather"

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

    cellColor = CellColorField(default_value=(0.37299999594688416, 0.15700000524520874, 0.05900000035762787), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    ce = cellColor
    cellColorR = cellColor.cellColorR
    cer = cellColorR
    cellColorG = cellColor.cellColorG
    ceg = cellColorG
    cellColorB = cellColor.cellColorB
    ceb = cellColorB

    creaseColor = CreaseColorField(default_value=(0.23499999940395355, 0.11800000071525574, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    cr = creaseColor
    creaseColorR = creaseColor.creaseColorR
    crr = creaseColorR
    creaseColorG = creaseColor.creaseColorG
    crg = creaseColorG
    creaseColorB = creaseColor.creaseColorB
    crb = creaseColorB

    cellSize = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    cs = cellSize

    density = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    d = density

    spottyness = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)
    s = spottyness

    randomness = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    r = randomness

    threshold = FloatField(default_value=0.8299999833106995, min_value=0.0, soft_max_value=1.0)
    th = threshold

    creases = BoolField(default_value=True)
    c = creases
