# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InRgbPlugOperator(
    Float3CompoundBasePlugOperator["InRgbAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRgbR", "ir"),
        ("inRgbG", "ig"),
        ("inRgbB", "ib"),
    )

    inRgbR = FloatField()
    ir = inRgbR

    inRgbG = FloatField()
    ig = inRgbG

    inRgbB = FloatField()
    ib = inRgbB


class InRgbAttrOperator(
    Float3CompoundBaseAttrOperator[InRgbPlugOperator]
):
    __slots__ = ()

    inRgbR = FloatField()
    ir = inRgbR

    inRgbG = FloatField()
    ig = inRgbG

    inRgbB = FloatField()
    ib = inRgbB


class InRgbField(
    Float3CompoundBaseField[InRgbAttrOperator, InRgbPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InRgbAttrOperator
    PLUG_CLS = InRgbPlugOperator

    inRgbR = FloatField()
    ir = inRgbR

    inRgbG = FloatField()
    ig = inRgbG

    inRgbB = FloatField()
    ib = inRgbB


class OutHsvPlugOperator(
    Float3CompoundBasePlugOperator["OutHsvAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outHsvH", "oh"),
        ("outHsvS", "os"),
        ("outHsvV", "ov"),
    )

    outHsvH = FloatField()
    oh = outHsvH

    outHsvS = FloatField()
    os = outHsvS

    outHsvV = FloatField()
    ov = outHsvV


class OutHsvAttrOperator(
    Float3CompoundBaseAttrOperator[OutHsvPlugOperator]
):
    __slots__ = ()

    outHsvH = FloatField()
    oh = outHsvH

    outHsvS = FloatField()
    os = outHsvS

    outHsvV = FloatField()
    ov = outHsvV


class OutHsvField(
    Float3CompoundBaseField[OutHsvAttrOperator, OutHsvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutHsvAttrOperator
    PLUG_CLS = OutHsvPlugOperator

    outHsvH = FloatField()
    oh = outHsvH

    outHsvS = FloatField()
    os = outHsvS

    outHsvV = FloatField()
    ov = outHsvV
