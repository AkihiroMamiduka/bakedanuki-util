# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_float_to_rgba import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedAiFloatToRgba(DG):
    __slots__ = ()

    NODE_TYPE = "aiFloatToRgba"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    r = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    g = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    b = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    a = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
