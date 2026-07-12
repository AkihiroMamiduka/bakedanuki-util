# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.point_light import (
    BoundingBoxField,
    CenterField,
    ColorField,
    DrawOverrideField,
    FarPointWorldField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    LightDataField,
    ObjectColorRGBField,
    OpticalFXvisibilityField,
    OutlinerColorField,
    PointCameraField,
    PointWorldField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    ShadowColorField,
    UvCoordField,
    UvFilterSizeField,
    WireColorRGBField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.char import CharField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2

    NAME_MAP = {
        FLAT: "Flat",
        USE_TEMPLATE: "Use Template",
        GROUP_BY_NODE: "Group By Node",
    }


class ViewModeEnumField(
    EnumField[ViewModeEnumAttrOperator, ViewModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewModeEnumAttrOperator
    PLUG_CLS = ViewModeEnumPlugOperator


class UiTreatmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000

    NAME_MAP = {
        STANDARD: "Standard",
        SHADER: "Shader",
        CUSTOM: "Custom",
    }


class UiTreatmentEnumField(
    EnumField[UiTreatmentEnumAttrOperator, UiTreatmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UiTreatmentEnumAttrOperator
    PLUG_CLS = UiTreatmentEnumPlugOperator


class UseObjectColorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2

    NAME_MAP = {
        DEFAULT: "Default",
        INDEXED: "Indexed",
        RGB: "RGB",
    }


class UseObjectColorEnumField(
    EnumField[UseObjectColorEnumAttrOperator, UseObjectColorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseObjectColorEnumAttrOperator
    PLUG_CLS = UseObjectColorEnumPlugOperator


class GhostingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5

    NAME_MAP = {
        PRE_AND_POST_FRAMES: "Pre And Post Frames",
        PRE_FRAMES: "Pre Frames",
        POST_FRAMES: "Post Frames",
        CUSTOM_FRAMES: "Custom Frames",
        PRE_AND_POST_KEYFRAMES: "Pre And Post Keyframes",
        ALL_KEYFRAMES: "All Keyframes",
    }


class GhostingModeEnumField(
    EnumField[GhostingModeEnumAttrOperator, GhostingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostingModeEnumAttrOperator
    PLUG_CLS = GhostingModeEnumPlugOperator


class DecayRateEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_DECAY = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3


class DecayRateEnumAttrOperator(EnumAttrOperator):
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


class FogTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    LINEAR = 1
    EXPONENTIAL = 2


class FogTypeEnumAttrOperator(EnumAttrOperator):
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


class PointLight(Shape):
    __slots__ = ()

    NODE_TYPE = "pointLight"

    hyperLayout = MessageField()
    hl = hyperLayout

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    blackBox = BoolField(default_value=False)
    bbx = blackBox

    borderConnections = MessageField(multi=True)
    boc = borderConnections

    isHierarchicalConnection = BoolField(multi=True, default_value=False)
    ish = isHierarchicalConnection

    publishedNodeInfo = PublishedNodeInfoField(multi=True)
    pni = publishedNodeInfo

    rmbCommand = DataStringField()
    rmc = rmbCommand

    templateName = DataStringField()
    tna = templateName

    templatePath = DataStringField()
    tpt = templatePath

    viewName = DataStringField()
    vwn = viewName

    iconName = DataStringField()
    icn = iconName

    viewMode = ViewModeEnumField(default_value=2)
    vwm = viewMode

    templateVersion = LongField(default_value=0)
    tpv = templateVersion

    uiTreatment = UiTreatmentEnumField(default_value=0)
    uit = uiTreatment

    customTreatment = DataStringField()
    ctrt = customTreatment

    creator = DataStringField()
    ctor = creator

    creationDate = DataStringField()
    cdat = creationDate

    containerType = DataStringField()
    ctyp = containerType

    boundingBox = BoundingBoxField(writable=False)
    bb = boundingBox
    boundingBoxMin = boundingBox.boundingBoxMin
    bbmn = boundingBoxMin
    boundingBoxMax = boundingBox.boundingBoxMax
    bbmx = boundingBoxMax
    boundingBoxSize = boundingBox.boundingBoxSize
    bbsi = boundingBoxSize

    center = CenterField(default_value=(0.0, 0.0, 0.0), writable=False)
    c = center
    boundingBoxCenterX = center.boundingBoxCenterX
    bcx = boundingBoxCenterX
    boundingBoxCenterY = center.boundingBoxCenterY
    bcy = boundingBoxCenterY
    boundingBoxCenterZ = center.boundingBoxCenterZ
    bcz = boundingBoxCenterZ

    matrix = DataMatrixField(writable=False)
    m = matrix

    inverseMatrix = DataMatrixField(writable=False)
    im = inverseMatrix

    worldMatrix = DataMatrixField(multi=True, writable=False)
    wm = worldMatrix

    worldInverseMatrix = DataMatrixField(multi=True, writable=False)
    wim = worldInverseMatrix

    parentMatrix = DataMatrixField(multi=True, writable=False)
    pm = parentMatrix

    parentInverseMatrix = DataMatrixField(multi=True, writable=False)
    pim = parentInverseMatrix

    visibility = BoolField(default_value=True)
    v = visibility

    intermediateObject = BoolField(default_value=False)
    io = intermediateObject

    template = BoolField(default_value=False)
    tmp = template

    instObjGroups = InstObjGroupsField(multi=True)
    iog = instObjGroups

    objectColorRGB = ObjectColorRGBField(default_value=(0.0, 0.0, 0.0))
    obcc = objectColorRGB
    objectColorR = objectColorRGB.objectColorR
    obcr = objectColorR
    objectColorG = objectColorRGB.objectColorG
    obcg = objectColorG
    objectColorB = objectColorRGB.objectColorB
    obcb = objectColorB

    wireColorRGB = WireColorRGBField(default_value=(0.0, 0.0, 0.0))
    wfcc = wireColorRGB
    wireColorR = wireColorRGB.wireColorR
    wfcr = wireColorR
    wireColorG = wireColorRGB.wireColorG
    wfcg = wireColorG
    wireColorB = wireColorRGB.wireColorB
    wfcb = wireColorB

    useObjectColor = UseObjectColorEnumField(default_value=0)
    uoc = useObjectColor

    objectColor = ShortField(default_value=0, min_value=0, max_value=7)
    oc = objectColor

    drawOverride = DrawOverrideField()
    do = drawOverride
    overrideDisplayType = drawOverride.overrideDisplayType
    ovdt = overrideDisplayType
    overrideLevelOfDetail = drawOverride.overrideLevelOfDetail
    ovlod = overrideLevelOfDetail
    overrideShading = drawOverride.overrideShading
    ovs = overrideShading
    overrideTexturing = drawOverride.overrideTexturing
    ovt = overrideTexturing
    overridePlayback = drawOverride.overridePlayback
    ovp = overridePlayback
    overrideEnabled = drawOverride.overrideEnabled
    ove = overrideEnabled
    overrideVisibility = drawOverride.overrideVisibility
    ovv = overrideVisibility
    hideOnPlayback = drawOverride.hideOnPlayback
    hpb = hideOnPlayback
    overrideRGBColors = drawOverride.overrideRGBColors
    ovrgbf = overrideRGBColors
    overrideColor = drawOverride.overrideColor
    ovc = overrideColor
    overrideColorRGB = drawOverride.overrideColorRGB
    ovrgb = overrideColorRGB
    overrideColorA = drawOverride.overrideColorA
    ovca = overrideColorA

    lodVisibility = BoolField(default_value=True)
    lodv = lodVisibility

    selectionChildHighlighting = BoolField(default_value=True)
    sech = selectionChildHighlighting

    renderInfo = RenderInfoField(default_value=(0.0, 1.0, 0.0))
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    layerRenderable = renderInfo.layerRenderable
    rndr = layerRenderable
    layerOverrideColor = renderInfo.layerOverrideColor
    lovc = layerOverrideColor

    renderLayerInfo = RenderLayerInfoField(multi=True, default_value=(0.0, 1.0, 0.0))
    rlio = renderLayerInfo

    ghosting = BoolField(default_value=False)
    gh = ghosting

    ghostingMode = GhostingModeEnumField(default_value=0)
    gm = ghostingMode

    ghostCustomSteps = GhostCustomStepsField(default_value=(3.0, 3.0, 1.0))
    gcs = ghostCustomSteps
    ghostPreFrames = ghostCustomSteps.ghostPreFrames
    gprf = ghostPreFrames
    ghostPostFrames = ghostCustomSteps.ghostPostFrames
    gpof = ghostPostFrames
    ghostsStep = ghostCustomSteps.ghostsStep
    gstp = ghostsStep

    ghostFrames = TypedField()
    gf = ghostFrames

    ghostOpacityRange = GhostOpacityRangeField(default_value=(0.15000000596046448, 0.5), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(default_value=(0.44699999690055847, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(default_value=(0.878000020980835, 0.6779999732971191, 0.6629999876022339), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gac = ghostColorPost
    ghostColorPostR = ghostColorPost.ghostColorPostR
    gar = ghostColorPostR
    ghostColorPostG = ghostColorPost.ghostColorPostG
    gag = ghostColorPostG
    ghostColorPostB = ghostColorPost.ghostColorPostB
    gab = ghostColorPostB

    ghostDriver = MessageField()
    gdr = ghostDriver

    ghostUseDriver = BoolField(default_value=False)
    gud = ghostUseDriver

    hiddenInOutliner = BoolField(default_value=False)
    hio = hiddenInOutliner

    useOutlinerColor = BoolField(default_value=False)
    uocol = useOutlinerColor

    outlinerColor = OutlinerColorField(default_value=(0.0, 0.0, 0.0))
    oclr = outlinerColor
    outlinerColorR = outlinerColor.outlinerColorR
    oclrr = outlinerColorR
    outlinerColorG = outlinerColor.outlinerColorG
    oclrg = outlinerColorG
    outlinerColorB = outlinerColor.outlinerColorB
    oclrb = outlinerColorB

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    intensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
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

    pointCamera = PointCameraField(default_value=(1.0, 1.0, 1.0), readable=False)
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

    lightData = LightDataField(writable=False)
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

    opticalFXvisibility = OpticalFXvisibilityField(default_value=(1.0, 1.0, 1.0), writable=False)
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

    lightRadius = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
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

    dmapResolution = ShortField(default_value=512, min_value=16, max_value=16384, soft_max_value=8192)
    dr = dmapResolution

    dmapBias = FloatField(default_value=0.0010000000474974513, soft_min_value=1e-05, soft_max_value=1.0)
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

    dmapNearClipPlane = FloatField(default_value=0.0010000000474974513, min_value=1e-05)
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

    fogRadius = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    fr = fogRadius

    lightGlow = MessageField()
    lg = lightGlow

    objectType = CharField(default_value=1, min_value=0, max_value=255, readable=False)
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

    farPointWorld = FarPointWorldField(default_value=(1.0, 1.0, 1.0), readable=False)
    fw = farPointWorld
    farPointWorldX = farPointWorld.farPointWorldX
    fwx = farPointWorldX
    farPointWorldY = farPointWorld.farPointWorldY
    fwy = farPointWorldY
    farPointWorldZ = farPointWorld.farPointWorldZ
    fwz = farPointWorldZ

    fogIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    fin = fogIntensity

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiCastShadows = BoolField(default_value=True, category="arnold")
    ai_cast_shadows = aiCastShadows

    aiShadowDensity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_shadow_density = aiShadowDensity

    aiExposure = FloatField(default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0, category="arnold")
    ai_exposure = aiExposure

    aiSamples = LongField(default_value=1, min_value=0, max_value=100, soft_max_value=10, category="arnold")
    ai_samples = aiSamples

    aiNormalize = BoolField(default_value=True, category="arnold")
    ai_normalize = aiNormalize

    aiFilters = MessageField(multi=True, category="arnold")
    ai_filters = aiFilters

    aiDiffuse = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_diffuse = aiDiffuse

    aiSpecular = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_specular = aiSpecular

    aiSss = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_sss = aiSss

    aiIndirect = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_indirect = aiIndirect

    aiVolume = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_volume = aiVolume

    aiMaxBounces = LongField(default_value=999, category="arnold")
    ai_max_bounces = aiMaxBounces

    aiVolumeSamples = LongField(default_value=2, min_value=0, max_value=100, soft_max_value=10, category="arnold")
    ai_volume_samples = aiVolumeSamples

    aiAov = DataStringField(category="arnold")
    ai_aov = aiAov

    aiUseColorTemperature = BoolField(default_value=False, category="arnold")
    ai_use_color_temperature = aiUseColorTemperature

    aiColorTemperature = FloatField(default_value=6500.0, min_value=0.0, soft_min_value=1000.0, soft_max_value=15000.0, category="arnold")
    ai_color_temperature = aiColorTemperature

    aiCastVolumetricShadows = BoolField(default_value=True, category="arnold")
    ai_cast_volumetric_shadows = aiCastVolumetricShadows

    aiRadius = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0, category="arnold")
    ai_radius = aiRadius

    aiCamera = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_camera = aiCamera

    aiTransmission = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_transmission = aiTransmission
