# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.shading_engine import (
    AiCustomAOVsField,
    AiSurfaceShaderField,
    AiVolumeShaderField,
    BogusAttributeField,
    ChannelSetColorField,
    DefaultShadowsField,
    IgnoredShadowsField,
    LinkedShadowsField,
    PublishedNodeInfoField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator["ViewModeEnumAttrOperator"]):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator[ViewModeEnumPlugOperator]):
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


class UiTreatmentEnumPlugOperator(EnumPlugOperator["UiTreatmentEnumAttrOperator"]):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator[UiTreatmentEnumPlugOperator]):
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


class GeneratedShadingEngine(DG):
    __slots__ = ()

    NODE_TYPE = "shadingEngine"

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

    dagSetMembers = TypedField(multi=True, readable=False)
    dsm = dagSetMembers

    dnSetMembers = TypedField(multi=True, readable=False)
    dnsm = dnSetMembers

    memberWireframeColor = ShortField(default_value=-1, min_value=-1, max_value=23)
    mwc = memberWireframeColor

    channelSetColor = ChannelSetColorField(default_value=(0.5, 0.5, 0.5))
    cscol = channelSetColor
    channelSetColorR = channelSetColor.channelSetColorR
    cscolr = channelSetColorR
    channelSetColorG = channelSetColor.channelSetColorG
    cscolg = channelSetColorG
    channelSetColorB = channelSetColor.channelSetColorB
    cscolb = channelSetColorB

    channelSetColorIndex = ShortField(default_value=-1)
    csci = channelSetColorIndex

    annotation = DataStringField()
    an = annotation

    isLayer = BoolField(default_value=False)
    il = isLayer

    verticesOnlySet = BoolField(default_value=False)
    vo = verticesOnlySet

    edgesOnlySet = BoolField(default_value=False)
    eo = edgesOnlySet

    facetsOnlySet = BoolField(default_value=False)
    fo = facetsOnlySet

    editPointsOnlySet = BoolField(default_value=False)
    epo = editPointsOnlySet

    renderableOnlySet = BoolField(default_value=False)
    ro = renderableOnlySet

    partition = MessageField()
    pa = partition

    groupNodes = MessageField(multi=True, readable=False)
    gn = groupNodes

    usedBy = MessageField(multi=True)
    ub = usedBy

    hiddenInOutliner = BoolField(default_value=False)
    hio = hiddenInOutliner

    aiOverride = BoolField(default_value=True, category="arnold")
    ai_override = aiOverride

    unsolicited = TypedField(multi=True, readable=False)
    un = unsolicited

    displacementShader = TypedField()
    ds = displacementShader

    imageShader = TypedField()
    is_ = imageShader

    volumeShader = TypedField()
    vs = volumeShader

    surfaceShader = TypedField()
    ss = surfaceShader

    defaultLights = TypedField(readable=False)
    dl = defaultLights

    linkedLights = TypedField(multi=True, readable=False)
    ll = linkedLights

    ignoredLights = TypedField(multi=True, readable=False)
    xl = ignoredLights

    defaultShadows = DefaultShadowsField(readable=False)
    dsl = defaultShadows
    dShadowDirection = defaultShadows.dShadowDirection
    dsd = dShadowDirection
    dShadowIntensity = defaultShadows.dShadowIntensity
    dsi = dShadowIntensity
    dShadowAmbient = defaultShadows.dShadowAmbient
    dsa = dShadowAmbient
    dShadowDiffuse = defaultShadows.dShadowDiffuse
    dsf = dShadowDiffuse
    dShadowSpecular = defaultShadows.dShadowSpecular
    dss = dShadowSpecular
    dShadowShadowFraction = defaultShadows.dShadowShadowFraction
    dssf = dShadowShadowFraction
    dShadowPreShadowIntensity = defaultShadows.dShadowPreShadowIntensity
    dsps = dShadowPreShadowIntensity
    dShadowBlindData = defaultShadows.dShadowBlindData
    dbld = dShadowBlindData

    linkedShadows = LinkedShadowsField(multi=True, readable=False)
    ls = linkedShadows

    lShadowDirectionX = FloatField()
    lsx = lShadowDirectionX

    lShadowDirectionY = FloatField()
    lsy = lShadowDirectionY

    lShadowDirectionZ = FloatField()
    lsz = lShadowDirectionZ

    lShadowIntensityR = FloatField()
    lsr = lShadowIntensityR

    lShadowIntensityG = FloatField()
    lsg = lShadowIntensityG

    lShadowIntensityB = FloatField()
    lsb = lShadowIntensityB

    ignoredShadows = IgnoredShadowsField(multi=True, readable=False)
    xs = ignoredShadows

    xShadowDirectionX = FloatField()
    xsx = xShadowDirectionX

    xShadowDirectionY = FloatField()
    xsy = xShadowDirectionY

    xShadowDirectionZ = FloatField()
    xsz = xShadowDirectionZ

    xShadowIntensityR = FloatField()
    xsr = xShadowIntensityR

    xShadowIntensityG = FloatField()
    xsg = xShadowIntensityG

    xShadowIntensityB = FloatField()
    xsb = xShadowIntensityB

    bogusAttribute = BogusAttributeField(multi=True, readable=False)
    blt = bogusAttribute

    bogusDirectionX = FloatField()
    blx = bogusDirectionX

    bogusDirectionY = FloatField()
    bly = bogusDirectionY

    bogusDirectionZ = FloatField()
    blz = bogusDirectionZ

    bogusIntensityR = FloatField()
    blr = bogusIntensityR

    bogusIntensityG = FloatField()
    blg = bogusIntensityG

    bogusIntensityB = FloatField()
    blb = bogusIntensityB

    aiCustomAOVs = AiCustomAOVsField(multi=True, category="arnold")
    aovs = aiCustomAOVs

    aiSurfaceShader = AiSurfaceShaderField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_surface_shader = aiSurfaceShader
    aiSurfaceShaderR = aiSurfaceShader.aiSurfaceShaderR
    ai_surface_shaderr = aiSurfaceShaderR
    aiSurfaceShaderG = aiSurfaceShader.aiSurfaceShaderG
    ai_surface_shaderg = aiSurfaceShaderG
    aiSurfaceShaderB = aiSurfaceShader.aiSurfaceShaderB
    ai_surface_shaderb = aiSurfaceShaderB

    aiVolumeShader = AiVolumeShaderField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_volume_shader = aiVolumeShader
    aiVolumeShaderR = aiVolumeShader.aiVolumeShaderR
    ai_volume_shaderr = aiVolumeShaderR
    aiVolumeShaderG = aiVolumeShader.aiVolumeShaderG
    ai_volume_shaderg = aiVolumeShaderG
    aiVolumeShaderB = aiVolumeShader.aiVolumeShaderB
    ai_volume_shaderb = aiVolumeShaderB
