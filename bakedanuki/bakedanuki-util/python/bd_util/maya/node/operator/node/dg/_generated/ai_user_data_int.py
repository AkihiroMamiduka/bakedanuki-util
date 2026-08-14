# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_user_data_int import OutTransparencyField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiUserDataInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataInt"

    outValue = LongField(default_value=0, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    attribute = DataStringField()
    intAttrName = attribute

    default = LongField(default_value=0)
    defaultValue = default
