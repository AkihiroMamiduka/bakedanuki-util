# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_lambert import (
    HardwareColorField,
    KdColorField,
    NormalCameraField,
    NormalField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiLambert(DG):
    __slots__ = ()

    NODE_TYPE = "aiLambert"

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

    Kd = FloatField()

    KdColor = KdColorField()
    Kd_color = KdColor
    KdColorR = KdColor.KdColorR
    Kd_colorr = KdColorR
    KdColorG = KdColor.KdColorG
    Kd_colorg = KdColorG
    KdColorB = KdColor.KdColorB
    Kd_colorb = KdColorB

    opacity = OpacityField()
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
