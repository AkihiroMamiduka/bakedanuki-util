# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.remap_value import (
    ColorField,
    OutColorField,
    ValueField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class RemapValue(DG):
    __slots__ = ()

    NODE_TYPE = "remapValue"

    inputValue = FloatField()
    i = inputValue

    inputMin = FloatField()
    imn = inputMin

    inputMax = FloatField()
    imx = inputMax

    outputMin = FloatField()
    omn = outputMin

    outputMax = FloatField()
    omx = outputMax

    value = ValueField(multi=True)
    vl = value

    color = ColorField(multi=True)
    cl = color

    color_ColorR = FloatField()
    clcr = color_ColorR

    color_ColorG = FloatField()
    clcg = color_ColorG

    color_ColorB = FloatField()
    clcb = color_ColorB

    outValue = FloatField()
    ov = outValue

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
