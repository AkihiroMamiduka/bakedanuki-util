# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.ai_compare_string import (
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class TestEnumPlugOperator(EnumPlugOperator["TestEnumAttrOperator"]):
    __slots__ = ()

    EQUAL_EQUAL = 0
    NOT_EQUAL = 1


class TestEnumAttrOperator(EnumAttrOperator[TestEnumPlugOperator]):
    __slots__ = ()

    EQUAL_EQUAL = 0
    NOT_EQUAL = 1

    NAME_MAP = {
        EQUAL_EQUAL: "==",
        NOT_EQUAL: "!=",
    }


class TestEnumField(EnumField[TestEnumAttrOperator, TestEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TestEnumAttrOperator
    PLUG_CLS = TestEnumPlugOperator


class GeneratedAiCompareString(DG):
    __slots__ = ()

    NODE_TYPE = "aiCompareString"

    outValue = BoolField(default_value=False, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    test = TestEnumField(default_value=0)

    input1 = DataStringField()

    input2 = DataStringField()
