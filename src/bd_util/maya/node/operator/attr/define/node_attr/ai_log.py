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


class BasePlugOperator(
    Float3CompoundBasePlugOperator["BaseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseR", "baser"),
        ("baseG", "baseg"),
        ("baseB", "baseb"),
    )

    baseR = FloatField()
    baser = baseR

    baseG = FloatField()
    baseg = baseG

    baseB = FloatField()
    baseb = baseB


class BaseAttrOperator(
    Float3CompoundBaseAttrOperator[BasePlugOperator]
):
    __slots__ = ()

    baseR = FloatField()
    baser = baseR

    baseG = FloatField()
    baseg = baseG

    baseB = FloatField()
    baseb = baseB


class BaseField(
    Float3CompoundBaseField[BaseAttrOperator, BasePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseAttrOperator
    PLUG_CLS = BasePlugOperator

    baseR = FloatField()
    baser = baseR

    baseG = FloatField()
    baseg = baseG

    baseB = FloatField()
    baseb = baseB
