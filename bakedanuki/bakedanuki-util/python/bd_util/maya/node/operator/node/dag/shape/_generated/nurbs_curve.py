# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.nurbs_curve import (
    AiCurveShaderField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    EditPointsField,
    MinMaxValueField,
    UvPivotField,
    UvSetField,
    WorldNormalField,
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
from .....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from .....attr.define.std.dt.string import DataStringField


class FormEnumPlugOperator(EnumPlugOperator["FormEnumAttrOperator"]):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2


class FormEnumAttrOperator(EnumAttrOperator[FormEnumPlugOperator]):
    __slots__ = ()

    OPEN = 0
    CLOSED = 1
    PERIODIC = 2

    NAME_MAP = {
        OPEN: "Open",
        CLOSED: "Closed",
        PERIODIC: "Periodic",
    }


class FormEnumField(EnumField[FormEnumAttrOperator, FormEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = FormEnumAttrOperator
    PLUG_CLS = FormEnumPlugOperator


class AiModeEnumPlugOperator(EnumPlugOperator["AiModeEnumAttrOperator"]):
    __slots__ = ()

    RIBBON = 0
    THICK = 1
    ORIENTED = 2


class AiModeEnumAttrOperator(EnumAttrOperator[AiModeEnumPlugOperator]):
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


class GeneratedNurbsCurve(Shape):
    __slots__ = ()

    NODE_TYPE = "nurbsCurve"

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

    header = TypedField()
    hd = header

    create_ = DataNurbsCurveField(long_name="create", short_name="cr")
    cr = create_

    local = DataNurbsCurveField(writable=False)
    l = local

    lineWidth = FloatField(default_value=-1.0)
    ls = lineWidth

    worldSpace = DataNurbsCurveField(multi=True, writable=False)
    ws = worldSpace

    worldNormal = WorldNormalField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    wn = worldNormal

    form = FormEnumField(default_value=0, writable=False)
    f = form

    degree = ShortField(default_value=0, writable=False)
    d = degree

    spans = LongField(default_value=0, writable=False)
    s = spans

    editPoints = EditPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    eps = editPoints

    cached = DataNurbsCurveField()
    cc = cached

    inPlace = BoolField(default_value=False)
    ipo = inPlace

    dispCV = BoolField(default_value=False)
    dcv = dispCV

    dispEP = BoolField(default_value=False)
    dep = dispEP

    dispHull = BoolField(default_value=False)
    dh = dispHull

    dispCurveEndPoints = BoolField(default_value=False)
    dce = dispCurveEndPoints

    dispGeometry = BoolField(default_value=True)
    dg = dispGeometry

    tweakSize = LongField(default_value=-1)
    ts = tweakSize

    minMaxValue = MinMaxValueField(default_value=(0.0, 0.0), writable=False)
    mmv = minMaxValue
    minValue = minMaxValue.minValue
    min = minValue
    maxValue = minMaxValue.maxValue
    max = maxValue

    alwaysDrawOnTop = BoolField(default_value=False)
    adot = alwaysDrawOnTop

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

    aiMinPixelWidth = FloatField(default_value=0.0, category="arnold")
    ai_min_pixel_width = aiMinPixelWidth

    aiMode = AiModeEnumField(default_value=0, category="arnold")
    ai_mode = aiMode

    aiRenderCurve = BoolField(default_value=False, category="arnold")
    rcurve = aiRenderCurve

    aiCurveWidth = FloatField(
        default_value=0.009999999776482582,
        min_value=0.0,
        soft_max_value=1.0,
        category="arnold",
    )
    cwdth = aiCurveWidth

    aiSampleRate = LongField(
        default_value=5, min_value=1, soft_max_value=20, category="arnold"
    )
    srate = aiSampleRate

    aiCurveShader = AiCurveShaderField(
        default_value=(0.0, 0.0, 0.0), category="arnold"
    )
    ai_curve_shader = aiCurveShader
    aiCurveShaderR = aiCurveShader.aiCurveShaderR
    ai_curve_shaderr = aiCurveShaderR
    aiCurveShaderG = aiCurveShader.aiCurveShaderG
    ai_curve_shaderg = aiCurveShaderG
    aiCurveShaderB = aiCurveShader.aiCurveShaderB
    ai_curve_shaderb = aiCurveShaderB

    aiExportRefPoints = BoolField(default_value=True, category="arnold")
    ai_exprpt = aiExportRefPoints
