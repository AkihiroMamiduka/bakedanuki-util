# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.point_light import (
    ColorField,
    FarPointWorldField,
    LightDataValueField,
    OpticalFXvisibilityField,
    PointCameraField,
    PointWorldField,
    ShadowColorField,
    UvCoordField,
    UvFilterSizeField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.addr import AddrField
from .....attr.define.std.at.flt_matrix import FltMatrixField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.char import CharField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.dt.string import DataStringField


class DecayRateEnumPlugOperator(EnumPlugOperator["DecayRateEnumAttrOperator"]):
    __slots__ = ()

    NO_DECAY = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3


class DecayRateEnumAttrOperator(EnumAttrOperator[DecayRateEnumPlugOperator]):
    __slots__ = ()

    NO_DECAY = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3

    NAME_MAP = {
        NO_DECAY: "No Decay",
        LINEAR: "Linear",
        QUADRATIC: "Quadratic",
        CUBIC: "Cubic",
    }


class DecayRateEnumField(
    EnumField[DecayRateEnumAttrOperator, DecayRateEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DecayRateEnumAttrOperator
    PLUG_CLS = DecayRateEnumPlugOperator


class FogTypeEnumPlugOperator(EnumPlugOperator["FogTypeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 0
    LINEAR = 1
    EXPONENTIAL = 2


class FogTypeEnumAttrOperator(EnumAttrOperator[FogTypeEnumPlugOperator]):
    __slots__ = ()

    NORMAL = 0
    LINEAR = 1
    EXPONENTIAL = 2

    NAME_MAP = {
        NORMAL: "Normal",
        LINEAR: "Linear",
        EXPONENTIAL: "Exponential",
    }


class FogTypeEnumField(
    EnumField[FogTypeEnumAttrOperator, FogTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogTypeEnumAttrOperator
    PLUG_CLS = FogTypeEnumPlugOperator


class GeneratedPointLight(Shape):
    __slots__ = ()

    NODE_TYPE = "pointLight"

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    intensity = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    in_ = intensity

    useRayTraceShadows = BoolField(default_value=True)
    urs = useRayTraceShadows

    shadowColor = ShadowColorField(default_value=(0.0, 0.0, 0.0))
    sc = shadowColor
    shadColorR = shadowColor.shadColorR
    scr = shadColorR
    shadColorG = shadowColor.shadColorG
    scg = shadColorG
    shadColorB = shadowColor.shadColorB
    scb = shadColorB

    shadowRays = ShortField(default_value=1, min_value=1, soft_max_value=40)
    shr = shadowRays

    rayDepthLimit = ShortField(default_value=3, min_value=0, soft_max_value=10)
    rdl = rayDepthLimit

    centerOfIllumination = DoubleField(default_value=5.0, min_value=1e-10)
    col = centerOfIllumination

    pointCamera = PointCameraField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    matrixWorldToEye = FltMatrixField(readable=False)
    wte = matrixWorldToEye

    matrixEyeToWorld = FltMatrixField(readable=False)
    etw = matrixEyeToWorld

    objectId = AddrField(default_value=0.0, readable=False)
    oi = objectId

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    raySampler = AddrField(default_value=0.0, readable=False)
    rts = raySampler

    rayDepth = ShortField(default_value=0, readable=False)
    rd = rayDepth

    renderState = LongField(default_value=0, readable=False)
    rdst = renderState

    locatorScale = DoubleField(default_value=1.0, min_value=1e-10)
    lls = locatorScale

    uvCoord = UvCoordField(default_value=(0.0, 0.0), writable=False)
    uv = uvCoord
    uCoord = uvCoord.uCoord
    uu = uCoord
    vCoord = uvCoord.vCoord
    vv = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0), writable=False)
    fq = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    infoBits = LongField(default_value=0)
    ib = infoBits

    lightData = LightDataValueField(writable=False)
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
    lbl = lightBlindData

    opticalFXvisibility = OpticalFXvisibilityField(
        default_value=(1.0, 1.0, 1.0), writable=False
    )
    ov = opticalFXvisibility
    opticalFXvisibilityR = opticalFXvisibility.opticalFXvisibilityR
    ovr = opticalFXvisibilityR
    opticalFXvisibilityG = opticalFXvisibility.opticalFXvisibilityG
    ovg = opticalFXvisibilityG
    opticalFXvisibilityB = opticalFXvisibility.opticalFXvisibilityB
    ovb = opticalFXvisibilityB

    rayInstance = LongField(default_value=0, readable=False)
    ryi = rayInstance

    decayRate = DecayRateEnumField(default_value=0)
    de = decayRate

    emitDiffuse = BoolField(default_value=True)
    edi = emitDiffuse

    emitSpecular = BoolField(default_value=True)
    esp = emitSpecular

    lightRadius = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    lr = lightRadius

    castSoftShadows = BoolField(default_value=False)
    cw = castSoftShadows

    useDepthMapShadows = BoolField(default_value=False)
    dms = useDepthMapShadows

    reuseDmap = BoolField(default_value=False)
    du = reuseDmap

    useMidDistDmap = BoolField(default_value=True)
    md = useMidDistDmap

    dmapFilterSize = ShortField(default_value=1, min_value=1, soft_max_value=6)
    fs = dmapFilterSize

    dmapResolution = ShortField(
        default_value=512, min_value=16, max_value=16384, soft_max_value=8192
    )
    dr = dmapResolution

    dmapBias = FloatField(
        default_value=0.0010000000474974513,
        soft_min_value=1e-05,
        soft_max_value=1.0,
    )
    db = dmapBias

    dmapFocus = FloatField(default_value=90.0, min_value=0.0, max_value=360.0)
    df = dmapFocus

    dmapWidthFocus = FloatField(default_value=100.0)
    dw = dmapWidthFocus

    useDmapAutoFocus = BoolField(default_value=True)
    af = useDmapAutoFocus

    volumeShadowSamples = ShortField(default_value=20, min_value=1)
    nv = volumeShadowSamples

    fogShadowIntensity = ShortField(default_value=1, min_value=1, max_value=10)
    fsi = fogShadowIntensity

    useDmapAutoClipping = BoolField(default_value=True)
    uc = useDmapAutoClipping

    dmapNearClipPlane = FloatField(
        default_value=0.0010000000474974513, min_value=1e-05
    )
    nc = dmapNearClipPlane

    dmapFarClipPlane = FloatField(default_value=10000.0)
    fcp = dmapFarClipPlane

    useOnlySingleDmap = BoolField(default_value=True)
    us = useOnlySingleDmap

    useXPlusDmap = BoolField(default_value=True)
    xp = useXPlusDmap

    useXMinusDmap = BoolField(default_value=True)
    xn = useXMinusDmap

    useYPlusDmap = BoolField(default_value=True)
    yp = useYPlusDmap

    useYMinusDmap = BoolField(default_value=True)
    yn = useYMinusDmap

    useZPlusDmap = BoolField(default_value=True)
    zp = useZPlusDmap

    useZMinusDmap = BoolField(default_value=True)
    zn = useZMinusDmap

    dmapUseMacro = DataStringField()
    dc = dmapUseMacro

    dmapName = DataStringField()
    smn = dmapName

    dmapLightName = BoolField(default_value=True)
    ul = dmapLightName

    dmapSceneName = BoolField(default_value=False)
    um = dmapSceneName

    dmapFrameExt = BoolField(default_value=False)
    uf = dmapFrameExt

    writeDmap = BoolField(default_value=False)
    ws = writeDmap

    lastWrittenDmapAnimExtName = DataStringField()
    lw = lastWrittenDmapAnimExtName

    receiveShadows = BoolField(default_value=True)
    gs = receiveShadows

    fogGeometry = MessageField()
    fg = fogGeometry

    fogRadius = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    fr = fogRadius

    lightGlow = MessageField()
    lg = lightGlow

    objectType = CharField(
        default_value=1, min_value=0, max_value=255, readable=False
    )
    ot = objectType

    fogType = FogTypeEnumField(default_value=0)
    ft = fogType

    pointWorld = PointWorldField(default_value=(1.0, 1.0, 1.0), readable=False)
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    tx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    ty = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    tz = pointWorldZ

    farPointWorld = FarPointWorldField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
    fw = farPointWorld
    farPointWorldX = farPointWorld.farPointWorldX
    fwx = farPointWorldX
    farPointWorldY = farPointWorld.farPointWorldY
    fwy = farPointWorldY
    farPointWorldZ = farPointWorld.farPointWorldZ
    fwz = farPointWorldZ

    fogIntensity = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    fin = fogIntensity

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

    aiRadius = FloatField(
        default_value=0.0,
        min_value=0.0,
        soft_max_value=10.0,
        category="arnold",
    )
    ai_radius = aiRadius

    aiCamera = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_camera = aiCamera

    aiTransmission = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_transmission = aiTransmission
