# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_standard_surface import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class SubsurfaceTypeEnumPlugOperator(EnumPlugOperator["SubsurfaceTypeEnumAttrOperator"]):
    __slots__ = ()

    DIFFUSION = 0
    RANDOMWALK = 1
    RANDOMWALK_V2 = 2


class SubsurfaceTypeEnumAttrOperator(EnumAttrOperator[SubsurfaceTypeEnumPlugOperator]):
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


class GeneratedAiStandardSurface(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandardSurface"

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

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
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

    base = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    baseColor = BaseColorField(default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929))
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    diffuseRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    diffuse_roughness = diffuseRoughness

    specular = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularRoughness = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)
    specular_roughness = specularRoughness

    specularIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=3.0)
    specular_IOR = specularIOR

    specularAnisotropy = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    specular_anisotropy = specularAnisotropy

    specularRotation = FloatField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    specular_rotation = specularRotation

    metalness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    transmission = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    transmissionColor = TransmissionColorField(default_value=(1.0, 1.0, 1.0))
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionDepth = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    transmission_depth = transmissionDepth

    transmissionScatter = TransmissionScatterField(default_value=(0.0, 0.0, 0.0))
    transmission_scatter = transmissionScatter
    transmissionScatterR = transmissionScatter.transmissionScatterR
    transmission_scatterr = transmissionScatterR
    transmissionScatterG = transmissionScatter.transmissionScatterG
    transmission_scatterg = transmissionScatterG
    transmissionScatterB = transmissionScatter.transmissionScatterB
    transmission_scatterb = transmissionScatterB

    transmissionScatterAnisotropy = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    transmission_scatter_anisotropy = transmissionScatterAnisotropy

    transmissionDispersion = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    transmission_dispersion = transmissionDispersion

    transmissionExtraRoughness = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    transmission_extra_roughness = transmissionExtraRoughness

    transmitAovs = BoolField(default_value=False)
    transmit_aovs = transmitAovs

    subsurface = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    subsurfaceColor = SubsurfaceColorField(default_value=(1.0, 1.0, 1.0))
    subsurface_color = subsurfaceColor
    subsurfaceColorR = subsurfaceColor.subsurfaceColorR
    subsurface_colorr = subsurfaceColorR
    subsurfaceColorG = subsurfaceColor.subsurfaceColorG
    subsurface_colorg = subsurfaceColorG
    subsurfaceColorB = subsurfaceColor.subsurfaceColorB
    subsurface_colorb = subsurfaceColorB

    subsurfaceRadius = SubsurfaceRadiusField(default_value=(1.0, 1.0, 1.0))
    subsurface_radius = subsurfaceRadius
    subsurfaceRadiusR = subsurfaceRadius.subsurfaceRadiusR
    subsurface_radiusr = subsurfaceRadiusR
    subsurfaceRadiusG = subsurfaceRadius.subsurfaceRadiusG
    subsurface_radiusg = subsurfaceRadiusG
    subsurfaceRadiusB = subsurfaceRadius.subsurfaceRadiusB
    subsurface_radiusb = subsurfaceRadiusB

    subsurfaceScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    subsurface_scale = subsurfaceScale

    subsurfaceAnisotropy = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    subsurface_anisotropy = subsurfaceAnisotropy

    subsurfaceType = SubsurfaceTypeEnumField(default_value=1)
    subsurface_type = subsurfaceType

    sheen = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    sheenColor = SheenColorField(default_value=(1.0, 1.0, 1.0))
    sheen_color = sheenColor
    sheenColorR = sheenColor.sheenColorR
    sheen_colorr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    sheen_colorg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    sheen_colorb = sheenColorB

    sheenRoughness = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)
    sheen_roughness = sheenRoughness

    thinWalled = BoolField(default_value=False)
    thin_walled = thinWalled

    tangent = TangentField(default_value=(0.0, 0.0, 0.0))
    tangentX = tangent.tangentX
    tangentx = tangentX
    tangentY = tangent.tangentY
    tangenty = tangentY
    tangentZ = tangent.tangentZ
    tangentz = tangentZ

    coat = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    coatColor = CoatColorField(default_value=(1.0, 1.0, 1.0))
    coat_color = coatColor
    coatColorR = coatColor.coatColorR
    coat_colorr = coatColorR
    coatColorG = coatColor.coatColorG
    coat_colorg = coatColorG
    coatColorB = coatColor.coatColorB
    coat_colorb = coatColorB

    coatRoughness = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    coat_roughness = coatRoughness

    coatIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=5.0)
    coat_IOR = coatIOR

    coatAnisotropy = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_anisotropy = coatAnisotropy

    coatRotation = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_rotation = coatRotation

    coatNormal = CoatNormalField(default_value=(0.0, 0.0, 0.0))
    coat_normal = coatNormal
    coatNormalX = coatNormal.coatNormalX
    coat_normalx = coatNormalX
    coatNormalY = coatNormal.coatNormalY
    coat_normaly = coatNormalY
    coatNormalZ = coatNormal.coatNormalZ
    coat_normalz = coatNormalZ

    coatAffectColor = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_affect_color = coatAffectColor

    coatAffectRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_affect_roughness = coatAffectRoughness

    thinFilmThickness = FloatField(default_value=0.0, min_value=0.0, soft_max_value=2000.0)
    thin_film_thickness = thinFilmThickness

    thinFilmIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=3.0)
    thin_film_IOR = thinFilmIOR

    emission = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    emissionColor = EmissionColorField(default_value=(1.0, 1.0, 1.0))
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    opacity = OpacityField(default_value=(1.0, 1.0, 1.0))
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB

    caustics = BoolField(default_value=False)

    internalReflections = BoolField(default_value=True)
    internal_reflections = internalReflections

    exitToBackground = BoolField(default_value=False)
    exit_to_background = exitToBackground

    indirectDiffuse = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    indirect_diffuse = indirectDiffuse

    indirectSpecular = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    indirect_specular = indirectSpecular

    dielectricPriority = LongField(default_value=0, soft_min_value=-10, soft_max_value=10)
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
