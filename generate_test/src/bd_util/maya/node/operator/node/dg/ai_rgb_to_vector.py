# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_rgb_to_vector import (
    InputField,
    OutTransparencyField,
    OutValueField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RAW = 0
    CANONICAL = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RAW = 0
    CANONICAL = 1

    NAME_MAP = {
        RAW: "raw",
        CANONICAL: "canonical",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class AiRgbToVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiRgbToVector"

    outValue = OutValueField()
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

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

    mode = ModeEnumField()
