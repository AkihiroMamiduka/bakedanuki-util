# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shading_engine import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


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


class ShadingEngine(DG):
    __slots__ = ()

    NODE_TYPE = "shadingEngine"

    hyperLayout = MessageField()
    hl = hyperLayout

    isCollapsed = BoolField()
    isc = isCollapsed

    blackBox = BoolField()
    bbx = blackBox

    borderConnections = MessageField(multi=True)
    boc = borderConnections

    isHierarchicalConnection = BoolField(multi=True)
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

    viewMode = ViewModeEnumField()
    vwm = viewMode

    templateVersion = LongField()
    tpv = templateVersion

    uiTreatment = UiTreatmentEnumField()
    uit = uiTreatment

    customTreatment = DataStringField()
    ctrt = customTreatment

    creator = DataStringField()
    ctor = creator

    creationDate = DataStringField()
    cdat = creationDate

    containerType = DataStringField()
    ctyp = containerType

    dagSetMembers = TypedField(multi=True)
    dsm = dagSetMembers

    dnSetMembers = TypedField(multi=True)
    dnsm = dnSetMembers

    memberWireframeColor = ShortField()
    mwc = memberWireframeColor

    channelSetColor = ChannelSetColorField()
    cscol = channelSetColor
    channelSetColorR = channelSetColor.channelSetColorR
    cscolr = channelSetColorR
    channelSetColorG = channelSetColor.channelSetColorG
    cscolg = channelSetColorG
    channelSetColorB = channelSetColor.channelSetColorB
    cscolb = channelSetColorB

    channelSetColorIndex = ShortField()
    csci = channelSetColorIndex

    annotation = DataStringField()
    an = annotation

    isLayer = BoolField()
    il = isLayer

    verticesOnlySet = BoolField()
    vo = verticesOnlySet

    edgesOnlySet = BoolField()
    eo = edgesOnlySet

    facetsOnlySet = BoolField()
    fo = facetsOnlySet

    editPointsOnlySet = BoolField()
    epo = editPointsOnlySet

    renderableOnlySet = BoolField()
    ro = renderableOnlySet

    partition = MessageField()
    pa = partition

    groupNodes = MessageField(multi=True)
    gn = groupNodes

    usedBy = MessageField(multi=True)
    ub = usedBy

    hiddenInOutliner = BoolField()
    hio = hiddenInOutliner

    aiOverride = BoolField()
    ai_override = aiOverride

    unsolicited = TypedField(multi=True)
    un = unsolicited

    displacementShader = TypedField()
    ds = displacementShader

    imageShader = TypedField()
    is_ = imageShader

    volumeShader = TypedField()
    vs = volumeShader

    surfaceShader = TypedField()
    ss = surfaceShader

    defaultLights = TypedField()
    dl = defaultLights

    linkedLights = TypedField(multi=True)
    ll = linkedLights

    ignoredLights = TypedField(multi=True)
    xl = ignoredLights

    defaultShadows = DefaultShadowsField()
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

    linkedShadows = LinkedShadowsField(multi=True)
    ls = linkedShadows

    # TODO: linkedShadows.lShadowDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: linkedShadows.lShadowDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: linkedShadows.lShadowDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: linkedShadows.lShadowIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: linkedShadows.lShadowIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: linkedShadows.lShadowIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    ignoredShadows = IgnoredShadowsField(multi=True)
    xs = ignoredShadows

    # TODO: ignoredShadows.xShadowDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: ignoredShadows.xShadowDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: ignoredShadows.xShadowDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: ignoredShadows.xShadowIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: ignoredShadows.xShadowIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: ignoredShadows.xShadowIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    bogusAttribute = BogusAttributeField(multi=True)
    blt = bogusAttribute

    # TODO: bogusAttribute.bogusDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: bogusAttribute.bogusDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: bogusAttribute.bogusDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: bogusAttribute.bogusIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: bogusAttribute.bogusIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: bogusAttribute.bogusIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    aiCustomAOVs = AiCustomAOVsField(multi=True)
    aovs = aiCustomAOVs

    aiSurfaceShader = AiSurfaceShaderField()
    ai_surface_shader = aiSurfaceShader
    aiSurfaceShaderR = aiSurfaceShader.aiSurfaceShaderR
    ai_surface_shaderr = aiSurfaceShaderR
    aiSurfaceShaderG = aiSurfaceShader.aiSurfaceShaderG
    ai_surface_shaderg = aiSurfaceShaderG
    aiSurfaceShaderB = aiSurfaceShader.aiSurfaceShaderB
    ai_surface_shaderb = aiSurfaceShaderB

    aiVolumeShader = AiVolumeShaderField()
    ai_volume_shader = aiVolumeShader
    aiVolumeShaderR = aiVolumeShader.aiVolumeShaderR
    ai_volume_shaderr = aiVolumeShaderR
    aiVolumeShaderG = aiVolumeShader.aiVolumeShaderG
    ai_volume_shaderg = aiVolumeShaderG
    aiVolumeShaderB = aiVolumeShader.aiVolumeShaderB
    ai_volume_shaderb = aiVolumeShaderB
