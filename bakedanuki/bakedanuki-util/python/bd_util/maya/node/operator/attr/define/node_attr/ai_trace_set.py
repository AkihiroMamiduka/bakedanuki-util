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


class PassthroughPlugOperator(
    Float3CompoundBasePlugOperator["PassthroughAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("passthroughR", "passthroughr"),
        ("passthroughG", "passthroughg"),
        ("passthroughB", "passthroughb"),
    )

    passthroughR = FloatField(default_value=0.0)
    passthroughr = passthroughR

    passthroughG = FloatField(default_value=0.0)
    passthroughg = passthroughG

    passthroughB = FloatField(default_value=0.0)
    passthroughb = passthroughB


class PassthroughAttrOperator(
    Float3CompoundBaseAttrOperator[PassthroughPlugOperator]
):
    __slots__ = ()

    passthroughR = FloatField(default_value=0.0)
    passthroughr = passthroughR

    passthroughG = FloatField(default_value=0.0)
    passthroughg = passthroughG

    passthroughB = FloatField(default_value=0.0)
    passthroughb = passthroughB


class PassthroughField(
    Float3CompoundBaseField[PassthroughAttrOperator, PassthroughPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PassthroughAttrOperator
    PLUG_CLS = PassthroughPlugOperator

    passthroughR = FloatField(default_value=0.0)
    passthroughr = passthroughR

    passthroughG = FloatField(default_value=0.0)
    passthroughg = passthroughG

    passthroughB = FloatField(default_value=0.0)
    passthroughb = passthroughB
