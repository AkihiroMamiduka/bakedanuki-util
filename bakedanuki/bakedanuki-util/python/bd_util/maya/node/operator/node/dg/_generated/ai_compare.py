# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_compare import OutTransparencyField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class TestEnumPlugOperator(EnumPlugOperator["TestEnumAttrOperator"]):
    __slots__ = ()

    EQUAL_EQUAL = 0
    NOT_EQUAL = 1
    LESS = 2
    GREATER = 3
    LESS_EQUAL = 4
    GREATER_EQUAL = 5


class TestEnumAttrOperator(EnumAttrOperator[TestEnumPlugOperator]):
    __slots__ = ()

    EQUAL_EQUAL = 0
    NOT_EQUAL = 1
    LESS = 2
    GREATER = 3
    LESS_EQUAL = 4
    GREATER_EQUAL = 5

    NAME_MAP = {
        EQUAL_EQUAL: "==",
        NOT_EQUAL: "!=",
        LESS: "<",
        GREATER: ">",
        LESS_EQUAL: "<=",
        GREATER_EQUAL: ">=",
    }


class TestEnumField(
    EnumField[TestEnumAttrOperator, TestEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TestEnumAttrOperator
    PLUG_CLS = TestEnumPlugOperator


class GeneratedAiCompare(DG):
    __slots__ = ()

    NODE_TYPE = "aiCompare"

    outValue = BoolField(default_value=False, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    test = TestEnumField(default_value=0)

    input1 = FloatField(default_value=0.0)

    input2 = FloatField(default_value=0.0)
