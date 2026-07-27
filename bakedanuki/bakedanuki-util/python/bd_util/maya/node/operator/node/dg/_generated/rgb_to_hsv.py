# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.rgb_to_hsv import (
    InRgbField,
    OutHsvField,
)
from ....attr.define.std.at.scalar.enum import (
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


class GeneratedRgbToHsv(DG):
    __slots__ = ()

    NODE_TYPE = "rgbToHsv"

    inRgb = InRgbField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    i = inRgb
    inRgbR = inRgb.inRgbR
    ir = inRgbR
    inRgbG = inRgb.inRgbG
    ig = inRgbG
    inRgbB = inRgb.inRgbB
    ib = inRgbB

    renderPassMode = RenderPassModeEnumField(default_value=1)
    arp = renderPassMode

    outHsv = OutHsvField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = outHsv
    outHsvH = outHsv.outHsvH
    oh = outHsvH
    outHsvS = outHsv.outHsvS
    os = outHsvS
    outHsvV = outHsv.outHsvV
    ov = outHsvV
