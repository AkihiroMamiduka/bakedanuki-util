# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_color_convert import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class From_EnumPlugOperator(EnumPlugOperator["From_EnumAttrOperator"]):
    __slots__ = ()

    RGB = 0
    HSV = 1


class From_EnumAttrOperator(EnumAttrOperator[From_EnumPlugOperator]):
    __slots__ = ()

    RGB = 0
    HSV = 1

    NAME_MAP = {
        RGB: "RGB",
        HSV: "HSV",
    }


class From_EnumField(
    EnumField[From_EnumAttrOperator, From_EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = From_EnumAttrOperator
    PLUG_CLS = From_EnumPlugOperator


class ToEnumPlugOperator(EnumPlugOperator["ToEnumAttrOperator"]):
    __slots__ = ()

    RGB = 0
    HSV = 1


class ToEnumAttrOperator(EnumAttrOperator[ToEnumPlugOperator]):
    __slots__ = ()

    RGB = 0
    HSV = 1

    NAME_MAP = {
        RGB: "RGB",
        HSV: "HSV",
    }


class ToEnumField(
    EnumField[ToEnumAttrOperator, ToEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ToEnumAttrOperator
    PLUG_CLS = ToEnumPlugOperator


class GeneratedAiColorConvert(DG):
    __slots__ = ()

    NODE_TYPE = "aiColorConvert"

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

    input = InputField(default_value=(1.0, 1.0, 1.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    from_ = From_EnumField(default_value=0, long_name="from", short_name="from")

    to = ToEnumField(default_value=1)
