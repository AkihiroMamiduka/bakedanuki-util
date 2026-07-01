# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class ImageColorProfileEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10


class ImageColorProfileEnumAttrOperator(EnumAttrOperator):
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
    EnumField[ImageColorProfileEnumAttrOperator, ImageColorProfileEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageColorProfileEnumAttrOperator
    PLUG_CLS = ImageColorProfileEnumPlugOperator


class DisplayColorProfileEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10
    CINEON_LOG = 15


class DisplayColorProfileEnumAttrOperator(EnumAttrOperator):
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
    EnumField[DisplayColorProfileEnumAttrOperator, DisplayColorProfileEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayColorProfileEnumAttrOperator
    PLUG_CLS = DisplayColorProfileEnumPlugOperator


class ViewColorManager(DG):
    __slots__ = ()

    NODE_TYPE = "viewColorManager"

    imageColorProfile = ImageColorProfileEnumField()
    ip = imageColorProfile

    displayColorProfile = DisplayColorProfileEnumField()
    dp = displayColorProfile

    exposure = FloatField()
    exp = exposure

    contrast = FloatField()
    c = contrast

    contrastPivot = FloatField()
    cp = contrastPivot

    lutFile = DataStringField()
    lut = lutFile
