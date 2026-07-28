# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_random import (
    InputColorField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class InputTypeEnumPlugOperator(EnumPlugOperator["InputTypeEnumAttrOperator"]):
    __slots__ = ()

    INT = 0
    FLOAT = 1
    COLOR = 2


class InputTypeEnumAttrOperator(EnumAttrOperator[InputTypeEnumPlugOperator]):
    __slots__ = ()

    INT = 0
    FLOAT = 1
    COLOR = 2

    NAME_MAP = {
        INT: "int",
        FLOAT: "float",
        COLOR: "color",
    }


class InputTypeEnumField(
    EnumField[InputTypeEnumAttrOperator, InputTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputTypeEnumAttrOperator
    PLUG_CLS = InputTypeEnumPlugOperator


class GeneratedAiRandom(DG):
    __slots__ = ()

    NODE_TYPE = "aiRandom"

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

    inputType = InputTypeEnumField(default_value=0)
    input_type = inputType

    inputInt = LongField(default_value=0, soft_min_value=-100, soft_max_value=100)
    input_int = inputInt

    inputFloat = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    input_float = inputFloat

    inputColor = InputColorField(default_value=(0.0, 0.0, 0.0))
    input_color = inputColor
    inputColorR = inputColor.inputColorR
    input_colorr = inputColorR
    inputColorG = inputColor.inputColorG
    input_colorg = inputColorG
    inputColorB = inputColor.inputColorB
    input_colorb = inputColorB

    seed = LongField(default_value=0)

    grayscale = BoolField(default_value=False)
