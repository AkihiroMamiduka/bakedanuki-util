# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_read_int import OutTransparencyField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class AiReadInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiReadInt"

    outValue = LongField()
    out = outValue

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
