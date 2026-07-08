# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_read_rgb import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.dt.string import DataStringField


class AiReadRGB(DG):
    __slots__ = ()

    NODE_TYPE = "aiReadRGB"

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

    aovName = DataStringField()
    aov_name = aovName
