# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_matte import (
    ColorField,
    HardwareColorField,
    NormalCameraField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
    PassthroughField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiMatte(DG):
    __slots__ = ()

    NODE_TYPE = "aiMatte"

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.5, 0.5, 0.5), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 0.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    passthroughA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    passthrougha = passthroughA

    passthrough = PassthroughField(default_value=(0.0, 0.0, 0.0))
    passthroughR = passthrough.passthroughR
    passthroughr = passthroughR
    passthroughG = passthrough.passthroughG
    passthroughg = passthroughG
    passthroughB = passthrough.passthroughB
    passthroughb = passthroughB

    colorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    colora = colorA

    color = ColorField(default_value=(0.0, 0.0, 0.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    opacity = OpacityField(default_value=(1.0, 1.0, 1.0))
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB
