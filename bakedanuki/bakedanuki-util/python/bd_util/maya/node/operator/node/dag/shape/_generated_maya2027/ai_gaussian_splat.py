# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr_maya2027.ai_gaussian_splat import (
    BoundingBoxScaleField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    DiffuseTintField,
    EmissionTintField,
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
from .....attr.define.std.dt.mesh import DataMeshField
from .....attr.define.std.dt.string import DataStringField


class DrawModeEnumPlugOperator(EnumPlugOperator["DrawModeEnumAttrOperator"]):
    __slots__ = ()

    BOUNDING_BOX = 0
    POINT_CLOUD = 1
    GAUSSIAN_SPLAT = 2


class DrawModeEnumAttrOperator(EnumAttrOperator[DrawModeEnumPlugOperator]):
    __slots__ = ()

    BOUNDING_BOX = 0
    POINT_CLOUD = 1
    GAUSSIAN_SPLAT = 2

    NAME_MAP = {
        BOUNDING_BOX: "Bounding Box",
        POINT_CLOUD: "Point Cloud",
        GAUSSIAN_SPLAT: "Gaussian Splat",
    }


class DrawModeEnumField(
    EnumField[DrawModeEnumAttrOperator, DrawModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawModeEnumAttrOperator
    PLUG_CLS = DrawModeEnumPlugOperator


class UpAxisEnumPlugOperator(EnumPlugOperator["UpAxisEnumAttrOperator"]):
    __slots__ = ()

    Y_UP = 0
    Z_UP = 1
    MINUS_Y_UP = 2
    MINUS_Z_UP = 3


class UpAxisEnumAttrOperator(EnumAttrOperator[UpAxisEnumPlugOperator]):
    __slots__ = ()

    Y_UP = 0
    Z_UP = 1
    MINUS_Y_UP = 2
    MINUS_Z_UP = 3

    NAME_MAP = {
        Y_UP: "Y up",
        Z_UP: "Z up",
        MINUS_Y_UP: "-Y up",
        MINUS_Z_UP: "-Z up",
    }


class UpAxisEnumField(
    EnumField[UpAxisEnumAttrOperator, UpAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpAxisEnumAttrOperator
    PLUG_CLS = UpAxisEnumPlugOperator


class GeneratedAiGaussianSplat(Shape):
    __slots__ = ()

    NODE_TYPE = "aiGaussianSplat"

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

    filename = DataStringField()
    fn = filename

    drawMode = DrawModeEnumField(default_value=0)

    maxDisplayPoints = LongField(default_value=500000, min_value=0)

    displayPercentage = FloatField(
        default_value=100.0, min_value=0.0, max_value=100.0
    )

    minPixelWidth = FloatField(default_value=0.0, min_value=0.0)

    useFile = BoolField(default_value=True)

    inputColorSpace = DataStringField()

    maskMesh = DataMeshField()

    maskInvert = BoolField(default_value=False)

    upAxis = UpAxisEnumField(default_value=0)

    emissionWeight = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    emission_weight = emissionWeight

    emissionTint = EmissionTintField(default_value=(1.0, 1.0, 1.0))
    emission_tint = emissionTint
    emissionTintR = emissionTint.emissionTintR
    emission_tintr = emissionTintR
    emissionTintG = emissionTint.emissionTintG
    emission_tintg = emissionTintG
    emissionTintB = emissionTint.emissionTintB
    emission_tintb = emissionTintB

    diffuseWeight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    diffuse_weight = diffuseWeight

    diffuseTint = DiffuseTintField(default_value=(1.0, 1.0, 1.0))
    diffuse_tint = diffuseTint
    diffuseTintR = diffuseTint.diffuseTintR
    diffuse_tintr = diffuseTintR
    diffuseTintG = diffuseTint.diffuseTintG
    diffuse_tintg = diffuseTintG
    diffuseTintB = diffuseTint.diffuseTintB
    diffuse_tintb = diffuseTintB

    diffuseRoughness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    diffuse_roughness = diffuseRoughness

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

    aiInteriorSet = DataStringField(category="arnold")
    ai_interior_set = aiInteriorSet

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
