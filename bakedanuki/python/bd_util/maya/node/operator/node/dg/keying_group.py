# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.keying_group import (
    ChannelSetColorField,
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


class KeyingGroup(DG):
    __slots__ = ()

    NODE_TYPE = "keyingGroup"

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

    activators = MessageField(multi=True)
    act = activators

    category = DataStringField()
    cat = category

    minimizeRotation = BoolField(default_value=False)
    mr = minimizeRotation
