# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class AiMatteColorPlugOperator(
    Float3CompoundBasePlugOperator["AiMatteColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiMatteColorR", "ai_matte_colorr"),
        ("aiMatteColorG", "ai_matte_colorg"),
        ("aiMatteColorB", "ai_matte_colorb"),
    )

    aiMatteColorR = FloatField(default_value=0.0)
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField(default_value=0.0)
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField(default_value=0.0)
    ai_matte_colorb = aiMatteColorB


class AiMatteColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiMatteColorPlugOperator]
):
    __slots__ = ()

    aiMatteColorR = FloatField(default_value=0.0)
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField(default_value=0.0)
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField(default_value=0.0)
    ai_matte_colorb = aiMatteColorB


class AiMatteColorField(
    Float3CompoundBaseField[AiMatteColorAttrOperator, AiMatteColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiMatteColorAttrOperator
    PLUG_CLS = AiMatteColorPlugOperator

    aiMatteColorR = FloatField(default_value=0.0)
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField(default_value=0.0)
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField(default_value=0.0)
    ai_matte_colorb = aiMatteColorB


class BaseColorPlugOperator(
    Float3CompoundBasePlugOperator["BaseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseColorR", "base_colorr"),
        ("baseColorG", "base_colorg"),
        ("baseColorB", "base_colorb"),
    )

    baseColorR = FloatField(default_value=0.800000011920929)
    base_colorr = baseColorR

    baseColorG = FloatField(default_value=0.800000011920929)
    base_colorg = baseColorG

    baseColorB = FloatField(default_value=0.800000011920929)
    base_colorb = baseColorB


class BaseColorAttrOperator(
    Float3CompoundBaseAttrOperator[BaseColorPlugOperator]
):
    __slots__ = ()

    baseColorR = FloatField(default_value=0.800000011920929)
    base_colorr = baseColorR

    baseColorG = FloatField(default_value=0.800000011920929)
    base_colorg = baseColorG

    baseColorB = FloatField(default_value=0.800000011920929)
    base_colorb = baseColorB


class BaseColorField(
    Float3CompoundBaseField[BaseColorAttrOperator, BaseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseColorAttrOperator
    PLUG_CLS = BaseColorPlugOperator

    baseColorR = FloatField(default_value=0.800000011920929)
    base_colorr = baseColorR

    baseColorG = FloatField(default_value=0.800000011920929)
    base_colorg = baseColorG

    baseColorB = FloatField(default_value=0.800000011920929)
    base_colorb = baseColorB


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "specular_colorr"),
        ("specularColorG", "specular_colorg"),
        ("specularColorB", "specular_colorb"),
    )

    specularColorR = FloatField(default_value=1.0)
    specular_colorr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    specular_colorg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    specular_colorb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=1.0)
    specular_colorr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    specular_colorg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    specular_colorb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[
        SpecularColorAttrOperator, SpecularColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=1.0)
    specular_colorr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    specular_colorg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    specular_colorb = specularColorB


class TransmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionColorR", "transmission_colorr"),
        ("transmissionColorG", "transmission_colorg"),
        ("transmissionColorB", "transmission_colorb"),
    )

    transmissionColorR = FloatField(default_value=1.0)
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField(default_value=1.0)
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField(default_value=1.0)
    transmission_colorb = transmissionColorB


class TransmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionColorPlugOperator]
):
    __slots__ = ()

    transmissionColorR = FloatField(default_value=1.0)
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField(default_value=1.0)
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField(default_value=1.0)
    transmission_colorb = transmissionColorB


class TransmissionColorField(
    Float3CompoundBaseField[
        TransmissionColorAttrOperator, TransmissionColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TransmissionColorAttrOperator
    PLUG_CLS = TransmissionColorPlugOperator

    transmissionColorR = FloatField(default_value=1.0)
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField(default_value=1.0)
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField(default_value=1.0)
    transmission_colorb = transmissionColorB


class TransmissionScatterPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionScatterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionScatterR", "transmission_scatterr"),
        ("transmissionScatterG", "transmission_scatterg"),
        ("transmissionScatterB", "transmission_scatterb"),
    )

    transmissionScatterR = FloatField(default_value=0.0)
    transmission_scatterr = transmissionScatterR

    transmissionScatterG = FloatField(default_value=0.0)
    transmission_scatterg = transmissionScatterG

    transmissionScatterB = FloatField(default_value=0.0)
    transmission_scatterb = transmissionScatterB


class TransmissionScatterAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionScatterPlugOperator]
):
    __slots__ = ()

    transmissionScatterR = FloatField(default_value=0.0)
    transmission_scatterr = transmissionScatterR

    transmissionScatterG = FloatField(default_value=0.0)
    transmission_scatterg = transmissionScatterG

    transmissionScatterB = FloatField(default_value=0.0)
    transmission_scatterb = transmissionScatterB


class TransmissionScatterField(
    Float3CompoundBaseField[
        TransmissionScatterAttrOperator, TransmissionScatterPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TransmissionScatterAttrOperator
    PLUG_CLS = TransmissionScatterPlugOperator

    transmissionScatterR = FloatField(default_value=0.0)
    transmission_scatterr = transmissionScatterR

    transmissionScatterG = FloatField(default_value=0.0)
    transmission_scatterg = transmissionScatterG

    transmissionScatterB = FloatField(default_value=0.0)
    transmission_scatterb = transmissionScatterB


class SubsurfaceColorPlugOperator(
    Float3CompoundBasePlugOperator["SubsurfaceColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("subsurfaceColorR", "subsurface_colorr"),
        ("subsurfaceColorG", "subsurface_colorg"),
        ("subsurfaceColorB", "subsurface_colorb"),
    )

    subsurfaceColorR = FloatField(default_value=1.0)
    subsurface_colorr = subsurfaceColorR

    subsurfaceColorG = FloatField(default_value=1.0)
    subsurface_colorg = subsurfaceColorG

    subsurfaceColorB = FloatField(default_value=1.0)
    subsurface_colorb = subsurfaceColorB


class SubsurfaceColorAttrOperator(
    Float3CompoundBaseAttrOperator[SubsurfaceColorPlugOperator]
):
    __slots__ = ()

    subsurfaceColorR = FloatField(default_value=1.0)
    subsurface_colorr = subsurfaceColorR

    subsurfaceColorG = FloatField(default_value=1.0)
    subsurface_colorg = subsurfaceColorG

    subsurfaceColorB = FloatField(default_value=1.0)
    subsurface_colorb = subsurfaceColorB


class SubsurfaceColorField(
    Float3CompoundBaseField[
        SubsurfaceColorAttrOperator, SubsurfaceColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SubsurfaceColorAttrOperator
    PLUG_CLS = SubsurfaceColorPlugOperator

    subsurfaceColorR = FloatField(default_value=1.0)
    subsurface_colorr = subsurfaceColorR

    subsurfaceColorG = FloatField(default_value=1.0)
    subsurface_colorg = subsurfaceColorG

    subsurfaceColorB = FloatField(default_value=1.0)
    subsurface_colorb = subsurfaceColorB


class SubsurfaceRadiusPlugOperator(
    Float3CompoundBasePlugOperator["SubsurfaceRadiusAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("subsurfaceRadiusR", "subsurface_radiusr"),
        ("subsurfaceRadiusG", "subsurface_radiusg"),
        ("subsurfaceRadiusB", "subsurface_radiusb"),
    )

    subsurfaceRadiusR = FloatField(default_value=1.0)
    subsurface_radiusr = subsurfaceRadiusR

    subsurfaceRadiusG = FloatField(default_value=1.0)
    subsurface_radiusg = subsurfaceRadiusG

    subsurfaceRadiusB = FloatField(default_value=1.0)
    subsurface_radiusb = subsurfaceRadiusB


class SubsurfaceRadiusAttrOperator(
    Float3CompoundBaseAttrOperator[SubsurfaceRadiusPlugOperator]
):
    __slots__ = ()

    subsurfaceRadiusR = FloatField(default_value=1.0)
    subsurface_radiusr = subsurfaceRadiusR

    subsurfaceRadiusG = FloatField(default_value=1.0)
    subsurface_radiusg = subsurfaceRadiusG

    subsurfaceRadiusB = FloatField(default_value=1.0)
    subsurface_radiusb = subsurfaceRadiusB


class SubsurfaceRadiusField(
    Float3CompoundBaseField[
        SubsurfaceRadiusAttrOperator, SubsurfaceRadiusPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SubsurfaceRadiusAttrOperator
    PLUG_CLS = SubsurfaceRadiusPlugOperator

    subsurfaceRadiusR = FloatField(default_value=1.0)
    subsurface_radiusr = subsurfaceRadiusR

    subsurfaceRadiusG = FloatField(default_value=1.0)
    subsurface_radiusg = subsurfaceRadiusG

    subsurfaceRadiusB = FloatField(default_value=1.0)
    subsurface_radiusb = subsurfaceRadiusB


class SheenColorPlugOperator(
    Float3CompoundBasePlugOperator["SheenColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sheenColorR", "sheen_colorr"),
        ("sheenColorG", "sheen_colorg"),
        ("sheenColorB", "sheen_colorb"),
    )

    sheenColorR = FloatField(default_value=1.0)
    sheen_colorr = sheenColorR

    sheenColorG = FloatField(default_value=1.0)
    sheen_colorg = sheenColorG

    sheenColorB = FloatField(default_value=1.0)
    sheen_colorb = sheenColorB


class SheenColorAttrOperator(
    Float3CompoundBaseAttrOperator[SheenColorPlugOperator]
):
    __slots__ = ()

    sheenColorR = FloatField(default_value=1.0)
    sheen_colorr = sheenColorR

    sheenColorG = FloatField(default_value=1.0)
    sheen_colorg = sheenColorG

    sheenColorB = FloatField(default_value=1.0)
    sheen_colorb = sheenColorB


class SheenColorField(
    Float3CompoundBaseField[SheenColorAttrOperator, SheenColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SheenColorAttrOperator
    PLUG_CLS = SheenColorPlugOperator

    sheenColorR = FloatField(default_value=1.0)
    sheen_colorr = sheenColorR

    sheenColorG = FloatField(default_value=1.0)
    sheen_colorg = sheenColorG

    sheenColorB = FloatField(default_value=1.0)
    sheen_colorb = sheenColorB


class TangentPlugOperator(
    Float3CompoundBasePlugOperator["TangentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentX", "tangentx"),
        ("tangentY", "tangenty"),
        ("tangentZ", "tangentz"),
    )

    tangentX = FloatField(default_value=0.0)
    tangentx = tangentX

    tangentY = FloatField(default_value=0.0)
    tangenty = tangentY

    tangentZ = FloatField(default_value=0.0)
    tangentz = tangentZ


class TangentAttrOperator(Float3CompoundBaseAttrOperator[TangentPlugOperator]):
    __slots__ = ()

    tangentX = FloatField(default_value=0.0)
    tangentx = tangentX

    tangentY = FloatField(default_value=0.0)
    tangenty = tangentY

    tangentZ = FloatField(default_value=0.0)
    tangentz = tangentZ


class TangentField(
    Float3CompoundBaseField[TangentAttrOperator, TangentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentAttrOperator
    PLUG_CLS = TangentPlugOperator

    tangentX = FloatField(default_value=0.0)
    tangentx = tangentX

    tangentY = FloatField(default_value=0.0)
    tangenty = tangentY

    tangentZ = FloatField(default_value=0.0)
    tangentz = tangentZ


class CoatColorPlugOperator(
    Float3CompoundBasePlugOperator["CoatColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coatColorR", "coat_colorr"),
        ("coatColorG", "coat_colorg"),
        ("coatColorB", "coat_colorb"),
    )

    coatColorR = FloatField(default_value=1.0)
    coat_colorr = coatColorR

    coatColorG = FloatField(default_value=1.0)
    coat_colorg = coatColorG

    coatColorB = FloatField(default_value=1.0)
    coat_colorb = coatColorB


class CoatColorAttrOperator(
    Float3CompoundBaseAttrOperator[CoatColorPlugOperator]
):
    __slots__ = ()

    coatColorR = FloatField(default_value=1.0)
    coat_colorr = coatColorR

    coatColorG = FloatField(default_value=1.0)
    coat_colorg = coatColorG

    coatColorB = FloatField(default_value=1.0)
    coat_colorb = coatColorB


class CoatColorField(
    Float3CompoundBaseField[CoatColorAttrOperator, CoatColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoatColorAttrOperator
    PLUG_CLS = CoatColorPlugOperator

    coatColorR = FloatField(default_value=1.0)
    coat_colorr = coatColorR

    coatColorG = FloatField(default_value=1.0)
    coat_colorg = coatColorG

    coatColorB = FloatField(default_value=1.0)
    coat_colorb = coatColorB


class CoatNormalPlugOperator(
    Float3CompoundBasePlugOperator["CoatNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coatNormalX", "coat_normalx"),
        ("coatNormalY", "coat_normaly"),
        ("coatNormalZ", "coat_normalz"),
    )

    coatNormalX = FloatField(default_value=0.0)
    coat_normalx = coatNormalX

    coatNormalY = FloatField(default_value=0.0)
    coat_normaly = coatNormalY

    coatNormalZ = FloatField(default_value=0.0)
    coat_normalz = coatNormalZ


class CoatNormalAttrOperator(
    Float3CompoundBaseAttrOperator[CoatNormalPlugOperator]
):
    __slots__ = ()

    coatNormalX = FloatField(default_value=0.0)
    coat_normalx = coatNormalX

    coatNormalY = FloatField(default_value=0.0)
    coat_normaly = coatNormalY

    coatNormalZ = FloatField(default_value=0.0)
    coat_normalz = coatNormalZ


class CoatNormalField(
    Float3CompoundBaseField[CoatNormalAttrOperator, CoatNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoatNormalAttrOperator
    PLUG_CLS = CoatNormalPlugOperator

    coatNormalX = FloatField(default_value=0.0)
    coat_normalx = coatNormalX

    coatNormalY = FloatField(default_value=0.0)
    coat_normaly = coatNormalY

    coatNormalZ = FloatField(default_value=0.0)
    coat_normalz = coatNormalZ


class EmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionColorR", "emission_colorr"),
        ("emissionColorG", "emission_colorg"),
        ("emissionColorB", "emission_colorb"),
    )

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[
        EmissionColorAttrOperator, EmissionColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
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

    opacityR = FloatField(default_value=1.0)
    opacityr = opacityR

    opacityG = FloatField(default_value=1.0)
    opacityg = opacityG

    opacityB = FloatField(default_value=1.0)
    opacityb = opacityB


class OpacityAttrOperator(Float3CompoundBaseAttrOperator[OpacityPlugOperator]):
    __slots__ = ()

    opacityR = FloatField(default_value=1.0)
    opacityr = opacityR

    opacityG = FloatField(default_value=1.0)
    opacityg = opacityG

    opacityB = FloatField(default_value=1.0)
    opacityb = opacityB


class OpacityField(
    Float3CompoundBaseField[OpacityAttrOperator, OpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityAttrOperator
    PLUG_CLS = OpacityPlugOperator

    opacityR = FloatField(default_value=1.0)
    opacityr = opacityR

    opacityG = FloatField(default_value=1.0)
    opacityg = opacityG

    opacityB = FloatField(default_value=1.0)
    opacityb = opacityB


class Id1PlugOperator(Float3CompoundBasePlugOperator["Id1AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id1R", "id1r"),
        ("id1G", "id1g"),
        ("id1B", "id1b"),
    )

    id1R = FloatField(default_value=0.0)
    id1r = id1R

    id1G = FloatField(default_value=0.0)
    id1g = id1G

    id1B = FloatField(default_value=0.0)
    id1b = id1B


class Id1AttrOperator(Float3CompoundBaseAttrOperator[Id1PlugOperator]):
    __slots__ = ()

    id1R = FloatField(default_value=0.0)
    id1r = id1R

    id1G = FloatField(default_value=0.0)
    id1g = id1G

    id1B = FloatField(default_value=0.0)
    id1b = id1B


class Id1Field(Float3CompoundBaseField[Id1AttrOperator, Id1PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id1AttrOperator
    PLUG_CLS = Id1PlugOperator

    id1R = FloatField(default_value=0.0)
    id1r = id1R

    id1G = FloatField(default_value=0.0)
    id1g = id1G

    id1B = FloatField(default_value=0.0)
    id1b = id1B


class Id2PlugOperator(Float3CompoundBasePlugOperator["Id2AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id2R", "id2r"),
        ("id2G", "id2g"),
        ("id2B", "id2b"),
    )

    id2R = FloatField(default_value=0.0)
    id2r = id2R

    id2G = FloatField(default_value=0.0)
    id2g = id2G

    id2B = FloatField(default_value=0.0)
    id2b = id2B


class Id2AttrOperator(Float3CompoundBaseAttrOperator[Id2PlugOperator]):
    __slots__ = ()

    id2R = FloatField(default_value=0.0)
    id2r = id2R

    id2G = FloatField(default_value=0.0)
    id2g = id2G

    id2B = FloatField(default_value=0.0)
    id2b = id2B


class Id2Field(Float3CompoundBaseField[Id2AttrOperator, Id2PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id2AttrOperator
    PLUG_CLS = Id2PlugOperator

    id2R = FloatField(default_value=0.0)
    id2r = id2R

    id2G = FloatField(default_value=0.0)
    id2g = id2G

    id2B = FloatField(default_value=0.0)
    id2b = id2B


class Id3PlugOperator(Float3CompoundBasePlugOperator["Id3AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id3R", "id3r"),
        ("id3G", "id3g"),
        ("id3B", "id3b"),
    )

    id3R = FloatField(default_value=0.0)
    id3r = id3R

    id3G = FloatField(default_value=0.0)
    id3g = id3G

    id3B = FloatField(default_value=0.0)
    id3b = id3B


class Id3AttrOperator(Float3CompoundBaseAttrOperator[Id3PlugOperator]):
    __slots__ = ()

    id3R = FloatField(default_value=0.0)
    id3r = id3R

    id3G = FloatField(default_value=0.0)
    id3g = id3G

    id3B = FloatField(default_value=0.0)
    id3b = id3B


class Id3Field(Float3CompoundBaseField[Id3AttrOperator, Id3PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id3AttrOperator
    PLUG_CLS = Id3PlugOperator

    id3R = FloatField(default_value=0.0)
    id3r = id3R

    id3G = FloatField(default_value=0.0)
    id3g = id3G

    id3B = FloatField(default_value=0.0)
    id3b = id3B


class Id4PlugOperator(Float3CompoundBasePlugOperator["Id4AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id4R", "id4r"),
        ("id4G", "id4g"),
        ("id4B", "id4b"),
    )

    id4R = FloatField(default_value=0.0)
    id4r = id4R

    id4G = FloatField(default_value=0.0)
    id4g = id4G

    id4B = FloatField(default_value=0.0)
    id4b = id4B


class Id4AttrOperator(Float3CompoundBaseAttrOperator[Id4PlugOperator]):
    __slots__ = ()

    id4R = FloatField(default_value=0.0)
    id4r = id4R

    id4G = FloatField(default_value=0.0)
    id4g = id4G

    id4B = FloatField(default_value=0.0)
    id4b = id4B


class Id4Field(Float3CompoundBaseField[Id4AttrOperator, Id4PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id4AttrOperator
    PLUG_CLS = Id4PlugOperator

    id4R = FloatField(default_value=0.0)
    id4r = id4R

    id4G = FloatField(default_value=0.0)
    id4g = id4G

    id4B = FloatField(default_value=0.0)
    id4b = id4B


class Id5PlugOperator(Float3CompoundBasePlugOperator["Id5AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id5R", "id5r"),
        ("id5G", "id5g"),
        ("id5B", "id5b"),
    )

    id5R = FloatField(default_value=0.0)
    id5r = id5R

    id5G = FloatField(default_value=0.0)
    id5g = id5G

    id5B = FloatField(default_value=0.0)
    id5b = id5B


class Id5AttrOperator(Float3CompoundBaseAttrOperator[Id5PlugOperator]):
    __slots__ = ()

    id5R = FloatField(default_value=0.0)
    id5r = id5R

    id5G = FloatField(default_value=0.0)
    id5g = id5G

    id5B = FloatField(default_value=0.0)
    id5b = id5B


class Id5Field(Float3CompoundBaseField[Id5AttrOperator, Id5PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id5AttrOperator
    PLUG_CLS = Id5PlugOperator

    id5R = FloatField(default_value=0.0)
    id5r = id5R

    id5G = FloatField(default_value=0.0)
    id5g = id5G

    id5B = FloatField(default_value=0.0)
    id5b = id5B


class Id6PlugOperator(Float3CompoundBasePlugOperator["Id6AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id6R", "id6r"),
        ("id6G", "id6g"),
        ("id6B", "id6b"),
    )

    id6R = FloatField(default_value=0.0)
    id6r = id6R

    id6G = FloatField(default_value=0.0)
    id6g = id6G

    id6B = FloatField(default_value=0.0)
    id6b = id6B


class Id6AttrOperator(Float3CompoundBaseAttrOperator[Id6PlugOperator]):
    __slots__ = ()

    id6R = FloatField(default_value=0.0)
    id6r = id6R

    id6G = FloatField(default_value=0.0)
    id6g = id6G

    id6B = FloatField(default_value=0.0)
    id6b = id6B


class Id6Field(Float3CompoundBaseField[Id6AttrOperator, Id6PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id6AttrOperator
    PLUG_CLS = Id6PlugOperator

    id6R = FloatField(default_value=0.0)
    id6r = id6R

    id6G = FloatField(default_value=0.0)
    id6g = id6G

    id6B = FloatField(default_value=0.0)
    id6b = id6B


class Id7PlugOperator(Float3CompoundBasePlugOperator["Id7AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id7R", "id7r"),
        ("id7G", "id7g"),
        ("id7B", "id7b"),
    )

    id7R = FloatField(default_value=0.0)
    id7r = id7R

    id7G = FloatField(default_value=0.0)
    id7g = id7G

    id7B = FloatField(default_value=0.0)
    id7b = id7B


class Id7AttrOperator(Float3CompoundBaseAttrOperator[Id7PlugOperator]):
    __slots__ = ()

    id7R = FloatField(default_value=0.0)
    id7r = id7R

    id7G = FloatField(default_value=0.0)
    id7g = id7G

    id7B = FloatField(default_value=0.0)
    id7b = id7B


class Id7Field(Float3CompoundBaseField[Id7AttrOperator, Id7PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id7AttrOperator
    PLUG_CLS = Id7PlugOperator

    id7R = FloatField(default_value=0.0)
    id7r = id7R

    id7G = FloatField(default_value=0.0)
    id7g = id7G

    id7B = FloatField(default_value=0.0)
    id7b = id7B


class Id8PlugOperator(Float3CompoundBasePlugOperator["Id8AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("id8R", "id8r"),
        ("id8G", "id8g"),
        ("id8B", "id8b"),
    )

    id8R = FloatField(default_value=0.0)
    id8r = id8R

    id8G = FloatField(default_value=0.0)
    id8g = id8G

    id8B = FloatField(default_value=0.0)
    id8b = id8B


class Id8AttrOperator(Float3CompoundBaseAttrOperator[Id8PlugOperator]):
    __slots__ = ()

    id8R = FloatField(default_value=0.0)
    id8r = id8R

    id8G = FloatField(default_value=0.0)
    id8g = id8G

    id8B = FloatField(default_value=0.0)
    id8b = id8B


class Id8Field(Float3CompoundBaseField[Id8AttrOperator, Id8PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Id8AttrOperator
    PLUG_CLS = Id8PlugOperator

    id8R = FloatField(default_value=0.0)
    id8r = id8R

    id8G = FloatField(default_value=0.0)
    id8g = id8G

    id8B = FloatField(default_value=0.0)
    id8b = id8B
