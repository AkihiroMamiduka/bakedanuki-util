# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_facing_ratio import OutTransparencyField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiFacingRatio(DG):
    __slots__ = ()

    NODE_TYPE = "aiFacingRatio"

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

    bias = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)

    gain = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)

    linear = BoolField(default_value=False)

    invert = BoolField(default_value=False)
