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

    Kd = FloatField(default_value=0.699999988079071, min_value=0.0, soft_max_value=1.0)

    KdColor = KdColorField(default_value=(1.0, 1.0, 1.0))
    Kd_color = KdColor
    KdColorR = KdColor.KdColorR
    Kd_colorr = KdColorR
    KdColorG = KdColor.KdColorG
    Kd_colorg = KdColorG
    KdColorB = KdColor.KdColorB
    Kd_colorb = KdColorB

    opacity = OpacityField(default_value=(1.0, 1.0, 1.0))
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
