# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_user_data_vector import (
    DefaultValueField,
    OutTransparencyField,
    OutValueField,
)
from ...attr.define.std.dt.string import DataStringField


class AiUserDataVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataVector"

    outValue = OutValueField()
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    defaultValue = DefaultValueField()
    defaultValueX = defaultValue.defaultValueX
    defaultValuex = defaultValueX
    defaultValueY = defaultValue.defaultValueY
    defaultValuey = defaultValueY
    defaultValueZ = defaultValue.defaultValueZ
    defaultValuez = defaultValueZ

    vectorAttrName = DataStringField()
