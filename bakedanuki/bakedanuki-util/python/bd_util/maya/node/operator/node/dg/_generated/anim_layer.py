# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.anim_layer import (
    ChannelSetColorField,
    PublishedNodeInfoField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField
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


class _GeneratedAnimLayer(DG):
    __slots__ = ()

    NODE_TYPE = "animLayer"

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

    blendNodes = MessageField(multi=True)
    bnds = blendNodes

    childrenLayers = MessageField(multi=True)
    cdly = childrenLayers

    parentLayer = MessageField()
    play = parentLayer

    mute = BoolField(default_value=False)
    mt = mute

    parentMute = BoolField(default_value=False)
    pmte = parentMute

    solo = BoolField(default_value=False)
    sl = solo

    childsoloed = BoolField(default_value=False)
    csol = childsoloed

    childrenSolo = BoolField(multi=True, default_value=False)
    chsl = childrenSolo

    siblingSolo = BoolField(default_value=False)
    sslo = siblingSolo

    outMute = BoolField(default_value=False)
    omte = outMute

    lock = BoolField(default_value=False)
    lo = lock

    ghost = BoolField(default_value=False)
    gh = ghost

    ghostColor = ShortField(default_value=5, min_value=2, max_value=24)
    ghc = ghostColor

    preferred = BoolField(default_value=False)
    pref = preferred

    selected = BoolField(default_value=False)
    slct = selected

    override = BoolField(default_value=False)
    ovrd = override

    passthrough = BoolField(default_value=True)
    pthg = passthrough

    collapse = BoolField(default_value=False)
    coll = collapse

    weight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    wgth = weight

    parentWeight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    pwth = parentWeight

    foregroundWeight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    fgwt = foregroundWeight

    backgroundWeight = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    bgwt = backgroundWeight

    cteRoot = MessageField()
    cter = cteRoot

    rotationAccumulationMode = RotationAccumulationModeEnumField(default_value=0)
    ram = rotationAccumulationMode

    outRotationAccumulationMode = OutRotationAccumulationModeEnumField(default_value=0)
    oram = outRotationAccumulationMode

    scaleAccumulationMode = ScaleAccumulationModeEnumField(default_value=1)
    sam = scaleAccumulationMode

    exclusive = BoolField(default_value=False)
    exc = exclusive

    clips = MessageField(writable=False)
    cl = clips

    ghostedClips = MessageField(multi=True, readable=False)
    gc = ghostedClips
