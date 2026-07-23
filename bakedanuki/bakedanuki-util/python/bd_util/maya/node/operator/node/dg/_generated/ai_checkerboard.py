# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_checkerboard import (
    Color1Field,
    Color2Field,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiCheckerboard(DG):
    __slots__ = ()

    NODE_TYPE = "aiCheckerboard"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    color1 = Color1Field(default_value=(1.0, 1.0, 1.0))
    color1R = color1.color1R
    color1r = color1R
    color1G = color1.color1G
    color1g = color1G
    color1B = color1.color1B
    color1b = color1B

    color2 = Color2Field(default_value=(0.0, 0.0, 0.0))
    color2R = color2.color2R
    color2r = color2R
    color2G = color2.color2G
    color2g = color2G
    color2B = color2.color2B
    color2b = color2B

    uFrequency = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    u_frequency = uFrequency

    vFrequency = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    v_frequency = vFrequency

    uOffset = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    u_offset = uOffset

    vOffset = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    v_offset = vOffset

    contrast = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    filterStrength = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    filter_strength = filterStrength

    filterOffset = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    filter_offset = filterOffset

    uvset = DataStringField()
