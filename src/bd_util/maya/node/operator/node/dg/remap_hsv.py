# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.remap_hsv import (
    ColorField,
    HueField,
    OutColorField,
    SaturationField,
    ValueField,
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


class RemapHsv(DG):
    __slots__ = ()

    NODE_TYPE = "remapHsv"

    color = ColorField()
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    inputMin = FloatField()
    imn = inputMin

    inputMax = FloatField()
    imx = inputMax

    outputMin = FloatField()
    omn = outputMin

    outputMax = FloatField()
    omx = outputMax

    hue = HueField(multi=True)
    h = hue

    saturation = SaturationField(multi=True)
    s = saturation

    value = ValueField(multi=True)
    v = value

    renderPassMode = RenderPassModeEnumField()
    arp = renderPassMode

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
