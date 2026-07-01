# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


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


class Resolution(DG):
    __slots__ = ()

    NODE_TYPE = "resolution"

    width = LongField()
    w = width

    height = LongField()
    h = height

    pixelAspect = FloatField()
    pa = pixelAspect

    aspectLock = BoolField()
    al = aspectLock

    deviceAspectRatio = FloatField()
    dar = deviceAspectRatio

    lockDeviceAspectRatio = BoolField()
    ldar = lockDeviceAspectRatio

    dotsPerInch = FloatField()
    dpi = dotsPerInch

    oddFieldFirst = BoolField()
    off = oddFieldFirst

    fields = FieldsEnumField()
    fld = fields

    zerothScanline = ZerothScanlineEnumField()
    zsl = zerothScanline

    imageSizeUnits = ImageSizeUnitsEnumField()
    isu = imageSizeUnits

    pixelDensityUnits = PixelDensityUnitsEnumField()
    pdu = pixelDensityUnits
