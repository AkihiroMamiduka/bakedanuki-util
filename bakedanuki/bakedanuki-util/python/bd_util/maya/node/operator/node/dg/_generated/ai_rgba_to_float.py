# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_rgba_to_float import (
    InputField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    MIN = 0
    MAX = 1
    AVERAGE = 2
    SUM = 3
    LUMINANCE = 4
    R = 5
    G = 6
    B = 7
    A = 8


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    MIN = 0
    MAX = 1
    AVERAGE = 2
    SUM = 3
    LUMINANCE = 4
    R = 5
    G = 6
    B = 7
    A = 8

    NAME_MAP = {
        MIN: "min",
        MAX: "max",
        AVERAGE: "average",
        SUM: "sum",
        LUMINANCE: "luminance",
        R: "r",
        G: "g",
        B: "b",
        A: "a",
    }


class ModeEnumField(EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class GeneratedAiRgbaToFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiRgbaToFloat"

    outValue = FloatField(default_value=0.0, writable=False)
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

    inputA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    inputa = inputA

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    mode = ModeEnumField(default_value=2)
