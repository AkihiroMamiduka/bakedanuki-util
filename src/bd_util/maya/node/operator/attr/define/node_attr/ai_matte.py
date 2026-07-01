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


class PassthroughPlugOperator(
    Float3CompoundBasePlugOperator["PassthroughAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("passthroughR", "passthroughr"),
        ("passthroughG", "passthroughg"),
        ("passthroughB", "passthroughb"),
    )

    passthroughR = FloatField()
    passthroughr = passthroughR

    passthroughG = FloatField()
    passthroughg = passthroughG

    passthroughB = FloatField()
    passthroughb = passthroughB


class PassthroughAttrOperator(
    Float3CompoundBaseAttrOperator[PassthroughPlugOperator]
):
    __slots__ = ()

    passthroughR = FloatField()
    passthroughr = passthroughR

    passthroughG = FloatField()
    passthroughg = passthroughG

    passthroughB = FloatField()
    passthroughb = passthroughB


class PassthroughField(
    Float3CompoundBaseField[PassthroughAttrOperator, PassthroughPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PassthroughAttrOperator
    PLUG_CLS = PassthroughPlugOperator

    passthroughR = FloatField()
    passthroughr = passthroughR

    passthroughG = FloatField()
    passthroughg = passthroughG

    passthroughB = FloatField()
    passthroughb = passthroughB


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "colorr"),
        ("colorG", "colorg"),
        ("colorB", "colorb"),
    )

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


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
