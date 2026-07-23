# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.volume_shader import (
    OutColorField,
    OutMatteOpacityField,
    OutTransparencyField,
)


class _GeneratedVolumeShader(DG):
    __slots__ = ()

    NODE_TYPE = "volumeShader"

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
