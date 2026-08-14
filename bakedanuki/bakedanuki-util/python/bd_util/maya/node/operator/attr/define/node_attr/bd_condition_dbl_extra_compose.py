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


class Output_outputLogicEnumPlugOperator(
    EnumPlugOperator["Output_outputLogicEnumAttrOperator"]
):
    __slots__ = ()

    AND = 0
    OR = 1


class Output_outputLogicEnumAttrOperator(
    EnumAttrOperator[Output_outputLogicEnumPlugOperator]
):
    __slots__ = ()

    AND = 0
    OR = 1

    NAME_MAP = {
        AND: "And",
        OR: "Or",
    }


class Output_outputLogicEnumField(
    EnumField[
        Output_outputLogicEnumAttrOperator, Output_outputLogicEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Output_outputLogicEnumAttrOperator
    PLUG_CLS = Output_outputLogicEnumPlugOperator


class Output_outputComparisonEnumPlugOperator(
    EnumPlugOperator["Output_outputComparisonEnumAttrOperator"]
):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class Output_outputComparisonEnumAttrOperator(
    EnumAttrOperator[Output_outputComparisonEnumPlugOperator]
):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5

    NAME_MAP = {
        EQUAL: "Equal",
        NOT_EQUAL: "Not Equal",
        GREATER_THAN: "Greater Than",
        GREATER_OR_EQUAL: "Greater or Equal",
        LESS_THAN: "Less Than",
        LESS_OR_EQUAL: "Less or Equal",
    }


class Output_outputComparisonEnumField(
    EnumField[
        Output_outputComparisonEnumAttrOperator,
        Output_outputComparisonEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Output_outputComparisonEnumAttrOperator
    PLUG_CLS = Output_outputComparisonEnumPlugOperator


class OutputPlugOperator(CompoundPlugOperator["OutputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputLogic", "olgc"),
        ("outputComparison", "ocpr"),
        ("outputCompareValue", "ocv"),
    )

    outputLogic = Output_outputLogicEnumField(default_value=0, writable=False)
    olgc = outputLogic

    outputComparison = Output_outputComparisonEnumField(
        default_value=0, writable=False
    )
    ocpr = outputComparison

    outputCompareValue = DoubleField(default_value=0.0, writable=False)
    ocv = outputCompareValue


class OutputAttrOperator(CompoundAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputLogic = Output_outputLogicEnumField(default_value=0, writable=False)
    olgc = outputLogic

    outputComparison = Output_outputComparisonEnumField(
        default_value=0, writable=False
    )
    ocpr = outputComparison

    outputCompareValue = DoubleField(default_value=0.0, writable=False)
    ocv = outputCompareValue


class OutputField(CompoundField[OutputAttrOperator, OutputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputLogic = Output_outputLogicEnumField(default_value=0, writable=False)
    olgc = outputLogic

    outputComparison = Output_outputComparisonEnumField(
        default_value=0, writable=False
    )
    ocpr = outputComparison

    outputCompareValue = DoubleField(default_value=0.0, writable=False)
    ocv = outputCompareValue
