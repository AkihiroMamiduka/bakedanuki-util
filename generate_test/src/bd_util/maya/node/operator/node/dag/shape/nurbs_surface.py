# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.nurbs_surface import (
    BoundingBoxField,
    BoundingBoxScaleField,
    CenterField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    DegreeUVField,
    DrawOverrideField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    MinMaxRangeUField,
    MinMaxRangeVField,
    ObjectColorRGBField,
    OutlinerColorField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    SpansUVField,
    UvPivotField,
    UvSetField,
    WireColorRGBField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.byte import ByteField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField
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


class ModeUEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3
    BEST_GUESS_BASED_ON_SCREEN_SIZE = 4


class ModeUEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3
    BEST_GUESS_BASED_ON_SCREEN_SIZE = 4

    NAME_MAP = {
        PER_SURF_HASH_OF_ISOPARMS_IN_3D: "Per Surf # of Isoparms in 3D",
        PER_SURF_HASH_OF_ISOPARMS: "Per Surf # of Isoparms",
        PER_SPAN_HASH_OF_ISOPARMS: "Per Span # of Isoparms",
        BEST_GUESS_BASED_ON_SCREEN_SIZE: "Best Guess Based on Screen Size",
    }


class ModeUEnumField(
    EnumField[ModeUEnumAttrOperator, ModeUEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeUEnumAttrOperator
    PLUG_CLS = ModeUEnumPlugOperator


class ModeVEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3
    BEST_GUESS_BASED_ON_SCREEN_SIZE = 4


class ModeVEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3
    BEST_GUESS_BASED_ON_SCREEN_SIZE = 4

    NAME_MAP = {
        PER_SURF_HASH_OF_ISOPARMS_IN_3D: "Per Surf # of Isoparms in 3D",
        PER_SURF_HASH_OF_ISOPARMS: "Per Surf # of Isoparms",
        PER_SPAN_HASH_OF_ISOPARMS: "Per Span # of Isoparms",
        BEST_GUESS_BASED_ON_SCREEN_SIZE: "Best Guess Based on Screen Size",
    }


class ModeVEnumField(
    EnumField[ModeVEnumAttrOperator, ModeVEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeVEnumAttrOperator
    PLUG_CLS = ModeVEnumPlugOperator


class FormUEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2


class FormUEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2

    NAME_MAP = {
        OPEN: "Open",
        CLOSED: "Closed",
        PERIODIC: "Periodic",
    }


class FormUEnumField(
    EnumField[FormUEnumAttrOperator, FormUEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormUEnumAttrOperator
    PLUG_CLS = FormUEnumPlugOperator


class FormVEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2


class FormVEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2

    NAME_MAP = {
        OPEN: "Open",
        CLOSED: "Closed",
        PERIODIC: "Periodic",
    }


class FormVEnumField(
    EnumField[FormVEnumAttrOperator, FormVEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormVEnumAttrOperator
    PLUG_CLS = FormVEnumPlugOperator


class CurvatureToleranceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3
    NO_CURVATURE_CHECK = 4


class CurvatureToleranceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3
    NO_CURVATURE_CHECK = 4

    NAME_MAP = {
        HIGHEST_QUALITY: "Highest Quality",
        HIGH_QUALITY: "High Quality",
        MEDIUM_QUALITY: "Medium Quality",
        LOW_QUALITY: "Low Quality",
        NO_CURVATURE_CHECK: "No Curvature Check",
    }


class CurvatureToleranceEnumField(
    EnumField[CurvatureToleranceEnumAttrOperator, CurvatureToleranceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurvatureToleranceEnumAttrOperator
    PLUG_CLS = CurvatureToleranceEnumPlugOperator


class BasicTessellationTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OBJECT = 0
    SCREEN = 1


class BasicTessellationTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OBJECT = 0
    SCREEN = 1

    NAME_MAP = {
        OBJECT: "Object",
        SCREEN: "Screen",
    }


class BasicTessellationTypeEnumField(
    EnumField[BasicTessellationTypeEnumAttrOperator, BasicTessellationTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BasicTessellationTypeEnumAttrOperator
    PLUG_CLS = BasicTessellationTypeEnumPlugOperator


class AiSubdivTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    CATCLARK = 1
    LINEAR = 2


class AiSubdivTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    CATCLARK = 1
    LINEAR = 2

    NAME_MAP = {
        NONE: "none",
        CATCLARK: "catclark",
        LINEAR: "linear",
    }


class AiSubdivTypeEnumField(
    EnumField[AiSubdivTypeEnumAttrOperator, AiSubdivTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivTypeEnumAttrOperator
    PLUG_CLS = AiSubdivTypeEnumPlugOperator


class AiSubdivAdaptiveMetricEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    EDGE_LENGTH = 1
    FLATNESS = 2


class AiSubdivAdaptiveMetricEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    EDGE_LENGTH = 1
    FLATNESS = 2

    NAME_MAP = {
        AUTO: "auto",
        EDGE_LENGTH: "edge_length",
        FLATNESS: "flatness",
    }


class AiSubdivAdaptiveMetricEnumField(
    EnumField[AiSubdivAdaptiveMetricEnumAttrOperator, AiSubdivAdaptiveMetricEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivAdaptiveMetricEnumAttrOperator
    PLUG_CLS = AiSubdivAdaptiveMetricEnumPlugOperator


class AiSubdivAdaptiveSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RASTER = 0
    OBJECT = 1


class AiSubdivAdaptiveSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RASTER = 0
    OBJECT = 1

    NAME_MAP = {
        RASTER: "raster",
        OBJECT: "object",
    }


class AiSubdivAdaptiveSpaceEnumField(
    EnumField[AiSubdivAdaptiveSpaceEnumAttrOperator, AiSubdivAdaptiveSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivAdaptiveSpaceEnumAttrOperator
    PLUG_CLS = AiSubdivAdaptiveSpaceEnumPlugOperator


class AiSubdivUvSmoothingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PIN_CORNERS = 0
    PIN_BORDERS = 1
    LINEAR = 2
    SMOOTH = 3


class AiSubdivUvSmoothingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PIN_CORNERS = 0
    PIN_BORDERS = 1
    LINEAR = 2
    SMOOTH = 3

    NAME_MAP = {
        PIN_CORNERS: "pin_corners",
        PIN_BORDERS: "pin_borders",
        LINEAR: "linear",
        SMOOTH: "smooth",
    }


class AiSubdivUvSmoothingEnumField(
    EnumField[AiSubdivUvSmoothingEnumAttrOperator, AiSubdivUvSmoothingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivUvSmoothingEnumAttrOperator
    PLUG_CLS = AiSubdivUvSmoothingEnumPlugOperator


class AiMotionVectorUnitEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_FRAME = 0
    PER_SECOND = 1


class AiMotionVectorUnitEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_FRAME = 0
    PER_SECOND = 1

    NAME_MAP = {
        PER_FRAME: "Per Frame",
        PER_SECOND: "Per Second",
    }


class AiMotionVectorUnitEnumField(
    EnumField[AiMotionVectorUnitEnumAttrOperator, AiMotionVectorUnitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiMotionVectorUnitEnumAttrOperator
    PLUG_CLS = AiMotionVectorUnitEnumPlugOperator


class NurbsSurface(Shape):
    __slots__ = ()

    NODE_TYPE = "nurbsSurface"

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

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(default_value=1, min_value=1, max_value=5, soft_max_value=5)
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    tweak = BoolField(default_value=False)
    tw = tweak

    relativeTweak = BoolField(default_value=True)
    rtw = relativeTweak

    controlPoints = ControlPointsField(multi=True, default_value=(0.0, 0.0, 0.0))
    cp = controlPoints

    weights = DoubleField(multi=True, default_value=1.0)
    wt = weights

    tweakLocation = TypedField(readable=False)
    twl = tweakLocation

    blindDataNodes = MessageField(multi=True, readable=False)
    bn = blindDataNodes

    uvPivot = UvPivotField(default_value=(0.0, 0.0))
    pv = uvPivot
    uvPivotX = uvPivot.uvPivotX
    pvx = uvPivotX
    uvPivotY = uvPivot.uvPivotY
    pvy = uvPivotY

    uvSet = UvSetField(multi=True)
    uvst = uvSet

    currentUVSet = DataStringField()
    cuvs = currentUVSet

    displayImmediate = BoolField(default_value=False)
    di = displayImmediate

    displayColors = BoolField(default_value=False)
    dcol = displayColors

    displayColorChannel = DataStringField()
    dcc = displayColorChannel

    currentColorSet = DataStringField()
    ccls = currentColorSet

    colorSet = ColorSetField(multi=True)
    clst = colorSet

    ignoreHwShader = BoolField(default_value=False)
    ih = ignoreHwShader

    doubleSided = BoolField(default_value=True)
    ds = doubleSided

    opposite = BoolField(default_value=False)
    op = opposite

    holdOut = BoolField(default_value=False)
    hot = holdOut

    smoothShading = BoolField(default_value=True)
    smo = smoothShading

    boundingBoxScale = BoundingBoxScaleField(default_value=(1.5, 1.5, 1.5), min_value=(1.0, 1.0, 1.0))
    bbs = boundingBoxScale
    boundingBoxScaleX = boundingBoxScale.boundingBoxScaleX
    bscx = boundingBoxScaleX
    boundingBoxScaleY = boundingBoxScale.boundingBoxScaleY
    bscy = boundingBoxScaleY
    boundingBoxScaleZ = boundingBoxScale.boundingBoxScaleZ
    bscz = boundingBoxScaleZ

    featureDisplacement = BoolField(default_value=True)
    fbda = featureDisplacement

    initialSampleRate = LongField(default_value=6, min_value=0, soft_max_value=100)
    dsr = initialSampleRate

    extraSampleRate = LongField(default_value=5, min_value=0, soft_max_value=50)
    xsr = extraSampleRate

    textureThreshold = LongField(default_value=0, min_value=0, max_value=100)
    fth = textureThreshold

    normalThreshold = FloatField(default_value=30.0, min_value=0.0, max_value=180.0)
    nat = normalThreshold

    displayHWEnvironment = BoolField(default_value=False)
    dhe = displayHWEnvironment

    collisionOffsetVelocityIncrement = CollisionOffsetVelocityIncrementField(multi=True, default_value=(0.0, 0.0, 0.0))
    covi = collisionOffsetVelocityIncrement

    collisionDepthVelocityIncrement = CollisionDepthVelocityIncrementField(multi=True, default_value=(0.0, 0.0, 0.0))
    cdvi = collisionDepthVelocityIncrement

    collisionOffsetVelocityMultiplier = CollisionOffsetVelocityMultiplierField(multi=True, default_value=(0.0, 0.0, 0.0))
    covm = collisionOffsetVelocityMultiplier

    collisionDepthVelocityMultiplier = CollisionDepthVelocityMultiplierField(multi=True, default_value=(0.0, 0.0, 0.0))
    cdvm = collisionDepthVelocityMultiplier

    header = TypedField()
    hd = header

    create_ = DataNurbsSurfaceField(long_name="create", short_name="cr")
    cr = create_

    local = DataNurbsSurfaceField(writable=False)
    l = local

    worldSpace = DataNurbsSurfaceField(multi=True, writable=False)
    ws = worldSpace

    divisionsU = ByteField(default_value=0, min_value=0, max_value=64)
    dvu = divisionsU

    divisionsV = ByteField(default_value=0, min_value=0, max_value=64)
    dvv = divisionsV

    curvePrecision = ByteField(default_value=4, min_value=0, max_value=127)
    cpr = curvePrecision

    curvePrecisionShaded = ByteField(default_value=1, min_value=0, max_value=63)
    cps = curvePrecisionShaded

    simplifyMode = ByteField(default_value=0, min_value=0, max_value=1)
    sm = simplifyMode

    simplifyU = ByteField(default_value=1, min_value=1, max_value=24)
    smu = simplifyU

    simplifyV = ByteField(default_value=1, min_value=1, max_value=24)
    smv = simplifyV

    smoothEdge = BoolField(default_value=False)
    ues = smoothEdge

    smoothEdgeRatio = DoubleField(default_value=0.99, min_value=0.1, max_value=0.999, soft_min_value=0.95)
    esr = smoothEdgeRatio

    useChordHeight = BoolField(default_value=False)
    uch = useChordHeight

    objSpaceChordHeight = BoolField(default_value=True)
    uco = objSpaceChordHeight

    useChordHeightRatio = BoolField(default_value=True)
    ucr = useChordHeightRatio

    edgeSwap = BoolField(default_value=False)
    es = edgeSwap

    useMinScreen = BoolField(default_value=False)
    uns = useMinScreen

    selCVDisp = BoolField(default_value=False)
    scvd = selCVDisp

    dispCV = BoolField(default_value=False)
    dcv = dispCV

    dispEP = BoolField(default_value=False)
    dep = dispEP

    dispHull = BoolField(default_value=False)
    dh = dispHull

    dispGeometry = BoolField(default_value=True)
    dg = dispGeometry

    dispOrigin = BoolField(default_value=False)
    dor = dispOrigin

    numberU = LongField(default_value=3, min_value=1, soft_max_value=20)
    nu = numberU

    modeU = ModeUEnumField(default_value=3)
    mu = modeU

    numberV = LongField(default_value=3, min_value=1, soft_max_value=20)
    nv = numberV

    modeV = ModeVEnumField(default_value=3)
    mv = modeV

    chordHeight = DoubleField(default_value=0.1, min_value=0.001, soft_max_value=0.2)
    ch = chordHeight

    chordHeightRatio = DoubleField(default_value=0.983, min_value=0.1, max_value=0.999, soft_min_value=0.9)
    chr = chordHeightRatio

    minScreen = DoubleField(default_value=14.0)
    mns = minScreen

    formU = FormUEnumField(default_value=0, writable=False)
    fu = formU

    formV = FormVEnumField(default_value=0, writable=False)
    fv = formV

    cached = DataNurbsSurfaceField()
    cc = cached

    trimFace = TypedField(multi=True)
    tf = trimFace

    patchUVIds = TypedField(multi=True)
    pu = patchUVIds

    inPlace = BoolField(default_value=False)
    ipo = inPlace

    tweakSizeU = LongField(default_value=-1)
    tsu = tweakSizeU

    tweakSizeV = LongField(default_value=-1)
    tsv = tweakSizeV

    minMaxRangeU = MinMaxRangeUField(default_value=(0.0, 0.0), writable=False)
    mmu = minMaxRangeU
    minValueU = minMaxRangeU.minValueU
    mnu = minValueU
    maxValueU = minMaxRangeU.maxValueU
    mxu = maxValueU

    minMaxRangeV = MinMaxRangeVField(default_value=(0.0, 0.0), writable=False)
    mmv = minMaxRangeV
    minValueV = minMaxRangeV.minValueV
    mnv = minValueV
    maxValueV = minMaxRangeV.maxValueV
    mxv = maxValueV

    degreeUV = DegreeUVField(default_value=(0, 0), writable=False)
    d = degreeUV
    degreeU = degreeUV.degreeU
    du = degreeU
    degreeV = degreeUV.degreeV
    dv = degreeV

    spansUV = SpansUVField(default_value=(0, 0), writable=False)
    sp = spansUV
    spansU = spansUV.spansU
    su = spansU
    spansV = spansUV.spansV
    sv = spansV

    displayRenderTessellation = BoolField(default_value=False)
    drt = displayRenderTessellation

    renderTriangleCount = LongField(default_value=0, writable=False)
    tcn = renderTriangleCount

    fixTextureWarp = BoolField(default_value=False)
    ftwp = fixTextureWarp

    gridDivisionPerSpanU = ShortField(default_value=4, min_value=1, max_value=15)
    gdsu = gridDivisionPerSpanU

    gridDivisionPerSpanV = ShortField(default_value=4, min_value=1, max_value=15)
    gdsv = gridDivisionPerSpanV

    explicitTessellationAttributes = BoolField(default_value=False)
    eta = explicitTessellationAttributes

    uDivisionsFactor = DoubleField(default_value=1.5, min_value=0.1, soft_max_value=5.0)
    nufa = uDivisionsFactor

    vDivisionsFactor = DoubleField(default_value=1.5, min_value=0.1, soft_max_value=5.0)
    nvfa = vDivisionsFactor

    curvatureTolerance = CurvatureToleranceEnumField(default_value=2)
    cvto = curvatureTolerance

    basicTessellationType = BasicTessellationTypeEnumField(default_value=0)
    btt = basicTessellationType

    dispSF = BoolField(default_value=False)
    dsf = dispSF

    normalsDisplayScale = DoubleField(default_value=1.0, soft_min_value=0.01, soft_max_value=10.0)
    ndf = normalsDisplayScale

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiSelfShadows = BoolField(default_value=True, category="arnold")
    ai_self_shadows = aiSelfShadows

    aiOpaque = BoolField(default_value=True, category="arnold")
    ai_opaque = aiOpaque

    aiMatte = BoolField(default_value=False, category="arnold")
    ai_matte = aiMatte

    aiTraceSets = DataStringField(category="arnold")
    trace_sets = aiTraceSets

    aiSssSetname = DataStringField(category="arnold")
    ai_sss_setname = aiSssSetname

    aiToonId = DataStringField(category="arnold")
    ai_toon_id = aiToonId

    aiVisibleInDiffuseReflection = BoolField(default_value=True, category="arnold")
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(default_value=True, category="arnold")
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(default_value=True, category="arnold")
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(default_value=True, category="arnold")
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    aiSubdivType = AiSubdivTypeEnumField(default_value=0, category="arnold")
    ai_subdiv_type = aiSubdivType

    aiSubdivIterations = ByteField(default_value=1, min_value=0, max_value=100, soft_min_value=0, soft_max_value=10, category="arnold")
    ai_subdiv_iterations = aiSubdivIterations

    aiSubdivAdaptiveMetric = AiSubdivAdaptiveMetricEnumField(default_value=0, category="arnold")
    ai_subdiv_adaptive_metric = aiSubdivAdaptiveMetric

    aiSubdivPixelError = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0, category="arnold")
    ai_subdiv_adaptive_error = aiSubdivPixelError

    aiSubdivAdaptiveSpace = AiSubdivAdaptiveSpaceEnumField(default_value=0, category="arnold")
    ai_subdiv_adaptive_space = aiSubdivAdaptiveSpace

    aiSubdivUvSmoothing = AiSubdivUvSmoothingEnumField(default_value=0, category="arnold")
    ai_subdiv_uv_smoothing = aiSubdivUvSmoothing

    aiSubdivSmoothDerivs = BoolField(default_value=False, category="arnold")
    ai_subdiv_smooth_derivs = aiSubdivSmoothDerivs

    aiSubdivFrustumIgnore = BoolField(default_value=False, category="arnold")
    ai_subdiv_frustum_ignore = aiSubdivFrustumIgnore

    aiDispHeight = FloatField(default_value=1.0, category="arnold")
    ai_disp_height = aiDispHeight

    aiDispPadding = FloatField(default_value=0.0, category="arnold")
    ai_disp_padding = aiDispPadding

    aiDispZeroValue = FloatField(default_value=0.0, category="arnold")
    ai_disp_zero_value = aiDispZeroValue

    aiDispAutobump = BoolField(default_value=False, category="arnold")
    ai_disp_autobump = aiDispAutobump

    aiAutobumpVisibility = ByteField(default_value=1, min_value=0, max_value=255, category="arnold")
    ai_autobump_visibility = aiAutobumpVisibility

    aiExportTangents = BoolField(default_value=False, category="arnold")
    ai_exptan = aiExportTangents

    aiExportColors = BoolField(default_value=False, category="arnold")
    ai_expcol = aiExportColors

    aiExportRefPoints = BoolField(default_value=True, category="arnold")
    ai_exprpt = aiExportRefPoints

    aiExportRefNormals = BoolField(default_value=False, category="arnold")
    ai_exprnrm = aiExportRefNormals

    aiExportRefTangents = BoolField(default_value=False, category="arnold")
    ai_exprtan = aiExportRefTangents

    aiStepSize = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_step_size = aiStepSize

    aiVolumePadding = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_volume_padding = aiVolumePadding

    aiMotionVectorSource = DataStringField(category="arnold")
    ai_motion_vector_source = aiMotionVectorSource

    aiMotionVectorUnit = AiMotionVectorUnitEnumField(default_value=0, category="arnold")
    ai_motion_vector_unit = aiMotionVectorUnit

    aiMotionVectorScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0, category="arnold")
    ai_motion_vector_scale = aiMotionVectorScale
