# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value", "v"),
        ("weight", "w"),
    )

    value = DoubleAngleField(default_value=0.0)
    v = value

    weight = DoubleField(default_value=0.0)
    w = weight


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    value = DoubleAngleField(default_value=0.0)
    v = value

    weight = DoubleField(default_value=0.0)
    w = weight


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator
