# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_standard import (
    AiMatteColorField,
    EmissionColorField,
    KdColorField,
    KrColorField,
    KsColorField,
    KsssColorField,
    KtColorField,
    NormalCameraField,
    NormalField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
    ReflectionExitColorField,
    RefractionExitColorField,
    SssRadiusField,
    TransmittanceField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class SpecularDistributionEnumPlugOperator(
    EnumPlugOperator["SpecularDistributionEnumAttrOperator"]
):
    __slots__ = ()

    BECKMANN = 0
    GGX = 1


class SpecularDistributionEnumAttrOperator(
    EnumAttrOperator[SpecularDistributionEnumPlugOperator]
):
    __slots__ = ()

    BECKMANN = 0
    GGX = 1

    NAME_MAP = {
        BECKMANN: "beckmann",
        GGX: "ggx",
    }


class SpecularDistributionEnumField(
    EnumField[
        SpecularDistributionEnumAttrOperator,
        SpecularDistributionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularDistributionEnumAttrOperator
    PLUG_CLS = SpecularDistributionEnumPlugOperator


class GeneratedAiStandard(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandard"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
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
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    aiEnableMatte = BoolField(default_value=False)
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField(default_value=(0.0, 0.0, 0.0))
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ai_matte_color_a = aiMatteColorA

    Kd = FloatField(
        default_value=0.699999988079071, min_value=0.0, max_value=1.0
    )

    KdColor = KdColorField(default_value=(1.0, 1.0, 1.0))
    Kd_color = KdColor
    KdColorR = KdColor.KdColorR
    Kd_colorr = KdColorR
    KdColorG = KdColor.KdColorG
    Kd_colorg = KdColorG
    KdColorB = KdColor.KdColorB
    Kd_colorb = KdColorB

    diffuseRoughness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    diffuse_roughness = diffuseRoughness

    Ks = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    KsColor = KsColorField(default_value=(1.0, 1.0, 1.0))
    Ks_color = KsColor
    KsColorR = KsColor.KsColorR
    Ks_colorr = KsColorR
    KsColorG = KsColor.KsColorG
    Ks_colorg = KsColorG
    KsColorB = KsColor.KsColorB
    Ks_colorb = KsColorB

    specularRoughness = FloatField(
        default_value=0.4669046998023987, min_value=0.0, max_value=1.0
    )
    specular_roughness = specularRoughness

    specularAnisotropy = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    specular_anisotropy = specularAnisotropy

    specularRotation = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    specular_rotation = specularRotation

    specularDistribution = SpecularDistributionEnumField(default_value=1)
    specular_distribution = specularDistribution

    Kr = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    KrColor = KrColorField(default_value=(1.0, 1.0, 1.0))
    Kr_color = KrColor
    KrColorR = KrColor.KrColorR
    Kr_colorr = KrColorR
    KrColorG = KrColor.KrColorG
    Kr_colorg = KrColorG
    KrColorB = KrColor.KrColorB
    Kr_colorb = KrColorB

    reflectionExitColor = ReflectionExitColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    reflection_exit_color = reflectionExitColor
    reflectionExitColorR = reflectionExitColor.reflectionExitColorR
    reflection_exit_colorr = reflectionExitColorR
    reflectionExitColorG = reflectionExitColor.reflectionExitColorG
    reflection_exit_colorg = reflectionExitColorG
    reflectionExitColorB = reflectionExitColor.reflectionExitColorB
    reflection_exit_colorb = reflectionExitColorB

    reflectionExitUseEnvironment = BoolField(default_value=False)
    reflection_exit_use_environment = reflectionExitUseEnvironment

    Kt = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    KtColor = KtColorField(default_value=(1.0, 1.0, 1.0))
    Kt_color = KtColor
    KtColorR = KtColor.KtColorR
    Kt_colorr = KtColorR
    KtColorG = KtColor.KtColorG
    Kt_colorg = KtColorG
    KtColorB = KtColor.KtColorB
    Kt_colorb = KtColorB

    transmittance = TransmittanceField(default_value=(1.0, 1.0, 1.0))
    transmittanceR = transmittance.transmittanceR
    transmittancer = transmittanceR
    transmittanceG = transmittance.transmittanceG
    transmittanceg = transmittanceG
    transmittanceB = transmittance.transmittanceB
    transmittanceb = transmittanceB

    refractionRoughness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    refraction_roughness = refractionRoughness

    refractionExitColor = RefractionExitColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    refraction_exit_color = refractionExitColor
    refractionExitColorR = refractionExitColor.refractionExitColorR
    refraction_exit_colorr = refractionExitColorR
    refractionExitColorG = refractionExitColor.refractionExitColorG
    refraction_exit_colorg = refractionExitColorG
    refractionExitColorB = refractionExitColor.refractionExitColorB
    refraction_exit_colorb = refractionExitColorB

    refractionExitUseEnvironment = BoolField(default_value=False)
    refraction_exit_use_environment = refractionExitUseEnvironment

    IOR = FloatField(default_value=1.0, min_value=0.0, soft_max_value=3.0)

    dispersionAbbe = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=100.0
    )
    dispersion_abbe = dispersionAbbe

    Kb = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    Fresnel = BoolField(default_value=False)

    Krn = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    specularFresnel = BoolField(default_value=False)
    specular_Fresnel = specularFresnel

    Ksn = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    FresnelUseIOR = BoolField(default_value=False)
    Fresnel_use_IOR = FresnelUseIOR

    FresnelAffectDiff = BoolField(default_value=True)
    Fresnel_affect_diff = FresnelAffectDiff

    emission = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    emissionColor = EmissionColorField(default_value=(1.0, 1.0, 1.0))
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    directSpecular = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    direct_specular = directSpecular

    indirectSpecular = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    indirect_specular = indirectSpecular

    directDiffuse = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    direct_diffuse = directDiffuse

    indirectDiffuse = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    indirect_diffuse = indirectDiffuse

    enableGlossyCaustics = BoolField(default_value=False)
    enable_glossy_caustics = enableGlossyCaustics

    enableReflectiveCaustics = BoolField(default_value=False)
    enable_reflective_caustics = enableReflectiveCaustics

    enableRefractiveCaustics = BoolField(default_value=False)
    enable_refractive_caustics = enableRefractiveCaustics

    enableInternalReflections = BoolField(default_value=True)
    enable_internal_reflections = enableInternalReflections

    Ksss = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    KsssColor = KsssColorField(default_value=(1.0, 1.0, 1.0))
    Ksss_color = KsssColor
    KsssColorR = KsssColor.KsssColorR
    Ksss_colorr = KsssColorR
    KsssColorG = KsssColor.KsssColorG
    Ksss_colorg = KsssColorG
    KsssColorB = KsssColor.KsssColorB
    Ksss_colorb = KsssColorB

    sssRadius = SssRadiusField(
        default_value=(
            0.10000000149011612,
            0.10000000149011612,
            0.10000000149011612,
        )
    )
    sss_radius = sssRadius
    sssRadiusR = sssRadius.sssRadiusR
    sss_radiusr = sssRadiusR
    sssRadiusG = sssRadius.sssRadiusG
    sss_radiusg = sssRadiusG
    sssRadiusB = sssRadius.sssRadiusB
    sss_radiusb = sssRadiusB

    bounceFactor = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=4.0
    )
    bounce_factor = bounceFactor

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
