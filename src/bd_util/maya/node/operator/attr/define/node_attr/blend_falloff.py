# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.typed import TypedField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_OPERATION = 0
    MULTIPLY = 1
    DIVIDE = 2
    ADD = 3
    SUBTRACT = 4
    OVERRIDE = 5
    MAX = 6
    ALPHABLEND = 7


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_OPERATION = 0
    MULTIPLY = 1
    DIVIDE = 2
    ADD = 3
    SUBTRACT = 4
    OVERRIDE = 5
    MAX = 6
    ALPHABLEND = 7

    NAME_MAP = {
        NO_OPERATION: "No Operation",
        MULTIPLY: "Multiply",
        DIVIDE: "Divide",
        ADD: "Add",
        SUBTRACT: "Subtract",
        OVERRIDE: "Override",
        MAX: "Max",
        ALPHABLEND: "AlphaBlend",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mode", "mod"),
        ("weight", "wgt"),
        ("weightFunction", "whf"),
    )

    mode = ModeEnumField()
    mod = mode

    weight = DoubleField()
    wgt = weight

    weightFunction = TypedField()
    whf = weightFunction


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    mode = ModeEnumField()
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
