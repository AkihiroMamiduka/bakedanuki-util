# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_axf_shader import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiAxfShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiAxfShader"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocl = outColor
    outColorR = outColor.outColorR
    oclr = outColorR
    outColorG = outColor.outColorG
    oclg = outColorG
    outColorB = outColor.outColorB
    oclb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    axfFilePath = DataStringField()
    axfFP = axfFilePath

    texturePath = DataStringField()
    texPth = texturePath

    uvScale = FloatField(default_value=1.0)
    uvscl = uvScale
