# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_waiter import (
    CacheInPPField,
    ChannelSetColorField,
    LabelColorField,
    PublishedNodeInfoField,
    TranslateInPPField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


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


class MASH_Waiter(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Waiter"

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

    outputPoints = TypedField()

    inputPoints = TypedField()

    shellPositions = DataVectorArrayField()

    multiInstancer = TypedField(multi=True)

    translateInPP = TranslateInPPField()
    inPositionPP = translateInPP.inPositionPP
    inArray = inPositionPP
    inScalePP = translateInPP.inScalePP
    inScPP = inScalePP
    inRotationPP = translateInPP.inRotationPP
    inRotPP = inRotationPP
    inIdPP = translateInPP.inIdPP
    inVisibilityPP = translateInPP.inVisibilityPP
    inVisPP = inVisibilityPP

    cacheInPP = CacheInPPField()
    cacheInArrayPP = cacheInPP.cacheInArrayPP
    cacheRotationPP = cacheInPP.cacheRotationPP
    cacheScalePP = cacheInPP.cacheScalePP
    cacheIdPP = cacheInPP.cacheIdPP
    cacheVisibilityPP = cacheInPP.cacheVisibilityPP

    enablePosCache = BoolField()

    enableRotCache = BoolField()

    enableScaleCache = BoolField()

    enableVisCache = BoolField()

    enableIDCache = BoolField()

    positions = DataVectorArrayField()
    ppA = positions

    matrixOutPP = TypedField()

    initialState = DataVectorArrayField()
    initSt = initialState

    setMessage = MessageField(multi=True)
    smsg = setMessage

    waiterMessage = MessageField()

    useSetMembers = BoolField()
    useSM = useSetMembers

    batchRenderMultiplier = LongField()

    pointCount = LongField()

    showPercent = FloatField()

    numberOfOutputs = LongField()
    numO = numberOfOutputs

    ribArchives = DataStringField()

    filename = DataStringField()

    emptyInstancer = BoolField()

    labelColor = LabelColorField()
    labelColorR = labelColor.labelColorR
    labelColorr = labelColorR
    labelColorG = labelColor.labelColorG
    labelColorg = labelColorG
    labelColorB = labelColor.labelColorB
    labelColorb = labelColorB

    outlinerJSON = DataStringField()
