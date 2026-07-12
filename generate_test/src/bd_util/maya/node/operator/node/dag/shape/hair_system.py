# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.hair_system import (
    AiHairShaderField,
    AttractionScaleField,
    BoundingBoxField,
    CenterField,
    ClumpCurlField,
    ClumpFlatnessField,
    ClumpWidthScaleField,
    CollisionDataField,
    DisplacementScaleField,
    DisplayColorField,
    DrawOverrideField,
    FieldDataField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    HairColorField,
    HairColorScaleField,
    HairWidthScaleField,
    InstObjGroupsField,
    ObjectColorRGBField,
    OutlinerColorField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    SpecularColorField,
    StiffnessScaleField,
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
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


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


class SimulationMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    STATIC = 1
    DYNAMIC_FOLLICLES_ONLY = 2
    ALL_FOLLICLES = 3


class SimulationMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    STATIC = 1
    DYNAMIC_FOLLICLES_ONLY = 2
    ALL_FOLLICLES = 3

    NAME_MAP = {
        OFF: "Off",
        STATIC: "Static",
        DYNAMIC_FOLLICLES_ONLY: "Dynamic Follicles Only",
        ALL_FOLLICLES: "All Follicles",
    }


class SimulationMethodEnumField(
    EnumField[SimulationMethodEnumAttrOperator, SimulationMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SimulationMethodEnumAttrOperator
    PLUG_CLS = SimulationMethodEnumPlugOperator


class CollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2


class CollisionFlagEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2

    NAME_MAP = {
        VERTEX: "Vertex",
        EDGE: "Edge",
    }


class CollisionFlagEnumField(
    EnumField[CollisionFlagEnumAttrOperator, CollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionFlagEnumAttrOperator
    PLUG_CLS = CollisionFlagEnumPlugOperator


class SelfCollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2


class SelfCollisionFlagEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2

    NAME_MAP = {
        VERTEX: "Vertex",
        EDGE: "Edge",
    }


class SelfCollisionFlagEnumField(
    EnumField[SelfCollisionFlagEnumAttrOperator, SelfCollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfCollisionFlagEnumAttrOperator
    PLUG_CLS = SelfCollisionFlagEnumPlugOperator


class EvaluationOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SEQUENTIAL = 0
    PARALLEL = 1


class EvaluationOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SEQUENTIAL = 0
    PARALLEL = 1

    NAME_MAP = {
        SEQUENTIAL: "Sequential",
        PARALLEL: "Parallel",
    }


class EvaluationOrderEnumField(
    EnumField[EvaluationOrderEnumAttrOperator, EvaluationOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EvaluationOrderEnumAttrOperator
    PLUG_CLS = EvaluationOrderEnumPlugOperator


class BendModelEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SIMPLE = 0
    TWIST_TRACKING = 1


class BendModelEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SIMPLE = 0
    TWIST_TRACKING = 1

    NAME_MAP = {
        SIMPLE: "Simple",
        TWIST_TRACKING: "Twist Tracking",
    }


class BendModelEnumField(
    EnumField[BendModelEnumAttrOperator, BendModelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BendModelEnumAttrOperator
    PLUG_CLS = BendModelEnumPlugOperator


class NoiseMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RANDOM = 0
    SURFACE_UV = 1
    CLUMP_UV = 2


class NoiseMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RANDOM = 0
    SURFACE_UV = 1
    CLUMP_UV = 2

    NAME_MAP = {
        RANDOM: "Random",
        SURFACE_UV: "Surface UV",
        CLUMP_UV: "Clump UV",
    }


class NoiseMethodEnumField(
    EnumField[NoiseMethodEnumAttrOperator, NoiseMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseMethodEnumAttrOperator
    PLUG_CLS = NoiseMethodEnumPlugOperator


class SubClumpMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SURFACE_UV = 0
    CLUMP_UV = 1


class SubClumpMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SURFACE_UV = 0
    CLUMP_UV = 1

    NAME_MAP = {
        SURFACE_UV: "Surface UV",
        CLUMP_UV: "Clump UV",
    }


class SubClumpMethodEnumField(
    EnumField[SubClumpMethodEnumAttrOperator, SubClumpMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubClumpMethodEnumAttrOperator
    PLUG_CLS = SubClumpMethodEnumPlugOperator


class CacheableAttributesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITION = 0
    POSITION_AND_VELOCITY = 1
    DYNAMIC_STATE = 2


class CacheableAttributesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITION = 0
    POSITION_AND_VELOCITY = 1
    DYNAMIC_STATE = 2

    NAME_MAP = {
        POSITION: "Position",
        POSITION_AND_VELOCITY: "Position And Velocity",
        DYNAMIC_STATE: "Dynamic State",
    }


class CacheableAttributesEnumField(
    EnumField[CacheableAttributesEnumAttrOperator, CacheableAttributesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheableAttributesEnumAttrOperator
    PLUG_CLS = CacheableAttributesEnumPlugOperator


class SolverDisplayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    COLLISION_THICKNESS = 1
    SELF_COLLISION_THICKNESS = 2


class SolverDisplayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    COLLISION_THICKNESS = 1
    SELF_COLLISION_THICKNESS = 2

    NAME_MAP = {
        OFF: "Off",
        COLLISION_THICKNESS: "Collision Thickness",
        SELF_COLLISION_THICKNESS: "Self Collision Thickness",
    }


class SolverDisplayEnumField(
    EnumField[SolverDisplayEnumAttrOperator, SolverDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverDisplayEnumAttrOperator
    PLUG_CLS = SolverDisplayEnumPlugOperator


class AiModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RIBBON = 0
    THICK = 1
    ORIENTED = 2


class AiModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RIBBON = 0
    THICK = 1
    ORIENTED = 2

    NAME_MAP = {
        RIBBON: "ribbon",
        THICK: "thick",
        ORIENTED: "oriented",
    }


class AiModeEnumField(
    EnumField[AiModeEnumAttrOperator, AiModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiModeEnumAttrOperator
    PLUG_CLS = AiModeEnumPlugOperator


class HairSystem(Shape):
    __slots__ = ()

    NODE_TYPE = "hairSystem"

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

    simulationMethod = SimulationMethodEnumField(default_value=3)
    sim = simulationMethod

    inputHair = TypedField(multi=True)
    ih = inputHair

    inputHairPin = TypedField(multi=True)
    ihp = inputHairPin

    collide = BoolField(default_value=True)
    cld = collide

    collideStrength = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    clst = collideStrength

    collideOverSample = LongField(default_value=0, min_value=0, soft_max_value=20)
    cos = collideOverSample

    selfCollide = BoolField(default_value=False)
    scd = selfCollide

    collideGround = BoolField(default_value=False)
    cdg = collideGround

    groundHeight = DoubleField(default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0)
    ghe = groundHeight

    collisionFlag = CollisionFlagEnumField(default_value=2)
    cofl = collisionFlag

    selfCollisionFlag = SelfCollisionFlagEnumField(default_value=2)
    scfl = selfCollisionFlag

    collisionLayer = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    cll = collisionLayer

    evaluationOrder = EvaluationOrderEnumField(default_value=1)
    evo = evaluationOrder

    stretchResistance = FloatField(default_value=10.0, soft_min_value=0.0, soft_max_value=200.0)
    stch = stretchResistance

    compressionResistance = FloatField(default_value=10.0, soft_min_value=0.0, soft_max_value=200.0)
    comr = compressionResistance

    restLengthScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    rlsc = restLengthScale

    twistResistance = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    trs = twistResistance

    bendResistance = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=200.0)
    bnd = bendResistance

    bendAnisotropy = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bnda = bendAnisotropy

    bendModel = BendModelEnumField(default_value=0)
    bmdl = bendModel

    extraBendLinks = LongField(default_value=0, min_value=0, soft_max_value=20)
    ebdl = extraBendLinks

    stiffness = DoubleField(default_value=0.15, soft_min_value=0.0, soft_max_value=1.0)
    sfn = stiffness

    stiffnessScale = StiffnessScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    sts = stiffnessScale

    lengthFlex = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lfx = lengthFlex

    damp = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    dmp = damp

    stretchDamp = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=10.0)
    sdmp = stretchDamp

    drag = DoubleField(default_value=0.05, soft_min_value=0.0, soft_max_value=1.0)
    drg = drag

    tangentialDrag = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=1.0)
    tdrg = tangentialDrag

    friction = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    frc = friction

    stickiness = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    stck = stickiness

    bounce = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    boce = bounce

    mass = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    mss = mass

    dynamicsWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    dw = dynamicsWeight

    collideWidthOffset = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    wid = collideWidthOffset

    selfCollideWidthScale = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=2.0)
    scws = selfCollideWidthScale

    staticCling = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    stc = staticCling

    repulsion = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    rpl = repulsion

    numCollideNeighbors = LongField(default_value=4, soft_min_value=1, soft_max_value=100)
    ncn = numCollideNeighbors

    maxSelfCollisionIterations = LongField(default_value=1, soft_min_value=0, soft_max_value=20)
    msci = maxSelfCollisionIterations

    iterations = LongField(default_value=4, soft_min_value=1, soft_max_value=100)
    itr = iterations

    drawCollideWidth = BoolField(default_value=False)
    dwd = drawCollideWidth

    widthDrawSkip = LongField(default_value=2, min_value=0, soft_max_value=20)
    wds = widthDrawSkip

    ignoreSolverGravity = BoolField(default_value=False)
    igsg = ignoreSolverGravity

    ignoreSolverWind = BoolField(default_value=False)
    igsw = ignoreSolverWind

    gravity = DoubleField(default_value=0.98, soft_min_value=0.0, soft_max_value=10.0)
    grv = gravity

    turbulenceStrength = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    tst = turbulenceStrength

    turbulenceFrequency = DoubleField(default_value=0.2, min_value=0.0, soft_max_value=2.0)
    tfr = turbulenceFrequency

    turbulenceSpeed = DoubleField(default_value=0.2, min_value=0.0, soft_max_value=2.0)
    tbs = turbulenceSpeed

    attractionDamp = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    ad = attractionDamp

    startCurveAttract = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    sct = startCurveAttract

    attractionScale = AttractionScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    ats = attractionScale

    motionDrag = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mdg = motionDrag

    displayQuality = DoubleField(default_value=100.0, soft_min_value=0.0, soft_max_value=100.0)
    dpq = displayQuality

    noStretch = BoolField(default_value=False)
    nst = noStretch

    subSegments = LongField(default_value=0, min_value=0, soft_max_value=10)
    ssg = subSegments

    clumpWidth = DoubleField(default_value=0.3, min_value=0.0, soft_max_value=1.0)
    cwd = clumpWidth

    clumpWidthScale = ClumpWidthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    cws = clumpWidthScale

    clumpTwist = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ctw = clumpTwist

    clumpCurl = ClumpCurlField(multi=True, default_value=(0.0, 0.0, 0.0))
    clc = clumpCurl

    clumpFlatness = ClumpFlatnessField(multi=True, default_value=(0.0, 0.0, 0.0))
    cfl = clumpFlatness

    bendFollow = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    bnf = bendFollow

    hairWidth = DoubleField(default_value=0.01, min_value=0.0, soft_max_value=0.1)
    hwd = hairWidth

    hairWidthScale = HairWidthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    hws = hairWidthScale

    baldnessMap = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    bmp = baldnessMap

    opacity = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    opc = opacity

    hairColor = HairColorField(default_value=(0.30000001192092896, 0.25, 0.15000000596046448))
    hcl = hairColor
    hairColorR = hairColor.hairColorR
    hcr = hairColorR
    hairColorG = hairColor.hairColorG
    hcg = hairColorG
    hairColorB = hairColor.hairColorB
    hcb = hairColorB

    hairColorScale = HairColorScaleField(multi=True)
    hcs = hairColorScale

    hairColorScale_ColorR = FloatField()
    hcscr = hairColorScale_ColorR

    hairColorScale_ColorG = FloatField()
    hcscg = hairColorScale_ColorG

    hairColorScale_ColorB = FloatField()
    hcscb = hairColorScale_ColorB

    hairsPerClump = LongField(default_value=10, min_value=1, soft_max_value=100)
    hpc = hairsPerClump

    thinning = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    thn = thinning

    translucence = DoubleField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    tlc = translucence

    specularColor = SpecularColorField(default_value=(0.3499999940395355, 0.3499999940395355, 0.30000001192092896))
    spc = specularColor
    specularColorR = specularColor.specularColorR
    spr = specularColorR
    specularColorG = specularColor.specularColorG
    spg = specularColorG
    specularColorB = specularColor.specularColorB
    spb = specularColorB

    specularPower = DoubleField(default_value=3.0, min_value=0.0, soft_max_value=20.0)
    spp = specularPower

    castShadows = BoolField(default_value=True)
    csd = castShadows

    diffuseRand = DoubleField(default_value=0.2, min_value=0.0, max_value=1.0)
    dfr = diffuseRand

    specularRand = DoubleField(default_value=0.4, min_value=0.0, max_value=1.0)
    sra = specularRand

    hueRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    chr = hueRand

    satRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    csr = satRand

    valRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cvr = valRand

    multiStreaks = LongField(default_value=0, min_value=0, max_value=100, soft_max_value=20)
    mst = multiStreaks

    multiStreakSpread1 = DoubleField(default_value=0.3, soft_min_value=0.0, soft_max_value=1.0)
    ms1 = multiStreakSpread1

    multiStreakSpread2 = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    ms2 = multiStreakSpread2

    lightEachHair = BoolField(default_value=False)
    leh = lightEachHair

    displacementScale = DisplacementScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    dsc = displacementScale

    curl = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    crl = curl

    curlFrequency = DoubleField(default_value=10.0, soft_min_value=0.0001, soft_max_value=100.0)
    crf = curlFrequency

    noiseMethod = NoiseMethodEnumField(default_value=0)
    nmt = noiseMethod

    noise = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    noi = noise

    detailNoise = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dno = detailNoise

    noiseFrequency = DoubleField(default_value=0.4, soft_min_value=0.0, soft_max_value=2.0)
    nof = noiseFrequency

    noiseFrequencyU = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    nfu = noiseFrequencyU

    noiseFrequencyV = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    nfv = noiseFrequencyV

    noiseFrequencyW = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    nfw = noiseFrequencyW

    subClumpMethod = SubClumpMethodEnumField(default_value=0)
    scm = subClumpMethod

    subClumping = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    scp = subClumping

    subClumpRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    scr = subClumpRand

    numUClumps = DoubleField(default_value=15.0, soft_min_value=1.0, soft_max_value=100.0)
    nuc = numUClumps

    numVClumps = DoubleField(default_value=15.0, soft_min_value=1.0, soft_max_value=100.0)
    nvc = numVClumps

    clumpInterpolation = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cin = clumpInterpolation

    interpolationRange = DoubleField(default_value=8.0, soft_min_value=0.0, soft_max_value=20.0)
    inr = interpolationRange

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    startTime = TimeField(default_value=0.0, writable=False)
    sti = startTime

    startFrame = DoubleField(default_value=1.0)
    stf = startFrame

    lastEvalTime = TimeField(default_value=-2.5)
    lst = lastEvalTime

    inputForce = DataVectorArrayField(multi=True)
    ifc = inputForce

    fieldData = FieldDataField(writable=False)
    fd = fieldData
    fieldDataPosition = fieldData.fieldDataPosition
    fdp = fieldDataPosition
    fieldDataVelocity = fieldData.fieldDataVelocity
    fdv = fieldDataVelocity
    fieldDataMass = fieldData.fieldDataMass
    fdm = fieldDataMass
    fieldDataDeltaTime = fieldData.fieldDataDeltaTime
    fdt = fieldDataDeltaTime

    usePre70ForceIntensity = BoolField(default_value=False)
    upfi = usePre70ForceIntensity

    collisionData = CollisionDataField(readable=False)
    cda = collisionData
    collisionGeometry = collisionData.collisionGeometry
    cge = collisionGeometry
    collisionResilience = collisionData.collisionResilience
    crs = collisionResilience
    collisionFriction = collisionData.collisionFriction
    cfr = collisionFriction

    diskCache = MessageField()
    dc = diskCache

    nextState = GenericField(readable=False)
    nxst = nextState

    currentState = GenericField(writable=False)
    cust = currentState

    startState = GenericField(writable=False)
    stst = startState

    nucleusId = GenericField(writable=False)
    nuid = nucleusId

    active = BoolField(default_value=False)
    actv = active

    attachObjectId = GenericField()
    aoid = attachObjectId

    disableFollicleAnim = BoolField(default_value=False)
    dfam = disableFollicleAnim

    cacheableAttributes = CacheableAttributesEnumField(default_value=0)
    caat = cacheableAttributes

    hairCounts = GenericField()
    nhct = hairCounts

    vertexCounts = GenericField()
    nvct = vertexCounts

    positions = GenericField()
    poss = positions

    velocities = GenericField()
    vels = velocities

    internalState = GenericField()
    inst = internalState

    playFromCache = BoolField(default_value=False)
    pfc = playFromCache

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    outputHair = DataVectorArrayField(multi=True, writable=False)
    oh = outputHair

    outputRenderHairs = TypedField(writable=False)
    orh = outputRenderHairs

    solverDisplay = SolverDisplayEnumField(default_value=0)
    svds = solverDisplay

    displayColor = DisplayColorField(default_value=(1.0, 0.800000011920929, 0.0))
    dcl = displayColor
    displayColorR = displayColor.displayColorR
    dcr = displayColorR
    displayColorG = displayColor.displayColorG
    dcg = displayColorG
    displayColorB = displayColor.displayColorB
    dcb = displayColorB

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

    aiMinPixelWidth = FloatField(default_value=0.0, category="arnold")
    ai_min_pixel_width = aiMinPixelWidth

    aiMode = AiModeEnumField(default_value=0, category="arnold")
    ai_mode = aiMode

    primaryVisibility = BoolField(default_value=True, category="arnold")
    vis = primaryVisibility

    castsShadows = BoolField(default_value=True, category="arnold")
    csh = castsShadows

    aiExportHairUVs = BoolField(default_value=False, category="arnold")
    ai_export_hair_uvs = aiExportHairUVs

    aiExportHairColors = BoolField(default_value=False, category="arnold")
    ai_export_hair_colors = aiExportHairColors

    aiOverrideHair = BoolField(default_value=False, category="arnold")
    ai_override_hair = aiOverrideHair

    aiHairShader = AiHairShaderField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_hair_shader = aiHairShader
    aiHairShaderR = aiHairShader.aiHairShaderR
    ai_hair_shaderr = aiHairShaderR
    aiHairShaderG = aiHairShader.aiHairShaderG
    ai_hair_shaderg = aiHairShaderG
    aiHairShaderB = aiHairShader.aiHairShaderB
    ai_hair_shaderb = aiHairShaderB

    aiIndirectDiffuse = FloatField(default_value=1.0, category="arnold")
