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

    # TODO: color.color_ColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: color.color_ColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: color.color_ColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

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
