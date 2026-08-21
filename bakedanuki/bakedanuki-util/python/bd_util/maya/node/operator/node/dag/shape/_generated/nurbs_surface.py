# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.nurbs_surface import (
    BoundingBoxScaleField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    DegreeUVField,
    MinMaxRangeUField,
    MinMaxRangeVField,
    SpansUVField,
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
from .....attr.define.std.at.scalar.numeric.range.byte import ByteField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField
from .....attr.define.std.dt.string import DataStringField


class ModeUEnumPlugOperator(EnumPlugOperator["ModeUEnumAttrOperator"]):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3
    BEST_GUESS_BASED_ON_SCREEN_SIZE = 4


class ModeUEnumAttrOperator(EnumAttrOperator[ModeUEnumPlugOperator]):
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


class ModeUEnumField(EnumField[ModeUEnumAttrOperator, ModeUEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeUEnumAttrOperator
    PLUG_CLS = ModeUEnumPlugOperator


class ModeVEnumPlugOperator(EnumPlugOperator["ModeVEnumAttrOperator"]):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3
    BEST_GUESS_BASED_ON_SCREEN_SIZE = 4


class ModeVEnumAttrOperator(EnumAttrOperator[ModeVEnumPlugOperator]):
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


class ModeVEnumField(EnumField[ModeVEnumAttrOperator, ModeVEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeVEnumAttrOperator
    PLUG_CLS = ModeVEnumPlugOperator


class FormUEnumPlugOperator(EnumPlugOperator["FormUEnumAttrOperator"]):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2


class FormUEnumAttrOperator(EnumAttrOperator[FormUEnumPlugOperator]):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2

    NAME_MAP = {
        OPEN: "Open",
        CLOSED: "Closed",
        PERIODIC: "Periodic",
    }


class FormUEnumField(EnumField[FormUEnumAttrOperator, FormUEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = FormUEnumAttrOperator
    PLUG_CLS = FormUEnumPlugOperator


class FormVEnumPlugOperator(EnumPlugOperator["FormVEnumAttrOperator"]):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2


class FormVEnumAttrOperator(EnumAttrOperator[FormVEnumPlugOperator]):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2

    NAME_MAP = {
        OPEN: "Open",
        CLOSED: "Closed",
        PERIODIC: "Periodic",
    }


class FormVEnumField(EnumField[FormVEnumAttrOperator, FormVEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = FormVEnumAttrOperator
    PLUG_CLS = FormVEnumPlugOperator


class CurvatureToleranceEnumPlugOperator(
    EnumPlugOperator["CurvatureToleranceEnumAttrOperator"]
):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3
    NO_CURVATURE_CHECK = 4


class CurvatureToleranceEnumAttrOperator(
    EnumAttrOperator[CurvatureToleranceEnumPlugOperator]
):
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
    EnumField[
        CurvatureToleranceEnumAttrOperator, CurvatureToleranceEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CurvatureToleranceEnumAttrOperator
    PLUG_CLS = CurvatureToleranceEnumPlugOperator


class BasicTessellationTypeEnumPlugOperator(
    EnumPlugOperator["BasicTessellationTypeEnumAttrOperator"]
):
    __slots__ = ()

    OBJECT = 0
    SCREEN = 1


class BasicTessellationTypeEnumAttrOperator(
    EnumAttrOperator[BasicTessellationTypeEnumPlugOperator]
):
    __slots__ = ()

    OBJECT = 0
    SCREEN = 1

    NAME_MAP = {
        OBJECT: "Object",
        SCREEN: "Screen",
    }


class BasicTessellationTypeEnumField(
    EnumField[
        BasicTessellationTypeEnumAttrOperator,
        BasicTessellationTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = BasicTessellationTypeEnumAttrOperator
    PLUG_CLS = BasicTessellationTypeEnumPlugOperator


class AiSubdivTypeEnumPlugOperator(
    EnumPlugOperator["AiSubdivTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    CATCLARK = 1
    LINEAR = 2


class AiSubdivTypeEnumAttrOperator(
    EnumAttrOperator[AiSubdivTypeEnumPlugOperator]
):
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


class AiSubdivAdaptiveMetricEnumPlugOperator(
    EnumPlugOperator["AiSubdivAdaptiveMetricEnumAttrOperator"]
):
    __slots__ = ()

    AUTO = 0
    EDGE_LENGTH = 1
    FLATNESS = 2


class AiSubdivAdaptiveMetricEnumAttrOperator(
    EnumAttrOperator[AiSubdivAdaptiveMetricEnumPlugOperator]
):
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
    EnumField[
        AiSubdivAdaptiveMetricEnumAttrOperator,
        AiSubdivAdaptiveMetricEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivAdaptiveMetricEnumAttrOperator
    PLUG_CLS = AiSubdivAdaptiveMetricEnumPlugOperator


class AiSubdivAdaptiveSpaceEnumPlugOperator(
    EnumPlugOperator["AiSubdivAdaptiveSpaceEnumAttrOperator"]
):
    __slots__ = ()

    RASTER = 0
    OBJECT = 1


class AiSubdivAdaptiveSpaceEnumAttrOperator(
    EnumAttrOperator[AiSubdivAdaptiveSpaceEnumPlugOperator]
):
    __slots__ = ()

    RASTER = 0
    OBJECT = 1

    NAME_MAP = {
        RASTER: "raster",
        OBJECT: "object",
    }


class AiSubdivAdaptiveSpaceEnumField(
    EnumField[
        AiSubdivAdaptiveSpaceEnumAttrOperator,
        AiSubdivAdaptiveSpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivAdaptiveSpaceEnumAttrOperator
    PLUG_CLS = AiSubdivAdaptiveSpaceEnumPlugOperator


class AiSubdivUvSmoothingEnumPlugOperator(
    EnumPlugOperator["AiSubdivUvSmoothingEnumAttrOperator"]
):
    __slots__ = ()

    PIN_CORNERS = 0
    PIN_BORDERS = 1
    LINEAR = 2
    SMOOTH = 3


class AiSubdivUvSmoothingEnumAttrOperator(
    EnumAttrOperator[AiSubdivUvSmoothingEnumPlugOperator]
):
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
    EnumField[
        AiSubdivUvSmoothingEnumAttrOperator,
        AiSubdivUvSmoothingEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivUvSmoothingEnumAttrOperator
    PLUG_CLS = AiSubdivUvSmoothingEnumPlugOperator


class AiMotionVectorUnitEnumPlugOperator(
    EnumPlugOperator["AiMotionVectorUnitEnumAttrOperator"]
):
    __slots__ = ()

    PER_FRAME = 0
    PER_SECOND = 1


class AiMotionVectorUnitEnumAttrOperator(
    EnumAttrOperator[AiMotionVectorUnitEnumPlugOperator]
):
    __slots__ = ()

    PER_FRAME = 0
    PER_SECOND = 1

    NAME_MAP = {
        PER_FRAME: "Per Frame",
        PER_SECOND: "Per Second",
    }


class AiMotionVectorUnitEnumField(
    EnumField[
        AiMotionVectorUnitEnumAttrOperator, AiMotionVectorUnitEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiMotionVectorUnitEnumAttrOperator
    PLUG_CLS = AiMotionVectorUnitEnumPlugOperator


class GeneratedNurbsSurface(Shape):
    __slots__ = ()

    NODE_TYPE = "nurbsSurface"

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

    curvePrecisionShaded = ByteField(
        default_value=1, min_value=0, max_value=63
    )
    cps = curvePrecisionShaded

    simplifyMode = ByteField(default_value=0, min_value=0, max_value=1)
    sm = simplifyMode

    simplifyU = ByteField(default_value=1, min_value=1, max_value=24)
    smu = simplifyU

    simplifyV = ByteField(default_value=1, min_value=1, max_value=24)
    smv = simplifyV

    smoothEdge = BoolField(default_value=False)
    ues = smoothEdge

    smoothEdgeRatio = DoubleField(
        default_value=0.99, min_value=0.1, max_value=0.999, soft_min_value=0.95
    )
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

    chordHeight = DoubleField(
        default_value=0.1, min_value=0.001, soft_max_value=0.2
    )
    ch = chordHeight

    chordHeightRatio = DoubleField(
        default_value=0.983, min_value=0.1, max_value=0.999, soft_min_value=0.9
    )
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

    gridDivisionPerSpanU = ShortField(
        default_value=4, min_value=1, max_value=15
    )
    gdsu = gridDivisionPerSpanU

    gridDivisionPerSpanV = ShortField(
        default_value=4, min_value=1, max_value=15
    )
    gdsv = gridDivisionPerSpanV

    explicitTessellationAttributes = BoolField(default_value=False)
    eta = explicitTessellationAttributes

    uDivisionsFactor = DoubleField(
        default_value=1.5, min_value=0.1, soft_max_value=5.0
    )
    nufa = uDivisionsFactor

    vDivisionsFactor = DoubleField(
        default_value=1.5, min_value=0.1, soft_max_value=5.0
    )
    nvfa = vDivisionsFactor

    curvatureTolerance = CurvatureToleranceEnumField(default_value=2)
    cvto = curvatureTolerance

    basicTessellationType = BasicTessellationTypeEnumField(default_value=0)
    btt = basicTessellationType

    dispSF = BoolField(default_value=False)
    dsf = dispSF

    normalsDisplayScale = DoubleField(
        default_value=1.0, soft_min_value=0.01, soft_max_value=10.0
    )
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

    aiSubdivType = AiSubdivTypeEnumField(default_value=0, category="arnold")
    ai_subdiv_type = aiSubdivType

    aiSubdivIterations = ByteField(
        default_value=1,
        min_value=0,
        max_value=100,
        soft_min_value=0,
        soft_max_value=10,
        category="arnold",
    )
    ai_subdiv_iterations = aiSubdivIterations

    aiSubdivAdaptiveMetric = AiSubdivAdaptiveMetricEnumField(
        default_value=0, category="arnold"
    )
    ai_subdiv_adaptive_metric = aiSubdivAdaptiveMetric

    aiSubdivPixelError = FloatField(
        default_value=0.0,
        min_value=0.0,
        soft_max_value=10.0,
        category="arnold",
    )
    ai_subdiv_adaptive_error = aiSubdivPixelError

    aiSubdivAdaptiveSpace = AiSubdivAdaptiveSpaceEnumField(
        default_value=0, category="arnold"
    )
    ai_subdiv_adaptive_space = aiSubdivAdaptiveSpace

    aiSubdivUvSmoothing = AiSubdivUvSmoothingEnumField(
        default_value=0, category="arnold"
    )
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

    aiAutobumpVisibility = ByteField(
        default_value=1, min_value=0, max_value=255, category="arnold"
    )
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

    aiStepSize = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_step_size = aiStepSize

    aiVolumePadding = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_volume_padding = aiVolumePadding

    aiMotionVectorSource = DataStringField(category="arnold")
    ai_motion_vector_source = aiMotionVectorSource

    aiMotionVectorUnit = AiMotionVectorUnitEnumField(
        default_value=0, category="arnold"
    )
    ai_motion_vector_unit = aiMotionVectorUnit

    aiMotionVectorScale = FloatField(
        default_value=1.0,
        soft_min_value=0.0,
        soft_max_value=2.0,
        category="arnold",
    )
    ai_motion_vector_scale = aiMotionVectorScale
