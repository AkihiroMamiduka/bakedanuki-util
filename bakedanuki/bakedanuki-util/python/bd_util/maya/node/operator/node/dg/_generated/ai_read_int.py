# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_read_int import OutTransparencyField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiReadInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiReadInt"

    outValue = LongField(default_value=0, writable=False)
    out = outValue

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
