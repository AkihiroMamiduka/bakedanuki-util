# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class WhitepointPlugOperator(
    Float3CompoundBasePlugOperator["WhitepointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("whitepointR", "wpr"),
        ("whitepointG", "wpg"),
        ("whitepointB", "wpb"),
    )

    whitepointR = FloatField()
    wpr = whitepointR

    whitepointG = FloatField()
    wpg = whitepointG

    whitepointB = FloatField()
    wpb = whitepointB


class WhitepointAttrOperator(
    Float3CompoundBaseAttrOperator[WhitepointPlugOperator]
):
    __slots__ = ()

    whitepointR = FloatField()
    wpr = whitepointR

    whitepointG = FloatField()
    wpg = whitepointG

    whitepointB = FloatField()
    wpb = whitepointB


class WhitepointField(
    Float3CompoundBaseField[WhitepointAttrOperator, WhitepointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WhitepointAttrOperator
    PLUG_CLS = WhitepointPlugOperator

    whitepointR = FloatField()
    wpr = whitepointR

    whitepointG = FloatField()
    wpg = whitepointG

    whitepointB = FloatField()
    wpb = whitepointB


class TransformPlugOperator(
    CompoundPlugOperator["TransformAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transformRow1", "tr1"),
        ("transformRow2", "tr2"),
        ("transformRow3", "tr3"),
    )

    transformRow1 = Float3Field()
    tr1 = transformRow1

    transformRow2 = Float3Field()
    tr2 = transformRow2

    transformRow3 = Float3Field()
    tr3 = transformRow3


class TransformAttrOperator(
    CompoundAttrOperator[TransformPlugOperator]
):
    __slots__ = ()

    transformRow1 = Float3Field()
    tr1 = transformRow1

    transformRow2 = Float3Field()
    tr2 = transformRow2

    transformRow3 = Float3Field()
    tr3 = transformRow3


class TransformField(
    CompoundField[TransformAttrOperator, TransformPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformAttrOperator
    PLUG_CLS = TransformPlugOperator

    transformRow1 = Float3Field()
    tr1 = transformRow1

    transformRow2 = Float3Field()
    tr2 = transformRow2

    transformRow3 = Float3Field()
    tr3 = transformRow3
