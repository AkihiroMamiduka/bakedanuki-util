# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_bump2d import (
    NormalField,
    OutTransparencyField,
    OutValueField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiBump2d(DG):
    __slots__ = ()

    NODE_TYPE = "aiBump2d"

    outValue = OutValueField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    bumpMap = FloatField(default_value=0.0)
    bump_map = bumpMap

    bumpHeight = FloatField(default_value=0.009999999776482582, soft_min_value=0.0, soft_max_value=1.0)
    bump_height = bumpHeight

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
