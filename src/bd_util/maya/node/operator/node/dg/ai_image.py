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

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
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

    filter = FilterEnumField(default_value=3)

    mipmapBias = LongField(default_value=0)
    mipmap_bias = mipmapBias

    singleChannel = BoolField(default_value=False)
    single_channel = singleChannel

    startChannel = ByteField(default_value=0, min_value=0, max_value=255)
    start_channel = startChannel

    swrap = SwrapEnumField(default_value=0)

    twrap = TwrapEnumField(default_value=0)

    sscale = FloatField(default_value=1.0)

    tscale = FloatField(default_value=1.0)

    sflip = BoolField(default_value=False)

    tflip = BoolField(default_value=False)

    soffset = FloatField(default_value=0.0)

    toffset = FloatField(default_value=0.0)

    swapSt = BoolField(default_value=False)
    swap_st = swapSt

    uvcoords = UvcoordsField(default_value=(0.0, 0.0))
    uvcoordsX = uvcoords.uvcoordsX
    uvcoordsx = uvcoordsX
    uvcoordsY = uvcoords.uvcoordsY
    uvcoordsy = uvcoordsY

    uvset = DataStringField()

    multiply = MultiplyField(default_value=(1.0, 1.0, 1.0))
    multiplyR = multiply.multiplyR
    multiplyr = multiplyR
    multiplyG = multiply.multiplyG
    multiplyg = multiplyG
    multiplyB = multiply.multiplyB
    multiplyb = multiplyB

    offset = OffsetField(default_value=(0.0, 0.0, 0.0))
    offsetR = offset.offsetR
    offsetr = offsetR
    offsetG = offset.offsetG
    offsetg = offsetG
    offsetB = offset.offsetB
    offsetb = offsetB

    ignoreMissingTextures = BoolField(default_value=False)
    ignore_missing_textures = ignoreMissingTextures

    missingTextureColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    missing_texture_colora = missingTextureColorA

    missingTextureColor = MissingTextureColorField(default_value=(0.0, 0.0, 0.0))
    missing_texture_color = missingTextureColor
    missingTextureColorR = missingTextureColor.missingTextureColorR
    missing_texture_colorr = missingTextureColorR
    missingTextureColorG = missingTextureColor.missingTextureColorG
    missing_texture_colorg = missingTextureColorG
    missingTextureColorB = missingTextureColor.missingTextureColorB
    missing_texture_colorb = missingTextureColorB

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    autoTx = BoolField(default_value=True, category="arnold")
    autotx = autoTx

    colorManagementConfigFileEnabled = BoolField(default_value=False, category="arnold")
    cmcf = colorManagementConfigFileEnabled

    colorManagementConfigFilePath = DataStringField(category="arnold")
    cmcp = colorManagementConfigFilePath

    colorManagementEnabled = BoolField(default_value=False, category="arnold")
    cme = colorManagementEnabled

    colorProfile = LongField(default_value=0, category="arnold")
    cp = colorProfile

    workingSpace = DataStringField(category="arnold")
    ws = workingSpace

    useFrameExtension = BoolField(default_value=False, category="arnold")

    frame = FloatField(default_value=0.0, category="arnold")

    ignoreColorSpaceFileRules = BoolField(default_value=False, category="arnold")
    ifr = ignoreColorSpaceFileRules
