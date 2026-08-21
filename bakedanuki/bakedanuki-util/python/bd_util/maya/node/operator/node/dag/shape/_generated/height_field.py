# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.height_field import (
    BoundingBoxScaleField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    UvPivotField,
    UvSetField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.string import DataStringField


class GeneratedHeightField(Shape):
    __slots__ = ()

    NODE_TYPE = "heightField"

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

    resolution = LongField(
        default_value=10, min_value=1, max_value=2000, soft_max_value=100
    )
    res = resolution

    color = ColorField(default_value=(0.5, 0.5, 0.5))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    displacement = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dis = displacement

    heightScale = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    hc = heightScale

    cacheNeedsRebuilding = BoolField(default_value=True, writable=False)
    cnr = cacheNeedsRebuilding
