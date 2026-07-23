# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_is_finite import (
    InputField,
    OutTransparencyField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField


class _GeneratedAiIsFinite(DG):
    __slots__ = ()

    NODE_TYPE = "aiIsFinite"

    outValue = BoolField(default_value=False, writable=False)
    out = outValue

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
