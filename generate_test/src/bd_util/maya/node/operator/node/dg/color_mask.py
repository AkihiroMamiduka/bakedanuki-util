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
    _ic = inColor
    inColorR = inColor.inColorR
    _icr = inColorR
    inColorG = inColor.inColorG
    _icg = inColorG
    inColorB = inColor.inColorB
    _icb = inColorB

    inAlpha = FloatField()
    _ia = inAlpha

    preserveColor = BoolField()
    _pvc = preserveColor

    mask = MaskField()
    _m = mask
    maskR = mask.maskR
    _mr = maskR
    maskG = mask.maskG
    _mg = maskG
    maskB = mask.maskB
    _mb = maskB

    maskAlpha = FloatField()
    _ma = maskAlpha

    maskAlphaIsLuminance = BoolField()
    _mal = maskAlphaIsLuminance

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
