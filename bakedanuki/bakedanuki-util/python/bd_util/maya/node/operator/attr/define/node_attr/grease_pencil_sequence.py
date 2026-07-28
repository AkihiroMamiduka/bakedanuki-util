# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.unit.time import TimeField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "clr"),
        ("colorG", "clg"),
        ("colorB", "clb"),
    )

    colorR = FloatField(default_value=0.5609999895095825)
    clr = colorR

    colorG = FloatField(default_value=0.7570000290870667)
    clg = colorG

    colorB = FloatField(default_value=0.8119999766349792)
    clb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.5609999895095825)
    clr = colorR

    colorG = FloatField(default_value=0.7570000290870667)
    clg = colorG

    colorB = FloatField(default_value=0.8119999766349792)
    clb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.5609999895095825)
    clr = colorR

    colorG = FloatField(default_value=0.7570000290870667)
    clg = colorG

    colorB = FloatField(default_value=0.8119999766349792)
    clb = colorB


class FramePlugOperator(CompoundPlugOperator["FrameAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frameTime", "ftv"),
        ("frameLabel", "fl"),
        ("frameImage", "fim"),
        ("frameAlpha", "fal"),
        ("frameEnable", "fen"),
    )

    frameTime = TimeField(default_value=0.0)
    ftv = frameTime

    frameLabel = DataStringField()
    fl = frameLabel

    frameImage = MessageField()
    fim = frameImage

    frameAlpha = FloatField(default_value=0.0)
    fal = frameAlpha

    frameEnable = BoolField(default_value=False)
    fen = frameEnable


class FrameAttrOperator(CompoundAttrOperator[FramePlugOperator]):
    __slots__ = ()

    frameTime = TimeField(default_value=0.0)
    ftv = frameTime

    frameLabel = DataStringField()
    fl = frameLabel

    frameImage = MessageField()
    fim = frameImage

    frameAlpha = FloatField(default_value=0.0)
    fal = frameAlpha

    frameEnable = BoolField(default_value=False)
    fen = frameEnable


class FrameField(CompoundField[FrameAttrOperator, FramePlugOperator]):
    __slots__ = ()

    ATTR_CLS = FrameAttrOperator
    PLUG_CLS = FramePlugOperator
