# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value", "v"),
        ("weight", "w"),
    )

    value = DoubleField(default_value=0.0)
    v = value

    weight = DoubleField(default_value=0.0)
    w = weight


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    value = DoubleField(default_value=0.0)
    v = value

    weight = DoubleField(default_value=0.0)
    w = weight


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator
