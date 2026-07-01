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


class MinColorPlugOperator(
    Float3CompoundBasePlugOperator["MinColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minColorR", "min_colorr"),
        ("minColorG", "min_colorg"),
        ("minColorB", "min_colorb"),
    )

    minColorR = FloatField()
    min_colorr = minColorR

    minColorG = FloatField()
    min_colorg = minColorG

    minColorB = FloatField()
    min_colorb = minColorB


class MinColorAttrOperator(
    Float3CompoundBaseAttrOperator[MinColorPlugOperator]
):
    __slots__ = ()

    minColorR = FloatField()
    min_colorr = minColorR

    minColorG = FloatField()
    min_colorg = minColorG

    minColorB = FloatField()
    min_colorb = minColorB


class MinColorField(
    Float3CompoundBaseField[MinColorAttrOperator, MinColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinColorAttrOperator
    PLUG_CLS = MinColorPlugOperator

    minColorR = FloatField()
    min_colorr = minColorR

    minColorG = FloatField()
    min_colorg = minColorG

    minColorB = FloatField()
    min_colorb = minColorB


class MaxColorPlugOperator(
    Float3CompoundBasePlugOperator["MaxColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxColorR", "max_colorr"),
        ("maxColorG", "max_colorg"),
        ("maxColorB", "max_colorb"),
    )

    maxColorR = FloatField()
    max_colorr = maxColorR

    maxColorG = FloatField()
    max_colorg = maxColorG

    maxColorB = FloatField()
    max_colorb = maxColorB


class MaxColorAttrOperator(
    Float3CompoundBaseAttrOperator[MaxColorPlugOperator]
):
    __slots__ = ()

    maxColorR = FloatField()
    max_colorr = maxColorR

    maxColorG = FloatField()
    max_colorg = maxColorG

    maxColorB = FloatField()
    max_colorb = maxColorB


class MaxColorField(
    Float3CompoundBaseField[MaxColorAttrOperator, MaxColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxColorAttrOperator
    PLUG_CLS = MaxColorPlugOperator

    maxColorR = FloatField()
    max_colorr = maxColorR

    maxColorG = FloatField()
    max_colorg = maxColorG

    maxColorB = FloatField()
    max_colorb = maxColorB
