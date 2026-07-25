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


class BasePlugOperator(
    Float3CompoundBasePlugOperator["BaseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseR", "baser"),
        ("baseG", "baseg"),
        ("baseB", "baseb"),
    )

    baseR = FloatField(default_value=2.7182817459106445)
    baser = baseR

    baseG = FloatField(default_value=2.7182817459106445)
    baseg = baseG

    baseB = FloatField(default_value=2.7182817459106445)
    baseb = baseB


class BaseAttrOperator(
    Float3CompoundBaseAttrOperator[BasePlugOperator]
):
    __slots__ = ()

    baseR = FloatField(default_value=2.7182817459106445)
    baser = baseR

    baseG = FloatField(default_value=2.7182817459106445)
    baseg = baseG

    baseB = FloatField(default_value=2.7182817459106445)
    baseb = baseB


class BaseField(
    Float3CompoundBaseField[BaseAttrOperator, BasePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseAttrOperator
    PLUG_CLS = BasePlugOperator

    baseR = FloatField(default_value=2.7182817459106445)
    baser = baseR

    baseG = FloatField(default_value=2.7182817459106445)
    baseg = baseG

    baseB = FloatField(default_value=2.7182817459106445)
    baseb = baseB


class ExponentPlugOperator(
    Float3CompoundBasePlugOperator["ExponentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("exponentR", "exponentr"),
        ("exponentG", "exponentg"),
        ("exponentB", "exponentb"),
    )

    exponentR = FloatField(default_value=0.0)
    exponentr = exponentR

    exponentG = FloatField(default_value=0.0)
    exponentg = exponentG

    exponentB = FloatField(default_value=0.0)
    exponentb = exponentB


class ExponentAttrOperator(
    Float3CompoundBaseAttrOperator[ExponentPlugOperator]
):
    __slots__ = ()

    exponentR = FloatField(default_value=0.0)
    exponentr = exponentR

    exponentG = FloatField(default_value=0.0)
    exponentg = exponentG

    exponentB = FloatField(default_value=0.0)
    exponentb = exponentB


class ExponentField(
    Float3CompoundBaseField[ExponentAttrOperator, ExponentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExponentAttrOperator
    PLUG_CLS = ExponentPlugOperator

    exponentR = FloatField(default_value=0.0)
    exponentr = exponentR

    exponentG = FloatField(default_value=0.0)
    exponentg = exponentG

    exponentB = FloatField(default_value=0.0)
    exponentb = exponentB
