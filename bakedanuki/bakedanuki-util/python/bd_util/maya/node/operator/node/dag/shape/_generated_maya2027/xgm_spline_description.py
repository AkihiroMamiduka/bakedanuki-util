# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr_maya2027.xgm_spline_description import (
    BoundingBoxScaleField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    HighlightPlacedColorField,
    PreSelHighlightColorField,
    SelectionHighlightColorField,
    ShowFrozenColorField,
    UvPivotField,
    UvSetField,
    WidthRampField,
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


class AiModeEnumPlugOperator(EnumPlugOperator["AiModeEnumAttrOperator"]):
    __slots__ = ()

    RIBBON = 0
    THICK = 1


class AiModeEnumAttrOperator(EnumAttrOperator[AiModeEnumPlugOperator]):
    __slots__ = ()

    RIBBON = 0
    THICK = 1

    NAME_MAP = {
        RIBBON: "Ribbon",
        THICK: "Thick",
    }


class AiModeEnumField(
    EnumField[AiModeEnumAttrOperator, AiModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiModeEnumAttrOperator
    PLUG_CLS = AiModeEnumPlugOperator


class GeneratedXgmSplineDescription(Shape):
    __slots__ = ()

    NODE_TYPE = "xgmSplineDescription"

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

    width = FloatField(
        default_value=0.10000000149011612,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    w = width

    widthTaper = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wdt = widthTaper

    widthTaperStart = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    wdts = widthTaperStart

    widthRamp = WidthRampField(multi=True, default_value=(0.0, 0.0, 1))
    wdr = widthRamp

    tubeShade = BoolField(default_value=False)
    ts = tubeShade

    faceCamera = BoolField(default_value=True)
    fca = faceCamera

    overallColorIntensity = FloatField(default_value=0.5)
    oci = overallColorIntensity

    falseColor = BoolField(default_value=False)
    fc = falseColor

    falseColorCurve = DataStringField()
    fcc = falseColorCurve

    preSelHighlight = BoolField(default_value=False)
    psh = preSelHighlight

    preSelHighlightColor = PreSelHighlightColorField(
        default_value=(0.44999998807907104, 1.0, 0.44999998807907104)
    )
    psc = preSelHighlightColor
    preSelHighlightColorR = preSelHighlightColor.preSelHighlightColorR
    pscr = preSelHighlightColorR
    preSelHighlightColorG = preSelHighlightColor.preSelHighlightColorG
    pscg = preSelHighlightColorG
    preSelHighlightColorB = preSelHighlightColor.preSelHighlightColorB
    pscb = preSelHighlightColorB

    selectionHighlight = BoolField(default_value=True)
    slh = selectionHighlight

    selectionHighlightColor = SelectionHighlightColorField(
        default_value=(1.0, 1.0, 0.0)
    )
    slc = selectionHighlightColor
    selectionHighlightColorR = selectionHighlightColor.selectionHighlightColorR
    slcr = selectionHighlightColorR
    selectionHighlightColorG = selectionHighlightColor.selectionHighlightColorG
    slcg = selectionHighlightColorG
    selectionHighlightColorB = selectionHighlightColor.selectionHighlightColorB
    slcb = selectionHighlightColorB

    showFrozen = BoolField(default_value=True)
    sfz = showFrozen

    showFrozenColor = ShowFrozenColorField(
        default_value=(0.0, 0.44999998807907104, 0.8999999761581421)
    )
    sfc = showFrozenColor
    showFrozenColorR = showFrozenColor.showFrozenColorR
    sfcr = showFrozenColorR
    showFrozenColorG = showFrozenColor.showFrozenColorG
    sfcg = showFrozenColorG
    showFrozenColorB = showFrozenColor.showFrozenColorB
    sfcb = showFrozenColorB

    highlightPlaced = BoolField(default_value=False)
    hp = highlightPlaced

    highlightPlacedColor = HighlightPlacedColorField(
        default_value=(0.0, 0.3176470696926117, 0.09019608050584793)
    )
    hpc = highlightPlacedColor
    highlightPlacedColorR = highlightPlacedColor.highlightPlacedColorR
    hpcr = highlightPlacedColorR
    highlightPlacedColorG = highlightPlacedColor.highlightPlacedColorG
    hpcg = highlightPlacedColorG
    highlightPlacedColorB = highlightPlacedColor.highlightPlacedColorB
    hpcb = highlightPlacedColorB

    highlightPlacedIntensity = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hpi = highlightPlacedIntensity

    showCVs = BoolField(default_value=False)
    scv = showCVs

    showCVsSize = FloatField(
        default_value=3.0, min_value=1.0, max_value=30.0, soft_max_value=10.0
    )
    scvs = showCVsSize

    showCVsOpacity = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    scvo = showCVsOpacity

    showMeshVoxels = BoolField(default_value=False)
    smv = showMeshVoxels

    activeSculpt = MessageField()
    as_ = activeSculpt

    renderDensityMultiplier = FloatField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.001,
        soft_max_value=100.0,
    )
    rdm = renderDensityMultiplier

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outRenderData = TypedField()
    ord = outRenderData

    outSplineData = TypedField()
    osd = outSplineData

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

    aiMinPixelWidth = FloatField(default_value=0.0, category="arnold")
    ai_min_pixel_width = aiMinPixelWidth

    aiMode = AiModeEnumField(default_value=0, category="arnold")
    ai_mode = aiMode
