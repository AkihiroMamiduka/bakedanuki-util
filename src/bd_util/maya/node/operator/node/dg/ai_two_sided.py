# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_two_sided import (
    BackField,
    FrontField,
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiTwoSided(DG):
    __slots__ = ()

    NODE_TYPE = "aiTwoSided"

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

    frontA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fronta = frontA

    front = FrontField(default_value=(0.0, 0.0, 0.0))
    frontR = front.frontR
    frontr = frontR
    frontG = front.frontG
    frontg = frontG
    frontB = front.frontB
    frontb = frontB

    backA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    backa = backA

    back = BackField(default_value=(0.0, 0.0, 0.0))
    backR = back.backR
    backr = backR
    backG = back.backG
    backg = backG
    backB = back.backB
    backb = backB
