# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InRgbPlugOperator(Float3CompoundBasePlugOperator["InRgbAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRgbR", "ir"),
        ("inRgbG", "ig"),
        ("inRgbB", "ib"),
    )

    inRgbR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ir = inRgbR

    inRgbG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ig = inRgbG

    inRgbB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ib = inRgbB


class InRgbAttrOperator(Float3CompoundBaseAttrOperator[InRgbPlugOperator]):
    __slots__ = ()

    inRgbR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ir = inRgbR

    inRgbG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ig = inRgbG

    inRgbB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ib = inRgbB


class InRgbField(
    Float3CompoundBaseField[InRgbAttrOperator, InRgbPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InRgbAttrOperator
    PLUG_CLS = InRgbPlugOperator

    inRgbR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ir = inRgbR

    inRgbG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ig = inRgbG

    inRgbB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ib = inRgbB


class OutHsvPlugOperator(Float3CompoundBasePlugOperator["OutHsvAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outHsvH", "oh"),
        ("outHsvS", "os"),
        ("outHsvV", "ov"),
    )

    outHsvH = FloatField(default_value=0.0, writable=False)
    oh = outHsvH

    outHsvS = FloatField(default_value=0.0, writable=False)
    os = outHsvS

    outHsvV = FloatField(default_value=0.0, writable=False)
    ov = outHsvV


class OutHsvAttrOperator(Float3CompoundBaseAttrOperator[OutHsvPlugOperator]):
    __slots__ = ()

    outHsvH = FloatField(default_value=0.0, writable=False)
    oh = outHsvH

    outHsvS = FloatField(default_value=0.0, writable=False)
    os = outHsvS

    outHsvV = FloatField(default_value=0.0, writable=False)
    ov = outHsvV


class OutHsvField(
    Float3CompoundBaseField[OutHsvAttrOperator, OutHsvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutHsvAttrOperator
    PLUG_CLS = OutHsvPlugOperator

    outHsvH = FloatField(default_value=0.0, writable=False)
    oh = outHsvH

    outHsvS = FloatField(default_value=0.0, writable=False)
    os = outHsvS

    outHsvV = FloatField(default_value=0.0, writable=False)
    ov = outHsvV
