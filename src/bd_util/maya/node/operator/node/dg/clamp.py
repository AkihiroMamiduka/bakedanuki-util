# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.clamp import (
    InputField,
    MaxField,
    MinField,
    OutputField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class RenderPassModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PASS_THROUGH = 0
    APPLY_TO_RENDER_PASSES = 1
    NO_CONTRIBUTION = 2
    WRITE_SHADER_RESULT_TO_BEAUTY_PASSES = 3


class RenderPassModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PASS_THROUGH = 0
    APPLY_TO_RENDER_PASSES = 1
    NO_CONTRIBUTION = 2
    WRITE_SHADER_RESULT_TO_BEAUTY_PASSES = 3

    NAME_MAP = {
        PASS_THROUGH: "Pass through",
        APPLY_TO_RENDER_PASSES: "Apply to Render Passes",
        NO_CONTRIBUTION: "No Contribution",
        WRITE_SHADER_RESULT_TO_BEAUTY_PASSES: "Write Shader Result to Beauty Passes",
    }


class RenderPassModeEnumField(
    EnumField[RenderPassModeEnumAttrOperator, RenderPassModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderPassModeEnumAttrOperator
    PLUG_CLS = RenderPassModeEnumPlugOperator


class Clamp(DG):
    __slots__ = ()

    NODE_TYPE = "clamp"

    min = MinField()
    mn = min
    minR = min.minR
    mnr = minR
    minG = min.minG
    mng = minG
    minB = min.minB
    mnb = minB

    max = MaxField()
    mx = max
    maxR = max.maxR
    mxr = maxR
    maxG = max.maxG
    mxg = maxG
    maxB = max.maxB
    mxb = maxB

    input = InputField()
    ip = input
    inputR = input.inputR
    ipr = inputR
    inputG = input.inputG
    ipg = inputG
    inputB = input.inputB
    ipb = inputB

    renderPassMode = RenderPassModeEnumField()
    arp = renderPassMode

    output = OutputField()
    op = output
    outputR = output.outputR
    opr = outputR
    outputG = output.outputG
    opg = outputG
    outputB = output.outputB
    opb = outputB
