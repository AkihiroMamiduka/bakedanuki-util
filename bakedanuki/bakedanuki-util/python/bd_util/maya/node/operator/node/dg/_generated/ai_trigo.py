# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_trigo import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class FunctionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    COS = 0
    SIN = 1
    TAN = 2
    ACOS = 3
    ASIN = 4
    ATAN = 5
    COSH = 6
    SINH = 7
    TANH = 8


class FunctionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    COS = 0
    SIN = 1
    TAN = 2
    ACOS = 3
    ASIN = 4
    ATAN = 5
    COSH = 6
    SINH = 7
    TANH = 8

    NAME_MAP = {
        COS: "cos",
        SIN: "sin",
        TAN: "tan",
        ACOS: "acos",
        ASIN: "asin",
        ATAN: "atan",
        COSH: "cosh",
        SINH: "sinh",
        TANH: "tanh",
    }


class FunctionEnumField(
    EnumField[FunctionEnumAttrOperator, FunctionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionEnumAttrOperator
    PLUG_CLS = FunctionEnumPlugOperator


class UnitsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1


class UnitsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1

    NAME_MAP = {
        RADIANS: "radians",
        DEGREES: "degrees",
    }


class UnitsEnumField(
    EnumField[UnitsEnumAttrOperator, UnitsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UnitsEnumAttrOperator
    PLUG_CLS = UnitsEnumPlugOperator


class _GeneratedAiTrigo(DG):
    __slots__ = ()

    NODE_TYPE = "aiTrigo"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    function = FunctionEnumField(default_value=0)

    units = UnitsEnumField(default_value=0)

    frequency = FloatField(default_value=1.0, soft_min_value=-5.0, soft_max_value=5.0)

    phase = FloatField(default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0)
