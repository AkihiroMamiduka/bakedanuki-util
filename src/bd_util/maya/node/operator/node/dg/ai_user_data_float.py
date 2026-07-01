# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_user_data_float import OutTransparencyField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiUserDataFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataFloat"

    outValue = FloatField()
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
    floatAttrName = attribute

    default = FloatField()
    defaultValue = default
