# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.color_mask import (
    InColorField,
    MaskField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ColorMask(DG):
    __slots__ = ()

    NODE_TYPE = "colorMask"

    inColor = InColorField()
    ic = inColor
    inColorR = inColor.inColorR
    icr = inColorR
    inColorG = inColor.inColorG
    icg = inColorG
    inColorB = inColor.inColorB
    icb = inColorB

    inAlpha = FloatField()
    ia = inAlpha

    preserveColor = BoolField()
    pvc = preserveColor

    mask = MaskField()
    m = mask
    maskR = mask.maskR
    mr = maskR
    maskG = mask.maskG
    mg = maskG
    maskB = mask.maskB
    mb = maskB

    maskAlpha = FloatField()
    ma = maskAlpha

    maskAlphaIsLuminance = BoolField()
    mal = maskAlphaIsLuminance

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
