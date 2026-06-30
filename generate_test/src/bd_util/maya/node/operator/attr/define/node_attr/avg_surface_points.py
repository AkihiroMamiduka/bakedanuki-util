# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class ResultPlugOperator(
    CompoundPlugOperator["ResultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("normal", "n"),
    )

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal


class ResultAttrOperator(
    CompoundAttrOperator[ResultPlugOperator]
):
    __slots__ = ()

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal


class ResultField(
    CompoundField[ResultAttrOperator, ResultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal
