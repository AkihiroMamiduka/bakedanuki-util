# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ErrorColorBadTexturePlugOperator(
    Float3CompoundBasePlugOperator["ErrorColorBadTextureAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("errorColorBadTextureR", "error_color_bad_texturer"),
        ("errorColorBadTextureG", "error_color_bad_textureg"),
        ("errorColorBadTextureB", "error_color_bad_textureb"),
    )

    errorColorBadTextureR = FloatField(default_value=1.0)
    error_color_bad_texturer = errorColorBadTextureR

    errorColorBadTextureG = FloatField(default_value=0.0)
    error_color_bad_textureg = errorColorBadTextureG

    errorColorBadTextureB = FloatField(default_value=0.0)
    error_color_bad_textureb = errorColorBadTextureB


class ErrorColorBadTextureAttrOperator(
    Float3CompoundBaseAttrOperator[ErrorColorBadTexturePlugOperator]
):
    __slots__ = ()

    errorColorBadTextureR = FloatField(default_value=1.0)
    error_color_bad_texturer = errorColorBadTextureR

    errorColorBadTextureG = FloatField(default_value=0.0)
    error_color_bad_textureg = errorColorBadTextureG

    errorColorBadTextureB = FloatField(default_value=0.0)
    error_color_bad_textureb = errorColorBadTextureB


class ErrorColorBadTextureField(
    Float3CompoundBaseField[ErrorColorBadTextureAttrOperator, ErrorColorBadTexturePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ErrorColorBadTextureAttrOperator
    PLUG_CLS = ErrorColorBadTexturePlugOperator

    errorColorBadTextureR = FloatField(default_value=1.0)
    error_color_bad_texturer = errorColorBadTextureR

    errorColorBadTextureG = FloatField(default_value=0.0)
    error_color_bad_textureg = errorColorBadTextureG

    errorColorBadTextureB = FloatField(default_value=0.0)
    error_color_bad_textureb = errorColorBadTextureB


class ErrorColorBadPixelPlugOperator(
    Float3CompoundBasePlugOperator["ErrorColorBadPixelAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("errorColorBadPixelR", "error_color_bad_pixelr"),
        ("errorColorBadPixelG", "error_color_bad_pixelg"),
        ("errorColorBadPixelB", "error_color_bad_pixelb"),
    )

    errorColorBadPixelR = FloatField(default_value=0.0)
    error_color_bad_pixelr = errorColorBadPixelR

    errorColorBadPixelG = FloatField(default_value=0.0)
    error_color_bad_pixelg = errorColorBadPixelG

    errorColorBadPixelB = FloatField(default_value=1.0)
    error_color_bad_pixelb = errorColorBadPixelB


class ErrorColorBadPixelAttrOperator(
    Float3CompoundBaseAttrOperator[ErrorColorBadPixelPlugOperator]
):
    __slots__ = ()

    errorColorBadPixelR = FloatField(default_value=0.0)
    error_color_bad_pixelr = errorColorBadPixelR

    errorColorBadPixelG = FloatField(default_value=0.0)
    error_color_bad_pixelg = errorColorBadPixelG

    errorColorBadPixelB = FloatField(default_value=1.0)
    error_color_bad_pixelb = errorColorBadPixelB


class ErrorColorBadPixelField(
    Float3CompoundBaseField[ErrorColorBadPixelAttrOperator, ErrorColorBadPixelPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ErrorColorBadPixelAttrOperator
    PLUG_CLS = ErrorColorBadPixelPlugOperator

    errorColorBadPixelR = FloatField(default_value=0.0)
    error_color_bad_pixelr = errorColorBadPixelR

    errorColorBadPixelG = FloatField(default_value=0.0)
    error_color_bad_pixelg = errorColorBadPixelG

    errorColorBadPixelB = FloatField(default_value=1.0)
    error_color_bad_pixelb = errorColorBadPixelB
