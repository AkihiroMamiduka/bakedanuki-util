# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_shadow_matte import (
    BackgroundColorField,
    DiffuseColorField,
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    ShadowColorField,
    SpecularColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class BackgroundEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCENE_BACKGROUND = 0
    BACKGROUND_COLOR = 1


class BackgroundEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCENE_BACKGROUND = 0
    BACKGROUND_COLOR = 1

    NAME_MAP = {
        SCENE_BACKGROUND: "scene_background",
        BACKGROUND_COLOR: "background_color",
    }


class BackgroundEnumField(
    EnumField[BackgroundEnumAttrOperator, BackgroundEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundEnumAttrOperator
    PLUG_CLS = BackgroundEnumPlugOperator


class AiShadowMatte(DG):
    __slots__ = ()

    NODE_TYPE = "aiShadowMatte"

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

    background = BackgroundEnumField()

    shadowColor = ShadowColorField()
    shadow_color = shadowColor
    shadowColorR = shadowColor.shadowColorR
    shadow_colorr = shadowColorR
    shadowColorG = shadowColor.shadowColorG
    shadow_colorg = shadowColorG
    shadowColorB = shadowColor.shadowColorB
    shadow_colorb = shadowColorB

    shadowOpacity = FloatField()
    shadow_opacity = shadowOpacity

    backgroundColor = BackgroundColorField()
    background_color = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    background_colorr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    background_colorg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    background_colorb = backgroundColorB

    diffuseColor = DiffuseColorField()
    diffuse_color = diffuseColor
    diffuseColorR = diffuseColor.diffuseColorR
    diffuse_colorr = diffuseColorR
    diffuseColorG = diffuseColor.diffuseColorG
    diffuse_colorg = diffuseColorG
    diffuseColorB = diffuseColor.diffuseColorB
    diffuse_colorb = diffuseColorB

    diffuseUseBackground = BoolField()
    diffuse_use_background = diffuseUseBackground

    diffuseIntensity = FloatField()
    diffuse_intensity = diffuseIntensity

    backlighting = FloatField()

    indirectDiffuseEnable = BoolField()
    indirect_diffuse_enable = indirectDiffuseEnable

    indirectSpecularEnable = BoolField()
    indirect_specular_enable = indirectSpecularEnable

    specularColor = SpecularColorField()
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularIntensity = FloatField()
    specular_intensity = specularIntensity

    specularRoughness = FloatField()
    specular_roughness = specularRoughness

    specularIOR = FloatField()
    specular_IOR = specularIOR

    alphaMask = BoolField()
    alpha_mask = alphaMask

    aovGroup = DataStringField()
    aov_group = aovGroup

    aovShadow = DataStringField()
    aov_shadow = aovShadow

    aovShadowDiff = DataStringField()
    aov_shadow_diff = aovShadowDiff

    aovShadowMask = DataStringField()
    aov_shadow_mask = aovShadowMask
