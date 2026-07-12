# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.mash_flight import (
    AlignRampField,
    ArrivalRampField,
    AttractorRampField,
    BoundingBoxField,
    CenterField,
    CohereRampField,
    CompInstObjGroupsField,
    ComponentTagsField,
    DrawOverrideField,
    FalloffObjectField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    GravitateLocationField,
    GravityRampField,
    InertiaField,
    InstObjGroupsField,
    LocalPositionField,
    LocalScaleField,
    ObjectColorRGBField,
    ObstacleRampField,
    ObstaclesField,
    OutlinerColorField,
    PredatorAndPreyRampField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    SeparateRampField,
    TargetsField,
    UpVectorField,
    WireColorRGBField,
    WorldPositionField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
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


class AvoidanceTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLEE = 1
    AROUND_X = 2
    OVER_SLASH_UNDER_Y = 3
    AROUND_Z = 4


class AvoidanceTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLEE = 1
    AROUND_X = 2
    OVER_SLASH_UNDER_Y = 3
    AROUND_Z = 4

    NAME_MAP = {
        FLEE: "Flee",
        AROUND_X: "Around (X)",
        OVER_SLASH_UNDER_Y: "Over/ Under (Y)",
        AROUND_Z: "Around (Z)",
    }


class AvoidanceTypeEnumField(
    EnumField[AvoidanceTypeEnumAttrOperator, AvoidanceTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AvoidanceTypeEnumAttrOperator
    PLUG_CLS = AvoidanceTypeEnumPlugOperator


class GravitateTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GIVEN_LOCATION = 1
    GROUP_CENTRE = 2


class GravitateTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    GIVEN_LOCATION = 1
    GROUP_CENTRE = 2

    NAME_MAP = {
        GIVEN_LOCATION: "Given Location",
        GROUP_CENTRE: "Group Centre",
    }


class GravitateTypeEnumField(
    EnumField[GravitateTypeEnumAttrOperator, GravitateTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravitateTypeEnumAttrOperator
    PLUG_CLS = GravitateTypeEnumPlugOperator


class DisplayTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 1
    ATTRACTOR = 2
    OBSTACLE = 3
    PREDATOR = 4
    PREY = 5
    NONE = 6


class DisplayTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 1
    ATTRACTOR = 2
    OBSTACLE = 3
    PREDATOR = 4
    PREY = 5
    NONE = 6

    NAME_MAP = {
        NORMAL: "Normal",
        ATTRACTOR: "Attractor",
        OBSTACLE: "Obstacle",
        PREDATOR: "Predator",
        PREY: "Prey",
        NONE: "None",
    }


class DisplayTypeEnumField(
    EnumField[DisplayTypeEnumAttrOperator, DisplayTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayTypeEnumAttrOperator
    PLUG_CLS = DisplayTypeEnumPlugOperator


class MASH_Flight(Shape):
    __slots__ = ()

    NODE_TYPE = "MASH_Flight"

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

    underWorldObject = BoolField(default_value=False)
    uwo = underWorldObject

    localPosition = LocalPositionField(default_value=(0.0, 0.0, 0.0))
    lp = localPosition
    localPositionX = localPosition.localPositionX
    lpx = localPositionX
    localPositionY = localPosition.localPositionY
    lpy = localPositionY
    localPositionZ = localPosition.localPositionZ
    lpz = localPositionZ

    worldPosition = WorldPositionField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    wp = worldPosition

    localScale = LocalScaleField(default_value=(1.0, 1.0, 1.0))
    los = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    outputPoints = TypedField(writable=False)

    inputPoints = TypedField()

    savedData = TypedField()

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    inPredators = DataVectorArrayField()

    inPrey = DataVectorArrayField()

    inputInertia = DataVectorArrayField()

    inInertiaPP = DataVectorArrayField()

    initialState = TypedField()

    targetPP = DataVectorArrayField()

    locomotion = DataVectorArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    alignmentStrength = FloatField(default_value=9.0, min_value=0.0, soft_max_value=10.0)

    cohesionStrength = FloatField(default_value=2.5, min_value=0.0, soft_max_value=10.0)

    seperationStrength = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    enable = BoolField(default_value=True)
    en = enable

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    raEn = randEnvelope

    StepEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    StEnv = StepEnvelope

    steeringForce = FloatField(default_value=0.9800000190734863, min_value=0.0, max_value=1.0, soft_min_value=0.8)

    maxSpeed = FloatField(default_value=5.0, min_value=0.001, soft_max_value=10.0)

    minSpeed = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)

    searchDistance = FloatField(default_value=90.0, min_value=0.001, soft_max_value=100.0)

    seperationThreshold = FloatField(default_value=0.05000000074505806, min_value=0.001, max_value=1.0)

    alignThreshold = FloatField(default_value=0.6499999761581421, min_value=0.001, max_value=1.0)

    FoV = FloatField(default_value=120.0, min_value=1.0, max_value=360.0)

    predatorStrength = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    preyStrength = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    preyDistance = FloatField(default_value=50.0, min_value=0.001, soft_max_value=100.0)

    predatorDistance = FloatField(default_value=50.0, min_value=0.001, soft_max_value=100.0)

    gravitateStrength = FloatField(default_value=6.0, min_value=0.0, soft_max_value=2.0)

    gravitateDistance = FloatField(default_value=90.0, min_value=0.001, soft_max_value=100.0)

    gravitateThreshold = FloatField(default_value=0.25, min_value=0.001, max_value=1.0)

    startFrame = LongField(default_value=1)

    inertia = InertiaField(default_value=(0.0, 0.0, 0.0))
    inertia0 = inertia.inertia0
    inertia1 = inertia.inertia1
    inertia2 = inertia.inertia2

    mass = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    massVariance = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    rotationalSteering = FloatField(default_value=0.800000011920929, min_value=0.0, max_value=1.0)

    rotationalThreshold = FloatField(default_value=0.75, min_value=0.0, soft_max_value=1.0)

    alignRamp = AlignRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    cohereRamp = CohereRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    separateRamp = SeparateRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    obstacleRamp = ObstacleRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    attractorRamp = AttractorRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    predatorAndPreyRamp = PredatorAndPreyRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    gravityRamp = GravityRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    arrivalRamp = ArrivalRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    falloffInfo = TypedField()

    legacy2017 = BoolField(default_value=False)

    obstacleMeshes = DataMeshField(multi=True)

    inputMesh = DataMeshField()
    inM = inputMesh

    obstacles = ObstaclesField(multi=True, default_value=(0.0, 0.0, 0.0))

    gravitateLocation = GravitateLocationField(default_value=(0.0, 0.0, 0.0))
    gravitateLocation0 = gravitateLocation.gravitateLocation0
    gravitateLocation1 = gravitateLocation.gravitateLocation1
    gravitateLocation2 = gravitateLocation.gravitateLocation2

    targets = TargetsField(multi=True, default_value=(0.0, 0.0, 0.0))

    arrivalDamp = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    arrivalMode = BoolField(default_value=False)

    arriveThreshold = FloatField(default_value=0.30000001192092896, min_value=0.001, max_value=1.0)

    arriveVariance = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)

    targetStrength = FloatField(default_value=5.0, min_value=0.0, soft_max_value=2.0)

    targetDistance = FloatField(default_value=150.0, min_value=0.0, soft_max_value=100.0)

    obstacleStrength = FloatField(default_value=10.0, min_value=0.0, soft_max_value=2.0)

    obstacleDistance = FloatField(default_value=50.0, min_value=0.0, soft_max_value=100.0)

    displayCount = LongField(default_value=0, min_value=0, soft_max_value=10)

    numberOfNeighbours = LongField(default_value=50, min_value=1, soft_max_value=20)

    pauseFrequency = LongField(default_value=1, min_value=1, soft_max_value=20)

    pauseLength = LongField(default_value=25, min_value=1, soft_max_value=20)

    pauseRandom = LongField(default_value=15, min_value=1, soft_max_value=20)

    pauseOnBlocked = BoolField(default_value=False)

    fields = MessageField(multi=True)

    avoidanceType = AvoidanceTypeEnumField(default_value=1)

    gravitateType = GravitateTypeEnumField(default_value=1)

    displayType = DisplayTypeEnumField(default_value=1)

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    upVector0 = upVector.upVector0
    upVector1 = upVector.upVector1
    upVector2 = upVector.upVector2
