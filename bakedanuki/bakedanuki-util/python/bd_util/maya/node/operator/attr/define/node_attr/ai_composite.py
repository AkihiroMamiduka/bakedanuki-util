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
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
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


class APlugOperator(
    Float3CompoundBasePlugOperator["AAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("AR", "Ar"),
        ("AG", "Ag"),
        ("AB", "Ab"),
    )

    AR = FloatField(default_value=1.0)
    Ar = AR

    AG = FloatField(default_value=0.0)
    Ag = AG

    AB = FloatField(default_value=0.0)
    Ab = AB


class AAttrOperator(
    Float3CompoundBaseAttrOperator[APlugOperator]
):
    __slots__ = ()

    AR = FloatField(default_value=1.0)
    Ar = AR

    AG = FloatField(default_value=0.0)
    Ag = AG

    AB = FloatField(default_value=0.0)
    Ab = AB


class AField(
    Float3CompoundBaseField[AAttrOperator, APlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AAttrOperator
    PLUG_CLS = APlugOperator

    AR = FloatField(default_value=1.0)
    Ar = AR

    AG = FloatField(default_value=0.0)
    Ag = AG

    AB = FloatField(default_value=0.0)
    Ab = AB


class BPlugOperator(
    Float3CompoundBasePlugOperator["BAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("BR", "Br"),
        ("BG", "Bg"),
        ("BB", "Bb"),
    )

    BR = FloatField(default_value=0.0)
    Br = BR

    BG = FloatField(default_value=1.0)
    Bg = BG

    BB = FloatField(default_value=0.0)
    Bb = BB


class BAttrOperator(
    Float3CompoundBaseAttrOperator[BPlugOperator]
):
    __slots__ = ()

    BR = FloatField(default_value=0.0)
    Br = BR

    BG = FloatField(default_value=1.0)
    Bg = BG

    BB = FloatField(default_value=0.0)
    Bb = BB


class BField(
    Float3CompoundBaseField[BAttrOperator, BPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BAttrOperator
    PLUG_CLS = BPlugOperator

    BR = FloatField(default_value=0.0)
    Br = BR

    BG = FloatField(default_value=1.0)
    Bg = BG

    BB = FloatField(default_value=0.0)
    Bb = BB
