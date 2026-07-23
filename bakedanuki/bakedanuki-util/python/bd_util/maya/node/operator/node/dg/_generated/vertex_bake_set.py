# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.vertex_bake_set import (
    ChannelSetColorField,
    MaxColorField,
    MinColorField,
    PublishedNodeInfoField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
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


class _GeneratedVertexBakeSet(DG):
    __slots__ = ()

    NODE_TYPE = "vertexBakeSet"

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

    bakeAlpha = BoolField(default_value=False)
    alpha = bakeAlpha

    alphaMode = AlphaModeEnumField(default_value=1)
    mode = alphaMode

    occlusionRays = LongField(default_value=64, min_value=0, soft_max_value=256)
    mor = occlusionRays

    occlusionFalloff = FloatField(default_value=0.0, min_value=0.0)
    mof = occlusionFalloff

    colorMode = ColorModeEnumField(default_value=0)
    clm = colorMode

    orthogonalReflection = BoolField(default_value=False)
    orf = orthogonalReflection

    normalDirection = NormalDirectionEnumField(default_value=1)
    ndr = normalDirection

    customShader = MessageField()
    csh = customShader

    sharedVertices = BoolField(default_value=False)
    shared = sharedVertices

    bakeColor = BoolField(default_value=True)
    color = bakeColor

    colorBlending = ColorBlendingEnumField(default_value=0)
    cblend = colorBlending

    alphaBlending = AlphaBlendingEnumField(default_value=0)
    ablend = alphaBlending

    scaleRgba = FloatField(default_value=1.0, min_value=0.0, max_value=10000.0, soft_min_value=0.1, soft_max_value=2.1)
    scale = scaleRgba

    clampMin = BoolField(default_value=False)
    min = clampMin

    minColor = MinColorField(default_value=(0.0, 0.0, 0.0))
    lc = minColor
    minColorR = minColor.minColorR
    lr = minColorR
    minColorG = minColor.minColorG
    lg = minColorG
    minColorB = minColor.minColorB
    lb = minColorB

    minAlpha = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mina = minAlpha

    clampMax = BoolField(default_value=False)
    max = clampMax

    maxColor = MaxColorField(default_value=(0.0, 0.0, 0.0))
    hc = maxColor
    maxColorR = maxColor.maxColorR
    hr = maxColorR
    maxColorG = maxColor.maxColorG
    hg = maxColorG
    maxColorB = maxColor.maxColorB
    hb = maxColorB

    maxAlpha = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    maxa = maxAlpha

    useFaceNormals = BoolField(default_value=False)
    ufn = useFaceNormals

    colorSetName = DataStringField()
    csn = colorSetName
