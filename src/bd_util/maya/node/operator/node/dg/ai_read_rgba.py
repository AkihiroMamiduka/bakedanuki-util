# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_read_rgba import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiReadRGBA(DG):
    __slots__ = ()

    NODE_TYPE = "aiReadRGBA"

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

    aovName = DataStringField()
    aov_name = aovName
