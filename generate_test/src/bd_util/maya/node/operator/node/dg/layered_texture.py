# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.layered_texture import (
    HardwareColorField,
    InputsField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class LayeredTexture(DG):
    __slots__ = ()

    NODE_TYPE = "layeredTexture"

    inputs = InputsField(multi=True)
    cs = inputs

    # TODO: inputs.colorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputs.colorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputs.colorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField()
    oa = outAlpha

    hardwareColor = HardwareColorField()
    hc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hcb = hardwareColorB

    alphaIsLuminance = BoolField()
    ail = alphaIsLuminance

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB
