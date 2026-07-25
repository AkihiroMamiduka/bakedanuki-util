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


class BlackPlugOperator(
    Float3CompoundBasePlugOperator["BlackAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blackR", "blackr"),
        ("blackG", "blackg"),
        ("blackB", "blackb"),
    )

    blackR = FloatField(default_value=0.0)
    blackr = blackR

    blackG = FloatField(default_value=0.0)
    blackg = blackG

    blackB = FloatField(default_value=0.0)
    blackb = blackB


class BlackAttrOperator(
    Float3CompoundBaseAttrOperator[BlackPlugOperator]
):
    __slots__ = ()

    blackR = FloatField(default_value=0.0)
    blackr = blackR

    blackG = FloatField(default_value=0.0)
    blackg = blackG

    blackB = FloatField(default_value=0.0)
    blackb = blackB


class BlackField(
    Float3CompoundBaseField[BlackAttrOperator, BlackPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlackAttrOperator
    PLUG_CLS = BlackPlugOperator

    blackR = FloatField(default_value=0.0)
    blackr = blackR

    blackG = FloatField(default_value=0.0)
    blackg = blackG

    blackB = FloatField(default_value=0.0)
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

    whiteR = FloatField(default_value=1.0)
    whiter = whiteR

    whiteG = FloatField(default_value=1.0)
    whiteg = whiteG

    whiteB = FloatField(default_value=1.0)
    whiteb = whiteB


class WhiteAttrOperator(
    Float3CompoundBaseAttrOperator[WhitePlugOperator]
):
    __slots__ = ()

    whiteR = FloatField(default_value=1.0)
    whiter = whiteR

    whiteG = FloatField(default_value=1.0)
    whiteg = whiteG

    whiteB = FloatField(default_value=1.0)
    whiteb = whiteB


class WhiteField(
    Float3CompoundBaseField[WhiteAttrOperator, WhitePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WhiteAttrOperator
    PLUG_CLS = WhitePlugOperator

    whiteR = FloatField(default_value=1.0)
    whiter = whiteR

    whiteG = FloatField(default_value=1.0)
    whiteg = whiteG

    whiteB = FloatField(default_value=1.0)
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

    normalX = FloatField(default_value=0.0)
    normalx = normalX

    normalY = FloatField(default_value=0.0)
    normaly = normalY

    normalZ = FloatField(default_value=0.0)
    normalz = normalZ


class NormalAttrOperator(
    Float3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = FloatField(default_value=0.0)
    normalx = normalX

    normalY = FloatField(default_value=0.0)
    normaly = normalY

    normalZ = FloatField(default_value=0.0)
    normalz = normalZ


class NormalField(
    Float3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = FloatField(default_value=0.0)
    normalx = normalX

    normalY = FloatField(default_value=0.0)
    normaly = normalY

    normalZ = FloatField(default_value=0.0)
    normalz = normalZ
