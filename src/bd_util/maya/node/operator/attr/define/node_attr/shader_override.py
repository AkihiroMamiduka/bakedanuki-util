# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class AttrValuePlugOperator(
    Float3CompoundBasePlugOperator["AttrValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrValueR", "atvr"),
        ("attrValueG", "atvg"),
        ("attrValueB", "atvb"),
    )

    attrValueR = FloatField()
    atvr = attrValueR

    attrValueG = FloatField()
    atvg = attrValueG

    attrValueB = FloatField()
    atvb = attrValueB


class AttrValueAttrOperator(
    Float3CompoundBaseAttrOperator[AttrValuePlugOperator]
):
    __slots__ = ()

    attrValueR = FloatField()
    atvr = attrValueR

    attrValueG = FloatField()
    atvg = attrValueG

    attrValueB = FloatField()
    atvb = attrValueB


class AttrValueField(
    Float3CompoundBaseField[AttrValueAttrOperator, AttrValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttrValueAttrOperator
    PLUG_CLS = AttrValuePlugOperator

    attrValueR = FloatField()
    atvr = attrValueR

    attrValueG = FloatField()
    atvg = attrValueG

    attrValueB = FloatField()
    atvb = attrValueB
