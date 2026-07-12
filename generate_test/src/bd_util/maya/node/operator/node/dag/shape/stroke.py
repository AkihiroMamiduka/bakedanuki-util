# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.stroke import (
    BoundingBoxField,
    CameraPointField,
    CenterField,
    DrawOverrideField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    NormalField,
    ObjectColorRGBField,
    OutNormalField,
    OutPointField,
    OutlinerColorField,
    PathCurveField,
    PressureScaleField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    WireColorRGBField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2

    NAME_MAP = {
        FLAT: "Flat",
        USE_TEMPLATE: "Use Template",
        GROUP_BY_NODE: "Group By Node",
    }


class ViewModeEnumField(
    EnumField[ViewModeEnumAttrOperator, ViewModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewModeEnumAttrOperator
    PLUG_CLS = ViewModeEnumPlugOperator


class UiTreatmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000

    NAME_MAP = {
        STANDARD: "Standard",
        SHADER: "Shader",
        CUSTOM: "Custom",
    }


class UiTreatmentEnumField(
    EnumField[UiTreatmentEnumAttrOperator, UiTreatmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UiTreatmentEnumAttrOperator
    PLUG_CLS = UiTreatmentEnumPlugOperator


class UseObjectColorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2

    NAME_MAP = {
        DEFAULT: "Default",
        INDEXED: "Indexed",
        RGB: "RGB",
    }


class UseObjectColorEnumField(
    EnumField[UseObjectColorEnumAttrOperator, UseObjectColorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseObjectColorEnumAttrOperator
    PLUG_CLS = UseObjectColorEnumPlugOperator


class GhostingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5

    NAME_MAP = {
        PRE_AND_POST_FRAMES: "Pre And Post Frames",
        PRE_FRAMES: "Pre Frames",
        POST_FRAMES: "Post Frames",
        CUSTOM_FRAMES: "Custom Frames",
        PRE_AND_POST_KEYFRAMES: "Pre And Post Keyframes",
        ALL_KEYFRAMES: "All Keyframes",
    }


class GhostingModeEnumField(
    EnumField[GhostingModeEnumAttrOperator, GhostingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostingModeEnumAttrOperator
    PLUG_CLS = GhostingModeEnumPlugOperator


class MeshVertexColorModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    COLOR = 1
    ILLUMINATED = 2


class MeshVertexColorModeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[MeshVertexColorModeEnumAttrOperator, MeshVertexColorModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MeshVertexColorModeEnumAttrOperator
    PLUG_CLS = MeshVertexColorModeEnumPlugOperator


class PressureMap1EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23


class PressureMap1EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23

    NAME_MAP = {
        OFF: "Off",
        SCALE: "Scale",
        WIDTH: "Width",
        SOFTNESS: "Softness",
        COLOR: "Color",
        TRANSPARENCY: "Transparency",
        TUBE_WIDTH: "Tube Width",
        TUBE_LENGTH: "Tube Length",
        INCANDESCENCE: "Incandescence",
        GLOW_SPREAD: "Glow Spread",
        TUBES_PER_STEP: "Tubes Per Step",
        ELEVATION: "Elevation",
        AZIMUTH: "Azimuth",
        PATH_FOLLOW: "Path Follow",
        PATH_ATTRACT: "Path Attract",
        RANDOM: "Random",
        WIGGLE: "Wiggle",
        CURL: "Curl",
        NOISE: "Noise",
        TURBULENCE: "Turbulence",
        NUM_TWIGS: "Num Twigs",
        NUM_LEAVES: "Num Leaves",
        NUM_PETALS: "Num Petals",
        SURFACEOFFSET: "surfaceOffset",
    }


class PressureMap1EnumField(
    EnumField[PressureMap1EnumAttrOperator, PressureMap1EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMap1EnumAttrOperator
    PLUG_CLS = PressureMap1EnumPlugOperator


class PressureMap2EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23


class PressureMap2EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23

    NAME_MAP = {
        OFF: "Off",
        SCALE: "Scale",
        WIDTH: "Width",
        SOFTNESS: "Softness",
        COLOR: "Color",
        TRANSPARENCY: "Transparency",
        TUBE_WIDTH: "Tube Width",
        TUBE_LENGTH: "Tube Length",
        INCANDESCENCE: "Incandescence",
        GLOW_SPREAD: "Glow Spread",
        TUBES_PER_STEP: "Tubes Per Step",
        ELEVATION: "Elevation",
        AZIMUTH: "Azimuth",
        PATH_FOLLOW: "Path Follow",
        PATH_ATTRACT: "Path Attract",
        RANDOM: "Random",
        WIGGLE: "Wiggle",
        CURL: "Curl",
        NOISE: "Noise",
        TURBULENCE: "Turbulence",
        NUM_TWIGS: "Num Twigs",
        NUM_LEAVES: "Num Leaves",
        NUM_PETALS: "Num Petals",
        SURFACEOFFSET: "surfaceOffset",
    }


class PressureMap2EnumField(
    EnumField[PressureMap2EnumAttrOperator, PressureMap2EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMap2EnumAttrOperator
    PLUG_CLS = PressureMap2EnumPlugOperator


class PressureMap3EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23


class PressureMap3EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23

    NAME_MAP = {
        OFF: "Off",
        SCALE: "Scale",
        WIDTH: "Width",
        SOFTNESS: "Softness",
        COLOR: "Color",
        TRANSPARENCY: "Transparency",
        TUBE_WIDTH: "Tube Width",
        TUBE_LENGTH: "Tube Length",
        INCANDESCENCE: "Incandescence",
        GLOW_SPREAD: "Glow Spread",
        TUBES_PER_STEP: "Tubes Per Step",
        ELEVATION: "Elevation",
        AZIMUTH: "Azimuth",
        PATH_FOLLOW: "Path Follow",
        PATH_ATTRACT: "Path Attract",
        RANDOM: "Random",
        WIGGLE: "Wiggle",
        CURL: "Curl",
        NOISE: "Noise",
        TURBULENCE: "Turbulence",
        NUM_TWIGS: "Num Twigs",
        NUM_LEAVES: "Num Leaves",
        NUM_PETALS: "Num Petals",
        SURFACEOFFSET: "surfaceOffset",
    }


class PressureMap3EnumField(
    EnumField[PressureMap3EnumAttrOperator, PressureMap3EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMap3EnumAttrOperator
    PLUG_CLS = PressureMap3EnumPlugOperator


class Stroke(Shape):
    __slots__ = ()

    NODE_TYPE = "stroke"

    hyperLayout = MessageField()
    hl = hyperLayout

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    blackBox = BoolField(default_value=False)
    bbx = blackBox

    borderConnections = MessageField(multi=True)
    boc = borderConnections

    isHierarchicalConnection = BoolField(multi=True, default_value=False)
    ish = isHierarchicalConnection

    publishedNodeInfo = PublishedNodeInfoField(multi=True)
    pni = publishedNodeInfo

    rmbCommand = DataStringField()
    rmc = rmbCommand

    templateName = DataStringField()
    tna = templateName

    templatePath = DataStringField()
    tpt = templatePath

    viewName = DataStringField()
    vwn = viewName

    iconName = DataStringField()
    icn = iconName

    viewMode = ViewModeEnumField(default_value=2)
    vwm = viewMode

    templateVersion = LongField(default_value=0)
    tpv = templateVersion

    uiTreatment = UiTreatmentEnumField(default_value=0)
    uit = uiTreatment

    customTreatment = DataStringField()
    ctrt = customTreatment

    creator = DataStringField()
    ctor = creator

    creationDate = DataStringField()
    cdat = creationDate

    containerType = DataStringField()
    ctyp = containerType

    boundingBox = BoundingBoxField(writable=False)
    bb = boundingBox
    boundingBoxMin = boundingBox.boundingBoxMin
    bbmn = boundingBoxMin
    boundingBoxMax = boundingBox.boundingBoxMax
    bbmx = boundingBoxMax
    boundingBoxSize = boundingBox.boundingBoxSize
    bbsi = boundingBoxSize

    center = CenterField(default_value=(0.0, 0.0, 0.0), writable=False)
    c = center
    boundingBoxCenterX = center.boundingBoxCenterX
    bcx = boundingBoxCenterX
    boundingBoxCenterY = center.boundingBoxCenterY
    bcy = boundingBoxCenterY
    boundingBoxCenterZ = center.boundingBoxCenterZ
    bcz = boundingBoxCenterZ

    matrix = DataMatrixField(writable=False)
    m = matrix

    inverseMatrix = DataMatrixField(writable=False)
    im = inverseMatrix

    worldMatrix = DataMatrixField(multi=True, writable=False)
    wm = worldMatrix

    worldInverseMatrix = DataMatrixField(multi=True, writable=False)
    wim = worldInverseMatrix

    parentMatrix = DataMatrixField(multi=True, writable=False)
    pm = parentMatrix

    parentInverseMatrix = DataMatrixField(multi=True, writable=False)
    pim = parentInverseMatrix

    visibility = BoolField(default_value=True)
    v = visibility

    intermediateObject = BoolField(default_value=False)
    io = intermediateObject

    template = BoolField(default_value=False)
    tmp = template

    instObjGroups = InstObjGroupsField(multi=True)
    iog = instObjGroups

    objectColorRGB = ObjectColorRGBField(default_value=(0.0, 0.0, 0.0))
    obcc = objectColorRGB
    objectColorR = objectColorRGB.objectColorR
    obcr = objectColorR
    objectColorG = objectColorRGB.objectColorG
    obcg = objectColorG
    objectColorB = objectColorRGB.objectColorB
    obcb = objectColorB

    wireColorRGB = WireColorRGBField(default_value=(0.0, 0.0, 0.0))
    wfcc = wireColorRGB
    wireColorR = wireColorRGB.wireColorR
    wfcr = wireColorR
    wireColorG = wireColorRGB.wireColorG
    wfcg = wireColorG
    wireColorB = wireColorRGB.wireColorB
    wfcb = wireColorB

    useObjectColor = UseObjectColorEnumField(default_value=0)
    uoc = useObjectColor

    objectColor = ShortField(default_value=0, min_value=0, max_value=7)
    oc = objectColor

    drawOverride = DrawOverrideField()
    do = drawOverride
    overrideDisplayType = drawOverride.overrideDisplayType
    ovdt = overrideDisplayType
    overrideLevelOfDetail = drawOverride.overrideLevelOfDetail
    ovlod = overrideLevelOfDetail
    overrideShading = drawOverride.overrideShading
    ovs = overrideShading
    overrideTexturing = drawOverride.overrideTexturing
    ovt = overrideTexturing
    overridePlayback = drawOverride.overridePlayback
    ovp = overridePlayback
    overrideEnabled = drawOverride.overrideEnabled
    ove = overrideEnabled
    overrideVisibility = drawOverride.overrideVisibility
    ovv = overrideVisibility
    hideOnPlayback = drawOverride.hideOnPlayback
    hpb = hideOnPlayback
    overrideRGBColors = drawOverride.overrideRGBColors
    ovrgbf = overrideRGBColors
    overrideColor = drawOverride.overrideColor
    ovc = overrideColor
    overrideColorRGB = drawOverride.overrideColorRGB
    ovrgb = overrideColorRGB
    overrideColorA = drawOverride.overrideColorA
    ovca = overrideColorA

    lodVisibility = BoolField(default_value=True)
    lodv = lodVisibility

    selectionChildHighlighting = BoolField(default_value=True)
    sech = selectionChildHighlighting

    renderInfo = RenderInfoField(default_value=(0.0, 1.0, 0.0))
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    layerRenderable = renderInfo.layerRenderable
    rndr = layerRenderable
    layerOverrideColor = renderInfo.layerOverrideColor
    lovc = layerOverrideColor

    renderLayerInfo = RenderLayerInfoField(multi=True, default_value=(0.0, 1.0, 0.0))
    rlio = renderLayerInfo

    ghosting = BoolField(default_value=False)
    gh = ghosting

    ghostingMode = GhostingModeEnumField(default_value=0)
    gm = ghostingMode

    ghostCustomSteps = GhostCustomStepsField(default_value=(3.0, 3.0, 1.0))
    gcs = ghostCustomSteps
    ghostPreFrames = ghostCustomSteps.ghostPreFrames
    gprf = ghostPreFrames
    ghostPostFrames = ghostCustomSteps.ghostPostFrames
    gpof = ghostPostFrames
    ghostsStep = ghostCustomSteps.ghostsStep
    gstp = ghostsStep

    ghostFrames = TypedField()
    gf = ghostFrames

    ghostOpacityRange = GhostOpacityRangeField(default_value=(0.15000000596046448, 0.5), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(default_value=(0.44699999690055847, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(default_value=(0.878000020980835, 0.6779999732971191, 0.6629999876022339), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gac = ghostColorPost
    ghostColorPostR = ghostColorPost.ghostColorPostR
    gar = ghostColorPostR
    ghostColorPostG = ghostColorPost.ghostColorPostG
    gag = ghostColorPostG
    ghostColorPostB = ghostColorPost.ghostColorPostB
    gab = ghostColorPostB

    ghostDriver = MessageField()
    gdr = ghostDriver

    ghostUseDriver = BoolField(default_value=False)
    gud = ghostUseDriver

    hiddenInOutliner = BoolField(default_value=False)
    hio = hiddenInOutliner

    useOutlinerColor = BoolField(default_value=False)
    uocol = useOutlinerColor

    outlinerColor = OutlinerColorField(default_value=(0.0, 0.0, 0.0))
    oclr = outlinerColor
    outlinerColorR = outlinerColor.outlinerColorR
    oclrr = outlinerColorR
    outlinerColorG = outlinerColor.outlinerColorG
    oclrg = outlinerColorG
    outlinerColorB = outlinerColor.outlinerColorB
    oclrb = outlinerColorB

    displayPercent = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    dpc = displayPercent

    drawAsMesh = BoolField(default_value=True)
    dam = drawAsMesh

    seed = LongField(default_value=0, soft_min_value=0, soft_max_value=1000)
    sed = seed

    drawOrder = LongField(default_value=0, soft_min_value=-10, soft_max_value=10)
    dro = drawOrder

    surfaceOffset = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
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

    sampleDensity = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    sdn = sampleDensity

    smoothing = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    smo = smoothing

    perspective = BoolField(default_value=True)
    per = perspective

    useNormal = BoolField(default_value=False)
    usn = useNormal

    minimalTwist = BoolField(default_value=False)
    mnt = minimalTwist

    normal = NormalField(default_value=(0.0, 0.0, 1.0), soft_min_value=(-1.0, -1.0, -1.0), soft_max_value=(1.0, 1.0, 1.0))
    nml = normal
    normalX = normal.normalX
    nmx = normalX
    normalY = normal.normalY
    nmy = normalY
    normalZ = normal.normalZ
    nmz = normalZ

    minClip = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnc = minClip

    maxClip = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mxc = maxClip

    pathCurve = PathCurveField(multi=True)
    pcv = pathCurve

    collisionObject = GenericField(multi=True)
    clob = collisionObject

    outPoint = OutPointField(multi=True, default_value=(0.0, 0.0, 0.0))
    opt = outPoint

    outNormal = OutNormalField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    onm = outNormal

    pressureMap1 = PressureMap1EnumField(default_value=0)
    spm1 = pressureMap1

    pressureMin1 = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ps1 = pressureMin1

    pressureMax1 = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    px1 = pressureMax1

    pressureMap2 = PressureMap2EnumField(default_value=0)
    spm2 = pressureMap2

    pressureMin2 = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ps2 = pressureMin2

    pressureMax2 = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    px2 = pressureMax2

    pressureMap3 = PressureMap3EnumField(default_value=0)
    spm3 = pressureMap3

    pressureMin3 = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ps3 = pressureMin3

    pressureMax3 = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    px3 = pressureMax3

    pressureScale = PressureScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    psc = pressureScale

    pressure = DoubleField(multi=True, default_value=0.0)
    psr = pressure

    uvSetName = MessageField(multi=True)
    uvsetn = uvSetName
