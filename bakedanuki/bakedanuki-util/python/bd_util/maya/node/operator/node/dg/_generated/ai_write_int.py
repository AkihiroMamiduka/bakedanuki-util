# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_write_int import (
    BeautyField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiWriteInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiWriteInt"

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

    beautyA = FloatField(default_value=5.885453550164232e-43, min_value=0.0, max_value=1.0)
    passthrougha = beautyA

    beauty = BeautyField(default_value=(0.0, 0.0, 0.0))
    passthrough = beauty
    beautyR = beauty.beautyR
    passthroughr = beautyR
    beautyG = beauty.beautyG
    passthroughg = beautyG
    beautyB = beauty.beautyB
    passthroughb = beautyB

    input = LongField(default_value=0)
    aov_input = input

    aovName = DataStringField()
    aov_name = aovName
