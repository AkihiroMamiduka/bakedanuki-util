# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.ai_sky_dome_light import (
    AiShadowColorField,
    ColorField,
    CompInstObjGroupsField,
    ComponentTagsField,
    LightDataValueField,
    LocalPositionField,
    LocalScaleField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    PointCameraField,
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


class FormatEnumPlugOperator(EnumPlugOperator["FormatEnumAttrOperator"]):
    __slots__ = ()

    MIRRORED_BALL = 0
    ANGULAR = 1
    LATLONG = 2


class FormatEnumAttrOperator(EnumAttrOperator[FormatEnumPlugOperator]):
    __slots__ = ()

    MIRRORED_BALL = 0
    ANGULAR = 1
    LATLONG = 2

    NAME_MAP = {
        MIRRORED_BALL: "mirrored_ball",
        ANGULAR: "angular",
        LATLONG: "latlong",
    }


class FormatEnumField(
    EnumField[FormatEnumAttrOperator, FormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormatEnumAttrOperator
    PLUG_CLS = FormatEnumPlugOperator


class SkyFacingEnumPlugOperator(EnumPlugOperator["SkyFacingEnumAttrOperator"]):
    __slots__ = ()

    FRONT = 0
    BACK = 1
    BOTH = 2


class SkyFacingEnumAttrOperator(EnumAttrOperator[SkyFacingEnumPlugOperator]):
    __slots__ = ()

    FRONT = 0
    BACK = 1
    BOTH = 2

    NAME_MAP = {
        FRONT: "front",
        BACK: "back",
        BOTH: "both",
    }


class SkyFacingEnumField(
    EnumField[SkyFacingEnumAttrOperator, SkyFacingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyFacingEnumAttrOperator
    PLUG_CLS = SkyFacingEnumPlugOperator


class SamplingEnumPlugOperator(EnumPlugOperator["SamplingEnumAttrOperator"]):
    __slots__ = ()

    LOW_64X64 = 0
    MEDIUM_128X128 = 1
    HIGH_256X256 = 2
    HIGHER_512X512 = 3
    ULTRA_1024X1024 = 4


class SamplingEnumAttrOperator(EnumAttrOperator[SamplingEnumPlugOperator]):
    __slots__ = ()

    LOW_64X64 = 0
    MEDIUM_128X128 = 1
    HIGH_256X256 = 2
    HIGHER_512X512 = 3
    ULTRA_1024X1024 = 4

    NAME_MAP = {
        LOW_64X64: "Low (64x64)",
        MEDIUM_128X128: "Medium (128x128)",
        HIGH_256X256: "High (256x256)",
        HIGHER_512X512: "Higher (512x512)",
        ULTRA_1024X1024: "Ultra (1024x1024)",
    }


class SamplingEnumField(
    EnumField[SamplingEnumAttrOperator, SamplingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SamplingEnumAttrOperator
    PLUG_CLS = SamplingEnumPlugOperator


class PortalModeEnumPlugOperator(
    EnumPlugOperator["PortalModeEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    INTERIOR_ONLY = 1
    INTERIOR_EXTERIOR = 2


class PortalModeEnumAttrOperator(EnumAttrOperator[PortalModeEnumPlugOperator]):
    __slots__ = ()

    OFF = 0
    INTERIOR_ONLY = 1
    INTERIOR_EXTERIOR = 2

    NAME_MAP = {
        OFF: "off",
        INTERIOR_ONLY: "interior_only",
        INTERIOR_EXTERIOR: "interior_exterior",
    }


class PortalModeEnumField(
    EnumField[PortalModeEnumAttrOperator, PortalModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PortalModeEnumAttrOperator
    PLUG_CLS = PortalModeEnumPlugOperator


class GeneratedAiSkyDomeLight(Shape):
    __slots__ = ()

    NODE_TYPE = "aiSkyDomeLight"

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

    resolution = LongField(default_value=1000)

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    sc = color
    colorR = color.colorR
    scr = colorR
    colorG = color.colorG
    scg = colorG
    colorB = color.colorB
    scb = colorB

    format = FormatEnumField(default_value=2)
    for_ = format

    skyRadius = FloatField(default_value=1000.0)
    gskrd = skyRadius

    skyFacing = SkyFacingEnumField(default_value=0)
    faci = skyFacing

    sampling = SamplingEnumField(default_value=2)
    spl = sampling

    hwtexalpha = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hwta = hwtexalpha

    intensity = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=10.0
    )

    camera = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    transmission = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )

    portalMode = PortalModeEnumField(default_value=1)
    portal_mode = portalMode

    filters = MessageField(multi=True)

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 0.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocl = outColor
    outColorR = outColor.outColorR
    oclr = outColorR
    outColorG = outColor.outColorG
    oclg = outColorG
    outColorB = outColor.outColorB
    oclb = outColorB

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    lightData = LightDataValueField()
    ltd = lightData
    lightDirection = lightData.lightDirection
    ld = lightDirection
    lightIntensity = lightData.lightIntensity
    li = lightIntensity
    lightAmbient = lightData.lightAmbient
    la = lightAmbient
    lightDiffuse = lightData.lightDiffuse
    ldf = lightDiffuse
    lightSpecular = lightData.lightSpecular
    ls = lightSpecular
    lightShadowFraction = lightData.lightShadowFraction
    lsf = lightShadowFraction
    preShadowIntensity = lightData.preShadowIntensity
    psi = preShadowIntensity
    lightBlindData = lightData.lightBlindData
    lbld = lightBlindData

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiCastShadows = BoolField(default_value=True, category="arnold")
    ai_cast_shadows = aiCastShadows

    aiShadowDensity = FloatField(
        default_value=1.0,
        min_value=0.0,
        max_value=1.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
        category="arnold",
    )
    ai_shadow_density = aiShadowDensity

    aiExposure = FloatField(
        default_value=0.0,
        soft_min_value=-5.0,
        soft_max_value=5.0,
        category="arnold",
    )
    ai_exposure = aiExposure

    aiSamples = LongField(
        default_value=1,
        min_value=0,
        max_value=100,
        soft_max_value=10,
        category="arnold",
    )
    ai_samples = aiSamples

    aiNormalize = BoolField(default_value=True, category="arnold")
    ai_normalize = aiNormalize

    aiFilters = MessageField(multi=True, category="arnold")
    ai_filters = aiFilters

    aiDiffuse = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_diffuse = aiDiffuse

    aiSpecular = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_specular = aiSpecular

    aiSss = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_sss = aiSss

    aiIndirect = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_indirect = aiIndirect

    aiVolume = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_volume = aiVolume

    aiMaxBounces = LongField(default_value=999, category="arnold")
    ai_max_bounces = aiMaxBounces

    aiVolumeSamples = LongField(
        default_value=2,
        min_value=0,
        max_value=100,
        soft_max_value=10,
        category="arnold",
    )
    ai_volume_samples = aiVolumeSamples

    aiAov = DataStringField(category="arnold")
    ai_aov = aiAov

    aiUseColorTemperature = BoolField(default_value=False, category="arnold")
    ai_use_color_temperature = aiUseColorTemperature

    aiColorTemperature = FloatField(
        default_value=6500.0,
        min_value=0.0,
        soft_min_value=1000.0,
        soft_max_value=15000.0,
        category="arnold",
    )
    ai_color_temperature = aiColorTemperature

    aiCastVolumetricShadows = BoolField(default_value=True, category="arnold")
    ai_cast_volumetric_shadows = aiCastVolumetricShadows

    aiShadowColor = AiShadowColorField(
        default_value=(0.0, 0.0, 0.0), category="arnold"
    )
    ai_shadow_color = aiShadowColor
    aiShadowColorR = aiShadowColor.aiShadowColorR
    ai_shadow_colorr = aiShadowColorR
    aiShadowColorG = aiShadowColor.aiShadowColorG
    ai_shadow_colorg = aiShadowColorG
    aiShadowColorB = aiShadowColor.aiShadowColorB
    ai_shadow_colorb = aiShadowColorB

    aiAovIndirect = BoolField(default_value=False, category="arnold")
    ai_aov_indirect = aiAovIndirect
