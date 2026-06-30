# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_compare import OutTransparencyField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class TestEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EQUAL_EQUAL = 0
    NOT_EQUAL = 1
    LESS = 2
    GREATER = 3
    LESS_EQUAL = 4
    GREATER_EQUAL = 5


class TestEnumAttrOperator(EnumAttrOperator):
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


class AiCompare(DG):
    __slots__ = ()

    NODE_TYPE = "aiCompare"

    outValue = BoolField()
    out = outValue

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    test = TestEnumField()

    input1 = FloatField()

    input2 = FloatField()
