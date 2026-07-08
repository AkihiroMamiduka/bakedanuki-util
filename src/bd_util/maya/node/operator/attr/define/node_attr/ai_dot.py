# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


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
        ("input1X", "input1x"),
        ("input1Y", "input1y"),
        ("input1Z", "input1z"),
    )

    input1X = FloatField(default_value=1.0)
    input1x = input1X

    input1Y = FloatField(default_value=1.0)
    input1y = input1Y

    input1Z = FloatField(default_value=1.0)
    input1z = input1Z


class Input1AttrOperator(
    Float3CompoundBaseAttrOperator[Input1PlugOperator]
):
    __slots__ = ()

    input1X = FloatField(default_value=1.0)
    input1x = input1X

    input1Y = FloatField(default_value=1.0)
    input1y = input1Y

    input1Z = FloatField(default_value=1.0)
    input1z = input1Z


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1X = FloatField(default_value=1.0)
    input1x = input1X

    input1Y = FloatField(default_value=1.0)
    input1y = input1Y

    input1Z = FloatField(default_value=1.0)
    input1z = input1Z


class Input2PlugOperator(
    Float3CompoundBasePlugOperator["Input2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2X", "input2x"),
        ("input2Y", "input2y"),
        ("input2Z", "input2z"),
    )

    input2X = FloatField(default_value=1.0)
    input2x = input2X

    input2Y = FloatField(default_value=1.0)
    input2y = input2Y

    input2Z = FloatField(default_value=1.0)
    input2z = input2Z


class Input2AttrOperator(
    Float3CompoundBaseAttrOperator[Input2PlugOperator]
):
    __slots__ = ()

    input2X = FloatField(default_value=1.0)
    input2x = input2X

    input2Y = FloatField(default_value=1.0)
    input2y = input2Y

    input2Z = FloatField(default_value=1.0)
    input2z = input2Z


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2X = FloatField(default_value=1.0)
    input2x = input2X

    input2Y = FloatField(default_value=1.0)
    input2y = input2Y

    input2Z = FloatField(default_value=1.0)
    input2z = input2Z
