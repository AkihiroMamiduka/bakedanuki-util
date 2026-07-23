# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_user_data_float import OutTransparencyField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiUserDataFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataFloat"

    outValue = FloatField(default_value=0.0, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    attribute = DataStringField()
    floatAttrName = attribute

    default = FloatField(default_value=0.0)
    defaultValue = default
