# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.ai_light_decay import (
    OutTransparencyField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedAiLightDecay(DG):
    __slots__ = ()

    NODE_TYPE = "aiLightDecay"

    outValue = MessageField(writable=False)
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

    useNearAtten = BoolField(default_value=False)
    use_near_atten = useNearAtten

    useFarAtten = BoolField(default_value=False)
    use_far_atten = useFarAtten

    nearStart = DoubleLinearField(
        default_value=0.0, min_value=0.0, soft_max_value=1000.0
    )
    near_start = nearStart

    nearEnd = DoubleLinearField(
        default_value=0.0, min_value=0.0, soft_max_value=1000.0
    )
    near_end = nearEnd

    farStart = DoubleLinearField(
        default_value=0.0, min_value=0.0, soft_max_value=1000.0
    )
    far_start = farStart

    farEnd = DoubleLinearField(
        default_value=0.0, min_value=0.0, soft_max_value=1000.0
    )
    far_end = farEnd
