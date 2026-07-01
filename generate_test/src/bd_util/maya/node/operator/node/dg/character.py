# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.character import (
    ChannelSetColorField,
    ClipEvaluateField,
    ClipStatePercentEvalField,
    PublishedNodeInfoField,
    TranslationOffsetIndicesField,
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
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
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


class Character(DG):
    __slots__ = ()

    NODE_TYPE = "character"

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

    clipEvaluate = ClipEvaluateField()
    ce = clipEvaluate
    clipEvaluate_Hidden = clipEvaluate.clipEvaluate_Hidden
    ceh = clipEvaluate_Hidden
    clipEvaluate_Raw = clipEvaluate.clipEvaluate_Raw
    cer = clipEvaluate_Raw
    clipEvaluate_Inmap = clipEvaluate.clipEvaluate_Inmap
    cei = clipEvaluate_Inmap
    clipEvaluate_Outmap = clipEvaluate.clipEvaluate_Outmap
    ceo = clipEvaluate_Outmap

    clipEvaluate_InmapTo = ShortField()
    ceit = clipEvaluate_InmapTo

    clipEvaluate_InmapFrom = ShortField()
    ceif = clipEvaluate_InmapFrom

    clipEvaluate_OutmapTo = ShortField()
    ceot = clipEvaluate_OutmapTo

    clipEvaluate_OutmapFrom = ShortField()
    ceof = clipEvaluate_OutmapFrom

    clipStatePercentEval = ClipStatePercentEvalField()
    cspe = clipStatePercentEval
    clipStatePercentEval_Hidden = clipStatePercentEval.clipStatePercentEval_Hidden
    cspeh = clipStatePercentEval_Hidden
    clipStatePercentEval_Raw = clipStatePercentEval.clipStatePercentEval_Raw
    csper = clipStatePercentEval_Raw
    clipStatePercentEval_Inmap = clipStatePercentEval.clipStatePercentEval_Inmap
    cspei = clipStatePercentEval_Inmap
    clipStatePercentEval_Outmap = clipStatePercentEval.clipStatePercentEval_Outmap
    cspeo = clipStatePercentEval_Outmap

    clipStatePercentEval_InmapTo = ShortField()
    cspeit = clipStatePercentEval_InmapTo

    clipStatePercentEval_InmapFrom = ShortField()
    cspeif = clipStatePercentEval_InmapFrom

    clipStatePercentEval_OutmapTo = ShortField()
    cspeot = clipStatePercentEval_OutmapTo

    clipStatePercentEval_OutmapFrom = ShortField()
    cspeof = clipStatePercentEval_OutmapFrom

    unitlessValues = DoubleField(multi=True)
    uv = unitlessValues

    linearValues = DoubleLinearField(multi=True)
    lv = linearValues

    angularValues = DoubleAngleField(multi=True)
    av = angularValues

    timeValues = TimeField(multi=True)
    tv = timeValues

    unitlessClipValues = DoubleField(multi=True)
    uc = unitlessClipValues

    linearClipValues = DoubleLinearField(multi=True)
    lc = linearClipValues

    angularClipValues = DoubleAngleField(multi=True)
    ac = angularClipValues

    timeClipValues = TimeField(multi=True)
    tc = timeClipValues

    animationMapping = TypedField()
    am = animationMapping

    referenceMapping = TypedField()
    rm = referenceMapping

    clipIndexMap = TypedField()
    cim = clipIndexMap

    offsetObjects = MessageField(multi=True)
    ofo = offsetObjects

    offsetObjectLocalXForms = DataMatrixField(multi=True)
    oolxs = offsetObjectLocalXForms

    activeClipConnected = BoolField()
    acc = activeClipConnected

    evalCharacterKeys = BoolField()
    eck = evalCharacterKeys

    timelineClipStart = TimeField()
    tcs = timelineClipStart

    timelineClipEnd = TimeField()
    tce = timelineClipEnd

    offsetNode = MessageField()
    ofn = offsetNode

    translationOffsetIndicesX = LongField(multi=True)
    toix = translationOffsetIndicesX

    translationOffsetIndicesY = LongField(multi=True)
    toiy = translationOffsetIndicesY

    translationOffsetIndicesZ = LongField(multi=True)
    toiz = translationOffsetIndicesZ

    matchNode = MessageField()
    mn = matchNode

    copyUnitlessValues = DoubleField(multi=True)
    cuv = copyUnitlessValues

    copyLinearValues = DoubleLinearField(multi=True)
    clv = copyLinearValues

    copyAngularValues = DoubleAngleField(multi=True)
    cav = copyAngularValues

    copyTimeValues = TimeField(multi=True)
    ctv = copyTimeValues

    offsetObjectLocalXForm = DataMatrixField()
    oolx = offsetObjectLocalXForm

    translationOffsetIndices = TranslationOffsetIndicesField()
    toi = translationOffsetIndices
    translationOffsetIndexX = translationOffsetIndices.translationOffsetIndexX
    tox = translationOffsetIndexX
    translationOffsetY = translationOffsetIndices.translationOffsetY
    toy = translationOffsetY
    translationOffsetZ = translationOffsetIndices.translationOffsetZ
    toz = translationOffsetZ
