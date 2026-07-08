# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.remap_color import (
    BlueField,
    ColorField,
    GreenField,
    OutColorField,
    RedField,
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


class RemapColor(DG):
    __slots__ = ()

    NODE_TYPE = "remapColor"

    color = ColorField(default_value=(0.5, 0.5, 0.5))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    inputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    imn = inputMin

    inputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    imx = inputMax

    outputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omn = outputMin

    outputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    omx = outputMax

    red = RedField(multi=True, default_value=(0.0, 0.0, 0.0))
    r = red

    green = GreenField(multi=True, default_value=(0.0, 0.0, 0.0))
    g = green

    blue = BlueField(multi=True, default_value=(0.0, 0.0, 0.0))
    b = blue

    renderPassMode = RenderPassModeEnumField(default_value=1)
    arp = renderPassMode

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
