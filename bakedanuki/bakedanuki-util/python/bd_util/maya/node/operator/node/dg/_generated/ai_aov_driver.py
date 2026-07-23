# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class OutputModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GUI_ONLY = 0
    BATCH_ONLY = 1
    GUI_AND_BATCH = 2


class OutputModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    GUI_ONLY = 0
    BATCH_ONLY = 1
    GUI_AND_BATCH = 2

    NAME_MAP = {
        GUI_ONLY: "GUI Only",
        BATCH_ONLY: "Batch Only",
        GUI_AND_BATCH: "GUI and Batch",
    }


class OutputModeEnumField(
    EnumField[OutputModeEnumAttrOperator, OutputModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputModeEnumAttrOperator
    PLUG_CLS = OutputModeEnumPlugOperator


class ColorManagementEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RAW = 0
    USE_VIEW_TRANSFORM = 1
    USE_OUTPUT_TRANSFORM = 2


class ColorManagementEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RAW = 0
    USE_VIEW_TRANSFORM = 1
    USE_OUTPUT_TRANSFORM = 2

    NAME_MAP = {
        RAW: "Raw",
        USE_VIEW_TRANSFORM: "Use View Transform",
        USE_OUTPUT_TRANSFORM: "Use Output Transform",
    }


class ColorManagementEnumField(
    EnumField[ColorManagementEnumAttrOperator, ColorManagementEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorManagementEnumAttrOperator
    PLUG_CLS = ColorManagementEnumPlugOperator


class PngFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INT8 = 0
    INT16 = 1


class PngFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    INT8 = 0
    INT16 = 1

    NAME_MAP = {
        INT8: "int8",
        INT16: "int16",
    }


class PngFormatEnumField(
    EnumField[PngFormatEnumAttrOperator, PngFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PngFormatEnumAttrOperator
    PLUG_CLS = PngFormatEnumPlugOperator


class TiffCompressionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LZW = 1
    CCITTRLE = 2
    ZIP = 3
    PACKBITS = 4


class TiffCompressionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LZW = 1
    CCITTRLE = 2
    ZIP = 3
    PACKBITS = 4

    NAME_MAP = {
        NONE: "none",
        LZW: "lzw",
        CCITTRLE: "ccittrle",
        ZIP: "zip",
        PACKBITS: "packbits",
    }


class TiffCompressionEnumField(
    EnumField[TiffCompressionEnumAttrOperator, TiffCompressionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TiffCompressionEnumAttrOperator
    PLUG_CLS = TiffCompressionEnumPlugOperator


class TiffFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INT8 = 0
    INT16 = 1
    FLOAT32 = 2


class TiffFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    INT8 = 0
    INT16 = 1
    FLOAT32 = 2

    NAME_MAP = {
        INT8: "int8",
        INT16: "int16",
        FLOAT32: "float32",
    }


class TiffFormatEnumField(
    EnumField[TiffFormatEnumAttrOperator, TiffFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TiffFormatEnumAttrOperator
    PLUG_CLS = TiffFormatEnumPlugOperator


class ExrCompressionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    RLE = 1
    ZIPS = 2
    ZIP = 3
    PIZ = 4
    PXR24 = 5
    B44 = 6
    B44A = 7
    DWAA = 8
    DWAB = 9


class ExrCompressionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    RLE = 1
    ZIPS = 2
    ZIP = 3
    PIZ = 4
    PXR24 = 5
    B44 = 6
    B44A = 7
    DWAA = 8
    DWAB = 9

    NAME_MAP = {
        NONE: "none",
        RLE: "rle",
        ZIPS: "zips",
        ZIP: "zip",
        PIZ: "piz",
        PXR24: "pxr24",
        B44: "b44",
        B44A: "b44a",
        DWAA: "dwaa",
        DWAB: "dwab",
    }


class ExrCompressionEnumField(
    EnumField[ExrCompressionEnumAttrOperator, ExrCompressionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExrCompressionEnumAttrOperator
    PLUG_CLS = ExrCompressionEnumPlugOperator


class _GeneratedAiAOVDriver(DG):
    __slots__ = ()

    NODE_TYPE = "aiAOVDriver"

    mergeAOVs = BoolField(default_value=False)
    merge_AOVs = mergeAOVs

    aiTranslator = DataStringField()
    ai_translator = aiTranslator

    prefix = DataStringField()
    pre = prefix

    outputMode = OutputModeEnumField(default_value=2)
    output_mode = outputMode

    colorManagement = ColorManagementEnumField(default_value=2)
    color_management = colorManagement

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    quality = LongField(default_value=100, min_value=0, max_value=100, category="arnold")

    outputPadded = BoolField(default_value=False, category="arnold")
    output_padded = outputPadded

    dither = BoolField(default_value=True, category="arnold")

    pngFormat = PngFormatEnumField(default_value=0, category="arnold")
    png_format = pngFormat

    pngUnpremultAlpha = BoolField(default_value=False, category="arnold")
    png_unpremult_alpha = pngUnpremultAlpha

    pngSkipAlpha = BoolField(default_value=True, category="arnold")
    png_skip_alpha = pngSkipAlpha

    tiffCompression = TiffCompressionEnumField(default_value=1, category="arnold")
    tiff_compression = tiffCompression

    tiffFormat = TiffFormatEnumField(default_value=0, category="arnold")
    tiff_format = tiffFormat

    tiffTiled = BoolField(default_value=False, category="arnold")
    tiff_tiled = tiffTiled

    unpremultAlpha = BoolField(default_value=False, category="arnold")
    unpremult_alpha = unpremultAlpha

    skipAlpha = BoolField(default_value=False, category="arnold")
    skip_alpha = skipAlpha

    append = BoolField(default_value=False, category="arnold")

    deepexrTiled = BoolField(default_value=False, category="arnold")
    deepexr_tiled = deepexrTiled

    subpixelMerge = BoolField(default_value=True, category="arnold")
    subpixel_merge = subpixelMerge

    useRGBOpacity = BoolField(default_value=False, category="arnold")
    use_RGB_opacity = useRGBOpacity

    alphaTolerance = FloatField(default_value=0.009999999776482582, category="arnold")
    alpha_tolerance = alphaTolerance

    depthTolerance = FloatField(default_value=0.009999999776482582, category="arnold")
    depth_tolerance = depthTolerance

    alphaHalfPrecision = BoolField(default_value=False, category="arnold")
    alpha_half_precision = alphaHalfPrecision

    depthHalfPrecision = BoolField(default_value=False, category="arnold")
    depth_half_precision = depthHalfPrecision

    layerTolerance = FloatField(multi=True, default_value=5.872578867638367e-09, category="arnold")
    layer_tolerance = layerTolerance

    layerEnableFiltering = BoolField(multi=True, default_value=True, category="arnold")
    layer_enable_filtering = layerEnableFiltering

    layerHalfPrecision = BoolField(multi=True, default_value=False, category="arnold")
    layer_half_precision = layerHalfPrecision

    customAttributes = DataStringField(multi=True, category="arnold")
    custom_attributes = customAttributes

    exrCompression = ExrCompressionEnumField(default_value=3, category="arnold")
    exr_compression = exrCompression

    halfPrecision = BoolField(default_value=False, category="arnold")
    half_precision = halfPrecision

    exrTiled = BoolField(default_value=True, category="arnold")
    tiled = exrTiled

    multipart = BoolField(default_value=False, category="arnold")

    preserveLayerName = BoolField(default_value=False, category="arnold")
    preserve_layer_name = preserveLayerName

    autocrop = BoolField(default_value=False, category="arnold")

    input = MessageField(category="arnold")

    renderSession = DataStringField(category="arnold")
