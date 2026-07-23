# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_color_correct import (
    AddField,
    InputField,
    MultiplyField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedAiColorCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "aiColorCorrect"

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

    inputA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    inputa = inputA

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    alphaIsLuminance = BoolField(default_value=False)
    alpha_is_luminance = alphaIsLuminance

    alphaMultiply = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    alpha_multiply = alphaMultiply

    alphaAdd = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    alpha_add = alphaAdd

    invert = BoolField(default_value=False)

    invertAlpha = BoolField(default_value=False)
    invert_alpha = invertAlpha

    gamma = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    hueShift = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    hue_shift = hueShift

    saturation = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    contrast = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)

    contrastPivot = FloatField(default_value=0.18000000715255737, soft_min_value=0.0, soft_max_value=1.0)
    contrast_pivot = contrastPivot

    exposure = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)

    multiply = MultiplyField(default_value=(1.0, 1.0, 1.0))
    multiplyR = multiply.multiplyR
    multiplyr = multiplyR
    multiplyG = multiply.multiplyG
    multiplyg = multiplyG
    multiplyB = multiply.multiplyB
    multiplyb = multiplyB

    add = AddField(default_value=(0.0, 0.0, 0.0))
    addR = add.addR
    addr = addR
    addG = add.addG
    addg = addG
    addB = add.addB
    addb = addB

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
