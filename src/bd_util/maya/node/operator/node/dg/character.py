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

    unitlessValues = DoubleField(multi=True, default_value=0.0)
    uv = unitlessValues

    linearValues = DoubleLinearField(multi=True, default_value=0.0)
    lv = linearValues

    angularValues = DoubleAngleField(multi=True, default_value=0.0)
    av = angularValues

    timeValues = TimeField(multi=True, default_value=0.0)
    tv = timeValues

    unitlessClipValues = DoubleField(multi=True, default_value=0.0)
    uc = unitlessClipValues

    linearClipValues = DoubleLinearField(multi=True, default_value=0.0)
    lc = linearClipValues

    angularClipValues = DoubleAngleField(multi=True, default_value=0.0)
    ac = angularClipValues

    timeClipValues = TimeField(multi=True, default_value=0.0)
    tc = timeClipValues

    animationMapping = TypedField()
    am = animationMapping

    referenceMapping = TypedField()
    rm = referenceMapping

    clipIndexMap = TypedField()
    cim = clipIndexMap

    offsetObjects = MessageField(multi=True, readable=False)
    ofo = offsetObjects

    offsetObjectLocalXForms = DataMatrixField(multi=True)
    oolxs = offsetObjectLocalXForms

    activeClipConnected = BoolField(default_value=False)
    acc = activeClipConnected

    evalCharacterKeys = BoolField(default_value=True)
    eck = evalCharacterKeys

    timelineClipStart = TimeField(default_value=0.0)
    tcs = timelineClipStart

    timelineClipEnd = TimeField(default_value=0.0)
    tce = timelineClipEnd

    offsetNode = MessageField()
    ofn = offsetNode

    translationOffsetIndicesX = LongField(multi=True, default_value=-1)
    toix = translationOffsetIndicesX

    translationOffsetIndicesY = LongField(multi=True, default_value=-1)
    toiy = translationOffsetIndicesY

    translationOffsetIndicesZ = LongField(multi=True, default_value=-1)
    toiz = translationOffsetIndicesZ

    matchNode = MessageField(readable=False)
    mn = matchNode

    copyUnitlessValues = DoubleField(multi=True, default_value=0.0)
    cuv = copyUnitlessValues

    copyLinearValues = DoubleLinearField(multi=True, default_value=0.0)
    clv = copyLinearValues

    copyAngularValues = DoubleAngleField(multi=True, default_value=0.0)
    cav = copyAngularValues

    copyTimeValues = TimeField(multi=True, default_value=0.0)
    ctv = copyTimeValues

    offsetObjectLocalXForm = DataMatrixField()
    oolx = offsetObjectLocalXForm

    translationOffsetIndices = TranslationOffsetIndicesField(default_value=(-1.0, -1.0, -1.0))
    toi = translationOffsetIndices
    translationOffsetIndexX = translationOffsetIndices.translationOffsetIndexX
    tox = translationOffsetIndexX
    translationOffsetY = translationOffsetIndices.translationOffsetY
    toy = translationOffsetY
    translationOffsetZ = translationOffsetIndices.translationOffsetZ
    toz = translationOffsetZ
