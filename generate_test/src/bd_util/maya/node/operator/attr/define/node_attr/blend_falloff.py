# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.typed import TypedField


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mode", "mod"),
        ("weight", "wgt"),
        ("weightFunction", "whf"),
    )

    mode = EnumField()
    mod = mode

    weight = DoubleField()
    wgt = weight

    weightFunction = TypedField()
    whf = weightFunction


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    mode = EnumField()
    mod = mode

    weight = DoubleField()
    wgt = weight

    weightFunction = TypedField()
    whf = weightFunction


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator
