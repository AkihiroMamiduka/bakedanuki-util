# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
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

    mode = ModeEnumField(default_value=1)
    mod = mode

    weight = DoubleField(default_value=1.0)
    wgt = weight

    weightFunction = TypedField()
    whf = weightFunction


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    mode = ModeEnumField(default_value=1)
    mod = mode

    weight = DoubleField(default_value=1.0)
    wgt = weight

    weightFunction = TypedField()
    whf = weightFunction


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator
