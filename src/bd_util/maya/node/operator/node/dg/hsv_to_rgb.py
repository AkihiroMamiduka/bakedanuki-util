# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hsv_to_rgb import (
    InHsvField,
    OutRgbField,
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


class HsvToRgb(DG):
    __slots__ = ()

    NODE_TYPE = "hsvToRgb"

    inHsv = InHsvField()
    i = inHsv
    inHsvR = inHsv.inHsvR
    ir = inHsvR
    inHsvG = inHsv.inHsvG
    ig = inHsvG
    inHsvB = inHsv.inHsvB
    ib = inHsvB

    renderPassMode = RenderPassModeEnumField()
    arp = renderPassMode

    outRgb = OutRgbField()
    o = outRgb
    outRgbR = outRgb.outRgbR
    or_ = outRgbR
    outRgbG = outRgb.outRgbG
    og = outRgbG
    outRgbB = outRgb.outRgbB
    ob = outRgbB
