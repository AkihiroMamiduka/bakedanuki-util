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


class Out_1PlugOperator(Float3CompoundBasePlugOperator["Out_1AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_1R", "out_1r"),
        ("out_1G", "out_1g"),
        ("out_1B", "out_1b"),
    )

    out_1R = FloatField(default_value=0.0, writable=False)
    out_1r = out_1R

    out_1G = FloatField(default_value=0.0, writable=False)
    out_1g = out_1G

    out_1B = FloatField(default_value=0.0, writable=False)
    out_1b = out_1B


class Out_1AttrOperator(Float3CompoundBaseAttrOperator[Out_1PlugOperator]):
    __slots__ = ()

    out_1R = FloatField(default_value=0.0, writable=False)
    out_1r = out_1R

    out_1G = FloatField(default_value=0.0, writable=False)
    out_1g = out_1G

    out_1B = FloatField(default_value=0.0, writable=False)
    out_1b = out_1B


class Out_1Field(
    Float3CompoundBaseField[Out_1AttrOperator, Out_1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_1AttrOperator
    PLUG_CLS = Out_1PlugOperator

    out_1R = FloatField(default_value=0.0, writable=False)
    out_1r = out_1R

    out_1G = FloatField(default_value=0.0, writable=False)
    out_1g = out_1G

    out_1B = FloatField(default_value=0.0, writable=False)
    out_1b = out_1B


class Out_2PlugOperator(Float3CompoundBasePlugOperator["Out_2AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_2R", "out_2r"),
        ("out_2G", "out_2g"),
        ("out_2B", "out_2b"),
    )

    out_2R = FloatField(default_value=0.0, writable=False)
    out_2r = out_2R

    out_2G = FloatField(default_value=0.0, writable=False)
    out_2g = out_2G

    out_2B = FloatField(default_value=0.0, writable=False)
    out_2b = out_2B


class Out_2AttrOperator(Float3CompoundBaseAttrOperator[Out_2PlugOperator]):
    __slots__ = ()

    out_2R = FloatField(default_value=0.0, writable=False)
    out_2r = out_2R

    out_2G = FloatField(default_value=0.0, writable=False)
    out_2g = out_2G

    out_2B = FloatField(default_value=0.0, writable=False)
    out_2b = out_2B


class Out_2Field(
    Float3CompoundBaseField[Out_2AttrOperator, Out_2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_2AttrOperator
    PLUG_CLS = Out_2PlugOperator

    out_2R = FloatField(default_value=0.0, writable=False)
    out_2r = out_2R

    out_2G = FloatField(default_value=0.0, writable=False)
    out_2g = out_2G

    out_2B = FloatField(default_value=0.0, writable=False)
    out_2b = out_2B


class Out_3PlugOperator(Float3CompoundBasePlugOperator["Out_3AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_3R", "out_3r"),
        ("out_3G", "out_3g"),
        ("out_3B", "out_3b"),
    )

    out_3R = FloatField(default_value=0.0, writable=False)
    out_3r = out_3R

    out_3G = FloatField(default_value=0.0, writable=False)
    out_3g = out_3G

    out_3B = FloatField(default_value=0.0, writable=False)
    out_3b = out_3B


class Out_3AttrOperator(Float3CompoundBaseAttrOperator[Out_3PlugOperator]):
    __slots__ = ()

    out_3R = FloatField(default_value=0.0, writable=False)
    out_3r = out_3R

    out_3G = FloatField(default_value=0.0, writable=False)
    out_3g = out_3G

    out_3B = FloatField(default_value=0.0, writable=False)
    out_3b = out_3B


class Out_3Field(
    Float3CompoundBaseField[Out_3AttrOperator, Out_3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_3AttrOperator
    PLUG_CLS = Out_3PlugOperator

    out_3R = FloatField(default_value=0.0, writable=False)
    out_3r = out_3R

    out_3G = FloatField(default_value=0.0, writable=False)
    out_3g = out_3G

    out_3B = FloatField(default_value=0.0, writable=False)
    out_3b = out_3B


class Out_4PlugOperator(Float3CompoundBasePlugOperator["Out_4AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_4R", "out_4r"),
        ("out_4G", "out_4g"),
        ("out_4B", "out_4b"),
    )

    out_4R = FloatField(default_value=0.0, writable=False)
    out_4r = out_4R

    out_4G = FloatField(default_value=0.0, writable=False)
    out_4g = out_4G

    out_4B = FloatField(default_value=0.0, writable=False)
    out_4b = out_4B


class Out_4AttrOperator(Float3CompoundBaseAttrOperator[Out_4PlugOperator]):
    __slots__ = ()

    out_4R = FloatField(default_value=0.0, writable=False)
    out_4r = out_4R

    out_4G = FloatField(default_value=0.0, writable=False)
    out_4g = out_4G

    out_4B = FloatField(default_value=0.0, writable=False)
    out_4b = out_4B


class Out_4Field(
    Float3CompoundBaseField[Out_4AttrOperator, Out_4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_4AttrOperator
    PLUG_CLS = Out_4PlugOperator

    out_4R = FloatField(default_value=0.0, writable=False)
    out_4r = out_4R

    out_4G = FloatField(default_value=0.0, writable=False)
    out_4g = out_4G

    out_4B = FloatField(default_value=0.0, writable=False)
    out_4b = out_4B


class Out_5PlugOperator(Float3CompoundBasePlugOperator["Out_5AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_5R", "out_5r"),
        ("out_5G", "out_5g"),
        ("out_5B", "out_5b"),
    )

    out_5R = FloatField(default_value=0.0, writable=False)
    out_5r = out_5R

    out_5G = FloatField(default_value=0.0, writable=False)
    out_5g = out_5G

    out_5B = FloatField(default_value=0.0, writable=False)
    out_5b = out_5B


class Out_5AttrOperator(Float3CompoundBaseAttrOperator[Out_5PlugOperator]):
    __slots__ = ()

    out_5R = FloatField(default_value=0.0, writable=False)
    out_5r = out_5R

    out_5G = FloatField(default_value=0.0, writable=False)
    out_5g = out_5G

    out_5B = FloatField(default_value=0.0, writable=False)
    out_5b = out_5B


class Out_5Field(
    Float3CompoundBaseField[Out_5AttrOperator, Out_5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_5AttrOperator
    PLUG_CLS = Out_5PlugOperator

    out_5R = FloatField(default_value=0.0, writable=False)
    out_5r = out_5R

    out_5G = FloatField(default_value=0.0, writable=False)
    out_5g = out_5G

    out_5B = FloatField(default_value=0.0, writable=False)
    out_5b = out_5B


class Out_6PlugOperator(Float3CompoundBasePlugOperator["Out_6AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_6R", "out_6r"),
        ("out_6G", "out_6g"),
        ("out_6B", "out_6b"),
    )

    out_6R = FloatField(default_value=0.0, writable=False)
    out_6r = out_6R

    out_6G = FloatField(default_value=0.0, writable=False)
    out_6g = out_6G

    out_6B = FloatField(default_value=0.0, writable=False)
    out_6b = out_6B


class Out_6AttrOperator(Float3CompoundBaseAttrOperator[Out_6PlugOperator]):
    __slots__ = ()

    out_6R = FloatField(default_value=0.0, writable=False)
    out_6r = out_6R

    out_6G = FloatField(default_value=0.0, writable=False)
    out_6g = out_6G

    out_6B = FloatField(default_value=0.0, writable=False)
    out_6b = out_6B


class Out_6Field(
    Float3CompoundBaseField[Out_6AttrOperator, Out_6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_6AttrOperator
    PLUG_CLS = Out_6PlugOperator

    out_6R = FloatField(default_value=0.0, writable=False)
    out_6r = out_6R

    out_6G = FloatField(default_value=0.0, writable=False)
    out_6g = out_6G

    out_6B = FloatField(default_value=0.0, writable=False)
    out_6b = out_6B


class Out_7PlugOperator(Float3CompoundBasePlugOperator["Out_7AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_7R", "out_7r"),
        ("out_7G", "out_7g"),
        ("out_7B", "out_7b"),
    )

    out_7R = FloatField(default_value=0.0, writable=False)
    out_7r = out_7R

    out_7G = FloatField(default_value=0.0, writable=False)
    out_7g = out_7G

    out_7B = FloatField(default_value=0.0, writable=False)
    out_7b = out_7B


class Out_7AttrOperator(Float3CompoundBaseAttrOperator[Out_7PlugOperator]):
    __slots__ = ()

    out_7R = FloatField(default_value=0.0, writable=False)
    out_7r = out_7R

    out_7G = FloatField(default_value=0.0, writable=False)
    out_7g = out_7G

    out_7B = FloatField(default_value=0.0, writable=False)
    out_7b = out_7B


class Out_7Field(
    Float3CompoundBaseField[Out_7AttrOperator, Out_7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_7AttrOperator
    PLUG_CLS = Out_7PlugOperator

    out_7R = FloatField(default_value=0.0, writable=False)
    out_7r = out_7R

    out_7G = FloatField(default_value=0.0, writable=False)
    out_7g = out_7G

    out_7B = FloatField(default_value=0.0, writable=False)
    out_7b = out_7B


class Out_8PlugOperator(Float3CompoundBasePlugOperator["Out_8AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_8R", "out_8r"),
        ("out_8G", "out_8g"),
        ("out_8B", "out_8b"),
    )

    out_8R = FloatField(default_value=0.0, writable=False)
    out_8r = out_8R

    out_8G = FloatField(default_value=0.0, writable=False)
    out_8g = out_8G

    out_8B = FloatField(default_value=0.0, writable=False)
    out_8b = out_8B


class Out_8AttrOperator(Float3CompoundBaseAttrOperator[Out_8PlugOperator]):
    __slots__ = ()

    out_8R = FloatField(default_value=0.0, writable=False)
    out_8r = out_8R

    out_8G = FloatField(default_value=0.0, writable=False)
    out_8g = out_8G

    out_8B = FloatField(default_value=0.0, writable=False)
    out_8b = out_8B


class Out_8Field(
    Float3CompoundBaseField[Out_8AttrOperator, Out_8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_8AttrOperator
    PLUG_CLS = Out_8PlugOperator

    out_8R = FloatField(default_value=0.0, writable=False)
    out_8r = out_8R

    out_8G = FloatField(default_value=0.0, writable=False)
    out_8g = out_8G

    out_8B = FloatField(default_value=0.0, writable=False)
    out_8b = out_8B


class InputPlugOperator(Float3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputR", "inputr"),
        ("inputG", "inputg"),
        ("inputB", "inputb"),
    )

    inputR = FloatField(default_value=0.0)
    inputr = inputR

    inputG = FloatField(default_value=0.0)
    inputg = inputG

    inputB = FloatField(default_value=0.0)
    inputb = inputB


class InputAttrOperator(Float3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputR = FloatField(default_value=0.0)
    inputr = inputR

    inputG = FloatField(default_value=0.0)
    inputg = inputG

    inputB = FloatField(default_value=0.0)
    inputb = inputB


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputR = FloatField(default_value=0.0)
    inputr = inputR

    inputG = FloatField(default_value=0.0)
    inputg = inputG

    inputB = FloatField(default_value=0.0)
    inputb = inputB


class Tint1PlugOperator(Float3CompoundBasePlugOperator["Tint1AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint1R", "tint_1r"),
        ("tint1G", "tint_1g"),
        ("tint1B", "tint_1b"),
    )

    tint1R = FloatField(default_value=1.0)
    tint_1r = tint1R

    tint1G = FloatField(default_value=1.0)
    tint_1g = tint1G

    tint1B = FloatField(default_value=1.0)
    tint_1b = tint1B


class Tint1AttrOperator(Float3CompoundBaseAttrOperator[Tint1PlugOperator]):
    __slots__ = ()

    tint1R = FloatField(default_value=1.0)
    tint_1r = tint1R

    tint1G = FloatField(default_value=1.0)
    tint_1g = tint1G

    tint1B = FloatField(default_value=1.0)
    tint_1b = tint1B


class Tint1Field(
    Float3CompoundBaseField[Tint1AttrOperator, Tint1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint1AttrOperator
    PLUG_CLS = Tint1PlugOperator

    tint1R = FloatField(default_value=1.0)
    tint_1r = tint1R

    tint1G = FloatField(default_value=1.0)
    tint_1g = tint1G

    tint1B = FloatField(default_value=1.0)
    tint_1b = tint1B


class Tint2PlugOperator(Float3CompoundBasePlugOperator["Tint2AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint2R", "tint_2r"),
        ("tint2G", "tint_2g"),
        ("tint2B", "tint_2b"),
    )

    tint2R = FloatField(default_value=0.75)
    tint_2r = tint2R

    tint2G = FloatField(default_value=0.75)
    tint_2g = tint2G

    tint2B = FloatField(default_value=0.75)
    tint_2b = tint2B


class Tint2AttrOperator(Float3CompoundBaseAttrOperator[Tint2PlugOperator]):
    __slots__ = ()

    tint2R = FloatField(default_value=0.75)
    tint_2r = tint2R

    tint2G = FloatField(default_value=0.75)
    tint_2g = tint2G

    tint2B = FloatField(default_value=0.75)
    tint_2b = tint2B


class Tint2Field(
    Float3CompoundBaseField[Tint2AttrOperator, Tint2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint2AttrOperator
    PLUG_CLS = Tint2PlugOperator

    tint2R = FloatField(default_value=0.75)
    tint_2r = tint2R

    tint2G = FloatField(default_value=0.75)
    tint_2g = tint2G

    tint2B = FloatField(default_value=0.75)
    tint_2b = tint2B


class Tint3PlugOperator(Float3CompoundBasePlugOperator["Tint3AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint3R", "tint_3r"),
        ("tint3G", "tint_3g"),
        ("tint3B", "tint_3b"),
    )

    tint3R = FloatField(default_value=0.5)
    tint_3r = tint3R

    tint3G = FloatField(default_value=0.5)
    tint_3g = tint3G

    tint3B = FloatField(default_value=0.5)
    tint_3b = tint3B


class Tint3AttrOperator(Float3CompoundBaseAttrOperator[Tint3PlugOperator]):
    __slots__ = ()

    tint3R = FloatField(default_value=0.5)
    tint_3r = tint3R

    tint3G = FloatField(default_value=0.5)
    tint_3g = tint3G

    tint3B = FloatField(default_value=0.5)
    tint_3b = tint3B


class Tint3Field(
    Float3CompoundBaseField[Tint3AttrOperator, Tint3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint3AttrOperator
    PLUG_CLS = Tint3PlugOperator

    tint3R = FloatField(default_value=0.5)
    tint_3r = tint3R

    tint3G = FloatField(default_value=0.5)
    tint_3g = tint3G

    tint3B = FloatField(default_value=0.5)
    tint_3b = tint3B


class Tint4PlugOperator(Float3CompoundBasePlugOperator["Tint4AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint4R", "tint_4r"),
        ("tint4G", "tint_4g"),
        ("tint4B", "tint_4b"),
    )

    tint4R = FloatField(default_value=0.25)
    tint_4r = tint4R

    tint4G = FloatField(default_value=0.25)
    tint_4g = tint4G

    tint4B = FloatField(default_value=0.25)
    tint_4b = tint4B


class Tint4AttrOperator(Float3CompoundBaseAttrOperator[Tint4PlugOperator]):
    __slots__ = ()

    tint4R = FloatField(default_value=0.25)
    tint_4r = tint4R

    tint4G = FloatField(default_value=0.25)
    tint_4g = tint4G

    tint4B = FloatField(default_value=0.25)
    tint_4b = tint4B


class Tint4Field(
    Float3CompoundBaseField[Tint4AttrOperator, Tint4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint4AttrOperator
    PLUG_CLS = Tint4PlugOperator

    tint4R = FloatField(default_value=0.25)
    tint_4r = tint4R

    tint4G = FloatField(default_value=0.25)
    tint_4g = tint4G

    tint4B = FloatField(default_value=0.25)
    tint_4b = tint4B


class Tint5PlugOperator(Float3CompoundBasePlugOperator["Tint5AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint5R", "tint_5r"),
        ("tint5G", "tint_5g"),
        ("tint5B", "tint_5b"),
    )

    tint5R = FloatField(default_value=0.0)
    tint_5r = tint5R

    tint5G = FloatField(default_value=0.0)
    tint_5g = tint5G

    tint5B = FloatField(default_value=0.0)
    tint_5b = tint5B


class Tint5AttrOperator(Float3CompoundBaseAttrOperator[Tint5PlugOperator]):
    __slots__ = ()

    tint5R = FloatField(default_value=0.0)
    tint_5r = tint5R

    tint5G = FloatField(default_value=0.0)
    tint_5g = tint5G

    tint5B = FloatField(default_value=0.0)
    tint_5b = tint5B


class Tint5Field(
    Float3CompoundBaseField[Tint5AttrOperator, Tint5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint5AttrOperator
    PLUG_CLS = Tint5PlugOperator

    tint5R = FloatField(default_value=0.0)
    tint_5r = tint5R

    tint5G = FloatField(default_value=0.0)
    tint_5g = tint5G

    tint5B = FloatField(default_value=0.0)
    tint_5b = tint5B


class Tint6PlugOperator(Float3CompoundBasePlugOperator["Tint6AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint6R", "tint_6r"),
        ("tint6G", "tint_6g"),
        ("tint6B", "tint_6b"),
    )

    tint6R = FloatField(default_value=0.0)
    tint_6r = tint6R

    tint6G = FloatField(default_value=0.0)
    tint_6g = tint6G

    tint6B = FloatField(default_value=0.0)
    tint_6b = tint6B


class Tint6AttrOperator(Float3CompoundBaseAttrOperator[Tint6PlugOperator]):
    __slots__ = ()

    tint6R = FloatField(default_value=0.0)
    tint_6r = tint6R

    tint6G = FloatField(default_value=0.0)
    tint_6g = tint6G

    tint6B = FloatField(default_value=0.0)
    tint_6b = tint6B


class Tint6Field(
    Float3CompoundBaseField[Tint6AttrOperator, Tint6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint6AttrOperator
    PLUG_CLS = Tint6PlugOperator

    tint6R = FloatField(default_value=0.0)
    tint_6r = tint6R

    tint6G = FloatField(default_value=0.0)
    tint_6g = tint6G

    tint6B = FloatField(default_value=0.0)
    tint_6b = tint6B


class Tint7PlugOperator(Float3CompoundBasePlugOperator["Tint7AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint7R", "tint_7r"),
        ("tint7G", "tint_7g"),
        ("tint7B", "tint_7b"),
    )

    tint7R = FloatField(default_value=0.0)
    tint_7r = tint7R

    tint7G = FloatField(default_value=0.0)
    tint_7g = tint7G

    tint7B = FloatField(default_value=0.0)
    tint_7b = tint7B


class Tint7AttrOperator(Float3CompoundBaseAttrOperator[Tint7PlugOperator]):
    __slots__ = ()

    tint7R = FloatField(default_value=0.0)
    tint_7r = tint7R

    tint7G = FloatField(default_value=0.0)
    tint_7g = tint7G

    tint7B = FloatField(default_value=0.0)
    tint_7b = tint7B


class Tint7Field(
    Float3CompoundBaseField[Tint7AttrOperator, Tint7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint7AttrOperator
    PLUG_CLS = Tint7PlugOperator

    tint7R = FloatField(default_value=0.0)
    tint_7r = tint7R

    tint7G = FloatField(default_value=0.0)
    tint_7g = tint7G

    tint7B = FloatField(default_value=0.0)
    tint_7b = tint7B


class Tint8PlugOperator(Float3CompoundBasePlugOperator["Tint8AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tint8R", "tint_8r"),
        ("tint8G", "tint_8g"),
        ("tint8B", "tint_8b"),
    )

    tint8R = FloatField(default_value=0.0)
    tint_8r = tint8R

    tint8G = FloatField(default_value=0.0)
    tint_8g = tint8G

    tint8B = FloatField(default_value=0.0)
    tint_8b = tint8B


class Tint8AttrOperator(Float3CompoundBaseAttrOperator[Tint8PlugOperator]):
    __slots__ = ()

    tint8R = FloatField(default_value=0.0)
    tint_8r = tint8R

    tint8G = FloatField(default_value=0.0)
    tint_8g = tint8G

    tint8B = FloatField(default_value=0.0)
    tint_8b = tint8B


class Tint8Field(
    Float3CompoundBaseField[Tint8AttrOperator, Tint8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Tint8AttrOperator
    PLUG_CLS = Tint8PlugOperator

    tint8R = FloatField(default_value=0.0)
    tint_8r = tint8R

    tint8G = FloatField(default_value=0.0)
    tint_8g = tint8G

    tint8B = FloatField(default_value=0.0)
    tint_8b = tint8B
