# coding: utf-8

from typing import TYPE_CHECKING

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
from ..custom import (
    Double3Field,
    Double3PlugOperator,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class OperationEnumPlugOperator(EnumPlugOperator["OperationEnumAttrOperator"]):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class OperationEnumAttrOperator(EnumAttrOperator[OperationEnumPlugOperator]):
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


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class CasePlugOperator(CompoundPlugOperator["CaseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("operation", "op"),
        ("compare", "cmp"),
        ("value", "v"),
    )

    operation = OperationEnumField(default_value=0)
    op = operation

    compare = DoubleField(default_value=0.0)
    cmp = compare

    if TYPE_CHECKING:
        value: Double3PlugOperator
        v: Double3PlugOperator
    else:
        value = Double3Field(default_value=(0.0, 0.0, 0.0))
        v = value


class CaseAttrOperator(CompoundAttrOperator[CasePlugOperator]):
    __slots__ = ()

    operation = OperationEnumField(default_value=0)
    op = operation

    compare = DoubleField(default_value=0.0)
    cmp = compare

    value = Double3Field(default_value=(0.0, 0.0, 0.0))
    v = value


class CaseField(CompoundField[CaseAttrOperator, CasePlugOperator]):
    __slots__ = ()

    ATTR_CLS = CaseAttrOperator
    PLUG_CLS = CasePlugOperator


class ElseValuePlugOperator(
    Double3CompoundBasePlugOperator["ElseValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("elseValueX", "evx"),
        ("elseValueY", "evy"),
        ("elseValueZ", "evz"),
    )

    elseValueX = DoubleField(default_value=0.0)
    evx = elseValueX

    elseValueY = DoubleField(default_value=0.0)
    evy = elseValueY

    elseValueZ = DoubleField(default_value=0.0)
    evz = elseValueZ


class ElseValueAttrOperator(
    Double3CompoundBaseAttrOperator[ElseValuePlugOperator]
):
    __slots__ = ()

    elseValueX = DoubleField(default_value=0.0)
    evx = elseValueX

    elseValueY = DoubleField(default_value=0.0)
    evy = elseValueY

    elseValueZ = DoubleField(default_value=0.0)
    evz = elseValueZ


class ElseValueField(
    Double3CompoundBaseField[ElseValueAttrOperator, ElseValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ElseValueAttrOperator
    PLUG_CLS = ElseValuePlugOperator

    elseValueX = DoubleField(default_value=0.0)
    evx = elseValueX

    elseValueY = DoubleField(default_value=0.0)
    evy = elseValueY

    elseValueZ = DoubleField(default_value=0.0)
    evz = elseValueZ


class OutputPlugOperator(
    Double3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(Double3CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    Double3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ
