# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_barndoor import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedAiBarndoor(DG):
    __slots__ = ()

    NODE_TYPE = "aiBarndoor"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    barndoorTopLeft = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_top_left = barndoorTopLeft

    barndoorTopRight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_top_right = barndoorTopRight

    barndoorTopEdge = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_top_edge = barndoorTopEdge

    barndoorRightTop = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    barndoor_right_top = barndoorRightTop

    barndoorRightBottom = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    barndoor_right_bottom = barndoorRightBottom

    barndoorRightEdge = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_right_edge = barndoorRightEdge

    barndoorBottomLeft = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    barndoor_bottom_left = barndoorBottomLeft

    barndoorBottomRight = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    barndoor_bottom_right = barndoorBottomRight

    barndoorBottomEdge = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_bottom_edge = barndoorBottomEdge

    barndoorLeftTop = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_left_top = barndoorLeftTop

    barndoorLeftBottom = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_left_bottom = barndoorLeftBottom

    barndoorLeftEdge = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    barndoor_left_edge = barndoorLeftEdge
