# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_mix_shader import (
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    Shader1Field,
    Shader2Field,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLEND = 0
    ADD = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLEND = 0
    ADD = 1

    NAME_MAP = {
        BLEND: "blend",
        ADD: "add",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class AiMixShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiMixShader"

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

    mode = ModeEnumField()

    mix = FloatField()

    addTransparency = BoolField()
    add_transparency = addTransparency

    shader1A = FloatField()
    shader1a = shader1A

    shader1 = Shader1Field()
    shader1R = shader1.shader1R
    shader1r = shader1R
    shader1G = shader1.shader1G
    shader1g = shader1G
    shader1B = shader1.shader1B
    shader1b = shader1B

    shader2A = FloatField()
    shader2a = shader2A

    shader2 = Shader2Field()
    shader2R = shader2.shader2R
    shader2r = shader2R
    shader2G = shader2.shader2G
    shader2g = shader2G
    shader2B = shader2.shader2B
    shader2b = shader2B
