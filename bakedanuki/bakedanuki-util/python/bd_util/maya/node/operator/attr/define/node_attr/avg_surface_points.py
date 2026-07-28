# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..custom import Double3Field


class ResultPlugOperator(CompoundPlugOperator["ResultAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("normal", "n"),
    )

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal


class ResultAttrOperator(CompoundAttrOperator[ResultPlugOperator]):
    __slots__ = ()

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal


class ResultField(CompoundField[ResultAttrOperator, ResultPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal
