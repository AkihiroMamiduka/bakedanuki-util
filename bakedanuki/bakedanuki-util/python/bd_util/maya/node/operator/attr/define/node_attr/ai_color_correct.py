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


class MultiplyPlugOperator(
    Float3CompoundBasePlugOperator["MultiplyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("multiplyR", "multiplyr"),
        ("multiplyG", "multiplyg"),
        ("multiplyB", "multiplyb"),
    )

    multiplyR = FloatField(default_value=1.0)
    multiplyr = multiplyR

    multiplyG = FloatField(default_value=1.0)
    multiplyg = multiplyG

    multiplyB = FloatField(default_value=1.0)
    multiplyb = multiplyB


class MultiplyAttrOperator(
    Float3CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiplyR = FloatField(default_value=1.0)
    multiplyr = multiplyR

    multiplyG = FloatField(default_value=1.0)
    multiplyg = multiplyG

    multiplyB = FloatField(default_value=1.0)
    multiplyb = multiplyB


class MultiplyField(
    Float3CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiplyR = FloatField(default_value=1.0)
    multiplyr = multiplyR

    multiplyG = FloatField(default_value=1.0)
    multiplyg = multiplyG

    multiplyB = FloatField(default_value=1.0)
    multiplyb = multiplyB


class AddPlugOperator(Float3CompoundBasePlugOperator["AddAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("addR", "addr"),
        ("addG", "addg"),
        ("addB", "addb"),
    )

    addR = FloatField(default_value=0.0)
    addr = addR

    addG = FloatField(default_value=0.0)
    addg = addG

    addB = FloatField(default_value=0.0)
    addb = addB


class AddAttrOperator(Float3CompoundBaseAttrOperator[AddPlugOperator]):
    __slots__ = ()

    addR = FloatField(default_value=0.0)
    addr = addR

    addG = FloatField(default_value=0.0)
    addg = addG

    addB = FloatField(default_value=0.0)
    addb = addB


class AddField(Float3CompoundBaseField[AddAttrOperator, AddPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AddAttrOperator
    PLUG_CLS = AddPlugOperator

    addR = FloatField(default_value=0.0)
    addr = addR

    addG = FloatField(default_value=0.0)
    addg = addG

    addB = FloatField(default_value=0.0)
    addb = addB
