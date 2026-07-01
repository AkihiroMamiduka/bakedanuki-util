# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.rgb_to_hsv import (
    InRgbField,
    OutHsvField,
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


class RgbToHsv(DG):
    __slots__ = ()

    NODE_TYPE = "rgbToHsv"

    inRgb = InRgbField()
    i = inRgb
    inRgbR = inRgb.inRgbR
    ir = inRgbR
    inRgbG = inRgb.inRgbG
    ig = inRgbG
    inRgbB = inRgb.inRgbB
    ib = inRgbB

    renderPassMode = RenderPassModeEnumField()
    arp = renderPassMode

    outHsv = OutHsvField()
    o = outHsv
    outHsvH = outHsv.outHsvH
    oh = outHsvH
    outHsvS = outHsv.outHsvS
    os = outHsvS
    outHsvV = outHsv.outHsvV
    ov = outHsvV
