# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.vertex_bake_set import (
    ChannelSetColorField,
    MaxColorField,
    MinColorField,
    PublishedNodeInfoField,
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


class AlphaModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PASS_THROUGH = 0
    SURFACE_TRANSPARENCY = 1
    LUMINANCE_OF_SURFACE_COLOR = 2
    COVERAGE = 3


class AlphaModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PASS_THROUGH = 0
    SURFACE_TRANSPARENCY = 1
    LUMINANCE_OF_SURFACE_COLOR = 2
    COVERAGE = 3

    NAME_MAP = {
        PASS_THROUGH: "Pass Through",
        SURFACE_TRANSPARENCY: "Surface Transparency",
        LUMINANCE_OF_SURFACE_COLOR: "Luminance of Surface Color",
        COVERAGE: "Coverage",
    }


class AlphaModeEnumField(
    EnumField[AlphaModeEnumAttrOperator, AlphaModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaModeEnumAttrOperator
    PLUG_CLS = AlphaModeEnumPlugOperator


class ColorModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LIGHT_AND_COLOR = 0
    ONLY_LIGHT = 1
    ONLY_GLOBAL_ILLUMINATION = 2
    OCCLUSION = 3
    CUSTOM_SHADER = 4


class ColorModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LIGHT_AND_COLOR = 0
    ONLY_LIGHT = 1
    ONLY_GLOBAL_ILLUMINATION = 2
    OCCLUSION = 3
    CUSTOM_SHADER = 4

    NAME_MAP = {
        LIGHT_AND_COLOR: "Light and Color",
        ONLY_LIGHT: "Only Light",
        ONLY_GLOBAL_ILLUMINATION: "Only Global Illumination",
        OCCLUSION: "Occlusion",
        CUSTOM_SHADER: "Custom Shader",
    }


class ColorModeEnumField(
    EnumField[ColorModeEnumAttrOperator, ColorModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorModeEnumAttrOperator
    PLUG_CLS = ColorModeEnumPlugOperator


class NormalDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FACE_CAMERA = 0
    SURFACE_FRONT = 1
    SURFACE_BACK = 2


class NormalDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FACE_CAMERA = 0
    SURFACE_FRONT = 1
    SURFACE_BACK = 2

    NAME_MAP = {
        FACE_CAMERA: "Face Camera",
        SURFACE_FRONT: "Surface Front",
        SURFACE_BACK: "Surface Back",
    }


class NormalDirectionEnumField(
    EnumField[NormalDirectionEnumAttrOperator, NormalDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalDirectionEnumAttrOperator
    PLUG_CLS = NormalDirectionEnumPlugOperator


class ColorBlendingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    AVERAGE = 5


class ColorBlendingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    AVERAGE = 5

    NAME_MAP = {
        OVERWRITE: "Overwrite",
        ADD: "Add",
        SUBTRACT: "Subtract",
        MULTIPLY: "Multiply",
        DIVIDE: "Divide",
        AVERAGE: "Average",
    }


class ColorBlendingEnumField(
    EnumField[ColorBlendingEnumAttrOperator, ColorBlendingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorBlendingEnumAttrOperator
    PLUG_CLS = ColorBlendingEnumPlugOperator


class AlphaBlendingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    AVERAGE = 5


class AlphaBlendingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    AVERAGE = 5

    NAME_MAP = {
        OVERWRITE: "Overwrite",
        ADD: "Add",
        SUBTRACT: "Subtract",
        MULTIPLY: "Multiply",
        DIVIDE: "Divide",
        AVERAGE: "Average",
    }


class AlphaBlendingEnumField(
    EnumField[AlphaBlendingEnumAttrOperator, AlphaBlendingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaBlendingEnumAttrOperator
    PLUG_CLS = AlphaBlendingEnumPlugOperator


class VertexBakeSet(DG):
    __slots__ = ()

    NODE_TYPE = "vertexBakeSet"

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

    bakeAlpha = BoolField()
    alpha = bakeAlpha

    alphaMode = AlphaModeEnumField()
    mode = alphaMode

    occlusionRays = LongField()
    mor = occlusionRays

    occlusionFalloff = FloatField()
    mof = occlusionFalloff

    colorMode = ColorModeEnumField()
    clm = colorMode

    orthogonalReflection = BoolField()
    orf = orthogonalReflection

    normalDirection = NormalDirectionEnumField()
    ndr = normalDirection

    customShader = MessageField()
    csh = customShader

    sharedVertices = BoolField()
    shared = sharedVertices

    bakeColor = BoolField()
    color = bakeColor

    colorBlending = ColorBlendingEnumField()
    cblend = colorBlending

    alphaBlending = AlphaBlendingEnumField()
    ablend = alphaBlending

    scaleRgba = FloatField()
    scale = scaleRgba

    clampMin = BoolField()
    min = clampMin

    minColor = MinColorField()
    lc = minColor
    minColorR = minColor.minColorR
    lr = minColorR
    minColorG = minColor.minColorG
    lg = minColorG
    minColorB = minColor.minColorB
    lb = minColorB

    minAlpha = FloatField()
    mina = minAlpha

    clampMax = BoolField()
    max = clampMax

    maxColor = MaxColorField()
    hc = maxColor
    maxColorR = maxColor.maxColorR
    hr = maxColorR
    maxColorG = maxColor.maxColorG
    hg = maxColorG
    maxColorB = maxColor.maxColorB
    hb = maxColorB

    maxAlpha = FloatField()
    maxa = maxAlpha

    useFaceNormals = BoolField()
    ufn = useFaceNormals

    colorSetName = DataStringField()
    csn = colorSetName
