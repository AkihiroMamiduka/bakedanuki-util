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


class OutDirectPlugOperator(
    Float3CompoundBasePlugOperator["OutDirectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outDirectR", "out_directr"),
        ("outDirectG", "out_directg"),
        ("outDirectB", "out_directb"),
    )

    outDirectR = FloatField(default_value=0.0, writable=False)
    out_directr = outDirectR

    outDirectG = FloatField(default_value=0.0, writable=False)
    out_directg = outDirectG

    outDirectB = FloatField(default_value=0.0, writable=False)
    out_directb = outDirectB


class OutDirectAttrOperator(
    Float3CompoundBaseAttrOperator[OutDirectPlugOperator]
):
    __slots__ = ()

    outDirectR = FloatField(default_value=0.0, writable=False)
    out_directr = outDirectR

    outDirectG = FloatField(default_value=0.0, writable=False)
    out_directg = outDirectG

    outDirectB = FloatField(default_value=0.0, writable=False)
    out_directb = outDirectB


class OutDirectField(
    Float3CompoundBaseField[OutDirectAttrOperator, OutDirectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutDirectAttrOperator
    PLUG_CLS = OutDirectPlugOperator

    outDirectR = FloatField(default_value=0.0, writable=False)
    out_directr = outDirectR

    outDirectG = FloatField(default_value=0.0, writable=False)
    out_directg = outDirectG

    outDirectB = FloatField(default_value=0.0, writable=False)
    out_directb = outDirectB


class OutIndirectPlugOperator(
    Float3CompoundBasePlugOperator["OutIndirectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outIndirectR", "out_indirectr"),
        ("outIndirectG", "out_indirectg"),
        ("outIndirectB", "out_indirectb"),
    )

    outIndirectR = FloatField(default_value=0.0, writable=False)
    out_indirectr = outIndirectR

    outIndirectG = FloatField(default_value=0.0, writable=False)
    out_indirectg = outIndirectG

    outIndirectB = FloatField(default_value=0.0, writable=False)
    out_indirectb = outIndirectB


class OutIndirectAttrOperator(
    Float3CompoundBaseAttrOperator[OutIndirectPlugOperator]
):
    __slots__ = ()

    outIndirectR = FloatField(default_value=0.0, writable=False)
    out_indirectr = outIndirectR

    outIndirectG = FloatField(default_value=0.0, writable=False)
    out_indirectg = outIndirectG

    outIndirectB = FloatField(default_value=0.0, writable=False)
    out_indirectb = outIndirectB


class OutIndirectField(
    Float3CompoundBaseField[OutIndirectAttrOperator, OutIndirectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutIndirectAttrOperator
    PLUG_CLS = OutIndirectPlugOperator

    outIndirectR = FloatField(default_value=0.0, writable=False)
    out_indirectr = outIndirectR

    outIndirectG = FloatField(default_value=0.0, writable=False)
    out_indirectg = outIndirectG

    outIndirectB = FloatField(default_value=0.0, writable=False)
    out_indirectb = outIndirectB


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
