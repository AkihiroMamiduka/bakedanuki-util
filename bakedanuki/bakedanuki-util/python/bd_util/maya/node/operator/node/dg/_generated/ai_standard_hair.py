# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_standard_hair import (
    AiMatteColorField,
    AiTransparencyField,
    BaseColorField,
    DiffuseColorField,
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
    Specular2TintField,
    SpecularTintField,
    TransmissionTintField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiStandardHair(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandardHair"

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    aiTransparency = AiTransparencyField(default_value=(0.0, 0.0, 0.0))
    ai_transparency = aiTransparency
    aiTransparencyR = aiTransparency.aiTransparencyR
    ai_transparencyr = aiTransparencyR
    aiTransparencyG = aiTransparency.aiTransparencyG
    ai_transparencyg = aiTransparencyG
    aiTransparencyB = aiTransparency.aiTransparencyB
    ai_transparencyb = aiTransparencyB

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

    base = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    baseColor = BaseColorField(default_value=(1.0, 1.0, 1.0))
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    melanin = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    melaninRedness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    melanin_redness = melaninRedness

    melaninRandomize = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    melanin_randomize = melaninRandomize

    roughness = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)

    roughnessAzimuthal = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)
    roughness_azimuthal = roughnessAzimuthal

    roughnessAnisotropic = BoolField(default_value=False)
    roughness_anisotropic = roughnessAnisotropic

    ior = FloatField(default_value=1.5499999523162842, min_value=0.0, soft_max_value=5.0)

    shift = FloatField(default_value=3.0, min_value=-90.0, max_value=90.0, soft_min_value=0.0, soft_max_value=20.0)

    specularTint = SpecularTintField(default_value=(1.0, 1.0, 1.0))
    specular_tint = specularTint
    specularTintR = specularTint.specularTintR
    specular_tintr = specularTintR
    specularTintG = specularTint.specularTintG
    specular_tintg = specularTintG
    specularTintB = specularTint.specularTintB
    specular_tintb = specularTintB

    specular2Tint = Specular2TintField(default_value=(1.0, 1.0, 1.0))
    specular2_tint = specular2Tint
    specular2TintR = specular2Tint.specular2TintR
    specular2_tintr = specular2TintR
    specular2TintG = specular2Tint.specular2TintG
    specular2_tintg = specular2TintG
    specular2TintB = specular2Tint.specular2TintB
    specular2_tintb = specular2TintB

    transmissionTint = TransmissionTintField(default_value=(1.0, 1.0, 1.0))
    transmission_tint = transmissionTint
    transmissionTintR = transmissionTint.transmissionTintR
    transmission_tintr = transmissionTintR
    transmissionTintG = transmissionTint.transmissionTintG
    transmission_tintg = transmissionTintG
    transmissionTintB = transmissionTint.transmissionTintB
    transmission_tintb = transmissionTintB

    diffuse = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    diffuseColor = DiffuseColorField(default_value=(1.0, 1.0, 1.0))
    diffuse_color = diffuseColor
    diffuseColorR = diffuseColor.diffuseColorR
    diffuse_colorr = diffuseColorR
    diffuseColorG = diffuseColor.diffuseColorG
    diffuse_colorg = diffuseColorG
    diffuseColorB = diffuseColor.diffuseColorB
    diffuse_colorb = diffuseColorB

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

    indirectDiffuse = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    indirect_diffuse = indirectDiffuse

    indirectSpecular = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    indirect_specular = indirectSpecular

    extraDepth = LongField(default_value=16, min_value=0, max_value=64)
    extra_depth = extraDepth

    extraSamples = LongField(default_value=0)
    extra_samples = extraSamples

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

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiEnableMatte = BoolField(default_value=False, category="arnold")
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_matte_color_a = aiMatteColorA
