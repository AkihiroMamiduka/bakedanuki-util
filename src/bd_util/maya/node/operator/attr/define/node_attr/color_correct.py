# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InColorPlugOperator(
    Float3CompoundBasePlugOperator["InColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inColorR", "_cr"),
        ("inColorG", "_cg"),
        ("inColorB", "_cb"),
    )

    inColorR = FloatField()
    cr = inColorR

    inColorG = FloatField()
    cg = inColorG

    inColorB = FloatField()
    cb = inColorB


class InColorAttrOperator(
    Float3CompoundBaseAttrOperator[InColorPlugOperator]
):
    __slots__ = ()

    inColorR = FloatField()
    cr = inColorR

    inColorG = FloatField()
    cg = inColorG

    inColorB = FloatField()
    cb = inColorB


class InColorField(
    Float3CompoundBaseField[InColorAttrOperator, InColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InColorAttrOperator
    PLUG_CLS = InColorPlugOperator

    inColorR = FloatField()
    cr = inColorR

    inColorG = FloatField()
    cg = inColorG

    inColorB = FloatField()
    cb = inColorB


class ColGainPlugOperator(
    Float3CompoundBasePlugOperator["ColGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colGainR", "_ccgr"),
        ("colGainG", "_ccgg"),
        ("colGainB", "_ccgb"),
    )

    colGainR = FloatField()
    ccgr = colGainR

    colGainG = FloatField()
    ccgg = colGainG

    colGainB = FloatField()
    ccgb = colGainB


class ColGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColGainPlugOperator]
):
    __slots__ = ()

    colGainR = FloatField()
    ccgr = colGainR

    colGainG = FloatField()
    ccgg = colGainG

    colGainB = FloatField()
    ccgb = colGainB


class ColGainField(
    Float3CompoundBaseField[ColGainAttrOperator, ColGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColGainAttrOperator
    PLUG_CLS = ColGainPlugOperator

    colGainR = FloatField()
    ccgr = colGainR

    colGainG = FloatField()
    ccgg = colGainG

    colGainB = FloatField()
    ccgb = colGainB


class ColOffsetPlugOperator(
    Float3CompoundBasePlugOperator["ColOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colOffsetR", "_cor"),
        ("colOffsetG", "_cog"),
        ("colOffsetB", "_cob"),
    )

    colOffsetR = FloatField()
    cor = colOffsetR

    colOffsetG = FloatField()
    cog = colOffsetG

    colOffsetB = FloatField()
    cob = colOffsetB


class ColOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColOffsetPlugOperator]
):
    __slots__ = ()

    colOffsetR = FloatField()
    cor = colOffsetR

    colOffsetG = FloatField()
    cog = colOffsetG

    colOffsetB = FloatField()
    cob = colOffsetB


class ColOffsetField(
    Float3CompoundBaseField[ColOffsetAttrOperator, ColOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColOffsetAttrOperator
    PLUG_CLS = ColOffsetPlugOperator

    colOffsetR = FloatField()
    cor = colOffsetR

    colOffsetG = FloatField()
    cog = colOffsetG

    colOffsetB = FloatField()
    cob = colOffsetB


class ColGammaPlugOperator(
    Float3CompoundBasePlugOperator["ColGammaAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colGammaX", "_cgax"),
        ("colGammaY", "_cgay"),
        ("colGammaZ", "_cgaz"),
    )

    colGammaX = FloatField()
    cgax = colGammaX

    colGammaY = FloatField()
    cgay = colGammaY

    colGammaZ = FloatField()
    cgaz = colGammaZ


class ColGammaAttrOperator(
    Float3CompoundBaseAttrOperator[ColGammaPlugOperator]
):
    __slots__ = ()

    colGammaX = FloatField()
    cgax = colGammaX

    colGammaY = FloatField()
    cgay = colGammaY

    colGammaZ = FloatField()
    cgaz = colGammaZ


class ColGammaField(
    Float3CompoundBaseField[ColGammaAttrOperator, ColGammaPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColGammaAttrOperator
    PLUG_CLS = ColGammaPlugOperator

    colGammaX = FloatField()
    cgax = colGammaX

    colGammaY = FloatField()
    cgay = colGammaY

    colGammaZ = FloatField()
    cgaz = colGammaZ


class ColClampMinPlugOperator(
    Float3CompoundBasePlugOperator["ColClampMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colClampMinR", "_ccmnr"),
        ("colClampMinG", "_ccmng"),
        ("colClampMinB", "_ccmnb"),
    )

    colClampMinR = FloatField()
    ccmnr = colClampMinR

    colClampMinG = FloatField()
    ccmng = colClampMinG

    colClampMinB = FloatField()
    ccmnb = colClampMinB


class ColClampMinAttrOperator(
    Float3CompoundBaseAttrOperator[ColClampMinPlugOperator]
):
    __slots__ = ()

    colClampMinR = FloatField()
    ccmnr = colClampMinR

    colClampMinG = FloatField()
    ccmng = colClampMinG

    colClampMinB = FloatField()
    ccmnb = colClampMinB


class ColClampMinField(
    Float3CompoundBaseField[ColClampMinAttrOperator, ColClampMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColClampMinAttrOperator
    PLUG_CLS = ColClampMinPlugOperator

    colClampMinR = FloatField()
    ccmnr = colClampMinR

    colClampMinG = FloatField()
    ccmng = colClampMinG

    colClampMinB = FloatField()
    ccmnb = colClampMinB


class ColClampMaxPlugOperator(
    Float3CompoundBasePlugOperator["ColClampMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colClampMaxR", "_ccmxr"),
        ("colClampMaxG", "_ccmxg"),
        ("colClampMaxB", "_ccmxb"),
    )

    colClampMaxR = FloatField()
    ccmxr = colClampMaxR

    colClampMaxG = FloatField()
    ccmxg = colClampMaxG

    colClampMaxB = FloatField()
    ccmxb = colClampMaxB


class ColClampMaxAttrOperator(
    Float3CompoundBaseAttrOperator[ColClampMaxPlugOperator]
):
    __slots__ = ()

    colClampMaxR = FloatField()
    ccmxr = colClampMaxR

    colClampMaxG = FloatField()
    ccmxg = colClampMaxG

    colClampMaxB = FloatField()
    ccmxb = colClampMaxB


class ColClampMaxField(
    Float3CompoundBaseField[ColClampMaxAttrOperator, ColClampMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColClampMaxAttrOperator
    PLUG_CLS = ColClampMaxPlugOperator

    colClampMaxR = FloatField()
    ccmxr = colClampMaxR

    colClampMaxG = FloatField()
    ccmxg = colClampMaxG

    colClampMaxB = FloatField()
    ccmxb = colClampMaxB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB
