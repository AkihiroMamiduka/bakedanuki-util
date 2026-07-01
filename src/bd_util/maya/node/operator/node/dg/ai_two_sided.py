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

    frontA = FloatField()
    fronta = frontA

    front = FrontField()
    frontR = front.frontR
    frontr = frontR
    frontG = front.frontG
    frontg = frontG
    frontB = front.frontB
    frontb = frontB

    backA = FloatField()
    backa = backA

    back = BackField()
    backR = back.backR
    backr = backR
    backG = back.backG
    backg = backG
    backB = back.backB
    backb = backB
