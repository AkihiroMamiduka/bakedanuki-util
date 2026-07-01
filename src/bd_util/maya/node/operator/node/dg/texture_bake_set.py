# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.texture_bake_set import (
    BackgroundColorField,
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


class SeparationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SHADINGGROUP_ON_SHAPE = 0
    SHAPE = 1
    THIS_WHOLE_SET = 2


class SeparationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SHADINGGROUP_ON_SHAPE = 0
    SHAPE = 1
    THIS_WHOLE_SET = 2

    NAME_MAP = {
        SHADINGGROUP_ON_SHAPE: "shadingGroup on shape",
        SHAPE: "shape",
        THIS_WHOLE_SET: "this whole set",
    }


class SeparationEnumField(
    EnumField[SeparationEnumAttrOperator, SeparationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SeparationEnumAttrOperator
    PLUG_CLS = SeparationEnumPlugOperator


class FileFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TIF = 1
    IFF = 2
    JPG = 3
    RGB = 4
    RLA = 5
    TGA = 6
    BMP = 7
    HDR = 8
    ALS = 9
    GIF = 10
    PIC = 11
    SGI = 12
    PNG = 13
    PHOTOSHOP = 14
    MACPAINT = 15


class FileFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TIF = 1
    IFF = 2
    JPG = 3
    RGB = 4
    RLA = 5
    TGA = 6
    BMP = 7
    HDR = 8
    ALS = 9
    GIF = 10
    PIC = 11
    SGI = 12
    PNG = 13
    PHOTOSHOP = 14
    MACPAINT = 15

    NAME_MAP = {
        TIF: "TIF",
        IFF: "IFF",
        JPG: "JPG",
        RGB: "RGB",
        RLA: "RLA",
        TGA: "TGA",
        BMP: "BMP",
        HDR: "HDR",
        ALS: "ALS",
        GIF: "GIF",
        PIC: "PIC",
        SGI: "SGI",
        PNG: "PNG",
        PHOTOSHOP: "Photoshop",
        MACPAINT: "MacPaint",
    }


class FileFormatEnumField(
    EnumField[FileFormatEnumAttrOperator, FileFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FileFormatEnumAttrOperator
    PLUG_CLS = FileFormatEnumPlugOperator


class BitsPerChannelEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _8_BITS = 1
    _16_BITS = 2
    _32_BITS = 4


class BitsPerChannelEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _8_BITS = 1
    _16_BITS = 2
    _32_BITS = 4

    NAME_MAP = {
        _8_BITS: "8 bits",
        _16_BITS: "16 bits",
        _32_BITS: "32 bits",
    }


class BitsPerChannelEnumField(
    EnumField[BitsPerChannelEnumAttrOperator, BitsPerChannelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BitsPerChannelEnumAttrOperator
    PLUG_CLS = BitsPerChannelEnumPlugOperator


class UvRangeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL_0_TO_1 = 0
    ENTIRE_RANGE = 1
    USER_SPECIFIED = 2


class UvRangeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL_0_TO_1 = 0
    ENTIRE_RANGE = 1
    USER_SPECIFIED = 2

    NAME_MAP = {
        NORMAL_0_TO_1: "Normal (0 to 1)",
        ENTIRE_RANGE: "Entire Range",
        USER_SPECIFIED: "User Specified",
    }


class UvRangeEnumField(
    EnumField[UvRangeEnumAttrOperator, UvRangeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvRangeEnumAttrOperator
    PLUG_CLS = UvRangeEnumPlugOperator


class BackgroundModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SHADER_DEFAULT = 0
    CUSTOM_COLOR = 1
    EXTEND_EDGE_COLOR = 2


class BackgroundModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SHADER_DEFAULT = 0
    CUSTOM_COLOR = 1
    EXTEND_EDGE_COLOR = 2

    NAME_MAP = {
        SHADER_DEFAULT: "Shader Default",
        CUSTOM_COLOR: "Custom Color",
        EXTEND_EDGE_COLOR: "Extend Edge Color",
    }


class BackgroundModeEnumField(
    EnumField[BackgroundModeEnumAttrOperator, BackgroundModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundModeEnumAttrOperator
    PLUG_CLS = BackgroundModeEnumPlugOperator


class TextureBakeSet(DG):
    __slots__ = ()

    NODE_TYPE = "textureBakeSet"

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

    separation = SeparationEnumField()
    sep = separation

    prefix = DataStringField()
    pre = prefix

    xResolution = LongField()
    xres = xResolution

    yResolution = LongField()
    yres = yResolution

    fileFormat = FileFormatEnumField()
    format = fileFormat

    bitsPerChannel = BitsPerChannelEnumField()
    bits = bitsPerChannel

    overrideUvSet = BoolField()
    overrideuv = overrideUvSet

    uvSetName = DataStringField()
    set = uvSetName

    uvRange = UvRangeEnumField()
    range = uvRange

    uMin = FloatField()
    ul = uMin

    uMax = FloatField()
    uh = uMax

    vMin = FloatField()
    vl = vMin

    vMax = FloatField()
    vh = vMax

    backgroundMode = BackgroundModeEnumField()
    bmode = backgroundMode

    backgroundColor = BackgroundColorField()
    bgc = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    bgr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    bgg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    bgb = backgroundColorB

    fillTextureSeams = FloatField()
    fillseams = fillTextureSeams

    fillScale = FloatField()
    fillscale = fillScale

    finalGatherQuality = FloatField()
    fgq = finalGatherQuality

    finalGatherReflect = FloatField()
    fgr = finalGatherReflect

    bakeToOneMap = BoolField()
    one = bakeToOneMap

    samples = LongField()
    nsp = samples
