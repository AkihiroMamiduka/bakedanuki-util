# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_trace_set import (
    OutColorField,
    OutTransparencyField,
    PassthroughField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiTraceSet(DG):
    __slots__ = ()

    NODE_TYPE = "aiTraceSet"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    passthroughA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    passthrougha = passthroughA

    passthrough = PassthroughField(default_value=(0.0, 0.0, 0.0))
    passthroughR = passthrough.passthroughR
    passthroughr = passthroughR
    passthroughG = passthrough.passthroughG
    passthroughg = passthroughG
    passthroughB = passthrough.passthroughB
    passthroughb = passthroughB

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField(default_value=True)
