# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.unit_scalar.time import TimeField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "clr"),
        ("colorG", "clg"),
        ("colorB", "clb"),
    )

    colorR = FloatField()
    clr = colorR

    colorG = FloatField()
    clg = colorG

    colorB = FloatField()
    clb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    clr = colorR

    colorG = FloatField()
    clg = colorG

    colorB = FloatField()
    clb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    clr = colorR

    colorG = FloatField()
    clg = colorG

    colorB = FloatField()
    clb = colorB


class FramePlugOperator(
    CompoundPlugOperator["FrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frameTime", "ftv"),
        ("frameLabel", "fl"),
        ("frameImage", "fim"),
        ("frameAlpha", "fal"),
        ("frameEnable", "fen"),
    )

    frameTime = TimeField()
    ftv = frameTime

    frameLabel = DataStringField()
    fl = frameLabel

    frameImage = MessageField()
    fim = frameImage

    frameAlpha = FloatField()
    fal = frameAlpha

    frameEnable = BoolField()
    fen = frameEnable


class FrameAttrOperator(
    CompoundAttrOperator[FramePlugOperator]
):
    __slots__ = ()

    frameTime = TimeField()
    ftv = frameTime

    frameLabel = DataStringField()
    fl = frameLabel

    frameImage = MessageField()
    fim = frameImage

    frameAlpha = FloatField()
    fal = frameAlpha

    frameEnable = BoolField()
    fen = frameEnable


class FrameField(
    CompoundField[FrameAttrOperator, FramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrameAttrOperator
    PLUG_CLS = FramePlugOperator
