# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.color_mask import (
    InColorField,
    MaskField,
    OutColorField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedColorMask(DG):
    __slots__ = ()

    NODE_TYPE = "colorMask"

    inColor = InColorField(default_value=(0.30000001192092896, 0.30000001192092896, 0.30000001192092896))
    ic = inColor
    inColorR = inColor.inColorR
    icr = inColorR
    inColorG = inColor.inColorG
    icg = inColorG
    inColorB = inColor.inColorB
    icb = inColorB

    inAlpha = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    ia = inAlpha

    preserveColor = BoolField(default_value=False)
    pvc = preserveColor

    mask = MaskField(default_value=(0.0, 0.0, 0.0))
    m = mask
    maskR = mask.maskR
    mr = maskR
    maskG = mask.maskG
    mg = maskG
    maskB = mask.maskB
    mb = maskB

    maskAlpha = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    ma = maskAlpha

    maskAlphaIsLuminance = BoolField(default_value=True)
    mal = maskAlphaIsLuminance

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
