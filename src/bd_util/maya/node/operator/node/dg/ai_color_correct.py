# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_color_correct import (
    AddField,
    InputField,
    MultiplyField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiColorCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "aiColorCorrect"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    inputA = FloatField()
    inputa = inputA

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    alphaIsLuminance = BoolField()
    alpha_is_luminance = alphaIsLuminance

    alphaMultiply = FloatField()
    alpha_multiply = alphaMultiply

    alphaAdd = FloatField()
    alpha_add = alphaAdd

    invert = BoolField()

    invertAlpha = BoolField()
    invert_alpha = invertAlpha

    gamma = FloatField()

    hueShift = FloatField()
    hue_shift = hueShift

    saturation = FloatField()

    contrast = FloatField()

    contrastPivot = FloatField()
    contrast_pivot = contrastPivot

    exposure = FloatField()

    multiply = MultiplyField()
    multiplyR = multiply.multiplyR
    multiplyr = multiplyR
    multiplyG = multiply.multiplyG
    multiplyg = multiplyG
    multiplyB = multiply.multiplyB
    multiplyb = multiplyB

    add = AddField()
    addR = add.addR
    addr = addR
    addG = add.addG
    addg = addG
    addB = add.addB
    addb = addB

    mask = FloatField()
