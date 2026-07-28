# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InHsvPlugOperator(Float3CompoundBasePlugOperator["InHsvAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inHsvR", "ir"),
        ("inHsvG", "ig"),
        ("inHsvB", "ib"),
    )

    inHsvR = FloatField(default_value=0.0, min_value=0.0, max_value=360.0)
    ir = inHsvR

    inHsvG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ig = inHsvG

    inHsvB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ib = inHsvB


class InHsvAttrOperator(Float3CompoundBaseAttrOperator[InHsvPlugOperator]):
    __slots__ = ()

    inHsvR = FloatField(default_value=0.0, min_value=0.0, max_value=360.0)
    ir = inHsvR

    inHsvG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ig = inHsvG

    inHsvB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ib = inHsvB


class InHsvField(
    Float3CompoundBaseField[InHsvAttrOperator, InHsvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InHsvAttrOperator
    PLUG_CLS = InHsvPlugOperator

    inHsvR = FloatField(default_value=0.0, min_value=0.0, max_value=360.0)
    ir = inHsvR

    inHsvG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ig = inHsvG

    inHsvB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ib = inHsvB


class OutRgbPlugOperator(Float3CompoundBasePlugOperator["OutRgbAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outRgbR", "or"),
        ("outRgbG", "og"),
        ("outRgbB", "ob"),
    )

    outRgbR = FloatField(default_value=0.0, writable=False)
    or_ = outRgbR

    outRgbG = FloatField(default_value=0.0, writable=False)
    og = outRgbG

    outRgbB = FloatField(default_value=0.0, writable=False)
    ob = outRgbB


class OutRgbAttrOperator(Float3CompoundBaseAttrOperator[OutRgbPlugOperator]):
    __slots__ = ()

    outRgbR = FloatField(default_value=0.0, writable=False)
    or_ = outRgbR

    outRgbG = FloatField(default_value=0.0, writable=False)
    og = outRgbG

    outRgbB = FloatField(default_value=0.0, writable=False)
    ob = outRgbB


class OutRgbField(
    Float3CompoundBaseField[OutRgbAttrOperator, OutRgbPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRgbAttrOperator
    PLUG_CLS = OutRgbPlugOperator

    outRgbR = FloatField(default_value=0.0, writable=False)
    or_ = outRgbR

    outRgbG = FloatField(default_value=0.0, writable=False)
    og = outRgbG

    outRgbB = FloatField(default_value=0.0, writable=False)
    ob = outRgbB
