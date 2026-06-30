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


class ShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["ShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowColorR", "shadow_colorr"),
        ("shadowColorG", "shadow_colorg"),
        ("shadowColorB", "shadow_colorb"),
    )

    shadowColorR = FloatField()
    shadow_colorr = shadowColorR

    shadowColorG = FloatField()
    shadow_colorg = shadowColorG

    shadowColorB = FloatField()
    shadow_colorb = shadowColorB


class ShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowColorPlugOperator]
):
    __slots__ = ()

    shadowColorR = FloatField()
    shadow_colorr = shadowColorR

    shadowColorG = FloatField()
    shadow_colorg = shadowColorG

    shadowColorB = FloatField()
    shadow_colorb = shadowColorB


class ShadowColorField(
    Float3CompoundBaseField[ShadowColorAttrOperator, ShadowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowColorAttrOperator
    PLUG_CLS = ShadowColorPlugOperator

    shadowColorR = FloatField()
    shadow_colorr = shadowColorR

    shadowColorG = FloatField()
    shadow_colorg = shadowColorG

    shadowColorB = FloatField()
    shadow_colorb = shadowColorB


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "background_colorr"),
        ("backgroundColorG", "background_colorg"),
        ("backgroundColorB", "background_colorb"),
    )

    backgroundColorR = FloatField()
    background_colorr = backgroundColorR

    backgroundColorG = FloatField()
    background_colorg = backgroundColorG

    backgroundColorB = FloatField()
    background_colorb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField()
    background_colorr = backgroundColorR

    backgroundColorG = FloatField()
    background_colorg = backgroundColorG

    backgroundColorB = FloatField()
    background_colorb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[BackgroundColorAttrOperator, BackgroundColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField()
    background_colorr = backgroundColorR

    backgroundColorG = FloatField()
    background_colorg = backgroundColorG

    backgroundColorB = FloatField()
    background_colorb = backgroundColorB


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
