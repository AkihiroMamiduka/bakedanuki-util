# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_facing_ratio import OutTransparencyField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiFacingRatio(DG):
    __slots__ = ()

    NODE_TYPE = "aiFacingRatio"

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

    bias = FloatField()

    gain = FloatField()

    linear = BoolField()

    invert = BoolField()
