# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_thin_film import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiThinFilm(DG):
    __slots__ = ()

    NODE_TYPE = "aiThinFilm"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    thicknessMin = FloatField(
        default_value=250.0, min_value=0.0, soft_max_value=1000.0
    )
    thickness_min = thicknessMin

    thicknessMax = FloatField(
        default_value=400.0, min_value=0.0, soft_max_value=1000.0
    )
    thickness_max = thicknessMax

    thickness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    iorMedium = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=3.0
    )
    ior_medium = iorMedium

    iorFilm = FloatField(default_value=1.5, min_value=0.0, soft_max_value=3.0)
    ior_film = iorFilm

    iorInternal = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=3.0
    )
    ior_internal = iorInternal
