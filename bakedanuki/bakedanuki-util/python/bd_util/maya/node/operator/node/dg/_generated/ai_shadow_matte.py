# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_shadow_matte import (
    BackgroundColorField,
    DiffuseColorField,
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    ShadowColorField,
    SpecularColorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class BackgroundEnumPlugOperator(
    EnumPlugOperator["BackgroundEnumAttrOperator"]
):
    __slots__ = ()

    SCENE_BACKGROUND = 0
    BACKGROUND_COLOR = 1


class BackgroundEnumAttrOperator(EnumAttrOperator[BackgroundEnumPlugOperator]):
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


class GeneratedAiShadowMatte(DG):
    __slots__ = ()

    NODE_TYPE = "aiShadowMatte"

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

    outTransparency = OutTransparencyField(
        default_value=(0.5, 0.5, 0.5), writable=False
    )
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

    background = BackgroundEnumField(default_value=0)

    shadowColor = ShadowColorField(default_value=(0.0, 0.0, 0.0))
    shadow_color = shadowColor
    shadowColorR = shadowColor.shadowColorR
    shadow_colorr = shadowColorR
    shadowColorG = shadowColor.shadowColorG
    shadow_colorg = shadowColorG
    shadowColorB = shadowColor.shadowColorB
    shadow_colorb = shadowColorB

    shadowOpacity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    shadow_opacity = shadowOpacity

    backgroundColor = BackgroundColorField(default_value=(1.0, 1.0, 1.0))
    background_color = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    background_colorr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    background_colorg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    background_colorb = backgroundColorB

    diffuseColor = DiffuseColorField(default_value=(1.0, 1.0, 1.0))
    diffuse_color = diffuseColor
    diffuseColorR = diffuseColor.diffuseColorR
    diffuse_colorr = diffuseColorR
    diffuseColorG = diffuseColor.diffuseColorG
    diffuse_colorg = diffuseColorG
    diffuseColorB = diffuseColor.diffuseColorB
    diffuse_colorb = diffuseColorB

    diffuseUseBackground = BoolField(default_value=True)
    diffuse_use_background = diffuseUseBackground

    diffuseIntensity = FloatField(
        default_value=0.699999988079071, min_value=0.0, soft_max_value=1.0
    )
    diffuse_intensity = diffuseIntensity

    backlighting = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0, soft_max_value=1.0
    )

    indirectDiffuseEnable = BoolField(default_value=False)
    indirect_diffuse_enable = indirectDiffuseEnable

    indirectSpecularEnable = BoolField(default_value=False)
    indirect_specular_enable = indirectSpecularEnable

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularIntensity = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    specular_intensity = specularIntensity

    specularRoughness = FloatField(
        default_value=0.20000000298023224, min_value=0.0, max_value=1.0
    )
    specular_roughness = specularRoughness

    specularIOR = FloatField(
        default_value=1.5, min_value=0.0, soft_max_value=10.0
    )
    specular_IOR = specularIOR

    alphaMask = BoolField(default_value=True)
    alpha_mask = alphaMask

    aovGroup = DataStringField()
    aov_group = aovGroup

    aovShadow = DataStringField()
    aov_shadow = aovShadow

    aovShadowDiff = DataStringField()
    aov_shadow_diff = aovShadowDiff

    aovShadowMask = DataStringField()
    aov_shadow_mask = aovShadowMask
