# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.surface_shader import (
    OutColorField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedSurfaceShader(DG):
    __slots__ = ()

    NODE_TYPE = "surfaceShader"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0))
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0))
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outMatteOpacity = OutMatteOpacityField(default_value=(1.0, 1.0, 1.0))
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0))
    og = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    materialAlphaGain = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    maga = materialAlphaGain
