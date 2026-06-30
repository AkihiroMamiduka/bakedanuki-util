# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
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


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
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


class HardwareColorPlugOperator(
    Float3CompoundBasePlugOperator["HardwareColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareColorR", "hwcr"),
        ("hardwareColorG", "hwcg"),
        ("hardwareColorB", "hwcb"),
    )

    hardwareColorR = FloatField()
    hwcr = hardwareColorR

    hardwareColorG = FloatField()
    hwcg = hardwareColorG

    hardwareColorB = FloatField()
    hwcb = hardwareColorB


class HardwareColorAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareColorPlugOperator]
):
    __slots__ = ()

    hardwareColorR = FloatField()
    hwcr = hardwareColorR

    hardwareColorG = FloatField()
    hwcg = hardwareColorG

    hardwareColorB = FloatField()
    hwcb = hardwareColorB


class HardwareColorField(
    Float3CompoundBaseField[HardwareColorAttrOperator, HardwareColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HardwareColorAttrOperator
    PLUG_CLS = HardwareColorPlugOperator

    hardwareColorR = FloatField()
    hwcr = hardwareColorR

    hardwareColorG = FloatField()
    hwcg = hardwareColorG

    hardwareColorB = FloatField()
    hwcb = hardwareColorB


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


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "specular_colorr"),
        ("specularColorG", "specular_colorg"),
        ("specularColorB", "specular_colorb"),
    )

    specularColorR = FloatField()
    specular_colorr = specularColorR

    specularColorG = FloatField()
    specular_colorg = specularColorG

    specularColorB = FloatField()
    specular_colorb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField()
    specular_colorr = specularColorR

    specularColorG = FloatField()
    specular_colorg = specularColorG

    specularColorB = FloatField()
    specular_colorb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField()
    specular_colorr = specularColorR

    specularColorG = FloatField()
    specular_colorg = specularColorG

    specularColorB = FloatField()
    specular_colorb = specularColorB


class SpecularFlipFlopPlugOperator(
    Float3CompoundBasePlugOperator["SpecularFlipFlopAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularFlipFlopR", "specular_flip_flopr"),
        ("specularFlipFlopG", "specular_flip_flopg"),
        ("specularFlipFlopB", "specular_flip_flopb"),
    )

    specularFlipFlopR = FloatField()
    specular_flip_flopr = specularFlipFlopR

    specularFlipFlopG = FloatField()
    specular_flip_flopg = specularFlipFlopG

    specularFlipFlopB = FloatField()
    specular_flip_flopb = specularFlipFlopB


class SpecularFlipFlopAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularFlipFlopPlugOperator]
):
    __slots__ = ()

    specularFlipFlopR = FloatField()
    specular_flip_flopr = specularFlipFlopR

    specularFlipFlopG = FloatField()
    specular_flip_flopg = specularFlipFlopG

    specularFlipFlopB = FloatField()
    specular_flip_flopb = specularFlipFlopB


class SpecularFlipFlopField(
    Float3CompoundBaseField[SpecularFlipFlopAttrOperator, SpecularFlipFlopPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularFlipFlopAttrOperator
    PLUG_CLS = SpecularFlipFlopPlugOperator

    specularFlipFlopR = FloatField()
    specular_flip_flopr = specularFlipFlopR

    specularFlipFlopG = FloatField()
    specular_flip_flopg = specularFlipFlopG

    specularFlipFlopB = FloatField()
    specular_flip_flopb = specularFlipFlopB


class SpecularLightFacingPlugOperator(
    Float3CompoundBasePlugOperator["SpecularLightFacingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularLightFacingR", "specular_light_facingr"),
        ("specularLightFacingG", "specular_light_facingg"),
        ("specularLightFacingB", "specular_light_facingb"),
    )

    specularLightFacingR = FloatField()
    specular_light_facingr = specularLightFacingR

    specularLightFacingG = FloatField()
    specular_light_facingg = specularLightFacingG

    specularLightFacingB = FloatField()
    specular_light_facingb = specularLightFacingB


class SpecularLightFacingAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularLightFacingPlugOperator]
):
    __slots__ = ()

    specularLightFacingR = FloatField()
    specular_light_facingr = specularLightFacingR

    specularLightFacingG = FloatField()
    specular_light_facingg = specularLightFacingG

    specularLightFacingB = FloatField()
    specular_light_facingb = specularLightFacingB


class SpecularLightFacingField(
    Float3CompoundBaseField[SpecularLightFacingAttrOperator, SpecularLightFacingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularLightFacingAttrOperator
    PLUG_CLS = SpecularLightFacingPlugOperator

    specularLightFacingR = FloatField()
    specular_light_facingr = specularLightFacingR

    specularLightFacingG = FloatField()
    specular_light_facingg = specularLightFacingG

    specularLightFacingB = FloatField()
    specular_light_facingb = specularLightFacingB


class TransmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionColorR", "transmission_colorr"),
        ("transmissionColorG", "transmission_colorg"),
        ("transmissionColorB", "transmission_colorb"),
    )

    transmissionColorR = FloatField()
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField()
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField()
    transmission_colorb = transmissionColorB


class TransmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionColorPlugOperator]
):
    __slots__ = ()

    transmissionColorR = FloatField()
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField()
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField()
    transmission_colorb = transmissionColorB


class TransmissionColorField(
    Float3CompoundBaseField[TransmissionColorAttrOperator, TransmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmissionColorAttrOperator
    PLUG_CLS = TransmissionColorPlugOperator

    transmissionColorR = FloatField()
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField()
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField()
    transmission_colorb = transmissionColorB


class FlakeColorPlugOperator(
    Float3CompoundBasePlugOperator["FlakeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("flakeColorR", "flake_colorr"),
        ("flakeColorG", "flake_colorg"),
        ("flakeColorB", "flake_colorb"),
    )

    flakeColorR = FloatField()
    flake_colorr = flakeColorR

    flakeColorG = FloatField()
    flake_colorg = flakeColorG

    flakeColorB = FloatField()
    flake_colorb = flakeColorB


class FlakeColorAttrOperator(
    Float3CompoundBaseAttrOperator[FlakeColorPlugOperator]
):
    __slots__ = ()

    flakeColorR = FloatField()
    flake_colorr = flakeColorR

    flakeColorG = FloatField()
    flake_colorg = flakeColorG

    flakeColorB = FloatField()
    flake_colorb = flakeColorB


class FlakeColorField(
    Float3CompoundBaseField[FlakeColorAttrOperator, FlakeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlakeColorAttrOperator
    PLUG_CLS = FlakeColorPlugOperator

    flakeColorR = FloatField()
    flake_colorr = flakeColorR

    flakeColorG = FloatField()
    flake_colorg = flakeColorG

    flakeColorB = FloatField()
    flake_colorb = flakeColorB


class FlakeFlipFlopPlugOperator(
    Float3CompoundBasePlugOperator["FlakeFlipFlopAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("flakeFlipFlopR", "flake_flip_flopr"),
        ("flakeFlipFlopG", "flake_flip_flopg"),
        ("flakeFlipFlopB", "flake_flip_flopb"),
    )

    flakeFlipFlopR = FloatField()
    flake_flip_flopr = flakeFlipFlopR

    flakeFlipFlopG = FloatField()
    flake_flip_flopg = flakeFlipFlopG

    flakeFlipFlopB = FloatField()
    flake_flip_flopb = flakeFlipFlopB


class FlakeFlipFlopAttrOperator(
    Float3CompoundBaseAttrOperator[FlakeFlipFlopPlugOperator]
):
    __slots__ = ()

    flakeFlipFlopR = FloatField()
    flake_flip_flopr = flakeFlipFlopR

    flakeFlipFlopG = FloatField()
    flake_flip_flopg = flakeFlipFlopG

    flakeFlipFlopB = FloatField()
    flake_flip_flopb = flakeFlipFlopB


class FlakeFlipFlopField(
    Float3CompoundBaseField[FlakeFlipFlopAttrOperator, FlakeFlipFlopPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlakeFlipFlopAttrOperator
    PLUG_CLS = FlakeFlipFlopPlugOperator

    flakeFlipFlopR = FloatField()
    flake_flip_flopr = flakeFlipFlopR

    flakeFlipFlopG = FloatField()
    flake_flip_flopg = flakeFlipFlopG

    flakeFlipFlopB = FloatField()
    flake_flip_flopb = flakeFlipFlopB


class FlakeLightFacingPlugOperator(
    Float3CompoundBasePlugOperator["FlakeLightFacingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("flakeLightFacingR", "flake_light_facingr"),
        ("flakeLightFacingG", "flake_light_facingg"),
        ("flakeLightFacingB", "flake_light_facingb"),
    )

    flakeLightFacingR = FloatField()
    flake_light_facingr = flakeLightFacingR

    flakeLightFacingG = FloatField()
    flake_light_facingg = flakeLightFacingG

    flakeLightFacingB = FloatField()
    flake_light_facingb = flakeLightFacingB


class FlakeLightFacingAttrOperator(
    Float3CompoundBaseAttrOperator[FlakeLightFacingPlugOperator]
):
    __slots__ = ()

    flakeLightFacingR = FloatField()
    flake_light_facingr = flakeLightFacingR

    flakeLightFacingG = FloatField()
    flake_light_facingg = flakeLightFacingG

    flakeLightFacingB = FloatField()
    flake_light_facingb = flakeLightFacingB


class FlakeLightFacingField(
    Float3CompoundBaseField[FlakeLightFacingAttrOperator, FlakeLightFacingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlakeLightFacingAttrOperator
    PLUG_CLS = FlakeLightFacingPlugOperator

    flakeLightFacingR = FloatField()
    flake_light_facingr = flakeLightFacingR

    flakeLightFacingG = FloatField()
    flake_light_facingg = flakeLightFacingG

    flakeLightFacingB = FloatField()
    flake_light_facingb = flakeLightFacingB


class CoatColorPlugOperator(
    Float3CompoundBasePlugOperator["CoatColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coatColorR", "coat_colorr"),
        ("coatColorG", "coat_colorg"),
        ("coatColorB", "coat_colorb"),
    )

    coatColorR = FloatField()
    coat_colorr = coatColorR

    coatColorG = FloatField()
    coat_colorg = coatColorG

    coatColorB = FloatField()
    coat_colorb = coatColorB


class CoatColorAttrOperator(
    Float3CompoundBaseAttrOperator[CoatColorPlugOperator]
):
    __slots__ = ()

    coatColorR = FloatField()
    coat_colorr = coatColorR

    coatColorG = FloatField()
    coat_colorg = coatColorG

    coatColorB = FloatField()
    coat_colorb = coatColorB


class CoatColorField(
    Float3CompoundBaseField[CoatColorAttrOperator, CoatColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoatColorAttrOperator
    PLUG_CLS = CoatColorPlugOperator

    coatColorR = FloatField()
    coat_colorr = coatColorR

    coatColorG = FloatField()
    coat_colorg = coatColorG

    coatColorB = FloatField()
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

    coatNormalX = FloatField()
    coat_normalx = coatNormalX

    coatNormalY = FloatField()
    coat_normaly = coatNormalY

    coatNormalZ = FloatField()
    coat_normalz = coatNormalZ


class CoatNormalAttrOperator(
    Float3CompoundBaseAttrOperator[CoatNormalPlugOperator]
):
    __slots__ = ()

    coatNormalX = FloatField()
    coat_normalx = coatNormalX

    coatNormalY = FloatField()
    coat_normaly = coatNormalY

    coatNormalZ = FloatField()
    coat_normalz = coatNormalZ


class CoatNormalField(
    Float3CompoundBaseField[CoatNormalAttrOperator, CoatNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoatNormalAttrOperator
    PLUG_CLS = CoatNormalPlugOperator

    coatNormalX = FloatField()
    coat_normalx = coatNormalX

    coatNormalY = FloatField()
    coat_normaly = coatNormalY

    coatNormalZ = FloatField()
    coat_normalz = coatNormalZ
