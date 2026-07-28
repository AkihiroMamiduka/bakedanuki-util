# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    inColorR = FloatField(default_value=0.30000001192092896)
    cr = inColorR

    inColorG = FloatField(default_value=0.30000001192092896)
    cg = inColorG

    inColorB = FloatField(default_value=0.30000001192092896)
    cb = inColorB


class InColorAttrOperator(Float3CompoundBaseAttrOperator[InColorPlugOperator]):
    __slots__ = ()

    inColorR = FloatField(default_value=0.30000001192092896)
    cr = inColorR

    inColorG = FloatField(default_value=0.30000001192092896)
    cg = inColorG

    inColorB = FloatField(default_value=0.30000001192092896)
    cb = inColorB


class InColorField(
    Float3CompoundBaseField[InColorAttrOperator, InColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InColorAttrOperator
    PLUG_CLS = InColorPlugOperator

    inColorR = FloatField(default_value=0.30000001192092896)
    cr = inColorR

    inColorG = FloatField(default_value=0.30000001192092896)
    cg = inColorG

    inColorB = FloatField(default_value=0.30000001192092896)
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

    colGainR = FloatField(default_value=1.0)
    ccgr = colGainR

    colGainG = FloatField(default_value=1.0)
    ccgg = colGainG

    colGainB = FloatField(default_value=1.0)
    ccgb = colGainB


class ColGainAttrOperator(Float3CompoundBaseAttrOperator[ColGainPlugOperator]):
    __slots__ = ()

    colGainR = FloatField(default_value=1.0)
    ccgr = colGainR

    colGainG = FloatField(default_value=1.0)
    ccgg = colGainG

    colGainB = FloatField(default_value=1.0)
    ccgb = colGainB


class ColGainField(
    Float3CompoundBaseField[ColGainAttrOperator, ColGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColGainAttrOperator
    PLUG_CLS = ColGainPlugOperator

    colGainR = FloatField(default_value=1.0)
    ccgr = colGainR

    colGainG = FloatField(default_value=1.0)
    ccgg = colGainG

    colGainB = FloatField(default_value=1.0)
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

    colOffsetR = FloatField(default_value=0.0)
    cor = colOffsetR

    colOffsetG = FloatField(default_value=0.0)
    cog = colOffsetG

    colOffsetB = FloatField(default_value=0.0)
    cob = colOffsetB


class ColOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColOffsetPlugOperator]
):
    __slots__ = ()

    colOffsetR = FloatField(default_value=0.0)
    cor = colOffsetR

    colOffsetG = FloatField(default_value=0.0)
    cog = colOffsetG

    colOffsetB = FloatField(default_value=0.0)
    cob = colOffsetB


class ColOffsetField(
    Float3CompoundBaseField[ColOffsetAttrOperator, ColOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColOffsetAttrOperator
    PLUG_CLS = ColOffsetPlugOperator

    colOffsetR = FloatField(default_value=0.0)
    cor = colOffsetR

    colOffsetG = FloatField(default_value=0.0)
    cog = colOffsetG

    colOffsetB = FloatField(default_value=0.0)
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

    colGammaX = FloatField(default_value=1.0)
    cgax = colGammaX

    colGammaY = FloatField(default_value=1.0)
    cgay = colGammaY

    colGammaZ = FloatField(default_value=1.0)
    cgaz = colGammaZ


class ColGammaAttrOperator(
    Float3CompoundBaseAttrOperator[ColGammaPlugOperator]
):
    __slots__ = ()

    colGammaX = FloatField(default_value=1.0)
    cgax = colGammaX

    colGammaY = FloatField(default_value=1.0)
    cgay = colGammaY

    colGammaZ = FloatField(default_value=1.0)
    cgaz = colGammaZ


class ColGammaField(
    Float3CompoundBaseField[ColGammaAttrOperator, ColGammaPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColGammaAttrOperator
    PLUG_CLS = ColGammaPlugOperator

    colGammaX = FloatField(default_value=1.0)
    cgax = colGammaX

    colGammaY = FloatField(default_value=1.0)
    cgay = colGammaY

    colGammaZ = FloatField(default_value=1.0)
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

    colClampMinR = FloatField(default_value=0.0)
    ccmnr = colClampMinR

    colClampMinG = FloatField(default_value=0.0)
    ccmng = colClampMinG

    colClampMinB = FloatField(default_value=0.0)
    ccmnb = colClampMinB


class ColClampMinAttrOperator(
    Float3CompoundBaseAttrOperator[ColClampMinPlugOperator]
):
    __slots__ = ()

    colClampMinR = FloatField(default_value=0.0)
    ccmnr = colClampMinR

    colClampMinG = FloatField(default_value=0.0)
    ccmng = colClampMinG

    colClampMinB = FloatField(default_value=0.0)
    ccmnb = colClampMinB


class ColClampMinField(
    Float3CompoundBaseField[ColClampMinAttrOperator, ColClampMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColClampMinAttrOperator
    PLUG_CLS = ColClampMinPlugOperator

    colClampMinR = FloatField(default_value=0.0)
    ccmnr = colClampMinR

    colClampMinG = FloatField(default_value=0.0)
    ccmng = colClampMinG

    colClampMinB = FloatField(default_value=0.0)
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

    colClampMaxR = FloatField(default_value=1.0)
    ccmxr = colClampMaxR

    colClampMaxG = FloatField(default_value=1.0)
    ccmxg = colClampMaxG

    colClampMaxB = FloatField(default_value=1.0)
    ccmxb = colClampMaxB


class ColClampMaxAttrOperator(
    Float3CompoundBaseAttrOperator[ColClampMaxPlugOperator]
):
    __slots__ = ()

    colClampMaxR = FloatField(default_value=1.0)
    ccmxr = colClampMaxR

    colClampMaxG = FloatField(default_value=1.0)
    ccmxg = colClampMaxG

    colClampMaxB = FloatField(default_value=1.0)
    ccmxb = colClampMaxB


class ColClampMaxField(
    Float3CompoundBaseField[ColClampMaxAttrOperator, ColClampMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColClampMaxAttrOperator
    PLUG_CLS = ColClampMaxPlugOperator

    colClampMaxR = FloatField(default_value=1.0)
    ccmxr = colClampMaxR

    colClampMaxG = FloatField(default_value=1.0)
    ccmxg = colClampMaxG

    colClampMaxB = FloatField(default_value=1.0)
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

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB
