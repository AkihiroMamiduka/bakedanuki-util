# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.ai_stand_in import (
    BoundingBoxScaleField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    MaxBoundingBoxField,
    MinBoundingBoxField,
    UvPivotField,
    UvSetField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.string import DataStringField


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    BOUNDING_BOX = 0
    PER_OBJECT_BOUNDING_BOX = 1
    POLYWIRE = 2
    WIREFRAME = 3
    POINT_CLOUD = 4
    SHADED_POLYWIRE = 5
    SHADED = 6


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    BOUNDING_BOX = 0
    PER_OBJECT_BOUNDING_BOX = 1
    POLYWIRE = 2
    WIREFRAME = 3
    POINT_CLOUD = 4
    SHADED_POLYWIRE = 5
    SHADED = 6

    NAME_MAP = {
        BOUNDING_BOX: "Bounding Box",
        PER_OBJECT_BOUNDING_BOX: "Per Object Bounding Box",
        POLYWIRE: "Polywire",
        WIREFRAME: "Wireframe",
        POINT_CLOUD: "Point Cloud",
        SHADED_POLYWIRE: "Shaded Polywire",
        SHADED: "Shaded",
    }


class ModeEnumField(EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class StandInDrawOverrideEnumPlugOperator(
    EnumPlugOperator["StandInDrawOverrideEnumAttrOperator"]
):
    __slots__ = ()

    USE_GLOBAL_SETTINGS = 0
    USE_LOCAL_SETTINGS = 1
    BOUNDING_BOX = 2
    DISABLE_DRAW = 3
    DISABLE_LOAD = 4


class StandInDrawOverrideEnumAttrOperator(
    EnumAttrOperator[StandInDrawOverrideEnumPlugOperator]
):
    __slots__ = ()

    USE_GLOBAL_SETTINGS = 0
    USE_LOCAL_SETTINGS = 1
    BOUNDING_BOX = 2
    DISABLE_DRAW = 3
    DISABLE_LOAD = 4

    NAME_MAP = {
        USE_GLOBAL_SETTINGS: "Use Global Settings",
        USE_LOCAL_SETTINGS: "Use Local Settings",
        BOUNDING_BOX: "Bounding Box",
        DISABLE_DRAW: "Disable Draw",
        DISABLE_LOAD: "Disable Load",
    }


class StandInDrawOverrideEnumField(
    EnumField[
        StandInDrawOverrideEnumAttrOperator,
        StandInDrawOverrideEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = StandInDrawOverrideEnumAttrOperator
    PLUG_CLS = StandInDrawOverrideEnumPlugOperator


class AbcCurvesBasisEnumPlugOperator(
    EnumPlugOperator["AbcCurvesBasisEnumAttrOperator"]
):
    __slots__ = ()

    AUTO = 0
    BEZIER = 1
    B_MINUS_SPLINE = 2
    CATMULL_MINUS_ROM = 3
    LINEAR = 4


class AbcCurvesBasisEnumAttrOperator(
    EnumAttrOperator[AbcCurvesBasisEnumPlugOperator]
):
    __slots__ = ()

    AUTO = 0
    BEZIER = 1
    B_MINUS_SPLINE = 2
    CATMULL_MINUS_ROM = 3
    LINEAR = 4

    NAME_MAP = {
        AUTO: "auto",
        BEZIER: "bezier",
        B_MINUS_SPLINE: "b-spline",
        CATMULL_MINUS_ROM: "catmull-rom",
        LINEAR: "linear",
    }


class AbcCurvesBasisEnumField(
    EnumField[AbcCurvesBasisEnumAttrOperator, AbcCurvesBasisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AbcCurvesBasisEnumAttrOperator
    PLUG_CLS = AbcCurvesBasisEnumPlugOperator


class GeneratedAiStandIn(Shape):
    __slots__ = ()

    NODE_TYPE = "aiStandIn"

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
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

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
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

    controlPoints = ControlPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
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

    boundingBoxScale = BoundingBoxScaleField(
        default_value=(1.5, 1.5, 1.5), min_value=(1.0, 1.0, 1.0)
    )
    bbs = boundingBoxScale
    boundingBoxScaleX = boundingBoxScale.boundingBoxScaleX
    bscx = boundingBoxScaleX
    boundingBoxScaleY = boundingBoxScale.boundingBoxScaleY
    bscy = boundingBoxScaleY
    boundingBoxScaleZ = boundingBoxScale.boundingBoxScaleZ
    bscz = boundingBoxScaleZ

    featureDisplacement = BoolField(default_value=True)
    fbda = featureDisplacement

    initialSampleRate = LongField(
        default_value=6, min_value=0, soft_max_value=100
    )
    dsr = initialSampleRate

    extraSampleRate = LongField(
        default_value=5, min_value=0, soft_max_value=50
    )
    xsr = extraSampleRate

    textureThreshold = LongField(default_value=0, min_value=0, max_value=100)
    fth = textureThreshold

    normalThreshold = FloatField(
        default_value=30.0, min_value=0.0, max_value=180.0
    )
    nat = normalThreshold

    displayHWEnvironment = BoolField(default_value=False)
    dhe = displayHWEnvironment

    collisionOffsetVelocityIncrement = CollisionOffsetVelocityIncrementField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    covi = collisionOffsetVelocityIncrement

    collisionDepthVelocityIncrement = CollisionDepthVelocityIncrementField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    cdvi = collisionDepthVelocityIncrement

    collisionOffsetVelocityMultiplier = CollisionOffsetVelocityMultiplierField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    covm = collisionOffsetVelocityMultiplier

    collisionDepthVelocityMultiplier = CollisionDepthVelocityMultiplierField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    cdvm = collisionDepthVelocityMultiplier

    dso = DataStringField()

    mode = ModeEnumField(default_value=0)

    selectedItems = DataStringField(writable=False)
    selected_items = selectedItems

    useFrameExtension = BoolField(default_value=False)

    frameNumber = LongField(default_value=0)

    useSubFrame = BoolField(default_value=False)

    frameOffset = FloatField(default_value=0.0)

    data = DataStringField()

    MinBoundingBox = MinBoundingBoxField(default_value=(-1.0, -1.0, -1.0))
    min = MinBoundingBox
    MinBoundingBox0 = MinBoundingBox.MinBoundingBox0
    min0 = MinBoundingBox0
    MinBoundingBox1 = MinBoundingBox.MinBoundingBox1
    min1 = MinBoundingBox1
    MinBoundingBox2 = MinBoundingBox.MinBoundingBox2
    min2 = MinBoundingBox2

    MaxBoundingBox = MaxBoundingBoxField(default_value=(1.0, 1.0, 1.0))
    max = MaxBoundingBox
    MaxBoundingBox0 = MaxBoundingBox.MaxBoundingBox0
    max0 = MaxBoundingBox0
    MaxBoundingBox1 = MaxBoundingBox.MaxBoundingBox1
    max1 = MaxBoundingBox1
    MaxBoundingBox2 = MaxBoundingBox.MaxBoundingBox2
    max2 = MaxBoundingBox2

    standInDrawOverride = StandInDrawOverrideEnumField(default_value=0)
    standin_draw_override = standInDrawOverride

    overrideNodes = BoolField(default_value=False)
    override_nodes = overrideNodes

    useAutoInstancing = BoolField(default_value=True)
    auto_instancing = useAutoInstancing

    aiNamespace = DataStringField()
    ai_namespace = aiNamespace

    overrides = DataStringField(multi=True)

    overrideReceiveShadows = BoolField(default_value=False)

    overrideDoubleSided = BoolField(default_value=False)

    overrideSelfShadows = BoolField(default_value=False)

    overrideOpaque = BoolField(default_value=False)

    overrideMatte = BoolField(default_value=False)

    operators = MessageField(multi=True)

    ignoreGroupNodes = BoolField(default_value=False)
    ignore_group_nodes = ignoreGroupNodes

    objectPath = DataStringField()
    objectpath = objectPath

    abcNamePrefix = DataStringField()
    abc_nameprefix = abcNamePrefix

    abcLayers = DataStringField()
    abc_layers = abcLayers

    abcFPS = FloatField(default_value=24.0)
    abc_fps = abcFPS

    abcRadiusAttribute = DataStringField()
    abc_radius_attribute = abcRadiusAttribute

    abcRadiusDefault = FloatField(default_value=0.009999999776482582)
    abc_radius_default = abcRadiusDefault

    abcRadiusScale = FloatField(default_value=1.0)
    abc_radius_scale = abcRadiusScale

    abcVelocityIgnore = BoolField(default_value=False)
    abc_velocity_ignore = abcVelocityIgnore

    abcVelocityScale = FloatField(default_value=1.0)
    abc_velocity_scale = abcVelocityScale

    abcVisibilityIgnore = BoolField(default_value=False)
    abc_visibility_ignore = abcVisibilityIgnore

    abcMakeInstance = BoolField(default_value=False)
    abc_make_instance = abcMakeInstance

    abcPullUserParams = BoolField(default_value=False)
    abc_pull_user_params = abcPullUserParams

    abcUseInstanceCache = BoolField(default_value=True)
    abc_use_instance_cache = abcUseInstanceCache

    abcCurvesBasis = AbcCurvesBasisEnumField(default_value=0)
    abc_curves_basis = abcCurvesBasis

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

    aiVisibleInDiffuseReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    overrideLightLinking = BoolField(default_value=True, category="arnold")
    oll = overrideLightLinking

    overrideShaders = BoolField(default_value=True, category="arnold")
    osh = overrideShaders
