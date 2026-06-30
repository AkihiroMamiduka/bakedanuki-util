# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_motion_vector import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiMotionVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiMotionVector"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    raw = BoolField()

    time0 = FloatField()

    time1 = FloatField()

    maxDisplace = FloatField()
    max_displace = maxDisplace
