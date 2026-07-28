# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.clamp import (
    InputField,
    MaxField,
    MinField,
    OutputField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class RenderPassModeEnumPlugOperator(
    EnumPlugOperator["RenderPassModeEnumAttrOperator"]
):
    __slots__ = ()

    PASS_THROUGH = 0
    APPLY_TO_RENDER_PASSES = 1
    NO_CONTRIBUTION = 2
    WRITE_SHADER_RESULT_TO_BEAUTY_PASSES = 3


class RenderPassModeEnumAttrOperator(
    EnumAttrOperator[RenderPassModeEnumPlugOperator]
):
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


class GeneratedClamp(DG):
    __slots__ = ()

    NODE_TYPE = "clamp"

    min = MinField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    mn = min
    minR = min.minR
    mnr = minR
    minG = min.minG
    mng = minG
    minB = min.minB
    mnb = minB

    max = MaxField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    mx = max
    maxR = max.maxR
    mxr = maxR
    maxG = max.maxG
    mxg = maxG
    maxB = max.maxB
    mxb = maxB

    input = InputField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(5.0, 5.0, 5.0),
    )
    ip = input
    inputR = input.inputR
    ipr = inputR
    inputG = input.inputG
    ipg = inputG
    inputB = input.inputB
    ipb = inputB

    renderPassMode = RenderPassModeEnumField(default_value=1)
    arp = renderPassMode

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    op = output
    outputR = output.outputR
    opr = outputR
    outputG = output.outputG
    opg = outputG
    outputB = output.outputB
    opb = outputB
