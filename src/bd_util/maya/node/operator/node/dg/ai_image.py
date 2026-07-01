# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_image import (
    MissingTextureColorField,
    MultiplyField,
    OffsetField,
    OutColorField,
    OutTransparencyField,
    UvcoordsField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.byte import ByteField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class FilterEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    BILINEAR = 1
    BICUBIC = 2
    SMART_BICUBIC = 3


class FilterEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST = 0
    BILINEAR = 1
    BICUBIC = 2
    SMART_BICUBIC = 3

    NAME_MAP = {
        CLOSEST: "closest",
        BILINEAR: "bilinear",
        BICUBIC: "bicubic",
        SMART_BICUBIC: "smart_bicubic",
    }


class FilterEnumField(
    EnumField[FilterEnumAttrOperator, FilterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterEnumAttrOperator
    PLUG_CLS = FilterEnumPlugOperator


class SwrapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4
    MISSING = 5


class SwrapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4
    MISSING = 5

    NAME_MAP = {
        PERIODIC: "periodic",
        BLACK: "black",
        CLAMP: "clamp",
        MIRROR: "mirror",
        FILE: "file",
        MISSING: "missing",
    }


class SwrapEnumField(
    EnumField[SwrapEnumAttrOperator, SwrapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SwrapEnumAttrOperator
    PLUG_CLS = SwrapEnumPlugOperator


class TwrapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4
    MISSING = 5


class TwrapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4
    MISSING = 5

    NAME_MAP = {
        PERIODIC: "periodic",
        BLACK: "black",
        CLAMP: "clamp",
        MIRROR: "mirror",
        FILE: "file",
        MISSING: "missing",
    }


class TwrapEnumField(
    EnumField[TwrapEnumAttrOperator, TwrapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwrapEnumAttrOperator
    PLUG_CLS = TwrapEnumPlugOperator


class AiImage(DG):
    __slots__ = ()

    NODE_TYPE = "aiImage"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    filename = DataStringField()

    colorSpace = DataStringField()
    cs = colorSpace

    filter = FilterEnumField()

    mipmapBias = LongField()
    mipmap_bias = mipmapBias

    singleChannel = BoolField()
    single_channel = singleChannel

    startChannel = ByteField()
    start_channel = startChannel

    swrap = SwrapEnumField()

    twrap = TwrapEnumField()

    sscale = FloatField()

    tscale = FloatField()

    sflip = BoolField()

    tflip = BoolField()

    soffset = FloatField()

    toffset = FloatField()

    swapSt = BoolField()
    swap_st = swapSt

    uvcoords = UvcoordsField()
    uvcoordsX = uvcoords.uvcoordsX
    uvcoordsx = uvcoordsX
    uvcoordsY = uvcoords.uvcoordsY
    uvcoordsy = uvcoordsY

    uvset = DataStringField()

    multiply = MultiplyField()
    multiplyR = multiply.multiplyR
    multiplyr = multiplyR
    multiplyG = multiply.multiplyG
    multiplyg = multiplyG
    multiplyB = multiply.multiplyB
    multiplyb = multiplyB

    offset = OffsetField()
    offsetR = offset.offsetR
    offsetr = offsetR
    offsetG = offset.offsetG
    offsetg = offsetG
    offsetB = offset.offsetB
    offsetb = offsetB

    ignoreMissingTextures = BoolField()
    ignore_missing_textures = ignoreMissingTextures

    missingTextureColorA = FloatField()
    missing_texture_colora = missingTextureColorA

    missingTextureColor = MissingTextureColorField()
    missing_texture_color = missingTextureColor
    missingTextureColorR = missingTextureColor.missingTextureColorR
    missing_texture_colorr = missingTextureColorR
    missingTextureColorG = missingTextureColor.missingTextureColorG
    missing_texture_colorg = missingTextureColorG
    missingTextureColorB = missingTextureColor.missingTextureColorB
    missing_texture_colorb = missingTextureColorB

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    autoTx = BoolField()
    autotx = autoTx

    colorManagementConfigFileEnabled = BoolField()
    cmcf = colorManagementConfigFileEnabled

    colorManagementConfigFilePath = DataStringField()
    cmcp = colorManagementConfigFilePath

    colorManagementEnabled = BoolField()
    cme = colorManagementEnabled

    colorProfile = LongField()
    cp = colorProfile

    workingSpace = DataStringField()
    ws = workingSpace

    useFrameExtension = BoolField()

    frame = FloatField()

    ignoreColorSpaceFileRules = BoolField()
    ifr = ignoreColorSpaceFileRules
