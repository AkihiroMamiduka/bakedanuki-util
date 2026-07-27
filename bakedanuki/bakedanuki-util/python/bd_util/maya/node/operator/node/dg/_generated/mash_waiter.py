# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_waiter import (
    CacheInPPField,
    ChannelSetColorField,
    LabelColorField,
    PublishedNodeInfoField,
    TranslateInPPField,
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
from ....attr.define.std.dt.vector_array import DataVectorArrayField


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


class GeneratedMASH_Waiter(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Waiter"

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

    outputPoints = TypedField(writable=False)

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

    enablePosCache = BoolField(default_value=False)

    enableRotCache = BoolField(default_value=False)

    enableScaleCache = BoolField(default_value=False)

    enableVisCache = BoolField(default_value=False)

    enableIDCache = BoolField(default_value=False)

    positions = DataVectorArrayField()
    ppA = positions

    matrixOutPP = TypedField()

    initialState = DataVectorArrayField()
    initSt = initialState

    setMessage = MessageField(multi=True)
    smsg = setMessage

    waiterMessage = MessageField()

    useSetMembers = BoolField(default_value=False)
    useSM = useSetMembers

    batchRenderMultiplier = LongField(default_value=1, min_value=1, soft_max_value=10)

    pointCount = LongField(default_value=0, readable=False, writable=False)

    showPercent = FloatField(default_value=100.0, min_value=0.0, max_value=100.0)

    numberOfOutputs = LongField(default_value=1, min_value=1, soft_max_value=100)
    numO = numberOfOutputs

    ribArchives = DataStringField()

    filename = DataStringField()

    emptyInstancer = BoolField(default_value=False)

    labelColor = LabelColorField(default_value=(0.9450980424880981, 0.3529411852359772, 0.35686275362968445))
    labelColorR = labelColor.labelColorR
    labelColorr = labelColorR
    labelColorG = labelColor.labelColorG
    labelColorg = labelColorG
    labelColorB = labelColor.labelColorB
    labelColorb = labelColorB

    outlinerJSON = DataStringField()
