# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_motion_vector import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedAiMotionVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiMotionVector"

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

    raw = BoolField(default_value=False)

    time0 = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    time1 = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    maxDisplace = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    max_displace = maxDisplace
