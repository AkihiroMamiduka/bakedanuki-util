# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_user_data_string import OutTransparencyField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiUserDataString(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataString"

    outValue = DataStringField(writable=False)
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
    stringAttrName = attribute

    default = DataStringField()
    defaultValue = default
