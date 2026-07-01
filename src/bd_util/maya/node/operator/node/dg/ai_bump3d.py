# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_bump3d import (
    NormalField,
    OutTransparencyField,
    OutValueField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiBump3d(DG):
    __slots__ = ()

    NODE_TYPE = "aiBump3d"

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

    bumpMap = FloatField()
    bump_map = bumpMap

    bumpHeight = FloatField()
    bump_height = bumpHeight

    epsilon = FloatField()

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
