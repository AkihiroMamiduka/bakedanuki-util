# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mandelbrot3_d import (
    ColorField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    FilterSizeField,
    ImplodeCenterField,
    OutColorField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
    ValueField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class MandelbrotTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    JULIA_SET = 0
    MANDELBROT_SET = 1
    MANDELBOX = 2
    BOX_WITH_JULIA_SET = 3
    BOX_WITH_MANDELBROT_SET = 4


class MandelbrotTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    JULIA_SET = 0
    MANDELBROT_SET = 1
    MANDELBOX = 2
    BOX_WITH_JULIA_SET = 3
    BOX_WITH_MANDELBROT_SET = 4

    NAME_MAP = {
        JULIA_SET: "Julia Set",
        MANDELBROT_SET: "Mandelbrot Set",
        MANDELBOX: "Mandelbox",
        BOX_WITH_JULIA_SET: "Box with Julia Set",
        BOX_WITH_MANDELBROT_SET: "Box with Mandelbrot Set",
    }


class MandelbrotTypeEnumField(
    EnumField[MandelbrotTypeEnumAttrOperator, MandelbrotTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MandelbrotTypeEnumAttrOperator
    PLUG_CLS = MandelbrotTypeEnumPlugOperator


class MandelbrotShadeMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLASSIC = 0
    SMOOTH = 1
    MINIMUM_RADIUS = 2
    ESCAPE_RADIUS = 3
    LINES_ONLY = 4


class MandelbrotShadeMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLASSIC = 0
    SMOOTH = 1
    MINIMUM_RADIUS = 2
    ESCAPE_RADIUS = 3
    LINES_ONLY = 4

    NAME_MAP = {
        CLASSIC: "Classic",
        SMOOTH: "Smooth",
        MINIMUM_RADIUS: "Minimum Radius",
        ESCAPE_RADIUS: "Escape Radius",
        LINES_ONLY: "Lines Only",
    }


class MandelbrotShadeMethodEnumField(
    EnumField[MandelbrotShadeMethodEnumAttrOperator, MandelbrotShadeMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MandelbrotShadeMethodEnumAttrOperator
    PLUG_CLS = MandelbrotShadeMethodEnumPlugOperator


class MandelbrotInsideMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ZERO = 0
    MAX_ITERATION = 1
    SHADED_INSIDE = 2
    SHADED_WITHOUT_LINES = 3
    LINES = 4
    INNER_LINES_ONLY = 5


class MandelbrotInsideMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ZERO = 0
    MAX_ITERATION = 1
    SHADED_INSIDE = 2
    SHADED_WITHOUT_LINES = 3
    LINES = 4
    INNER_LINES_ONLY = 5

    NAME_MAP = {
        ZERO: "Zero",
        MAX_ITERATION: "Max Iteration",
        SHADED_INSIDE: "Shaded Inside",
        SHADED_WITHOUT_LINES: "Shaded Without Lines",
        LINES: "Lines",
        INNER_LINES_ONLY: "Inner Lines Only",
    }


class MandelbrotInsideMethodEnumField(
    EnumField[MandelbrotInsideMethodEnumAttrOperator, MandelbrotInsideMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MandelbrotInsideMethodEnumAttrOperator
    PLUG_CLS = MandelbrotInsideMethodEnumPlugOperator


class _GeneratedMandelbrot3D(DG):
    __slots__ = ()

    NODE_TYPE = "mandelbrot3D"

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

    centerX = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    cnx = centerX

    centerY = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    cny = centerY

    centerZ = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    cnz = centerZ

    zoomFactor = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    zfc = zoomFactor

    value = ValueField(multi=True, default_value=(0.0, 0.0, 0.0))
    vl = value

    color = ColorField(multi=True)
    cl = color

    color_ColorR = FloatField()
    clcr = color_ColorR

    color_ColorG = FloatField()
    clcg = color_ColorG

    color_ColorB = FloatField()
    clcb = color_ColorB

    depth = LongField(default_value=20, min_value=1, soft_max_value=500)
    dm = depth

    amplitude = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    a = amplitude

    shift = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    shi = shift

    focus = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    foc = focus

    escapeRadius = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=10.0)
    esr = escapeRadius

    lobes = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    lbs = lobes

    wrapAmplitude = BoolField(default_value=True)
    wra = wrapAmplitude

    leafEffect = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lef = leafEffect

    checker = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    chk = checker

    lineBlending = BoolField(default_value=False)
    lbl = lineBlending

    lineFocus = FloatField(default_value=0.5, max_value=1.0, soft_min_value=0.0)
    lfc = lineFocus

    points = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    pts = points

    stalksU = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    stku = stalksU

    stalksV = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    stkv = stalksV

    circles = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    cir = circles

    circleRadius = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    ccr = circleRadius

    circleSizeRatio = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    csr = circleSizeRatio

    lineOffsetU = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    lou = lineOffsetU

    lineOffsetV = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    lov = lineOffsetV

    lineOffsetRatio = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    lor = lineOffsetRatio

    juliaU = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    jlu = juliaU

    juliaV = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    jlv = juliaV

    boxRadius = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    bxr = boxRadius

    boxMinRadius = FloatField(default_value=0.5, min_value=0.0, soft_max_value=2.0)
    bxm = boxMinRadius

    boxRatio = FloatField(default_value=-3.0, soft_min_value=-4.0, soft_max_value=4.0)
    brt = boxRatio

    mandelbrotType = MandelbrotTypeEnumField(default_value=1)
    nty = mandelbrotType

    mandelbrotShadeMethod = MandelbrotShadeMethodEnumField(default_value=1)
    msm = mandelbrotShadeMethod

    mandelbrotInsideMethod = MandelbrotInsideMethodEnumField(default_value=2)
    mim = mandelbrotInsideMethod

    implode = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    imp = implode

    implodeCenter = ImplodeCenterField(default_value=(0.0, 0.0, 0.0))
    imc = implodeCenter
    implodeCenterX = implodeCenter.implodeCenterX
    imx = implodeCenterX
    implodeCenterY = implodeCenter.implodeCenterY
    imy = implodeCenterY
    implodeCenterZ = implodeCenter.implodeCenterZ
    imz = implodeCenterZ
