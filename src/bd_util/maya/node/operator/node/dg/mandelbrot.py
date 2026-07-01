# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mandelbrot import (
    ColorField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    ImplodeCenterField,
    OutColorField,
    OutUVField,
    UvCoordField,
    UvFilterSizeField,
    ValueField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
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


class OrbitMappingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    FRONT_TO_BACK = 1
    BACK_TO_FRONT = 2


class OrbitMappingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    FRONT_TO_BACK = 1
    BACK_TO_FRONT = 2

    NAME_MAP = {
        OFF: "Off",
        FRONT_TO_BACK: "Front to Back",
        BACK_TO_FRONT: "Back to Front",
    }


class OrbitMappingEnumField(
    EnumField[OrbitMappingEnumAttrOperator, OrbitMappingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OrbitMappingEnumAttrOperator
    PLUG_CLS = OrbitMappingEnumPlugOperator


class OrbitMapColoringEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    FOG = 1
    TINT = 2


class OrbitMapColoringEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    FOG = 1
    TINT = 2

    NAME_MAP = {
        OFF: "Off",
        FOG: "Fog",
        TINT: "Tint",
    }


class OrbitMapColoringEnumField(
    EnumField[OrbitMapColoringEnumAttrOperator, OrbitMapColoringEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OrbitMapColoringEnumAttrOperator
    PLUG_CLS = OrbitMapColoringEnumPlugOperator


class Mandelbrot(DG):
    __slots__ = ()

    NODE_TYPE = "mandelbrot"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

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

    centerU = FloatField()
    cnu = centerU

    centerV = FloatField()
    cnv = centerV

    fineOffsetU = FloatField()
    fofu = fineOffsetU

    fineOffsetV = FloatField()
    fofv = fineOffsetV

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

    orbitMapping = OrbitMappingEnumField()
    obmp = orbitMapping

    orbitMapColoring = OrbitMapColoringEnumField()
    obmc = orbitMapColoring

    orbitMap = DoubleField()
    omp = orbitMap

    implode = FloatField()
    imp = implode

    implodeCenter = ImplodeCenterField()
    imc = implodeCenter
    implodeCenterU = implodeCenter.implodeCenterU
    imu = implodeCenterU
    implodeCenterV = implodeCenter.implodeCenterV
    imv = implodeCenterV

    outUV = OutUVField()
    ouv = outUV
    outU = outUV.outU
    ou = outU
    outV = outUV.outV
    ov = outV
