# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_blackbody import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiBlackbody(DG):
    __slots__ = ()

    NODE_TYPE = "aiBlackbody"

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

    temperature = FloatField(default_value=6500.0, min_value=0.0, soft_max_value=20000.0)

    normalize = BoolField(default_value=False)

    intensity = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
