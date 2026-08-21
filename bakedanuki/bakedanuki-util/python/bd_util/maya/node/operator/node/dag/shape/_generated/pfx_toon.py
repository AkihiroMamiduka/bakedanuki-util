# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.pfx_toon import (
    BorderColorField,
    CameraPointField,
    CreaseColorField,
    CurvatureWidthField,
    InputSurfaceField,
    IntersectionColorField,
    OutColorField,
    ProfileColorField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.generic import GenericField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.mesh import DataMeshField
from .....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class MeshVertexColorModeEnumPlugOperator(
    EnumPlugOperator["MeshVertexColorModeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    COLOR = 1
    ILLUMINATED = 2


class MeshVertexColorModeEnumAttrOperator(
    EnumAttrOperator[MeshVertexColorModeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    COLOR = 1
    ILLUMINATED = 2

    NAME_MAP = {
        NONE: "None",
        COLOR: "Color",
        ILLUMINATED: "Illuminated",
    }


class MeshVertexColorModeEnumField(
    EnumField[
        MeshVertexColorModeEnumAttrOperator,
        MeshVertexColorModeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = MeshVertexColorModeEnumAttrOperator
    PLUG_CLS = MeshVertexColorModeEnumPlugOperator


class ProfileLinesEnumPlugOperator(
    EnumPlugOperator["ProfileLinesEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    PAINT_EFFECTS = 1
    OFFSET_MESH = 2


class ProfileLinesEnumAttrOperator(
    EnumAttrOperator[ProfileLinesEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    PAINT_EFFECTS = 1
    OFFSET_MESH = 2

    NAME_MAP = {
        OFF: "Off",
        PAINT_EFFECTS: "Paint Effects",
        OFFSET_MESH: "Offset Mesh",
    }


class ProfileLinesEnumField(
    EnumField[ProfileLinesEnumAttrOperator, ProfileLinesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProfileLinesEnumAttrOperator
    PLUG_CLS = ProfileLinesEnumPlugOperator


class BorderLinesEnumPlugOperator(
    EnumPlugOperator["BorderLinesEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    OPEN_EDGE = 1
    SHADER_BOUNDARY = 2
    EDGE_AND_SHADER_BOUNDARY = 3


class BorderLinesEnumAttrOperator(
    EnumAttrOperator[BorderLinesEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    OPEN_EDGE = 1
    SHADER_BOUNDARY = 2
    EDGE_AND_SHADER_BOUNDARY = 3

    NAME_MAP = {
        OFF: "Off",
        OPEN_EDGE: "Open Edge",
        SHADER_BOUNDARY: "Shader Boundary",
        EDGE_AND_SHADER_BOUNDARY: "Edge and Shader Boundary",
    }


class BorderLinesEnumField(
    EnumField[BorderLinesEnumAttrOperator, BorderLinesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BorderLinesEnumAttrOperator
    PLUG_CLS = BorderLinesEnumPlugOperator


class LocalOcclusionEnumPlugOperator(
    EnumPlugOperator["LocalOcclusionEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    LINE_SURFACE = 1
    ALL_TOON_SURFACES = 2


class LocalOcclusionEnumAttrOperator(
    EnumAttrOperator[LocalOcclusionEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    LINE_SURFACE = 1
    ALL_TOON_SURFACES = 2

    NAME_MAP = {
        OFF: "Off",
        LINE_SURFACE: "Line Surface",
        ALL_TOON_SURFACES: "All Toon Surfaces",
    }


class LocalOcclusionEnumField(
    EnumField[LocalOcclusionEnumAttrOperator, LocalOcclusionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalOcclusionEnumAttrOperator
    PLUG_CLS = LocalOcclusionEnumPlugOperator


class GeneratedPfxToon(Shape):
    __slots__ = ()

    NODE_TYPE = "pfxToon"

    displayPercent = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=100.0
    )
    dpc = displayPercent

    drawAsMesh = BoolField(default_value=True)
    dam = drawAsMesh

    seed = LongField(default_value=0, soft_min_value=0, soft_max_value=1000)
    sed = seed

    drawOrder = LongField(
        default_value=0, soft_min_value=-10, soft_max_value=10
    )
    dro = drawOrder

    surfaceOffset = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    sof = surfaceOffset

    brush = TypedField()
    brs = brush

    motionBlurred = BoolField(default_value=True)
    mblr = motionBlurred

    primaryVisibility = BoolField(default_value=True)
    pvs = primaryVisibility

    controlCurve = GenericField(multi=True)
    clc = controlCurve

    outMainMesh = DataMeshField(writable=False)
    omm = outMainMesh

    outFlowerMesh = DataMeshField(writable=False)
    ofm = outFlowerMesh

    outLeafMesh = DataMeshField(writable=False)
    olm = outLeafMesh

    worldMainMesh = DataMeshField(multi=True, writable=False)
    wmm = worldMainMesh

    worldLeafMesh = DataMeshField(multi=True, writable=False)
    wlm = worldLeafMesh

    worldFlowerMesh = DataMeshField(multi=True, writable=False)
    wfm = worldFlowerMesh

    mainVertBufSize = LongField(default_value=0)
    mvbs = mainVertBufSize

    flowerVertBufSize = LongField(default_value=0)
    fvbs = flowerVertBufSize

    leafVertBufSize = LongField(default_value=0)
    lvbs = leafVertBufSize

    meshPolyLimit = LongField(default_value=0)
    mpl = meshPolyLimit

    meshVertexColorMode = MeshVertexColorModeEnumField(default_value=0)
    mvc = meshVertexColorMode

    meshHardEdges = BoolField(default_value=False)
    mhe = meshHardEdges

    meshQuadOutput = BoolField(default_value=False)
    mqo = meshQuadOutput

    cameraPoint = CameraPointField(default_value=(0.0, 0.0, 0.0))
    cpt = cameraPoint
    cameraPointX = cameraPoint.cameraPointX
    cpx = cameraPointX
    cameraPointY = cameraPoint.cameraPointY
    cpy = cameraPointY
    cameraPointZ = cameraPoint.cameraPointZ
    cpz = cameraPointZ

    lineModifier = TypedField(multi=True)
    lmd = lineModifier

    maxDrawSegments = LongField(default_value=1000000)
    mdsg = maxDrawSegments

    curveMode = LongField(default_value=0, min_value=0, max_value=2)
    cmd = curveMode

    leafCurveMode = LongField(default_value=0, min_value=0, max_value=2)
    lcm = leafCurveMode

    flowerCurveMode = LongField(default_value=0, min_value=0, max_value=2)
    fcm = flowerCurveMode

    degree = LongField(default_value=2, min_value=1, max_value=7)
    dgr = degree

    curveAlign = BoolField(default_value=False)
    cva = curveAlign

    outMainCurveCount = LongField(default_value=0, writable=False)
    omcc = outMainCurveCount

    outLeafCurveCount = LongField(default_value=0, writable=False)
    olcc = outLeafCurveCount

    outFlowerCurveCount = LongField(default_value=0, writable=False)
    ofcc = outFlowerCurveCount

    outMainCurves = DataNurbsCurveField(multi=True, writable=False)
    omc = outMainCurves

    outLeafCurves = DataNurbsCurveField(multi=True, writable=False)
    olc = outLeafCurves

    outFlowerCurves = DataNurbsCurveField(multi=True, writable=False)
    ofc = outFlowerCurves

    inputSurface = InputSurfaceField(multi=True)
    ins = inputSurface

    displayInViewport = BoolField(default_value=True)
    div = displayInViewport

    profileLines = ProfileLinesEnumField(default_value=1)
    pln = profileLines

    creaseLines = BoolField(default_value=True)
    cln = creaseLines

    borderLines = BorderLinesEnumField(default_value=1)
    bln = borderLines

    intersectionLines = BoolField(default_value=False)
    iln = intersectionLines

    selfIntersect = BoolField(default_value=False)
    sei = selfIntersect

    lineWidth = DoubleField(
        default_value=0.1, soft_min_value=0.0, soft_max_value=1.0
    )
    lwd = lineWidth

    lineWidthMap = DoubleField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=0.1
    )
    lwm = lineWidthMap

    lineOpacity = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    lop = lineOpacity

    lineOpacityMap = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    lpm = lineOpacityMap

    localOcclusion = LocalOcclusionEnumField(default_value=0)
    lcl = localOcclusion

    occlusionTolerance = DoubleField(
        default_value=0.01, soft_min_value=0.0, soft_max_value=1.0
    )
    otl = occlusionTolerance

    depthBias = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dbs = depthBias

    profileLineWidth = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    plw = profileLineWidth

    creaseLineWidth = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    clw = creaseLineWidth

    borderLineWidth = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    blw = borderLineWidth

    intersectionLineWidth = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    ilw = intersectionLineWidth

    lineOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    lof = lineOffset

    lineOffsetMap = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=0.1
    )
    lom = lineOffsetMap

    lightingBasedWidth = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    lbw = lightingBasedWidth

    occlusionWidthScale = BoolField(default_value=True)
    ows = occlusionWidthScale

    depthOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    dff = depthOffset

    creaseAngleMin = DoubleField(
        default_value=20.0, soft_min_value=0.0, soft_max_value=180.0
    )
    amn = creaseAngleMin

    creaseAngleMax = DoubleField(
        default_value=90.0, soft_min_value=0.0, soft_max_value=180.0
    )
    amx = creaseAngleMax

    hardCreasesOnly = BoolField(default_value=True)
    hco = hardCreasesOnly

    backfacingCreases = BoolField(default_value=True)
    bfc = backfacingCreases

    intersectionAngleMin = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=180.0
    )
    imn = intersectionAngleMin

    intersectionAngleMax = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=180.0
    )
    imx = intersectionAngleMax

    smoothProfile = BoolField(default_value=True)
    spf = smoothProfile

    tighterProfile = BoolField(default_value=False)
    tpf = tighterProfile

    curvatureModulation = BoolField(default_value=False)
    cmo = curvatureModulation

    curvatureWidth = CurvatureWidthField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    cwd = curvatureWidth

    profileWidthModulation = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    pwm = profileWidthModulation

    creaseWidthModulation = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    cwm = creaseWidthModulation

    borderWidthModulation = DoubleField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=2.0
    )
    bwm = borderWidthModulation

    intersectionWidthModulation = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    imd = intersectionWidthModulation

    profileBreakAngle = DoubleField(
        default_value=180.0, min_value=0.0, max_value=180.0
    )
    pba = profileBreakAngle

    creaseBreakAngle = DoubleField(
        default_value=80.0, min_value=0.0, max_value=180.0
    )
    cba = creaseBreakAngle

    borderBreakAngle = DoubleField(
        default_value=80.0, min_value=0.0, max_value=180.0
    )
    bba = borderBreakAngle

    intersectionBreakAngle = DoubleField(
        default_value=180.0, min_value=0.0, max_value=180.0
    )
    iba = intersectionBreakAngle

    removeFlushBorders = BoolField(default_value=False)
    rfb = removeFlushBorders

    flushTolerance = DoubleField(
        default_value=0.01, min_value=0.0, soft_max_value=0.1
    )
    tfl = flushTolerance

    flushAngleMax = DoubleField(
        default_value=4.0, min_value=0.0, soft_max_value=180.0
    )
    fmx = flushAngleMax

    lineEndThinning = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    let = lineEndThinning

    lineExtend = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    lex = lineExtend

    resampleProfile = BoolField(default_value=False)
    rpf = resampleProfile

    resampleCrease = BoolField(default_value=False)
    rcr = resampleCrease

    resampleBorder = BoolField(default_value=False)
    rbd = resampleBorder

    resampleIntersection = BoolField(default_value=False)
    rin = resampleIntersection

    maxSegmentLength = DoubleField(
        default_value=0.5,
        min_value=1e-05,
        soft_min_value=0.01,
        soft_max_value=1.0,
    )
    msl = maxSegmentLength

    minSegmentLength = DoubleField(
        default_value=0.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    mns = minSegmentLength

    screenSpaceResampling = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ssr = screenSpaceResampling

    pfxRandomize = BoolField(default_value=False)
    prz = pfxRandomize

    screenspaceWidth = BoolField(default_value=False)
    spw = screenspaceWidth

    distanceScaling = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dsl = distanceScaling

    minPixelWidth = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    mpw = minPixelWidth

    maxPixelWidth = DoubleField(
        default_value=1000.0, soft_min_value=0.0, soft_max_value=1000.0
    )
    mxp = maxPixelWidth

    profileColor = ProfileColorField(default_value=(0.0, 0.0, 0.0))
    pcl = profileColor
    profileColorR = profileColor.profileColorR
    pcr = profileColorR
    profileColorG = profileColor.profileColorG
    pcg = profileColorG
    profileColorB = profileColor.profileColorB
    pcb = profileColorB

    creaseColor = CreaseColorField(default_value=(0.0, 0.0, 0.0))
    ccl = creaseColor
    creaseColorR = creaseColor.creaseColorR
    ccr = creaseColorR
    creaseColorG = creaseColor.creaseColorG
    ccg = creaseColorG
    creaseColorB = creaseColor.creaseColorB
    ccb = creaseColorB

    borderColor = BorderColorField(default_value=(0.0, 0.0, 0.0))
    bcl = borderColor
    borderColorR = borderColor.borderColorR
    bcr = borderColorR
    borderColorG = borderColor.borderColorG
    bcg = borderColorG
    borderColorB = borderColor.borderColorB
    bcb = borderColorB

    intersectionColor = IntersectionColorField(default_value=(0.0, 0.0, 0.0))
    icl = intersectionColor
    intersectionColorR = intersectionColor.intersectionColorR
    icr = intersectionColorR
    intersectionColorG = intersectionColor.intersectionColorG
    icg = intersectionColorG
    intersectionColorB = intersectionColor.intersectionColorB
    icb = intersectionColorB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocl = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outProfileMesh = DataMeshField(multi=True, writable=False)
    opm = outProfileMesh
