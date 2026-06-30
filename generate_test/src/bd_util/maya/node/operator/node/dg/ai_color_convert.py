# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_color_convert import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class FromEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RGB = 0
    HSV = 1


class FromEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RGB = 0
    HSV = 1

    NAME_MAP = {
        RGB: "RGB",
        HSV: "HSV",
    }


class FromEnumField(
    EnumField[FromEnumAttrOperator, FromEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FromEnumAttrOperator
    PLUG_CLS = FromEnumPlugOperator


class ToEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RGB = 0
    HSV = 1


class ToEnumAttrOperator(EnumAttrOperator):
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


class AiColorConvert(DG):
    __slots__ = ()

    NODE_TYPE = "aiColorConvert"

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

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    from_ = FromEnumField()

    to = ToEnumField()
