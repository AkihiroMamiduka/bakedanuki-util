# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_standard_surface import (
    AiMatteColorField,
    BaseColorField,
    CoatColorField,
    CoatNormalField,
    EmissionColorField,
    Id1Field,
    Id2Field,
    Id3Field,
    Id4Field,
    Id5Field,
    Id6Field,
    Id7Field,
    Id8Field,
    NormalCameraField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
    SheenColorField,
    SpecularColorField,
    SubsurfaceColorField,
    SubsurfaceRadiusField,
    TangentField,
    TransmissionColorField,
    TransmissionScatterField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class SubsurfaceTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DIFFUSION = 0
    RANDOMWALK = 1
    RANDOMWALK_V2 = 2


class SubsurfaceTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DIFFUSION = 0
    RANDOMWALK = 1
    RANDOMWALK_V2 = 2

    NAME_MAP = {
        DIFFUSION: "diffusion",
        RANDOMWALK: "randomwalk",
        RANDOMWALK_V2: "randomwalk_v2",
    }


class SubsurfaceTypeEnumField(
    EnumField[SubsurfaceTypeEnumAttrOperator, SubsurfaceTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubsurfaceTypeEnumAttrOperator
    PLUG_CLS = SubsurfaceTypeEnumPlugOperator


class AiStandardSurface(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandardSurface"

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

    base = FloatField()

    baseColor = BaseColorField()
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    diffuseRoughness = FloatField()
    diffuse_roughness = diffuseRoughness

    specular = FloatField()

    specularColor = SpecularColorField()
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularRoughness = FloatField()
    specular_roughness = specularRoughness

    specularIOR = FloatField()
    specular_IOR = specularIOR

    specularAnisotropy = FloatField()
    specular_anisotropy = specularAnisotropy

    specularRotation = FloatField()
    specular_rotation = specularRotation

    metalness = FloatField()

    transmission = FloatField()

    transmissionColor = TransmissionColorField()
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionDepth = FloatField()
    transmission_depth = transmissionDepth

    transmissionScatter = TransmissionScatterField()
    transmission_scatter = transmissionScatter
    transmissionScatterR = transmissionScatter.transmissionScatterR
    transmission_scatterr = transmissionScatterR
    transmissionScatterG = transmissionScatter.transmissionScatterG
    transmission_scatterg = transmissionScatterG
    transmissionScatterB = transmissionScatter.transmissionScatterB
    transmission_scatterb = transmissionScatterB

    transmissionScatterAnisotropy = FloatField()
    transmission_scatter_anisotropy = transmissionScatterAnisotropy

    transmissionDispersion = FloatField()
    transmission_dispersion = transmissionDispersion

    transmissionExtraRoughness = FloatField()
    transmission_extra_roughness = transmissionExtraRoughness

    transmitAovs = BoolField()
    transmit_aovs = transmitAovs

    subsurface = FloatField()

    subsurfaceColor = SubsurfaceColorField()
    subsurface_color = subsurfaceColor
    subsurfaceColorR = subsurfaceColor.subsurfaceColorR
    subsurface_colorr = subsurfaceColorR
    subsurfaceColorG = subsurfaceColor.subsurfaceColorG
    subsurface_colorg = subsurfaceColorG
    subsurfaceColorB = subsurfaceColor.subsurfaceColorB
    subsurface_colorb = subsurfaceColorB

    subsurfaceRadius = SubsurfaceRadiusField()
    subsurface_radius = subsurfaceRadius
    subsurfaceRadiusR = subsurfaceRadius.subsurfaceRadiusR
    subsurface_radiusr = subsurfaceRadiusR
    subsurfaceRadiusG = subsurfaceRadius.subsurfaceRadiusG
    subsurface_radiusg = subsurfaceRadiusG
    subsurfaceRadiusB = subsurfaceRadius.subsurfaceRadiusB
    subsurface_radiusb = subsurfaceRadiusB

    subsurfaceScale = FloatField()
    subsurface_scale = subsurfaceScale

    subsurfaceAnisotropy = FloatField()
    subsurface_anisotropy = subsurfaceAnisotropy

    subsurfaceType = SubsurfaceTypeEnumField()
    subsurface_type = subsurfaceType

    sheen = FloatField()

    sheenColor = SheenColorField()
    sheen_color = sheenColor
    sheenColorR = sheenColor.sheenColorR
    sheen_colorr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    sheen_colorg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    sheen_colorb = sheenColorB

    sheenRoughness = FloatField()
    sheen_roughness = sheenRoughness

    thinWalled = BoolField()
    thin_walled = thinWalled

    tangent = TangentField()
    tangentX = tangent.tangentX
    tangentx = tangentX
    tangentY = tangent.tangentY
    tangenty = tangentY
    tangentZ = tangent.tangentZ
    tangentz = tangentZ

    coat = FloatField()

    coatColor = CoatColorField()
    coat_color = coatColor
    coatColorR = coatColor.coatColorR
    coat_colorr = coatColorR
    coatColorG = coatColor.coatColorG
    coat_colorg = coatColorG
    coatColorB = coatColor.coatColorB
    coat_colorb = coatColorB

    coatRoughness = FloatField()
    coat_roughness = coatRoughness

    coatIOR = FloatField()
    coat_IOR = coatIOR

    coatAnisotropy = FloatField()
    coat_anisotropy = coatAnisotropy

    coatRotation = FloatField()
    coat_rotation = coatRotation

    coatNormal = CoatNormalField()
    coat_normal = coatNormal
    coatNormalX = coatNormal.coatNormalX
    coat_normalx = coatNormalX
    coatNormalY = coatNormal.coatNormalY
    coat_normaly = coatNormalY
    coatNormalZ = coatNormal.coatNormalZ
    coat_normalz = coatNormalZ

    coatAffectColor = FloatField()
    coat_affect_color = coatAffectColor

    coatAffectRoughness = FloatField()
    coat_affect_roughness = coatAffectRoughness

    thinFilmThickness = FloatField()
    thin_film_thickness = thinFilmThickness

    thinFilmIOR = FloatField()
    thin_film_IOR = thinFilmIOR

    emission = FloatField()

    emissionColor = EmissionColorField()
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    opacity = OpacityField()
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB

    caustics = BoolField()

    internalReflections = BoolField()
    internal_reflections = internalReflections

    exitToBackground = BoolField()
    exit_to_background = exitToBackground

    indirectDiffuse = FloatField()
    indirect_diffuse = indirectDiffuse

    indirectSpecular = FloatField()
    indirect_specular = indirectSpecular

    dielectricPriority = LongField()
    dielectric_priority = dielectricPriority

    aovId1 = DataStringField()
    aov_id1 = aovId1

    id1 = Id1Field()
    id1R = id1.id1R
    id1r = id1R
    id1G = id1.id1G
    id1g = id1G
    id1B = id1.id1B
    id1b = id1B

    aovId2 = DataStringField()
    aov_id2 = aovId2

    id2 = Id2Field()
    id2R = id2.id2R
    id2r = id2R
    id2G = id2.id2G
    id2g = id2G
    id2B = id2.id2B
    id2b = id2B

    aovId3 = DataStringField()
    aov_id3 = aovId3

    id3 = Id3Field()
    id3R = id3.id3R
    id3r = id3R
    id3G = id3.id3G
    id3g = id3G
    id3B = id3.id3B
    id3b = id3B

    aovId4 = DataStringField()
    aov_id4 = aovId4

    id4 = Id4Field()
    id4R = id4.id4R
    id4r = id4R
    id4G = id4.id4G
    id4g = id4G
    id4B = id4.id4B
    id4b = id4B

    aovId5 = DataStringField()
    aov_id5 = aovId5

    id5 = Id5Field()
    id5R = id5.id5R
    id5r = id5R
    id5G = id5.id5G
    id5g = id5G
    id5B = id5.id5B
    id5b = id5B

    aovId6 = DataStringField()
    aov_id6 = aovId6

    id6 = Id6Field()
    id6R = id6.id6R
    id6r = id6R
    id6G = id6.id6G
    id6g = id6G
    id6B = id6.id6B
    id6b = id6B

    aovId7 = DataStringField()
    aov_id7 = aovId7

    id7 = Id7Field()
    id7R = id7.id7R
    id7r = id7R
    id7G = id7.id7G
    id7g = id7G
    id7B = id7.id7B
    id7b = id7B

    aovId8 = DataStringField()
    aov_id8 = aovId8

    id8 = Id8Field()
    id8R = id8.id8R
    id8r = id8R
    id8G = id8.id8G
    id8g = id8G
    id8B = id8.id8B
    id8b = id8B
