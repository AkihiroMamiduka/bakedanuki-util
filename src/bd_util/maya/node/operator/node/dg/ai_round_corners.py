# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_round_corners import (
    NormalField,
    OutTransparencyField,
    OutValueField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class AiRoundCorners(DG):
    __slots__ = ()

    NODE_TYPE = "aiRoundCorners"

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

    samples = LongField()

    radius = FloatField()

    normal = NormalField()
    normalCamera = normal
    normalX = normal.normalX
    normalCamerax = normalX
    normalY = normal.normalY
    normalCameray = normalY
    normalZ = normal.normalZ
    normalCameraz = normalZ

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField()

    selfOnly = BoolField()
    self_only = selfOnly

    objectSpace = BoolField()
    object_space = objectSpace

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    outAlpha = FloatField()
    out_alpha = outAlpha
