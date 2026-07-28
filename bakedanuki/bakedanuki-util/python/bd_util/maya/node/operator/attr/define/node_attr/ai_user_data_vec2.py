# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutValuePlugOperator(
    Float2CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "outx"),
        ("outValueY", "outy"),
    )

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY


class OutValueAttrOperator(
    Float2CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY


class OutValueField(
    Float2CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY


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


class DefaultValuePlugOperator(
    Float2CompoundBasePlugOperator["DefaultValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultValueX", "defaultValuex"),
        ("defaultValueY", "defaultValuey"),
    )

    defaultValueX = FloatField(default_value=0.0)
    defaultValuex = defaultValueX

    defaultValueY = FloatField(default_value=0.0)
    defaultValuey = defaultValueY


class DefaultValueAttrOperator(
    Float2CompoundBaseAttrOperator[DefaultValuePlugOperator]
):
    __slots__ = ()

    defaultValueX = FloatField(default_value=0.0)
    defaultValuex = defaultValueX

    defaultValueY = FloatField(default_value=0.0)
    defaultValuey = defaultValueY


class DefaultValueField(
    Float2CompoundBaseField[DefaultValueAttrOperator, DefaultValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultValueAttrOperator
    PLUG_CLS = DefaultValuePlugOperator

    defaultValueX = FloatField(default_value=0.0)
    defaultValuex = defaultValueX

    defaultValueY = FloatField(default_value=0.0)
    defaultValuey = defaultValueY
