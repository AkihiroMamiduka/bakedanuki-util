# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_random import (
    InputColorField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class InputTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INT = 0
    FLOAT = 1
    COLOR = 2


class InputTypeEnumAttrOperator(EnumAttrOperator):
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


class AiRandom(DG):
    __slots__ = ()

    NODE_TYPE = "aiRandom"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    inputType = InputTypeEnumField()
    input_type = inputType

    inputInt = LongField()
    input_int = inputInt

    inputFloat = FloatField()
    input_float = inputFloat

    inputColor = InputColorField()
    input_color = inputColor
    inputColorR = inputColor.inputColorR
    input_colorr = inputColorR
    inputColorG = inputColor.inputColorG
    input_colorg = inputColorG
    inputColorB = inputColor.inputColorB
    input_colorb = inputColorB

    seed = LongField()

    grayscale = BoolField()
