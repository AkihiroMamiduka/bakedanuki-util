# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.anim_layer import (
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
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
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


class RotationAccumulationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BY_COMPONENT = 0
    BY_LAYER = 1


class RotationAccumulationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BY_COMPONENT = 0
    BY_LAYER = 1

    NAME_MAP = {
        BY_COMPONENT: "By Component",
        BY_LAYER: "By Layer",
    }


class RotationAccumulationModeEnumField(
    EnumField[RotationAccumulationModeEnumAttrOperator, RotationAccumulationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationAccumulationModeEnumAttrOperator
    PLUG_CLS = RotationAccumulationModeEnumPlugOperator


class OutRotationAccumulationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BY_COMPONENT = 0
    BY_LAYER_CUMULATIVE = 1
    BY_LAYER_BLENDED = 2


class OutRotationAccumulationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BY_COMPONENT = 0
    BY_LAYER_CUMULATIVE = 1
    BY_LAYER_BLENDED = 2

    NAME_MAP = {
        BY_COMPONENT: "By Component",
        BY_LAYER_CUMULATIVE: "By Layer Cumulative",
        BY_LAYER_BLENDED: "By Layer Blended",
    }


class OutRotationAccumulationModeEnumField(
    EnumField[OutRotationAccumulationModeEnumAttrOperator, OutRotationAccumulationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRotationAccumulationModeEnumAttrOperator
    PLUG_CLS = OutRotationAccumulationModeEnumPlugOperator


class ScaleAccumulationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1


class ScaleAccumulationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1

    NAME_MAP = {
        ADDITIVE: "Additive",
        MULTIPLY: "Multiply",
    }


class ScaleAccumulationModeEnumField(
    EnumField[ScaleAccumulationModeEnumAttrOperator, ScaleAccumulationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAccumulationModeEnumAttrOperator
    PLUG_CLS = ScaleAccumulationModeEnumPlugOperator


class AnimLayer(DG):
    __slots__ = ()

    NODE_TYPE = "animLayer"

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

    blendNodes = MessageField(multi=True)
    bnds = blendNodes

    childrenLayers = MessageField(multi=True)
    cdly = childrenLayers

    parentLayer = MessageField()
    play = parentLayer

    mute = BoolField()
    mt = mute

    parentMute = BoolField()
    pmte = parentMute

    solo = BoolField()
    sl = solo

    childsoloed = BoolField()
    csol = childsoloed

    childrenSolo = BoolField(multi=True)
    chsl = childrenSolo

    siblingSolo = BoolField()
    sslo = siblingSolo

    outMute = BoolField()
    omte = outMute

    lock = BoolField()
    lo = lock

    ghost = BoolField()
    gh = ghost

    ghostColor = ShortField()
    ghc = ghostColor

    preferred = BoolField()
    pref = preferred

    selected = BoolField()
    slct = selected

    override = BoolField()
    ovrd = override

    passthrough = BoolField()
    pthg = passthrough

    collapse = BoolField()
    coll = collapse

    weight = DoubleField()
    wgth = weight

    parentWeight = DoubleField()
    pwth = parentWeight

    foregroundWeight = DoubleField()
    fgwt = foregroundWeight

    backgroundWeight = DoubleField()
    bgwt = backgroundWeight

    cteRoot = MessageField()
    cter = cteRoot

    rotationAccumulationMode = RotationAccumulationModeEnumField()
    ram = rotationAccumulationMode

    outRotationAccumulationMode = OutRotationAccumulationModeEnumField()
    oram = outRotationAccumulationMode

    scaleAccumulationMode = ScaleAccumulationModeEnumField()
    sam = scaleAccumulationMode

    exclusive = BoolField()
    exc = exclusive

    clips = MessageField()
    cl = clips

    ghostedClips = MessageField(multi=True)
    gc = ghostedClips
