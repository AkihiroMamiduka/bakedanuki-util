# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_standard import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SpecularDistributionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BECKMANN = 0
    GGX = 1


class SpecularDistributionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BECKMANN = 0
    GGX = 1

    NAME_MAP = {
        BECKMANN: "beckmann",
        GGX: "ggx",
    }


class SpecularDistributionEnumField(
    EnumField[SpecularDistributionEnumAttrOperator, SpecularDistributionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularDistributionEnumAttrOperator
    PLUG_CLS = SpecularDistributionEnumPlugOperator


class AiStandard(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandard"

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

    aiEnableMatte = BoolField()
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField()
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField()
    ai_matte_color_a = aiMatteColorA

    Kd = FloatField()

    KdColor = KdColorField()
    Kd_color = KdColor
    KdColorR = KdColor.KdColorR
    Kd_colorr = KdColorR
    KdColorG = KdColor.KdColorG
    Kd_colorg = KdColorG
    KdColorB = KdColor.KdColorB
    Kd_colorb = KdColorB

    diffuseRoughness = FloatField()
    diffuse_roughness = diffuseRoughness

    Ks = FloatField()

    KsColor = KsColorField()
    Ks_color = KsColor
    KsColorR = KsColor.KsColorR
    Ks_colorr = KsColorR
    KsColorG = KsColor.KsColorG
    Ks_colorg = KsColorG
    KsColorB = KsColor.KsColorB
    Ks_colorb = KsColorB

    specularRoughness = FloatField()
    specular_roughness = specularRoughness

    specularAnisotropy = FloatField()
    specular_anisotropy = specularAnisotropy

    specularRotation = FloatField()
    specular_rotation = specularRotation

    specularDistribution = SpecularDistributionEnumField()
    specular_distribution = specularDistribution

    Kr = FloatField()

    KrColor = KrColorField()
    Kr_color = KrColor
    KrColorR = KrColor.KrColorR
    Kr_colorr = KrColorR
    KrColorG = KrColor.KrColorG
    Kr_colorg = KrColorG
    KrColorB = KrColor.KrColorB
    Kr_colorb = KrColorB

    reflectionExitColor = ReflectionExitColorField()
    reflection_exit_color = reflectionExitColor
    reflectionExitColorR = reflectionExitColor.reflectionExitColorR
    reflection_exit_colorr = reflectionExitColorR
    reflectionExitColorG = reflectionExitColor.reflectionExitColorG
    reflection_exit_colorg = reflectionExitColorG
    reflectionExitColorB = reflectionExitColor.reflectionExitColorB
    reflection_exit_colorb = reflectionExitColorB

    reflectionExitUseEnvironment = BoolField()
    reflection_exit_use_environment = reflectionExitUseEnvironment

    Kt = FloatField()

    KtColor = KtColorField()
    Kt_color = KtColor
    KtColorR = KtColor.KtColorR
    Kt_colorr = KtColorR
    KtColorG = KtColor.KtColorG
    Kt_colorg = KtColorG
    KtColorB = KtColor.KtColorB
    Kt_colorb = KtColorB

    transmittance = TransmittanceField()
    transmittanceR = transmittance.transmittanceR
    transmittancer = transmittanceR
    transmittanceG = transmittance.transmittanceG
    transmittanceg = transmittanceG
    transmittanceB = transmittance.transmittanceB
    transmittanceb = transmittanceB

    refractionRoughness = FloatField()
    refraction_roughness = refractionRoughness

    refractionExitColor = RefractionExitColorField()
    refraction_exit_color = refractionExitColor
    refractionExitColorR = refractionExitColor.refractionExitColorR
    refraction_exit_colorr = refractionExitColorR
    refractionExitColorG = refractionExitColor.refractionExitColorG
    refraction_exit_colorg = refractionExitColorG
    refractionExitColorB = refractionExitColor.refractionExitColorB
    refraction_exit_colorb = refractionExitColorB

    refractionExitUseEnvironment = BoolField()
    refraction_exit_use_environment = refractionExitUseEnvironment

    IOR = FloatField()

    dispersionAbbe = FloatField()
    dispersion_abbe = dispersionAbbe

    Kb = FloatField()

    Fresnel = BoolField()

    Krn = FloatField()

    specularFresnel = BoolField()
    specular_Fresnel = specularFresnel

    Ksn = FloatField()

    FresnelUseIOR = BoolField()
    Fresnel_use_IOR = FresnelUseIOR

    FresnelAffectDiff = BoolField()
    Fresnel_affect_diff = FresnelAffectDiff

    emission = FloatField()

    emissionColor = EmissionColorField()
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    directSpecular = FloatField()
    direct_specular = directSpecular

    indirectSpecular = FloatField()
    indirect_specular = indirectSpecular

    directDiffuse = FloatField()
    direct_diffuse = directDiffuse

    indirectDiffuse = FloatField()
    indirect_diffuse = indirectDiffuse

    enableGlossyCaustics = BoolField()
    enable_glossy_caustics = enableGlossyCaustics

    enableReflectiveCaustics = BoolField()
    enable_reflective_caustics = enableReflectiveCaustics

    enableRefractiveCaustics = BoolField()
    enable_refractive_caustics = enableRefractiveCaustics

    enableInternalReflections = BoolField()
    enable_internal_reflections = enableInternalReflections

    Ksss = FloatField()

    KsssColor = KsssColorField()
    Ksss_color = KsssColor
    KsssColorR = KsssColor.KsssColorR
    Ksss_colorr = KsssColorR
    KsssColorG = KsssColor.KsssColorG
    Ksss_colorg = KsssColorG
    KsssColorB = KsssColor.KsssColorB
    Ksss_colorb = KsssColorB

    sssRadius = SssRadiusField()
    sss_radius = sssRadius
    sssRadiusR = sssRadius.sssRadiusR
    sss_radiusr = sssRadiusR
    sssRadiusG = sssRadius.sssRadiusG
    sss_radiusg = sssRadiusG
    sssRadiusB = sssRadius.sssRadiusB
    sss_radiusb = sssRadiusB

    bounceFactor = FloatField()
    bounce_factor = bounceFactor

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
