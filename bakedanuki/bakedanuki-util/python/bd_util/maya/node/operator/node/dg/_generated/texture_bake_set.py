# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.texture_bake_set import (
    BackgroundColorField,
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
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator["ViewModeEnumAttrOperator"]):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator[ViewModeEnumPlugOperator]):
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


class UiTreatmentEnumPlugOperator(EnumPlugOperator["UiTreatmentEnumAttrOperator"]):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator[UiTreatmentEnumPlugOperator]):
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


class AlphaModeEnumPlugOperator(EnumPlugOperator["AlphaModeEnumAttrOperator"]):
    __slots__ = ()

    PASS_THROUGH = 0
    SURFACE_TRANSPARENCY = 1
    LUMINANCE_OF_SURFACE_COLOR = 2
    COVERAGE = 3


class AlphaModeEnumAttrOperator(EnumAttrOperator[AlphaModeEnumPlugOperator]):
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


class ColorModeEnumPlugOperator(EnumPlugOperator["ColorModeEnumAttrOperator"]):
    __slots__ = ()

    LIGHT_AND_COLOR = 0
    ONLY_LIGHT = 1
    ONLY_GLOBAL_ILLUMINATION = 2
    OCCLUSION = 3
    CUSTOM_SHADER = 4


class ColorModeEnumAttrOperator(EnumAttrOperator[ColorModeEnumPlugOperator]):
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


class NormalDirectionEnumPlugOperator(EnumPlugOperator["NormalDirectionEnumAttrOperator"]):
    __slots__ = ()

    FACE_CAMERA = 0
    SURFACE_FRONT = 1
    SURFACE_BACK = 2


class NormalDirectionEnumAttrOperator(EnumAttrOperator[NormalDirectionEnumPlugOperator]):
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


class SeparationEnumPlugOperator(EnumPlugOperator["SeparationEnumAttrOperator"]):
    __slots__ = ()

    SHADINGGROUP_ON_SHAPE = 0
    SHAPE = 1
    THIS_WHOLE_SET = 2


class SeparationEnumAttrOperator(EnumAttrOperator[SeparationEnumPlugOperator]):
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


class FileFormatEnumPlugOperator(EnumPlugOperator["FileFormatEnumAttrOperator"]):
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


class FileFormatEnumAttrOperator(EnumAttrOperator[FileFormatEnumPlugOperator]):
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


class BitsPerChannelEnumPlugOperator(EnumPlugOperator["BitsPerChannelEnumAttrOperator"]):
    __slots__ = ()

    _8_BITS = 1
    _16_BITS = 2
    _32_BITS = 4


class BitsPerChannelEnumAttrOperator(EnumAttrOperator[BitsPerChannelEnumPlugOperator]):
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


class UvRangeEnumPlugOperator(EnumPlugOperator["UvRangeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL_0_TO_1 = 0
    ENTIRE_RANGE = 1
    USER_SPECIFIED = 2


class UvRangeEnumAttrOperator(EnumAttrOperator[UvRangeEnumPlugOperator]):
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


class BackgroundModeEnumPlugOperator(EnumPlugOperator["BackgroundModeEnumAttrOperator"]):
    __slots__ = ()

    SHADER_DEFAULT = 0
    CUSTOM_COLOR = 1
    EXTEND_EDGE_COLOR = 2


class BackgroundModeEnumAttrOperator(EnumAttrOperator[BackgroundModeEnumPlugOperator]):
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


class GeneratedTextureBakeSet(DG):
    __slots__ = ()

    NODE_TYPE = "textureBakeSet"

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

    separation = SeparationEnumField(default_value=0)
    sep = separation

    prefix = DataStringField()
    pre = prefix

    xResolution = LongField(default_value=512, min_value=1, max_value=16384, soft_min_value=128, soft_max_value=1024)
    xres = xResolution

    yResolution = LongField(default_value=512, min_value=1, max_value=16384, soft_min_value=128, soft_max_value=1024)
    yres = yResolution

    fileFormat = FileFormatEnumField(default_value=1)
    format = fileFormat

    bitsPerChannel = BitsPerChannelEnumField(default_value=1)
    bits = bitsPerChannel

    overrideUvSet = BoolField(default_value=False)
    overrideuv = overrideUvSet

    uvSetName = DataStringField()
    set = uvSetName

    uvRange = UvRangeEnumField(default_value=0)
    range = uvRange

    uMin = FloatField(default_value=1.0, min_value=-10000.0, max_value=10000.0, soft_min_value=0.0, soft_max_value=1.0)
    ul = uMin

    uMax = FloatField(default_value=1.0, min_value=-10000.0, max_value=10000.0, soft_min_value=0.0, soft_max_value=1.0)
    uh = uMax

    vMin = FloatField(default_value=1.0, min_value=-10000.0, max_value=10000.0, soft_min_value=0.0, soft_max_value=1.0)
    vl = vMin

    vMax = FloatField(default_value=1.0, min_value=-10000.0, max_value=10000.0, soft_min_value=0.0, soft_max_value=1.0)
    vh = vMax

    backgroundMode = BackgroundModeEnumField(default_value=0)
    bmode = backgroundMode

    backgroundColor = BackgroundColorField(default_value=(0.0, 0.0, 0.0), soft_min_value=(0.0, 0.0, 0.0), soft_max_value=(1.0, 1.0, 1.0))
    bgc = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    bgr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    bgg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    bgb = backgroundColorB

    fillTextureSeams = FloatField(default_value=1.0, min_value=0.0, max_value=32.0, soft_min_value=0.0, soft_max_value=3.0)
    fillseams = fillTextureSeams

    fillScale = FloatField(default_value=1.0, min_value=1.0, max_value=5.0)
    fillscale = fillScale

    finalGatherQuality = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    fgq = finalGatherQuality

    finalGatherReflect = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fgr = finalGatherReflect

    bakeToOneMap = BoolField(default_value=False)
    one = bakeToOneMap

    samples = LongField(default_value=1, min_value=0, soft_max_value=4)
    nsp = samples
