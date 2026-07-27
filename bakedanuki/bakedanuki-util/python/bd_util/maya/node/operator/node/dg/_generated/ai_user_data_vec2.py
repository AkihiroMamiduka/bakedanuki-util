# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_user_data_vec2 import (
    DefaultValueField,
    OutTransparencyField,
    OutValueField,
)
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiUserDataVec2(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataVec2"

    outValue = OutValueField(default_value=(0.0, 0.0), writable=False)
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    defaultValue = DefaultValueField(default_value=(0.0, 0.0))
    defaultValueX = defaultValue.defaultValueX
    defaultValuex = defaultValueX
    defaultValueY = defaultValue.defaultValueY
    defaultValuey = defaultValueY

    vec2AttrName = DataStringField()
