# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
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


class Input1PlugOperator(Float3CompoundBasePlugOperator["Input1AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1R", "input1r"),
        ("input1G", "input1g"),
        ("input1B", "input1b"),
    )

    input1R = FloatField(default_value=1.0)
    input1r = input1R

    input1G = FloatField(default_value=1.0)
    input1g = input1G

    input1B = FloatField(default_value=1.0)
    input1b = input1B


class Input1AttrOperator(Float3CompoundBaseAttrOperator[Input1PlugOperator]):
    __slots__ = ()

    input1R = FloatField(default_value=1.0)
    input1r = input1R

    input1G = FloatField(default_value=1.0)
    input1g = input1G

    input1B = FloatField(default_value=1.0)
    input1b = input1B


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1R = FloatField(default_value=1.0)
    input1r = input1R

    input1G = FloatField(default_value=1.0)
    input1g = input1G

    input1B = FloatField(default_value=1.0)
    input1b = input1B


class Input2PlugOperator(Float3CompoundBasePlugOperator["Input2AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2R", "input2r"),
        ("input2G", "input2g"),
        ("input2B", "input2b"),
    )

    input2R = FloatField(default_value=1.0)
    input2r = input2R

    input2G = FloatField(default_value=1.0)
    input2g = input2G

    input2B = FloatField(default_value=1.0)
    input2b = input2B


class Input2AttrOperator(Float3CompoundBaseAttrOperator[Input2PlugOperator]):
    __slots__ = ()

    input2R = FloatField(default_value=1.0)
    input2r = input2R

    input2G = FloatField(default_value=1.0)
    input2g = input2G

    input2B = FloatField(default_value=1.0)
    input2b = input2B


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2R = FloatField(default_value=1.0)
    input2r = input2R

    input2G = FloatField(default_value=1.0)
    input2g = input2G

    input2B = FloatField(default_value=1.0)
    input2b = input2B
