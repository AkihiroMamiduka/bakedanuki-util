# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_light_decay import OutTransparencyField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiLightDecay(DG):
    __slots__ = ()

    NODE_TYPE = "aiLightDecay"

    outValue = MessageField()
    out = outValue

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    useNearAtten = BoolField()
    use_near_atten = useNearAtten

    useFarAtten = BoolField()
    use_far_atten = useFarAtten

    nearStart = FloatField()
    near_start = nearStart

    nearEnd = FloatField()
    near_end = nearEnd

    farStart = FloatField()
    far_start = farStart

    farEnd = FloatField()
    far_end = farEnd
