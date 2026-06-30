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


class Input1PlugOperator(
    Float3CompoundBasePlugOperator["Input1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1R", "input1r"),
        ("input1G", "input1g"),
        ("input1B", "input1b"),
    )

    input1R = FloatField()
    input1r = input1R

    input1G = FloatField()
    input1g = input1G

    input1B = FloatField()
    input1b = input1B


class Input1AttrOperator(
    Float3CompoundBaseAttrOperator[Input1PlugOperator]
):
    __slots__ = ()

    input1R = FloatField()
    input1r = input1R

    input1G = FloatField()
    input1g = input1G

    input1B = FloatField()
    input1b = input1B


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1R = FloatField()
    input1r = input1R

    input1G = FloatField()
    input1g = input1G

    input1B = FloatField()
    input1b = input1B


class Input2PlugOperator(
    Float3CompoundBasePlugOperator["Input2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2R", "input2r"),
        ("input2G", "input2g"),
        ("input2B", "input2b"),
    )

    input2R = FloatField()
    input2r = input2R

    input2G = FloatField()
    input2g = input2G

    input2B = FloatField()
    input2b = input2B


class Input2AttrOperator(
    Float3CompoundBaseAttrOperator[Input2PlugOperator]
):
    __slots__ = ()

    input2R = FloatField()
    input2r = input2R

    input2G = FloatField()
    input2g = input2G

    input2B = FloatField()
    input2b = input2B


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2R = FloatField()
    input2r = input2R

    input2G = FloatField()
    input2g = input2G

    input2B = FloatField()
    input2b = input2B
