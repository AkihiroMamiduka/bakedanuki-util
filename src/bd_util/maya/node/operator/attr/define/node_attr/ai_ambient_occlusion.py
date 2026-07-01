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


class BlackPlugOperator(
    Float3CompoundBasePlugOperator["BlackAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blackR", "blackr"),
        ("blackG", "blackg"),
        ("blackB", "blackb"),
    )

    blackR = FloatField()
    blackr = blackR

    blackG = FloatField()
    blackg = blackG

    blackB = FloatField()
    blackb = blackB


class BlackAttrOperator(
    Float3CompoundBaseAttrOperator[BlackPlugOperator]
):
    __slots__ = ()

    blackR = FloatField()
    blackr = blackR

    blackG = FloatField()
    blackg = blackG

    blackB = FloatField()
    blackb = blackB


class BlackField(
    Float3CompoundBaseField[BlackAttrOperator, BlackPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlackAttrOperator
    PLUG_CLS = BlackPlugOperator

    blackR = FloatField()
    blackr = blackR

    blackG = FloatField()
    blackg = blackG

    blackB = FloatField()
    blackb = blackB


class WhitePlugOperator(
    Float3CompoundBasePlugOperator["WhiteAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("whiteR", "whiter"),
        ("whiteG", "whiteg"),
        ("whiteB", "whiteb"),
    )

    whiteR = FloatField()
    whiter = whiteR

    whiteG = FloatField()
    whiteg = whiteG

    whiteB = FloatField()
    whiteb = whiteB


class WhiteAttrOperator(
    Float3CompoundBaseAttrOperator[WhitePlugOperator]
):
    __slots__ = ()

    whiteR = FloatField()
    whiter = whiteR

    whiteG = FloatField()
    whiteg = whiteG

    whiteB = FloatField()
    whiteb = whiteB


class WhiteField(
    Float3CompoundBaseField[WhiteAttrOperator, WhitePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WhiteAttrOperator
    PLUG_CLS = WhitePlugOperator

    whiteR = FloatField()
    whiter = whiteR

    whiteG = FloatField()
    whiteg = whiteG

    whiteB = FloatField()
    whiteb = whiteB


class NormalPlugOperator(
    Float3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "normalx"),
        ("normalY", "normaly"),
        ("normalZ", "normalz"),
    )

    normalX = FloatField()
    normalx = normalX

    normalY = FloatField()
    normaly = normalY

    normalZ = FloatField()
    normalz = normalZ


class NormalAttrOperator(
    Float3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = FloatField()
    normalx = normalX

    normalY = FloatField()
    normaly = normalY

    normalZ = FloatField()
    normalz = normalZ


class NormalField(
    Float3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = FloatField()
    normalx = normalX

    normalY = FloatField()
    normaly = normalY

    normalZ = FloatField()
    normalz = normalZ
