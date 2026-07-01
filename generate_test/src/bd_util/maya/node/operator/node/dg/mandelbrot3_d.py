# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mandelbrot3_d import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


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


class Mandelbrot3D(DG):
    __slots__ = ()

    NODE_TYPE = "mandelbrot3D"

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

    centerX = FloatField()
    cnx = centerX

    centerY = FloatField()
    cny = centerY

    centerZ = FloatField()
    cnz = centerZ

    zoomFactor = FloatField()
    zfc = zoomFactor

    value = ValueField(multi=True)
    vl = value

    color = ColorField(multi=True)
    cl = color

    color_ColorR = FloatField()
    clcr = color_ColorR

    color_ColorG = FloatField()
    clcg = color_ColorG

    color_ColorB = FloatField()
    clcb = color_ColorB

    depth = LongField()
    dm = depth

    amplitude = FloatField()
    a = amplitude

    shift = FloatField()
    shi = shift

    focus = FloatField()
    foc = focus

    escapeRadius = FloatField()
    esr = escapeRadius

    lobes = FloatField()
    lbs = lobes

    wrapAmplitude = BoolField()
    wra = wrapAmplitude

    leafEffect = FloatField()
    lef = leafEffect

    checker = FloatField()
    chk = checker

    lineBlending = BoolField()
    lbl = lineBlending

    lineFocus = FloatField()
    lfc = lineFocus

    points = FloatField()
    pts = points

    stalksU = FloatField()
    stku = stalksU

    stalksV = FloatField()
    stkv = stalksV

    circles = FloatField()
    cir = circles

    circleRadius = FloatField()
    ccr = circleRadius

    circleSizeRatio = FloatField()
    csr = circleSizeRatio

    lineOffsetU = FloatField()
    lou = lineOffsetU

    lineOffsetV = FloatField()
    lov = lineOffsetV

    lineOffsetRatio = FloatField()
    lor = lineOffsetRatio

    juliaU = FloatField()
    jlu = juliaU

    juliaV = FloatField()
    jlv = juliaV

    boxRadius = FloatField()
    bxr = boxRadius

    boxMinRadius = FloatField()
    bxm = boxMinRadius

    boxRatio = FloatField()
    brt = boxRatio

    mandelbrotType = MandelbrotTypeEnumField()
    nty = mandelbrotType

    mandelbrotShadeMethod = MandelbrotShadeMethodEnumField()
    msm = mandelbrotShadeMethod

    mandelbrotInsideMethod = MandelbrotInsideMethodEnumField()
    mim = mandelbrotInsideMethod

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
