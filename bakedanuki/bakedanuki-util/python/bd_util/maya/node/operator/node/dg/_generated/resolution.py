# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class FieldsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    ODD = 1
    EVEN = 2
    BOTH_INTERLACED = 3
    BOTH_SEPARATE = 4


class FieldsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    ODD = 1
    EVEN = 2
    BOTH_INTERLACED = 3
    BOTH_SEPARATE = 4

    NAME_MAP = {
        NONE: "None",
        ODD: "Odd",
        EVEN: "Even",
        BOTH_INTERLACED: "Both, Interlaced",
        BOTH_SEPARATE: "Both, Separate",
    }


class FieldsEnumField(
    EnumField[FieldsEnumAttrOperator, FieldsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldsEnumAttrOperator
    PLUG_CLS = FieldsEnumPlugOperator


class ZerothScanlineEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AT_TOP = 0
    AT_BOTTOM = 1


class ZerothScanlineEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AT_TOP = 0
    AT_BOTTOM = 1

    NAME_MAP = {
        AT_TOP: "At Top",
        AT_BOTTOM: "At Bottom",
    }


class ZerothScanlineEnumField(
    EnumField[ZerothScanlineEnumAttrOperator, ZerothScanlineEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ZerothScanlineEnumAttrOperator
    PLUG_CLS = ZerothScanlineEnumPlugOperator


class ImageSizeUnitsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PIXELS = 0
    INCHES = 1
    CM = 2
    MM = 3
    POINTS = 4
    PICAS = 5


class ImageSizeUnitsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PIXELS = 0
    INCHES = 1
    CM = 2
    MM = 3
    POINTS = 4
    PICAS = 5

    NAME_MAP = {
        PIXELS: "pixels",
        INCHES: "inches",
        CM: "cm",
        MM: "mm",
        POINTS: "points",
        PICAS: "picas",
    }


class ImageSizeUnitsEnumField(
    EnumField[ImageSizeUnitsEnumAttrOperator, ImageSizeUnitsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageSizeUnitsEnumAttrOperator
    PLUG_CLS = ImageSizeUnitsEnumPlugOperator


class PixelDensityUnitsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PIXELS_SLASH_INCH = 0
    PIXELS_SLASH_CM = 1


class PixelDensityUnitsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PIXELS_SLASH_INCH = 0
    PIXELS_SLASH_CM = 1

    NAME_MAP = {
        PIXELS_SLASH_INCH: "pixels/inch",
        PIXELS_SLASH_CM: "pixels/cm",
    }


class PixelDensityUnitsEnumField(
    EnumField[PixelDensityUnitsEnumAttrOperator, PixelDensityUnitsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PixelDensityUnitsEnumAttrOperator
    PLUG_CLS = PixelDensityUnitsEnumPlugOperator


class _GeneratedResolution(DG):
    __slots__ = ()

    NODE_TYPE = "resolution"

    width = LongField(default_value=960, min_value=2, soft_min_value=128, soft_max_value=8192)
    w = width

    height = LongField(default_value=540, min_value=2, soft_min_value=128, soft_max_value=8192)
    h = height

    pixelAspect = FloatField(default_value=0.0)
    pa = pixelAspect

    aspectLock = BoolField(default_value=False)
    al = aspectLock

    deviceAspectRatio = FloatField(default_value=1.7777776718139648, min_value=0.0, soft_max_value=10.0)
    dar = deviceAspectRatio

    lockDeviceAspectRatio = BoolField(default_value=False)
    ldar = lockDeviceAspectRatio

    dotsPerInch = FloatField(default_value=72.0, min_value=1.0)
    dpi = dotsPerInch

    oddFieldFirst = BoolField(default_value=True)
    off = oddFieldFirst

    fields = FieldsEnumField(default_value=0)
    fld = fields

    zerothScanline = ZerothScanlineEnumField(default_value=0)
    zsl = zerothScanline

    imageSizeUnits = ImageSizeUnitsEnumField(default_value=0)
    isu = imageSizeUnits

    pixelDensityUnits = PixelDensityUnitsEnumField(default_value=0)
    pdu = pixelDensityUnits
