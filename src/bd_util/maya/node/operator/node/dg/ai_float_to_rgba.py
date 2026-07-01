# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_float_to_rgba import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiFloatToRgba(DG):
    __slots__ = ()

    NODE_TYPE = "aiFloatToRgba"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    r = FloatField()

    g = FloatField()

    b = FloatField()

    a = FloatField()
