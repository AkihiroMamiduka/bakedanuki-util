# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
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
    Float3CompoundBaseField[HardwareColorAttrOperator, HardwareColorPlugOperator]
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


class Shader1PlugOperator(
    Float3CompoundBasePlugOperator["Shader1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shader1R", "shader1r"),
        ("shader1G", "shader1g"),
        ("shader1B", "shader1b"),
    )

    shader1R = FloatField(default_value=0.0)
    shader1r = shader1R

    shader1G = FloatField(default_value=0.0)
    shader1g = shader1G

    shader1B = FloatField(default_value=0.0)
    shader1b = shader1B


class Shader1AttrOperator(
    Float3CompoundBaseAttrOperator[Shader1PlugOperator]
):
    __slots__ = ()

    shader1R = FloatField(default_value=0.0)
    shader1r = shader1R

    shader1G = FloatField(default_value=0.0)
    shader1g = shader1G

    shader1B = FloatField(default_value=0.0)
    shader1b = shader1B


class Shader1Field(
    Float3CompoundBaseField[Shader1AttrOperator, Shader1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Shader1AttrOperator
    PLUG_CLS = Shader1PlugOperator

    shader1R = FloatField(default_value=0.0)
    shader1r = shader1R

    shader1G = FloatField(default_value=0.0)
    shader1g = shader1G

    shader1B = FloatField(default_value=0.0)
    shader1b = shader1B


class Shader2PlugOperator(
    Float3CompoundBasePlugOperator["Shader2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shader2R", "shader2r"),
        ("shader2G", "shader2g"),
        ("shader2B", "shader2b"),
    )

    shader2R = FloatField(default_value=0.0)
    shader2r = shader2R

    shader2G = FloatField(default_value=0.0)
    shader2g = shader2G

    shader2B = FloatField(default_value=0.0)
    shader2b = shader2B


class Shader2AttrOperator(
    Float3CompoundBaseAttrOperator[Shader2PlugOperator]
):
    __slots__ = ()

    shader2R = FloatField(default_value=0.0)
    shader2r = shader2R

    shader2G = FloatField(default_value=0.0)
    shader2g = shader2G

    shader2B = FloatField(default_value=0.0)
    shader2b = shader2B


class Shader2Field(
    Float3CompoundBaseField[Shader2AttrOperator, Shader2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Shader2AttrOperator
    PLUG_CLS = Shader2PlugOperator

    shader2R = FloatField(default_value=0.0)
    shader2r = shader2R

    shader2G = FloatField(default_value=0.0)
    shader2g = shader2G

    shader2B = FloatField(default_value=0.0)
    shader2b = shader2B
