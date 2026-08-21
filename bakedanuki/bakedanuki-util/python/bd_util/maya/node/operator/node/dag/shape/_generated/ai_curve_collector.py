# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.ai_curve_collector import (
    AiCurveShaderField,
    AiWidthProfileField,
    CompInstObjGroupsField,
    ComponentTagsField,
    LocalPositionField,
    LocalScaleField,
    WorldPositionField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.dt.string import DataStringField


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


class GeneratedAiCurveCollector(Shape):
    __slots__ = ()

    NODE_TYPE = "aiCurveCollector"

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

    worldPosition = WorldPositionField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    wp = worldPosition

    localScale = LocalScaleField(default_value=(1.0, 1.0, 1.0))
    los = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    aiVisibleInDiffuseReflection = BoolField(default_value=True)
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(default_value=True)
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(default_value=True)
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(default_value=True)
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True)
    ai_viv = aiVisibleInVolume

    aiCurveWidth = FloatField(
        default_value=0.009999999776482582,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
        category="arnold",
    )

    aiSampleRate = LongField(
        default_value=5,
        min_value=1,
        soft_min_value=1,
        soft_max_value=20,
        category="arnold",
    )

    aiCurveShader = AiCurveShaderField(default_value=(0.0, 0.0, 0.0))
    aiCurveShaderR = aiCurveShader.aiCurveShaderR
    aiCurveShaderr = aiCurveShaderR
    aiCurveShaderG = aiCurveShader.aiCurveShaderG
    aiCurveShaderg = aiCurveShaderG
    aiCurveShaderB = aiCurveShader.aiCurveShaderB
    aiCurveShaderb = aiCurveShaderB

    aiExportRefPoints = BoolField(default_value=False)

    aiMinPixelWidth = FloatField(default_value=0.0)

    aiMode = AiModeEnumField(default_value=0)

    aiSelfShadows = BoolField(default_value=True)

    aiOpaque = BoolField(default_value=True)

    aiMatte = BoolField(default_value=False)

    aiTraceSets = DataStringField()
    trace_sets = aiTraceSets

    aiSssSetname = DataStringField()
    ai_sss_setname = aiSssSetname

    aiUserOptions = DataStringField()
    user_options = aiUserOptions

    aiWidthProfile = AiWidthProfileField(
        multi=True, default_value=(0.0, 0.0, 1)
    )
    wdthP = aiWidthProfile
