# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.remap_value import (
    ColorField,
    OutColorField,
    ValueField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedRemapValue(DG):
    __slots__ = ()

    NODE_TYPE = "remapValue"

    inputValue = FloatField(default_value=0.0)
    i = inputValue

    inputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    imn = inputMin

    inputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    imx = inputMax

    outputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omn = outputMin

    outputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    omx = outputMax

    value = ValueField(multi=True, default_value=(0.0, 0.0, 0.0))
    vl = value

    color = ColorField(multi=True)
    cl = color

    color_ColorR = FloatField()
    clcr = color_ColorR

    color_ColorG = FloatField()
    clcg = color_ColorG

    color_ColorB = FloatField()
    clcb = color_ColorB

    outValue = FloatField(default_value=0.0, writable=False)
    ov = outValue

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
