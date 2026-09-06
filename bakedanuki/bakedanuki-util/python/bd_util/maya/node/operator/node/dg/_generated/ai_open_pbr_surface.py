# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_open_pbr_surface import (
    AiMatteColorField,
    BaseColorField,
    CoatColorField,
    EmissionColorField,
    FuzzColorField,
    GeometryCoatNormalField,
    GeometryCoatTangentField,
    GeometryTangentField,
    Id1Field,
    Id2Field,
    Id3Field,
    Id4Field,
    Id5Field,
    Id6Field,
    Id7Field,
    Id8Field,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    SpecularColorField,
    SubsurfaceColorField,
    SubsurfaceRadiusScaleField,
    TransmissionColorField,
    TransmissionScatterField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiOpenPBRSurface(DG):
    __slots__ = ()

    NODE_TYPE = "aiOpenPBRSurface"

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

    baseWeight = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    base_weight = baseWeight

    baseColor = BaseColorField(
        default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929)
    )
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    baseMetalness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    base_metalness = baseMetalness

    baseDiffuseRoughness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    base_diffuse_roughness = baseDiffuseRoughness

    specularWeight = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    specular_weight = specularWeight

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularRoughness = FloatField(
        default_value=0.30000001192092896, min_value=0.0, max_value=1.0
    )
    specular_roughness = specularRoughness

    specularRoughnessAnisotropy = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    specular_roughness_anisotropy = specularRoughnessAnisotropy

    specularIOR = FloatField(
        default_value=1.5, soft_min_value=1.0, soft_max_value=3.0
    )
    specular_ior = specularIOR

    transmissionWeight = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    transmission_weight = transmissionWeight

    transmissionColor = TransmissionColorField(default_value=(1.0, 1.0, 1.0))
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionDepth = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    transmission_depth = transmissionDepth

    transmissionScatter = TransmissionScatterField(
        default_value=(0.0, 0.0, 0.0)
    )
    transmission_scatter = transmissionScatter
    transmissionScatterR = transmissionScatter.transmissionScatterR
    transmission_scatterr = transmissionScatterR
    transmissionScatterG = transmissionScatter.transmissionScatterG
    transmission_scatterg = transmissionScatterG
    transmissionScatterB = transmissionScatter.transmissionScatterB
    transmission_scatterb = transmissionScatterB

    transmissionScatterAnisotropy = FloatField(
        default_value=0.0, min_value=-1.0, max_value=1.0
    )
    transmission_scatter_anisotropy = transmissionScatterAnisotropy

    transmissionDispersionAbbeNumber = FloatField(
        default_value=20.0,
        min_value=0.0,
        soft_min_value=9.0,
        soft_max_value=91.0,
    )
    transmission_dispersion_abbe_number = transmissionDispersionAbbeNumber

    transmissionDispersionScale = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    transmission_dispersion_scale = transmissionDispersionScale

    transmissionTransmitAovs = BoolField(default_value=False)
    transmission_transmit_aovs = transmissionTransmitAovs

    transmissionShadowDensity = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    transmission_shadow_density = transmissionShadowDensity

    subsurfaceWeight = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    subsurface_weight = subsurfaceWeight

    subsurfaceColor = SubsurfaceColorField(
        default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929)
    )
    subsurface_color = subsurfaceColor
    subsurfaceColorR = subsurfaceColor.subsurfaceColorR
    subsurface_colorr = subsurfaceColorR
    subsurfaceColorG = subsurfaceColor.subsurfaceColorG
    subsurface_colorg = subsurfaceColorG
    subsurfaceColorB = subsurfaceColor.subsurfaceColorB
    subsurface_colorb = subsurfaceColorB

    subsurfaceRadius = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    subsurface_radius = subsurfaceRadius

    subsurfaceRadiusScale = SubsurfaceRadiusScaleField(
        default_value=(1.0, 0.5, 0.25)
    )
    subsurface_radius_scale = subsurfaceRadiusScale
    subsurfaceRadiusScaleR = subsurfaceRadiusScale.subsurfaceRadiusScaleR
    subsurface_radius_scaler = subsurfaceRadiusScaleR
    subsurfaceRadiusScaleG = subsurfaceRadiusScale.subsurfaceRadiusScaleG
    subsurface_radius_scaleg = subsurfaceRadiusScaleG
    subsurfaceRadiusScaleB = subsurfaceRadiusScale.subsurfaceRadiusScaleB
    subsurface_radius_scaleb = subsurfaceRadiusScaleB

    subsurfaceScatterAnisotropy = FloatField(
        default_value=0.0, min_value=-1.0, max_value=1.0
    )
    subsurface_scatter_anisotropy = subsurfaceScatterAnisotropy

    coatWeight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_weight = coatWeight

    coatColor = CoatColorField(default_value=(1.0, 1.0, 1.0))
    coat_color = coatColor
    coatColorR = coatColor.coatColorR
    coat_colorr = coatColorR
    coatColorG = coatColor.coatColorG
    coat_colorg = coatColorG
    coatColorB = coatColor.coatColorB
    coat_colorb = coatColorB

    coatRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_roughness = coatRoughness

    coatRoughnessAnisotropy = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    coat_roughness_anisotropy = coatRoughnessAnisotropy

    coatIOR = FloatField(
        default_value=1.600000023841858,
        min_value=0.0,
        soft_min_value=1.0,
        soft_max_value=3.0,
    )
    coat_ior = coatIOR

    coatDarkening = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    coat_darkening = coatDarkening

    fuzzWeight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fuzz_weight = fuzzWeight

    fuzzColor = FuzzColorField(default_value=(1.0, 1.0, 1.0))
    fuzz_color = fuzzColor
    fuzzColorR = fuzzColor.fuzzColorR
    fuzz_colorr = fuzzColorR
    fuzzColorG = fuzzColor.fuzzColorG
    fuzz_colorg = fuzzColorG
    fuzzColorB = fuzzColor.fuzzColorB
    fuzz_colorb = fuzzColorB

    fuzzRoughness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    fuzz_roughness = fuzzRoughness

    emissionLuminance = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1000.0
    )
    emission_luminance = emissionLuminance

    emissionColor = EmissionColorField(default_value=(1.0, 1.0, 1.0))
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    thinFilmWeight = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    thin_film_weight = thinFilmWeight

    thinFilmThickness = FloatField(
        default_value=0.5, min_value=0.0, soft_max_value=1.0
    )
    thin_film_thickness = thinFilmThickness

    thinFilmIOR = FloatField(
        default_value=1.399999976158142,
        min_value=0.0,
        soft_min_value=1.0,
        soft_max_value=3.0,
    )
    thin_film_ior = thinFilmIOR

    geometryOpacity = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    geometry_opacity = geometryOpacity

    geometryThinWalled = BoolField(default_value=False)
    geometry_thin_walled = geometryThinWalled

    geometryTangent = GeometryTangentField(default_value=(0.0, 0.0, 0.0))
    geometry_tangent = geometryTangent
    geometryTangentX = geometryTangent.geometryTangentX
    geometry_tangentx = geometryTangentX
    geometryTangentY = geometryTangent.geometryTangentY
    geometry_tangenty = geometryTangentY
    geometryTangentZ = geometryTangent.geometryTangentZ
    geometry_tangentz = geometryTangentZ

    geometryCoatNormal = GeometryCoatNormalField(default_value=(0.0, 0.0, 0.0))
    geometry_coat_normal = geometryCoatNormal
    geometryCoatNormalX = geometryCoatNormal.geometryCoatNormalX
    geometry_coat_normalx = geometryCoatNormalX
    geometryCoatNormalY = geometryCoatNormal.geometryCoatNormalY
    geometry_coat_normaly = geometryCoatNormalY
    geometryCoatNormalZ = geometryCoatNormal.geometryCoatNormalZ
    geometry_coat_normalz = geometryCoatNormalZ

    geometryCoatTangent = GeometryCoatTangentField(
        default_value=(0.0, 0.0, 0.0)
    )
    geometry_coat_tangent = geometryCoatTangent
    geometryCoatTangentX = geometryCoatTangent.geometryCoatTangentX
    geometry_coat_tangentx = geometryCoatTangentX
    geometryCoatTangentY = geometryCoatTangent.geometryCoatTangentY
    geometry_coat_tangenty = geometryCoatTangentY
    geometryCoatTangentZ = geometryCoatTangent.geometryCoatTangentZ
    geometry_coat_tangentz = geometryCoatTangentZ

    caustics = BoolField(default_value=False)

    internalReflections = BoolField(default_value=True)
    internal_reflections = internalReflections

    exitToBackground = BoolField(default_value=False)
    exit_to_background = exitToBackground

    indirectDiffuse = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    indirect_diffuse = indirectDiffuse

    indirectSpecular = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    indirect_specular = indirectSpecular

    dielectricPriority = LongField(default_value=0)
    dielectric_priority = dielectricPriority

    aovId1 = DataStringField()
    aov_id1 = aovId1

    id1 = Id1Field(default_value=(0.0, 0.0, 0.0))
    id1R = id1.id1R
    id1r = id1R
    id1G = id1.id1G
    id1g = id1G
    id1B = id1.id1B
    id1b = id1B

    aovId2 = DataStringField()
    aov_id2 = aovId2

    id2 = Id2Field(default_value=(0.0, 0.0, 0.0))
    id2R = id2.id2R
    id2r = id2R
    id2G = id2.id2G
    id2g = id2G
    id2B = id2.id2B
    id2b = id2B

    aovId3 = DataStringField()
    aov_id3 = aovId3

    id3 = Id3Field(default_value=(0.0, 0.0, 0.0))
    id3R = id3.id3R
    id3r = id3R
    id3G = id3.id3G
    id3g = id3G
    id3B = id3.id3B
    id3b = id3B

    aovId4 = DataStringField()
    aov_id4 = aovId4

    id4 = Id4Field(default_value=(0.0, 0.0, 0.0))
    id4R = id4.id4R
    id4r = id4R
    id4G = id4.id4G
    id4g = id4G
    id4B = id4.id4B
    id4b = id4B

    aovId5 = DataStringField()
    aov_id5 = aovId5

    id5 = Id5Field(default_value=(0.0, 0.0, 0.0))
    id5R = id5.id5R
    id5r = id5R
    id5G = id5.id5G
    id5g = id5G
    id5B = id5.id5B
    id5b = id5B

    aovId6 = DataStringField()
    aov_id6 = aovId6

    id6 = Id6Field(default_value=(0.0, 0.0, 0.0))
    id6R = id6.id6R
    id6r = id6R
    id6G = id6.id6G
    id6g = id6G
    id6B = id6.id6B
    id6b = id6B

    aovId7 = DataStringField()
    aov_id7 = aovId7

    id7 = Id7Field(default_value=(0.0, 0.0, 0.0))
    id7R = id7.id7R
    id7r = id7R
    id7G = id7.id7G
    id7g = id7G
    id7B = id7.id7B
    id7b = id7B

    aovId8 = DataStringField()
    aov_id8 = aovId8

    id8 = Id8Field(default_value=(0.0, 0.0, 0.0))
    id8R = id8.id8R
    id8r = id8R
    id8G = id8.id8G
    id8g = id8G
    id8B = id8.id8B
    id8b = id8B
