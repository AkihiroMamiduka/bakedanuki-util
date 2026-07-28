# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.gamma_correct import (
    GammaField,
    OutValueField,
    ValueField,
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


class GeneratedGammaCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "gammaCorrect"

    value = ValueField(default_value=(0.0, 0.0, 0.0))
    v = value
    valueX = value.valueX
    vx = valueX
    valueY = value.valueY
    vy = valueY
    valueZ = value.valueZ
    vz = valueZ

    gamma = GammaField(
        default_value=(1.0, 1.0, 1.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(5.0, 5.0, 5.0),
    )
    g = gamma
    gammaX = gamma.gammaX
    gx = gammaX
    gammaY = gamma.gammaY
    gy = gammaY
    gammaZ = gamma.gammaZ
    gz = gammaZ

    renderPassMode = RenderPassModeEnumField(default_value=1)
    arp = renderPassMode

    outValue = OutValueField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = outValue
    outValueX = outValue.outValueX
    ox = outValueX
    outValueY = outValue.outValueY
    oy = outValueY
    outValueZ = outValue.outValueZ
    oz = outValueZ
