# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class AiTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["AiTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiTransparencyR", "ai_transparencyr"),
        ("aiTransparencyG", "ai_transparencyg"),
        ("aiTransparencyB", "ai_transparencyb"),
    )

    aiTransparencyR = FloatField()
    ai_transparencyr = aiTransparencyR

    aiTransparencyG = FloatField()
    ai_transparencyg = aiTransparencyG

    aiTransparencyB = FloatField()
    ai_transparencyb = aiTransparencyB


class AiTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[AiTransparencyPlugOperator]
):
    __slots__ = ()

    aiTransparencyR = FloatField()
    ai_transparencyr = aiTransparencyR

    aiTransparencyG = FloatField()
    ai_transparencyg = aiTransparencyG

    aiTransparencyB = FloatField()
    ai_transparencyb = aiTransparencyB


class AiTransparencyField(
    Float3CompoundBaseField[AiTransparencyAttrOperator, AiTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiTransparencyAttrOperator
    PLUG_CLS = AiTransparencyPlugOperator

    aiTransparencyR = FloatField()
    ai_transparencyr = aiTransparencyR

    aiTransparencyG = FloatField()
    ai_transparencyg = aiTransparencyG

    aiTransparencyB = FloatField()
    ai_transparencyb = aiTransparencyB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class BaseColorPlugOperator(
    Float3CompoundBasePlugOperator["BaseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseColorR", "base_colorr"),
        ("baseColorG", "base_colorg"),
        ("baseColorB", "base_colorb"),
    )

    baseColorR = FloatField()
    base_colorr = baseColorR

    baseColorG = FloatField()
    base_colorg = baseColorG

    baseColorB = FloatField()
    base_colorb = baseColorB


class BaseColorAttrOperator(
    Float3CompoundBaseAttrOperator[BaseColorPlugOperator]
):
    __slots__ = ()

    baseColorR = FloatField()
    base_colorr = baseColorR

    baseColorG = FloatField()
    base_colorg = baseColorG

    baseColorB = FloatField()
    base_colorb = baseColorB


class BaseColorField(
    Float3CompoundBaseField[BaseColorAttrOperator, BaseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseColorAttrOperator
    PLUG_CLS = BaseColorPlugOperator

    baseColorR = FloatField()
    base_colorr = baseColorR

    baseColorG = FloatField()
    base_colorg = baseColorG

    baseColorB = FloatField()
    base_colorb = baseColorB


class SpecularTintPlugOperator(
    Float3CompoundBasePlugOperator["SpecularTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularTintR", "specular_tintr"),
        ("specularTintG", "specular_tintg"),
        ("specularTintB", "specular_tintb"),
    )

    specularTintR = FloatField()
    specular_tintr = specularTintR

    specularTintG = FloatField()
    specular_tintg = specularTintG

    specularTintB = FloatField()
    specular_tintb = specularTintB


class SpecularTintAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularTintPlugOperator]
):
    __slots__ = ()

    specularTintR = FloatField()
    specular_tintr = specularTintR

    specularTintG = FloatField()
    specular_tintg = specularTintG

    specularTintB = FloatField()
    specular_tintb = specularTintB


class SpecularTintField(
    Float3CompoundBaseField[SpecularTintAttrOperator, SpecularTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularTintAttrOperator
    PLUG_CLS = SpecularTintPlugOperator

    specularTintR = FloatField()
    specular_tintr = specularTintR

    specularTintG = FloatField()
    specular_tintg = specularTintG

    specularTintB = FloatField()
    specular_tintb = specularTintB


class Specular2TintPlugOperator(
    Float3CompoundBasePlugOperator["Specular2TintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specular2TintR", "specular2_tintr"),
        ("specular2TintG", "specular2_tintg"),
        ("specular2TintB", "specular2_tintb"),
    )

    specular2TintR = FloatField()
    specular2_tintr = specular2TintR

    specular2TintG = FloatField()
    specular2_tintg = specular2TintG

    specular2TintB = FloatField()
    specular2_tintb = specular2TintB


class Specular2TintAttrOperator(
    Float3CompoundBaseAttrOperator[Specular2TintPlugOperator]
):
    __slots__ = ()

    specular2TintR = FloatField()
    specular2_tintr = specular2TintR

    specular2TintG = FloatField()
    specular2_tintg = specular2TintG

    specular2TintB = FloatField()
    specular2_tintb = specular2TintB


class Specular2TintField(
    Float3CompoundBaseField[Specular2TintAttrOperator, Specular2TintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Specular2TintAttrOperator
    PLUG_CLS = Specular2TintPlugOperator

    specular2TintR = FloatField()
    specular2_tintr = specular2TintR

    specular2TintG = FloatField()
    specular2_tintg = specular2TintG

    specular2TintB = FloatField()
    specular2_tintb = specular2TintB


class TransmissionTintPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionTintR", "transmission_tintr"),
        ("transmissionTintG", "transmission_tintg"),
        ("transmissionTintB", "transmission_tintb"),
    )

    transmissionTintR = FloatField()
    transmission_tintr = transmissionTintR

    transmissionTintG = FloatField()
    transmission_tintg = transmissionTintG

    transmissionTintB = FloatField()
    transmission_tintb = transmissionTintB


class TransmissionTintAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionTintPlugOperator]
):
    __slots__ = ()

    transmissionTintR = FloatField()
    transmission_tintr = transmissionTintR

    transmissionTintG = FloatField()
    transmission_tintg = transmissionTintG

    transmissionTintB = FloatField()
    transmission_tintb = transmissionTintB


class TransmissionTintField(
    Float3CompoundBaseField[TransmissionTintAttrOperator, TransmissionTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmissionTintAttrOperator
    PLUG_CLS = TransmissionTintPlugOperator

    transmissionTintR = FloatField()
    transmission_tintr = transmissionTintR

    transmissionTintG = FloatField()
    transmission_tintg = transmissionTintG

    transmissionTintB = FloatField()
    transmission_tintb = transmissionTintB


class DiffuseColorPlugOperator(
    Float3CompoundBasePlugOperator["DiffuseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("diffuseColorR", "diffuse_colorr"),
        ("diffuseColorG", "diffuse_colorg"),
        ("diffuseColorB", "diffuse_colorb"),
    )

    diffuseColorR = FloatField()
    diffuse_colorr = diffuseColorR

    diffuseColorG = FloatField()
    diffuse_colorg = diffuseColorG

    diffuseColorB = FloatField()
    diffuse_colorb = diffuseColorB


class DiffuseColorAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseColorPlugOperator]
):
    __slots__ = ()

    diffuseColorR = FloatField()
    diffuse_colorr = diffuseColorR

    diffuseColorG = FloatField()
    diffuse_colorg = diffuseColorG

    diffuseColorB = FloatField()
    diffuse_colorb = diffuseColorB


class DiffuseColorField(
    Float3CompoundBaseField[DiffuseColorAttrOperator, DiffuseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DiffuseColorAttrOperator
    PLUG_CLS = DiffuseColorPlugOperator

    diffuseColorR = FloatField()
    diffuse_colorr = diffuseColorR

    diffuseColorG = FloatField()
    diffuse_colorg = diffuseColorG

    diffuseColorB = FloatField()
    diffuse_colorb = diffuseColorB


class EmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionColorR", "emission_colorr"),
        ("emissionColorG", "emission_colorg"),
        ("emissionColorB", "emission_colorb"),
    )

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[EmissionColorAttrOperator, EmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class OpacityPlugOperator(
    Float3CompoundBasePlugOperator["OpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityR", "opacityr"),
        ("opacityG", "opacityg"),
        ("opacityB", "opacityb"),
    )

    opacityR = FloatField()
    opacityr = opacityR

    opacityG = FloatField()
    opacityg = opacityG

    opacityB = FloatField()
    opacityb = opacityB


class OpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OpacityPlugOperator]
):
    __slots__ = ()

    opacityR = FloatField()
    opacityr = opacityR

    opacityG = FloatField()
    opacityg = opacityG

    opacityB = FloatField()
    opacityb = opacityB


class OpacityField(
    Float3CompoundBaseField[OpacityAttrOperator, OpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityAttrOperator
    PLUG_CLS = OpacityPlugOperator

    opacityR = FloatField()
    opacityr = opacityR

    opacityG = FloatField()
    opacityg = opacityG

    opacityB = FloatField()
    opacityb = opacityB


class Id1PlugOperator(
    Float3CompoundBasePlugOperator["Id1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id1R", "id1r"),
        ("id1G", "id1g"),
        ("id1B", "id1b"),
    )

    id1R = FloatField()
    id1r = id1R

    id1G = FloatField()
    id1g = id1G

    id1B = FloatField()
    id1b = id1B


class Id1AttrOperator(
    Float3CompoundBaseAttrOperator[Id1PlugOperator]
):
    __slots__ = ()

    id1R = FloatField()
    id1r = id1R

    id1G = FloatField()
    id1g = id1G

    id1B = FloatField()
    id1b = id1B


class Id1Field(
    Float3CompoundBaseField[Id1AttrOperator, Id1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id1AttrOperator
    PLUG_CLS = Id1PlugOperator

    id1R = FloatField()
    id1r = id1R

    id1G = FloatField()
    id1g = id1G

    id1B = FloatField()
    id1b = id1B


class Id2PlugOperator(
    Float3CompoundBasePlugOperator["Id2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id2R", "id2r"),
        ("id2G", "id2g"),
        ("id2B", "id2b"),
    )

    id2R = FloatField()
    id2r = id2R

    id2G = FloatField()
    id2g = id2G

    id2B = FloatField()
    id2b = id2B


class Id2AttrOperator(
    Float3CompoundBaseAttrOperator[Id2PlugOperator]
):
    __slots__ = ()

    id2R = FloatField()
    id2r = id2R

    id2G = FloatField()
    id2g = id2G

    id2B = FloatField()
    id2b = id2B


class Id2Field(
    Float3CompoundBaseField[Id2AttrOperator, Id2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id2AttrOperator
    PLUG_CLS = Id2PlugOperator

    id2R = FloatField()
    id2r = id2R

    id2G = FloatField()
    id2g = id2G

    id2B = FloatField()
    id2b = id2B


class Id3PlugOperator(
    Float3CompoundBasePlugOperator["Id3AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id3R", "id3r"),
        ("id3G", "id3g"),
        ("id3B", "id3b"),
    )

    id3R = FloatField()
    id3r = id3R

    id3G = FloatField()
    id3g = id3G

    id3B = FloatField()
    id3b = id3B


class Id3AttrOperator(
    Float3CompoundBaseAttrOperator[Id3PlugOperator]
):
    __slots__ = ()

    id3R = FloatField()
    id3r = id3R

    id3G = FloatField()
    id3g = id3G

    id3B = FloatField()
    id3b = id3B


class Id3Field(
    Float3CompoundBaseField[Id3AttrOperator, Id3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id3AttrOperator
    PLUG_CLS = Id3PlugOperator

    id3R = FloatField()
    id3r = id3R

    id3G = FloatField()
    id3g = id3G

    id3B = FloatField()
    id3b = id3B


class Id4PlugOperator(
    Float3CompoundBasePlugOperator["Id4AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id4R", "id4r"),
        ("id4G", "id4g"),
        ("id4B", "id4b"),
    )

    id4R = FloatField()
    id4r = id4R

    id4G = FloatField()
    id4g = id4G

    id4B = FloatField()
    id4b = id4B


class Id4AttrOperator(
    Float3CompoundBaseAttrOperator[Id4PlugOperator]
):
    __slots__ = ()

    id4R = FloatField()
    id4r = id4R

    id4G = FloatField()
    id4g = id4G

    id4B = FloatField()
    id4b = id4B


class Id4Field(
    Float3CompoundBaseField[Id4AttrOperator, Id4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id4AttrOperator
    PLUG_CLS = Id4PlugOperator

    id4R = FloatField()
    id4r = id4R

    id4G = FloatField()
    id4g = id4G

    id4B = FloatField()
    id4b = id4B


class Id5PlugOperator(
    Float3CompoundBasePlugOperator["Id5AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id5R", "id5r"),
        ("id5G", "id5g"),
        ("id5B", "id5b"),
    )

    id5R = FloatField()
    id5r = id5R

    id5G = FloatField()
    id5g = id5G

    id5B = FloatField()
    id5b = id5B


class Id5AttrOperator(
    Float3CompoundBaseAttrOperator[Id5PlugOperator]
):
    __slots__ = ()

    id5R = FloatField()
    id5r = id5R

    id5G = FloatField()
    id5g = id5G

    id5B = FloatField()
    id5b = id5B


class Id5Field(
    Float3CompoundBaseField[Id5AttrOperator, Id5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id5AttrOperator
    PLUG_CLS = Id5PlugOperator

    id5R = FloatField()
    id5r = id5R

    id5G = FloatField()
    id5g = id5G

    id5B = FloatField()
    id5b = id5B


class Id6PlugOperator(
    Float3CompoundBasePlugOperator["Id6AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id6R", "id6r"),
        ("id6G", "id6g"),
        ("id6B", "id6b"),
    )

    id6R = FloatField()
    id6r = id6R

    id6G = FloatField()
    id6g = id6G

    id6B = FloatField()
    id6b = id6B


class Id6AttrOperator(
    Float3CompoundBaseAttrOperator[Id6PlugOperator]
):
    __slots__ = ()

    id6R = FloatField()
    id6r = id6R

    id6G = FloatField()
    id6g = id6G

    id6B = FloatField()
    id6b = id6B


class Id6Field(
    Float3CompoundBaseField[Id6AttrOperator, Id6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id6AttrOperator
    PLUG_CLS = Id6PlugOperator

    id6R = FloatField()
    id6r = id6R

    id6G = FloatField()
    id6g = id6G

    id6B = FloatField()
    id6b = id6B


class Id7PlugOperator(
    Float3CompoundBasePlugOperator["Id7AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id7R", "id7r"),
        ("id7G", "id7g"),
        ("id7B", "id7b"),
    )

    id7R = FloatField()
    id7r = id7R

    id7G = FloatField()
    id7g = id7G

    id7B = FloatField()
    id7b = id7B


class Id7AttrOperator(
    Float3CompoundBaseAttrOperator[Id7PlugOperator]
):
    __slots__ = ()

    id7R = FloatField()
    id7r = id7R

    id7G = FloatField()
    id7g = id7G

    id7B = FloatField()
    id7b = id7B


class Id7Field(
    Float3CompoundBaseField[Id7AttrOperator, Id7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id7AttrOperator
    PLUG_CLS = Id7PlugOperator

    id7R = FloatField()
    id7r = id7R

    id7G = FloatField()
    id7g = id7G

    id7B = FloatField()
    id7b = id7B


class Id8PlugOperator(
    Float3CompoundBasePlugOperator["Id8AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id8R", "id8r"),
        ("id8G", "id8g"),
        ("id8B", "id8b"),
    )

    id8R = FloatField()
    id8r = id8R

    id8G = FloatField()
    id8g = id8G

    id8B = FloatField()
    id8b = id8B


class Id8AttrOperator(
    Float3CompoundBaseAttrOperator[Id8PlugOperator]
):
    __slots__ = ()

    id8R = FloatField()
    id8r = id8R

    id8G = FloatField()
    id8g = id8G

    id8B = FloatField()
    id8b = id8B


class Id8Field(
    Float3CompoundBaseField[Id8AttrOperator, Id8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Id8AttrOperator
    PLUG_CLS = Id8PlugOperator

    id8R = FloatField()
    id8r = id8R

    id8G = FloatField()
    id8g = id8G

    id8B = FloatField()
    id8b = id8B


class AiMatteColorPlugOperator(
    Float3CompoundBasePlugOperator["AiMatteColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiMatteColorR", "ai_matte_colorr"),
        ("aiMatteColorG", "ai_matte_colorg"),
        ("aiMatteColorB", "ai_matte_colorb"),
    )

    aiMatteColorR = FloatField()
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField()
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField()
    ai_matte_colorb = aiMatteColorB


class AiMatteColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiMatteColorPlugOperator]
):
    __slots__ = ()

    aiMatteColorR = FloatField()
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField()
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField()
    ai_matte_colorb = aiMatteColorB


class AiMatteColorField(
    Float3CompoundBaseField[AiMatteColorAttrOperator, AiMatteColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiMatteColorAttrOperator
    PLUG_CLS = AiMatteColorPlugOperator

    aiMatteColorR = FloatField()
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField()
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField()
    ai_matte_colorb = aiMatteColorB
