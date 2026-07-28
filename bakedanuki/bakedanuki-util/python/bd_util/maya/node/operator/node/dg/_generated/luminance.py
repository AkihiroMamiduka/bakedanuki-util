# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.luminance import ValueField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


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
        WRITE_SHADER_RESULT_TO_BEAUTY_PASSES: (
            "Write Shader Result to Beauty Passes"
        ),
    }


class RenderPassModeEnumField(
    EnumField[RenderPassModeEnumAttrOperator, RenderPassModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderPassModeEnumAttrOperator
    PLUG_CLS = RenderPassModeEnumPlugOperator


class GeneratedLuminance(DG):
    __slots__ = ()

    NODE_TYPE = "luminance"

    value = ValueField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    v = value
    valueR = value.valueR
    vr = valueR
    valueG = value.valueG
    vg = valueG
    valueB = value.valueB
    vb = valueB

    renderPassMode = RenderPassModeEnumField(default_value=1)
    arp = renderPassMode

    outValue = FloatField(default_value=0.0, writable=False)
    o = outValue
