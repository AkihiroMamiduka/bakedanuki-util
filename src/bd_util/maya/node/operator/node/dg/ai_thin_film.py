# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_thin_film import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiThinFilm(DG):
    __slots__ = ()

    NODE_TYPE = "aiThinFilm"

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

    thicknessMin = FloatField()
    thickness_min = thicknessMin

    thicknessMax = FloatField()
    thickness_max = thicknessMax

    thickness = FloatField()

    iorMedium = FloatField()
    ior_medium = iorMedium

    iorFilm = FloatField()
    ior_film = iorFilm

    iorInternal = FloatField()
    ior_internal = iorInternal
