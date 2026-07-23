# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_length import (
    InputField,
    OutTransparencyField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MANHATTAN = 0
    EUCLIDIAN = 1
    QUADRANCE = 2


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MANHATTAN = 0
    EUCLIDIAN = 1
    QUADRANCE = 2

    NAME_MAP = {
        MANHATTAN: "manhattan",
        EUCLIDIAN: "euclidian",
        QUADRANCE: "quadrance",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class _GeneratedAiLength(DG):
    __slots__ = ()

    NODE_TYPE = "aiLength"

    outValue = FloatField(default_value=0.0, writable=False)
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
    inputX = input.inputX
    inputx = inputX
    inputY = input.inputY
    inputy = inputY
    inputZ = input.inputZ
    inputz = inputZ

    mode = ModeEnumField(default_value=1)
