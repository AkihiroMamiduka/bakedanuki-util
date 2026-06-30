# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_matte import (
    ColorField,
    HardwareColorField,
    NormalCameraField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
    PassthroughField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiMatte(DG):
    __slots__ = ()

    NODE_TYPE = "aiMatte"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField()
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    passthroughA = FloatField()
    passthrougha = passthroughA

    passthrough = PassthroughField()
    passthroughR = passthrough.passthroughR
    passthroughr = passthroughR
    passthroughG = passthrough.passthroughG
    passthroughg = passthroughG
    passthroughB = passthrough.passthroughB
    passthroughb = passthroughB

    colorA = FloatField()
    colora = colorA

    color = ColorField()
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    opacity = OpacityField()
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB
