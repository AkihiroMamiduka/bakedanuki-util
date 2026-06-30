# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_barndoor import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiBarndoor(DG):
    __slots__ = ()

    NODE_TYPE = "aiBarndoor"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    barndoorTopLeft = FloatField()
    barndoor_top_left = barndoorTopLeft

    barndoorTopRight = FloatField()
    barndoor_top_right = barndoorTopRight

    barndoorTopEdge = FloatField()
    barndoor_top_edge = barndoorTopEdge

    barndoorRightTop = FloatField()
    barndoor_right_top = barndoorRightTop

    barndoorRightBottom = FloatField()
    barndoor_right_bottom = barndoorRightBottom

    barndoorRightEdge = FloatField()
    barndoor_right_edge = barndoorRightEdge

    barndoorBottomLeft = FloatField()
    barndoor_bottom_left = barndoorBottomLeft

    barndoorBottomRight = FloatField()
    barndoor_bottom_right = barndoorBottomRight

    barndoorBottomEdge = FloatField()
    barndoor_bottom_edge = barndoorBottomEdge

    barndoorLeftTop = FloatField()
    barndoor_left_top = barndoorLeftTop

    barndoorLeftBottom = FloatField()
    barndoor_left_bottom = barndoorLeftBottom

    barndoorLeftEdge = FloatField()
    barndoor_left_edge = barndoorLeftEdge
