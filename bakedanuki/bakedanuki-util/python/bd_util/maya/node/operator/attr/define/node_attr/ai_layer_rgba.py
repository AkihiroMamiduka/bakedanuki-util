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


class Input1PlugOperator(
    Float3CompoundBasePlugOperator["Input1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1R", "input1r"),
        ("input1G", "input1g"),
        ("input1B", "input1b"),
    )

    input1R = FloatField(default_value=0.0)
    input1r = input1R

    input1G = FloatField(default_value=0.0)
    input1g = input1G

    input1B = FloatField(default_value=0.0)
    input1b = input1B


class Input1AttrOperator(
    Float3CompoundBaseAttrOperator[Input1PlugOperator]
):
    __slots__ = ()

    input1R = FloatField(default_value=0.0)
    input1r = input1R

    input1G = FloatField(default_value=0.0)
    input1g = input1G

    input1B = FloatField(default_value=0.0)
    input1b = input1B


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1R = FloatField(default_value=0.0)
    input1r = input1R

    input1G = FloatField(default_value=0.0)
    input1g = input1G

    input1B = FloatField(default_value=0.0)
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

    input2R = FloatField(default_value=0.0)
    input2r = input2R

    input2G = FloatField(default_value=0.0)
    input2g = input2G

    input2B = FloatField(default_value=0.0)
    input2b = input2B


class Input2AttrOperator(
    Float3CompoundBaseAttrOperator[Input2PlugOperator]
):
    __slots__ = ()

    input2R = FloatField(default_value=0.0)
    input2r = input2R

    input2G = FloatField(default_value=0.0)
    input2g = input2G

    input2B = FloatField(default_value=0.0)
    input2b = input2B


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2R = FloatField(default_value=0.0)
    input2r = input2R

    input2G = FloatField(default_value=0.0)
    input2g = input2G

    input2B = FloatField(default_value=0.0)
    input2b = input2B


class Input3PlugOperator(
    Float3CompoundBasePlugOperator["Input3AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input3R", "input3r"),
        ("input3G", "input3g"),
        ("input3B", "input3b"),
    )

    input3R = FloatField(default_value=0.0)
    input3r = input3R

    input3G = FloatField(default_value=0.0)
    input3g = input3G

    input3B = FloatField(default_value=0.0)
    input3b = input3B


class Input3AttrOperator(
    Float3CompoundBaseAttrOperator[Input3PlugOperator]
):
    __slots__ = ()

    input3R = FloatField(default_value=0.0)
    input3r = input3R

    input3G = FloatField(default_value=0.0)
    input3g = input3G

    input3B = FloatField(default_value=0.0)
    input3b = input3B


class Input3Field(
    Float3CompoundBaseField[Input3AttrOperator, Input3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input3AttrOperator
    PLUG_CLS = Input3PlugOperator

    input3R = FloatField(default_value=0.0)
    input3r = input3R

    input3G = FloatField(default_value=0.0)
    input3g = input3G

    input3B = FloatField(default_value=0.0)
    input3b = input3B


class Input4PlugOperator(
    Float3CompoundBasePlugOperator["Input4AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input4R", "input4r"),
        ("input4G", "input4g"),
        ("input4B", "input4b"),
    )

    input4R = FloatField(default_value=0.0)
    input4r = input4R

    input4G = FloatField(default_value=0.0)
    input4g = input4G

    input4B = FloatField(default_value=0.0)
    input4b = input4B


class Input4AttrOperator(
    Float3CompoundBaseAttrOperator[Input4PlugOperator]
):
    __slots__ = ()

    input4R = FloatField(default_value=0.0)
    input4r = input4R

    input4G = FloatField(default_value=0.0)
    input4g = input4G

    input4B = FloatField(default_value=0.0)
    input4b = input4B


class Input4Field(
    Float3CompoundBaseField[Input4AttrOperator, Input4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input4AttrOperator
    PLUG_CLS = Input4PlugOperator

    input4R = FloatField(default_value=0.0)
    input4r = input4R

    input4G = FloatField(default_value=0.0)
    input4g = input4G

    input4B = FloatField(default_value=0.0)
    input4b = input4B


class Input5PlugOperator(
    Float3CompoundBasePlugOperator["Input5AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input5R", "input5r"),
        ("input5G", "input5g"),
        ("input5B", "input5b"),
    )

    input5R = FloatField(default_value=0.0)
    input5r = input5R

    input5G = FloatField(default_value=0.0)
    input5g = input5G

    input5B = FloatField(default_value=0.0)
    input5b = input5B


class Input5AttrOperator(
    Float3CompoundBaseAttrOperator[Input5PlugOperator]
):
    __slots__ = ()

    input5R = FloatField(default_value=0.0)
    input5r = input5R

    input5G = FloatField(default_value=0.0)
    input5g = input5G

    input5B = FloatField(default_value=0.0)
    input5b = input5B


class Input5Field(
    Float3CompoundBaseField[Input5AttrOperator, Input5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input5AttrOperator
    PLUG_CLS = Input5PlugOperator

    input5R = FloatField(default_value=0.0)
    input5r = input5R

    input5G = FloatField(default_value=0.0)
    input5g = input5G

    input5B = FloatField(default_value=0.0)
    input5b = input5B


class Input6PlugOperator(
    Float3CompoundBasePlugOperator["Input6AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input6R", "input6r"),
        ("input6G", "input6g"),
        ("input6B", "input6b"),
    )

    input6R = FloatField(default_value=0.0)
    input6r = input6R

    input6G = FloatField(default_value=0.0)
    input6g = input6G

    input6B = FloatField(default_value=0.0)
    input6b = input6B


class Input6AttrOperator(
    Float3CompoundBaseAttrOperator[Input6PlugOperator]
):
    __slots__ = ()

    input6R = FloatField(default_value=0.0)
    input6r = input6R

    input6G = FloatField(default_value=0.0)
    input6g = input6G

    input6B = FloatField(default_value=0.0)
    input6b = input6B


class Input6Field(
    Float3CompoundBaseField[Input6AttrOperator, Input6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input6AttrOperator
    PLUG_CLS = Input6PlugOperator

    input6R = FloatField(default_value=0.0)
    input6r = input6R

    input6G = FloatField(default_value=0.0)
    input6g = input6G

    input6B = FloatField(default_value=0.0)
    input6b = input6B


class Input7PlugOperator(
    Float3CompoundBasePlugOperator["Input7AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input7R", "input7r"),
        ("input7G", "input7g"),
        ("input7B", "input7b"),
    )

    input7R = FloatField(default_value=0.0)
    input7r = input7R

    input7G = FloatField(default_value=0.0)
    input7g = input7G

    input7B = FloatField(default_value=0.0)
    input7b = input7B


class Input7AttrOperator(
    Float3CompoundBaseAttrOperator[Input7PlugOperator]
):
    __slots__ = ()

    input7R = FloatField(default_value=0.0)
    input7r = input7R

    input7G = FloatField(default_value=0.0)
    input7g = input7G

    input7B = FloatField(default_value=0.0)
    input7b = input7B


class Input7Field(
    Float3CompoundBaseField[Input7AttrOperator, Input7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input7AttrOperator
    PLUG_CLS = Input7PlugOperator

    input7R = FloatField(default_value=0.0)
    input7r = input7R

    input7G = FloatField(default_value=0.0)
    input7g = input7G

    input7B = FloatField(default_value=0.0)
    input7b = input7B


class Input8PlugOperator(
    Float3CompoundBasePlugOperator["Input8AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input8R", "input8r"),
        ("input8G", "input8g"),
        ("input8B", "input8b"),
    )

    input8R = FloatField(default_value=0.0)
    input8r = input8R

    input8G = FloatField(default_value=0.0)
    input8g = input8G

    input8B = FloatField(default_value=0.0)
    input8b = input8B


class Input8AttrOperator(
    Float3CompoundBaseAttrOperator[Input8PlugOperator]
):
    __slots__ = ()

    input8R = FloatField(default_value=0.0)
    input8r = input8R

    input8G = FloatField(default_value=0.0)
    input8g = input8G

    input8B = FloatField(default_value=0.0)
    input8b = input8B


class Input8Field(
    Float3CompoundBaseField[Input8AttrOperator, Input8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input8AttrOperator
    PLUG_CLS = Input8PlugOperator

    input8R = FloatField(default_value=0.0)
    input8r = input8R

    input8G = FloatField(default_value=0.0)
    input8g = input8G

    input8B = FloatField(default_value=0.0)
    input8b = input8B
