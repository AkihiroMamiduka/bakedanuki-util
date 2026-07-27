# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_round_corners import (
    NormalField,
    OutTransparencyField,
    OutValueField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiRoundCorners(DG):
    __slots__ = ()

    NODE_TYPE = "aiRoundCorners"

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

    samples = LongField(default_value=6, min_value=0, soft_max_value=20)

    radius = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=10.0)

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalCamera = normal
    normalX = normal.normalX
    normalCamerax = normalX
    normalY = normal.normalY
    normalCameray = normalY
    normalZ = normal.normalZ
    normalCameraz = normalZ

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField(default_value=True)

    selfOnly = BoolField(default_value=False)
    self_only = selfOnly

    objectSpace = BoolField(default_value=True)
    object_space = objectSpace

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    outAlpha = FloatField(default_value=0.0, category="arnold")
    out_alpha = outAlpha
