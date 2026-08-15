# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.subdiv import (
    BoundingBoxScaleField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    UvPivotField,
    UvSetField,
    VertexField,
    VertexTweakField,
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


class FormatEnumPlugOperator(EnumPlugOperator["FormatEnumAttrOperator"]):
    __slots__ = ()

    UNIFORM = 0
    ADAPTIVE = 1


class FormatEnumAttrOperator(EnumAttrOperator[FormatEnumPlugOperator]):
    __slots__ = ()

    UNIFORM = 0
    ADAPTIVE = 1

    NAME_MAP = {
        UNIFORM: "Uniform",
        ADAPTIVE: "Adaptive",
    }


class FormatEnumField(
    EnumField[FormatEnumAttrOperator, FormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormatEnumAttrOperator
    PLUG_CLS = FormatEnumPlugOperator


class DisplayLevelEnumPlugOperator(
    EnumPlugOperator["DisplayLevelEnumAttrOperator"]
):
    __slots__ = ()

    _0_BASE = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    _12 = 12
    _13_FINEST = 13


class DisplayLevelEnumAttrOperator(
    EnumAttrOperator[DisplayLevelEnumPlugOperator]
):
    __slots__ = ()

    _0_BASE = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    _12 = 12
    _13_FINEST = 13

    NAME_MAP = {
        _0_BASE: "0 (Base)",
        _1: "1",
        _2: "2",
        _3: "3",
        _4: "4",
        _5: "5",
        _6: "6",
        _7: "7",
        _8: "8",
        _9: "9",
        _10: "10",
        _11: "11",
        _12: "12",
        _13_FINEST: "13 (Finest)",
    }


class DisplayLevelEnumField(
    EnumField[DisplayLevelEnumAttrOperator, DisplayLevelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayLevelEnumAttrOperator
    PLUG_CLS = DisplayLevelEnumPlugOperator


class DisplayFilterEnumPlugOperator(
    EnumPlugOperator["DisplayFilterEnumAttrOperator"]
):
    __slots__ = ()

    ALL = 0
    EDITED = 1


class DisplayFilterEnumAttrOperator(
    EnumAttrOperator[DisplayFilterEnumPlugOperator]
):
    __slots__ = ()

    ALL = 0
    EDITED = 1

    NAME_MAP = {
        ALL: "All",
        EDITED: "Edited",
    }


class DisplayFilterEnumField(
    EnumField[DisplayFilterEnumAttrOperator, DisplayFilterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayFilterEnumAttrOperator
    PLUG_CLS = DisplayFilterEnumPlugOperator


class ScalingHierarchyEnumPlugOperator(
    EnumPlugOperator["ScalingHierarchyEnumAttrOperator"]
):
    __slots__ = ()

    PROPAGATE = 0
    IGNORE = 1


class ScalingHierarchyEnumAttrOperator(
    EnumAttrOperator[ScalingHierarchyEnumPlugOperator]
):
    __slots__ = ()

    PROPAGATE = 0
    IGNORE = 1

    NAME_MAP = {
        PROPAGATE: "Propagate",
        IGNORE: "Ignore",
    }


class ScalingHierarchyEnumField(
    EnumField[
        ScalingHierarchyEnumAttrOperator, ScalingHierarchyEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ScalingHierarchyEnumAttrOperator
    PLUG_CLS = ScalingHierarchyEnumPlugOperator


class GeneratedSubdiv(Shape):
    __slots__ = ()

    NODE_TYPE = "subdiv"

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

    create_ = TypedField(long_name="create", short_name="cr")
    cr = create_

    cached = TypedField()
    cc = cached

    dispVertices = BoolField(default_value=False)
    dv = dispVertices

    dispVerticesAsLimitPoints = BoolField(default_value=False)
    dvl = dispVerticesAsLimitPoints

    localizeLimitPointsEdit = BoolField(default_value=False)
    llp = localizeLimitPointsEdit

    dispEdges = BoolField(default_value=False)
    de = dispEdges

    dispFaces = BoolField(default_value=False)
    df = dispFaces

    dispMaps = BoolField(default_value=False)
    dm = dispMaps

    dispUVBorder = BoolField(default_value=False)
    db = dispUVBorder

    dispCreases = BoolField(default_value=False)
    dcr = dispCreases

    dispGeometry = BoolField(default_value=True)
    dg = dispGeometry

    dispResolution = LongField(
        default_value=1,
        min_value=0,
        max_value=3,
        soft_min_value=0,
        soft_max_value=3,
    )
    dr = dispResolution

    vertex = VertexField(multi=True)
    vt = vertex

    vertexTweak = VertexTweakField(multi=True)
    vtw = vertexTweak

    outSubdiv = TypedField(writable=False)
    o = outSubdiv

    worldSubdiv = TypedField(multi=True, writable=False)
    ws = worldSubdiv

    edgeCrease = TypedField()
    ecr = edgeCrease

    textureCoord = TypedField()
    uvs = textureCoord

    faceUVIds = TypedField(multi=True)
    fuv = faceUVIds

    normalsDisplayScale = DoubleField(
        default_value=1.0, soft_min_value=0.01, soft_max_value=10.0
    )
    ndf = normalsDisplayScale

    format = FormatEnumField(default_value=1)
    f = format

    depth = LongField(
        default_value=2,
        min_value=0,
        max_value=7,
        soft_min_value=0,
        soft_max_value=5,
    )
    d = depth

    sampleCount = LongField(
        default_value=4,
        min_value=1,
        max_value=50,
        soft_min_value=1,
        soft_max_value=5,
    )
    sc = sampleCount

    displayLevel = DisplayLevelEnumField(default_value=0)
    dl = displayLevel

    displayFilter = DisplayFilterEnumField(default_value=0)
    dfl = displayFilter

    baseFaceCount = LongField(default_value=0, writable=False)
    bfc = baseFaceCount

    levelOneFaceCount = LongField(default_value=0, writable=False)
    ofc = levelOneFaceCount

    scalingHierarchy = ScalingHierarchyEnumField(default_value=1)
    sh = scalingHierarchy
