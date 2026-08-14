# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class ImageColorProfileEnumPlugOperator(
    EnumPlugOperator["ImageColorProfileEnumAttrOperator"]
):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10


class ImageColorProfileEnumAttrOperator(
    EnumAttrOperator[ImageColorProfileEnumPlugOperator]
):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10

    NAME_MAP = {
        LINEAR_SRGB: "Linear sRGB",
        SRGB: "sRGB",
        LINEAR_REC_709: "Linear Rec. 709",
        HDTV_REC_709: "HDTV (Rec. 709)",
        CIE_XYZ: "CIE XYZ",
    }


class ImageColorProfileEnumField(
    EnumField[
        ImageColorProfileEnumAttrOperator, ImageColorProfileEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ImageColorProfileEnumAttrOperator
    PLUG_CLS = ImageColorProfileEnumPlugOperator


class DisplayColorProfileEnumPlugOperator(
    EnumPlugOperator["DisplayColorProfileEnumAttrOperator"]
):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10
    CINEON_LOG = 15


class DisplayColorProfileEnumAttrOperator(
    EnumAttrOperator[DisplayColorProfileEnumPlugOperator]
):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10
    CINEON_LOG = 15

    NAME_MAP = {
        LINEAR_SRGB: "Linear sRGB",
        SRGB: "sRGB",
        LINEAR_REC_709: "Linear Rec. 709",
        HDTV_REC_709: "HDTV (Rec. 709)",
        CIE_XYZ: "CIE XYZ",
        CINEON_LOG: "Cineon log",
    }


class DisplayColorProfileEnumField(
    EnumField[
        DisplayColorProfileEnumAttrOperator,
        DisplayColorProfileEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = DisplayColorProfileEnumAttrOperator
    PLUG_CLS = DisplayColorProfileEnumPlugOperator


class GeneratedViewColorManager(DG):
    __slots__ = ()

    NODE_TYPE = "viewColorManager"

    imageColorProfile = ImageColorProfileEnumField(default_value=3)
    ip = imageColorProfile

    displayColorProfile = DisplayColorProfileEnumField(default_value=3)
    dp = displayColorProfile

    exposure = FloatField(
        default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0
    )
    exp = exposure

    contrast = FloatField(
        default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0
    )
    c = contrast

    contrastPivot = FloatField(default_value=0.18000000715255737)
    cp = contrastPivot

    lutFile = DataStringField()
    lut = lutFile
