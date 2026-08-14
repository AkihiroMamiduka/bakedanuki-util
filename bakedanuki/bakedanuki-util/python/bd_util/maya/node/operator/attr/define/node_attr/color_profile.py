# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float3Field,
)


class WhitepointPlugOperator(
    Float3CompoundBasePlugOperator["WhitepointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("whitepointR", "wpr"),
        ("whitepointG", "wpg"),
        ("whitepointB", "wpb"),
    )

    whitepointR = FloatField(default_value=0.0)
    wpr = whitepointR

    whitepointG = FloatField(default_value=0.0)
    wpg = whitepointG

    whitepointB = FloatField(default_value=0.0)
    wpb = whitepointB


class WhitepointAttrOperator(
    Float3CompoundBaseAttrOperator[WhitepointPlugOperator]
):
    __slots__ = ()

    whitepointR = FloatField(default_value=0.0)
    wpr = whitepointR

    whitepointG = FloatField(default_value=0.0)
    wpg = whitepointG

    whitepointB = FloatField(default_value=0.0)
    wpb = whitepointB


class WhitepointField(
    Float3CompoundBaseField[WhitepointAttrOperator, WhitepointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WhitepointAttrOperator
    PLUG_CLS = WhitepointPlugOperator

    whitepointR = FloatField(default_value=0.0)
    wpr = whitepointR

    whitepointG = FloatField(default_value=0.0)
    wpg = whitepointG

    whitepointB = FloatField(default_value=0.0)
    wpb = whitepointB


class TransformPlugOperator(CompoundPlugOperator["TransformAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transformRow1", "tr1"),
        ("transformRow2", "tr2"),
        ("transformRow3", "tr3"),
    )

    transformRow1 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr1 = transformRow1

    transformRow2 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr2 = transformRow2

    transformRow3 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr3 = transformRow3


class TransformAttrOperator(CompoundAttrOperator[TransformPlugOperator]):
    __slots__ = ()

    transformRow1 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr1 = transformRow1

    transformRow2 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr2 = transformRow2

    transformRow3 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr3 = transformRow3


class TransformField(
    CompoundField[TransformAttrOperator, TransformPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformAttrOperator
    PLUG_CLS = TransformPlugOperator

    transformRow1 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr1 = transformRow1

    transformRow2 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr2 = transformRow2

    transformRow3 = Float3Field(default_value=(0.0, 0.0, 0.0))
    tr3 = transformRow3
