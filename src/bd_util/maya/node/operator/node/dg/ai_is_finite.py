# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_is_finite import (
    InputField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class AiIsFinite(DG):
    __slots__ = ()

    NODE_TYPE = "aiIsFinite"

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

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB
