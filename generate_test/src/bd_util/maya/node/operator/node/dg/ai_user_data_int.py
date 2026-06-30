# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_user_data_int import OutTransparencyField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class AiUserDataInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataInt"

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

    attribute = DataStringField()
    intAttrName = attribute

    default = LongField()
    defaultValue = default
