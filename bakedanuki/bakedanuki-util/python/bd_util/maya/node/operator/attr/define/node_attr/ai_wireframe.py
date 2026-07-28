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


class FillColorPlugOperator(
    Float3CompoundBasePlugOperator["FillColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fillColorR", "fill_colorr"),
        ("fillColorG", "fill_colorg"),
        ("fillColorB", "fill_colorb"),
    )

    fillColorR = FloatField(default_value=1.0)
    fill_colorr = fillColorR

    fillColorG = FloatField(default_value=1.0)
    fill_colorg = fillColorG

    fillColorB = FloatField(default_value=1.0)
    fill_colorb = fillColorB


class FillColorAttrOperator(
    Float3CompoundBaseAttrOperator[FillColorPlugOperator]
):
    __slots__ = ()

    fillColorR = FloatField(default_value=1.0)
    fill_colorr = fillColorR

    fillColorG = FloatField(default_value=1.0)
    fill_colorg = fillColorG

    fillColorB = FloatField(default_value=1.0)
    fill_colorb = fillColorB


class FillColorField(
    Float3CompoundBaseField[FillColorAttrOperator, FillColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FillColorAttrOperator
    PLUG_CLS = FillColorPlugOperator

    fillColorR = FloatField(default_value=1.0)
    fill_colorr = fillColorR

    fillColorG = FloatField(default_value=1.0)
    fill_colorg = fillColorG

    fillColorB = FloatField(default_value=1.0)
    fill_colorb = fillColorB


class LineColorPlugOperator(
    Float3CompoundBasePlugOperator["LineColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lineColorR", "line_colorr"),
        ("lineColorG", "line_colorg"),
        ("lineColorB", "line_colorb"),
    )

    lineColorR = FloatField(default_value=0.0)
    line_colorr = lineColorR

    lineColorG = FloatField(default_value=0.0)
    line_colorg = lineColorG

    lineColorB = FloatField(default_value=0.0)
    line_colorb = lineColorB


class LineColorAttrOperator(
    Float3CompoundBaseAttrOperator[LineColorPlugOperator]
):
    __slots__ = ()

    lineColorR = FloatField(default_value=0.0)
    line_colorr = lineColorR

    lineColorG = FloatField(default_value=0.0)
    line_colorg = lineColorG

    lineColorB = FloatField(default_value=0.0)
    line_colorb = lineColorB


class LineColorField(
    Float3CompoundBaseField[LineColorAttrOperator, LineColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LineColorAttrOperator
    PLUG_CLS = LineColorPlugOperator

    lineColorR = FloatField(default_value=0.0)
    line_colorr = lineColorR

    lineColorG = FloatField(default_value=0.0)
    line_colorg = lineColorG

    lineColorB = FloatField(default_value=0.0)
    line_colorb = lineColorB
