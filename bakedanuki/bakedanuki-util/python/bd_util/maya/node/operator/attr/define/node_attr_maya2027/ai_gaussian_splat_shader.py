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

    outColorR = FloatField(default_value=0.5, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.5, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.5, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.5, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.5, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.5, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.5, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.5, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.5, writable=False)
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

    outTransparencyR = FloatField(default_value=0.5, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.5, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.5, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.5, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.5, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.5, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.5, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.5, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.5, writable=False)
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

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
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

    hardwareColorR = FloatField(default_value=0.5)
    hwcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hwcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hwcb = hardwareColorB


class HardwareColorAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareColorPlugOperator]
):
    __slots__ = ()

    hardwareColorR = FloatField(default_value=0.5)
    hwcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hwcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hwcb = hardwareColorB


class HardwareColorField(
    Float3CompoundBaseField[
        HardwareColorAttrOperator, HardwareColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HardwareColorAttrOperator
    PLUG_CLS = HardwareColorPlugOperator

    hardwareColorR = FloatField(default_value=0.5)
    hwcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hwcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hwcb = hardwareColorB


class EmissionTintPlugOperator(
    Float3CompoundBasePlugOperator["EmissionTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionTintR", "emission_tintr"),
        ("emissionTintG", "emission_tintg"),
        ("emissionTintB", "emission_tintb"),
    )

    emissionTintR = FloatField(default_value=1.0)
    emission_tintr = emissionTintR

    emissionTintG = FloatField(default_value=1.0)
    emission_tintg = emissionTintG

    emissionTintB = FloatField(default_value=1.0)
    emission_tintb = emissionTintB


class EmissionTintAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionTintPlugOperator]
):
    __slots__ = ()

    emissionTintR = FloatField(default_value=1.0)
    emission_tintr = emissionTintR

    emissionTintG = FloatField(default_value=1.0)
    emission_tintg = emissionTintG

    emissionTintB = FloatField(default_value=1.0)
    emission_tintb = emissionTintB


class EmissionTintField(
    Float3CompoundBaseField[EmissionTintAttrOperator, EmissionTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionTintAttrOperator
    PLUG_CLS = EmissionTintPlugOperator

    emissionTintR = FloatField(default_value=1.0)
    emission_tintr = emissionTintR

    emissionTintG = FloatField(default_value=1.0)
    emission_tintg = emissionTintG

    emissionTintB = FloatField(default_value=1.0)
    emission_tintb = emissionTintB


class DiffuseTintPlugOperator(
    Float3CompoundBasePlugOperator["DiffuseTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("diffuseTintR", "diffuse_tintr"),
        ("diffuseTintG", "diffuse_tintg"),
        ("diffuseTintB", "diffuse_tintb"),
    )

    diffuseTintR = FloatField(default_value=1.0)
    diffuse_tintr = diffuseTintR

    diffuseTintG = FloatField(default_value=1.0)
    diffuse_tintg = diffuseTintG

    diffuseTintB = FloatField(default_value=1.0)
    diffuse_tintb = diffuseTintB


class DiffuseTintAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseTintPlugOperator]
):
    __slots__ = ()

    diffuseTintR = FloatField(default_value=1.0)
    diffuse_tintr = diffuseTintR

    diffuseTintG = FloatField(default_value=1.0)
    diffuse_tintg = diffuseTintG

    diffuseTintB = FloatField(default_value=1.0)
    diffuse_tintb = diffuseTintB


class DiffuseTintField(
    Float3CompoundBaseField[DiffuseTintAttrOperator, DiffuseTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DiffuseTintAttrOperator
    PLUG_CLS = DiffuseTintPlugOperator

    diffuseTintR = FloatField(default_value=1.0)
    diffuse_tintr = diffuseTintR

    diffuseTintG = FloatField(default_value=1.0)
    diffuse_tintg = diffuseTintG

    diffuseTintB = FloatField(default_value=1.0)
    diffuse_tintb = diffuseTintB
