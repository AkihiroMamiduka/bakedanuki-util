# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.layered_texture import (
    HardwareColorField,
    InputsField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedLayeredTexture(DG):
    __slots__ = ()

    NODE_TYPE = "layeredTexture"

    inputs = InputsField(multi=True)
    cs = inputs

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hcb = hardwareColorB

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB
