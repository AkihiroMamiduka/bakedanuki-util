# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InHsvPlugOperator(
    Float3CompoundBasePlugOperator["InHsvAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inHsvR", "ir"),
        ("inHsvG", "ig"),
        ("inHsvB", "ib"),
    )

    inHsvR = FloatField()
    ir = inHsvR

    inHsvG = FloatField()
    ig = inHsvG

    inHsvB = FloatField()
    ib = inHsvB


class InHsvAttrOperator(
    Float3CompoundBaseAttrOperator[InHsvPlugOperator]
):
    __slots__ = ()

    inHsvR = FloatField()
    ir = inHsvR

    inHsvG = FloatField()
    ig = inHsvG

    inHsvB = FloatField()
    ib = inHsvB


class InHsvField(
    Float3CompoundBaseField[InHsvAttrOperator, InHsvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InHsvAttrOperator
    PLUG_CLS = InHsvPlugOperator

    inHsvR = FloatField()
    ir = inHsvR

    inHsvG = FloatField()
    ig = inHsvG

    inHsvB = FloatField()
    ib = inHsvB


class OutRgbPlugOperator(
    Float3CompoundBasePlugOperator["OutRgbAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outRgbR", "or"),
        ("outRgbG", "og"),
        ("outRgbB", "ob"),
    )

    outRgbR = FloatField()
    or_ = outRgbR

    outRgbG = FloatField()
    og = outRgbG

    outRgbB = FloatField()
    ob = outRgbB


class OutRgbAttrOperator(
    Float3CompoundBaseAttrOperator[OutRgbPlugOperator]
):
    __slots__ = ()

    outRgbR = FloatField()
    or_ = outRgbR

    outRgbG = FloatField()
    og = outRgbG

    outRgbB = FloatField()
    ob = outRgbB


class OutRgbField(
    Float3CompoundBaseField[OutRgbAttrOperator, OutRgbPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRgbAttrOperator
    PLUG_CLS = OutRgbPlugOperator

    outRgbR = FloatField()
    or_ = outRgbR

    outRgbG = FloatField()
    og = outRgbG

    outRgbB = FloatField()
    ob = outRgbB
