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


class APlugOperator(
    Float3CompoundBasePlugOperator["AAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("AR", "Ar"),
        ("AG", "Ag"),
        ("AB", "Ab"),
    )

    AR = FloatField()
    Ar = AR

    AG = FloatField()
    Ag = AG

    AB = FloatField()
    Ab = AB


class AAttrOperator(
    Float3CompoundBaseAttrOperator[APlugOperator]
):
    __slots__ = ()

    AR = FloatField()
    Ar = AR

    AG = FloatField()
    Ag = AG

    AB = FloatField()
    Ab = AB


class AField(
    Float3CompoundBaseField[AAttrOperator, APlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AAttrOperator
    PLUG_CLS = APlugOperator

    AR = FloatField()
    Ar = AR

    AG = FloatField()
    Ag = AG

    AB = FloatField()
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

    BR = FloatField()
    Br = BR

    BG = FloatField()
    Bg = BG

    BB = FloatField()
    Bb = BB


class BAttrOperator(
    Float3CompoundBaseAttrOperator[BPlugOperator]
):
    __slots__ = ()

    BR = FloatField()
    Br = BR

    BG = FloatField()
    Bg = BG

    BB = FloatField()
    Bb = BB


class BField(
    Float3CompoundBaseField[BAttrOperator, BPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BAttrOperator
    PLUG_CLS = BPlugOperator

    BR = FloatField()
    Br = BR

    BG = FloatField()
    Bg = BG

    BB = FloatField()
    Bb = BB
