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


class InputPlugOperator(
    Float3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputR", "inputr"),
        ("inputG", "inputg"),
        ("inputB", "inputb"),
    )

    inputR = FloatField()
    inputr = inputR

    inputG = FloatField()
    inputg = inputG

    inputB = FloatField()
    inputb = inputB


class InputAttrOperator(
    Float3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputR = FloatField()
    inputr = inputR

    inputG = FloatField()
    inputg = inputG

    inputB = FloatField()
    inputb = inputB


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputR = FloatField()
    inputr = inputR

    inputG = FloatField()
    inputg = inputG

    inputB = FloatField()
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

    multiplyR = FloatField()
    multiplyr = multiplyR

    multiplyG = FloatField()
    multiplyg = multiplyG

    multiplyB = FloatField()
    multiplyb = multiplyB


class MultiplyAttrOperator(
    Float3CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiplyR = FloatField()
    multiplyr = multiplyR

    multiplyG = FloatField()
    multiplyg = multiplyG

    multiplyB = FloatField()
    multiplyb = multiplyB


class MultiplyField(
    Float3CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiplyR = FloatField()
    multiplyr = multiplyR

    multiplyG = FloatField()
    multiplyg = multiplyG

    multiplyB = FloatField()
    multiplyb = multiplyB


class AddPlugOperator(
    Float3CompoundBasePlugOperator["AddAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("addR", "addr"),
        ("addG", "addg"),
        ("addB", "addb"),
    )

    addR = FloatField()
    addr = addR

    addG = FloatField()
    addg = addG

    addB = FloatField()
    addb = addB


class AddAttrOperator(
    Float3CompoundBaseAttrOperator[AddPlugOperator]
):
    __slots__ = ()

    addR = FloatField()
    addr = addR

    addG = FloatField()
    addg = addG

    addB = FloatField()
    addb = addB


class AddField(
    Float3CompoundBaseField[AddAttrOperator, AddPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AddAttrOperator
    PLUG_CLS = AddPlugOperator

    addR = FloatField()
    addr = addR

    addG = FloatField()
    addg = addG

    addB = FloatField()
    addb = addB
