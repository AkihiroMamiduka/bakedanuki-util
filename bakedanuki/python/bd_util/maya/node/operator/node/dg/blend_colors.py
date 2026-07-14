# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.blend_colors import (
    Color1Field,
    Color2Field,
    OutputField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


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


class BlendColors(DG):
    __slots__ = ()

    NODE_TYPE = "blendColors"

    blender = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    b = blender

    color1 = Color1Field(default_value=(1.0, 0.0, 0.0), soft_min_value=(0.0, 0.0, 0.0), soft_max_value=(1.0, 1.0, 1.0))
    c1 = color1
    color1R = color1.color1R
    c1r = color1R
    color1G = color1.color1G
    c1g = color1G
    color1B = color1.color1B
    c1b = color1B

    color2 = Color2Field(default_value=(0.0, 0.0, 1.0), soft_min_value=(0.0, 0.0, 0.0), soft_max_value=(1.0, 1.0, 1.0))
    c2 = color2
    color2R = color2.color2R
    c2r = color2R
    color2G = color2.color2G
    c2g = color2G
    color2B = color2.color2B
    c2b = color2B

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
