# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutValuePlugOperator(
    Float3CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "outx"),
        ("outValueY", "outy"),
        ("outValueZ", "outz"),
    )

    outValueX = FloatField()
    outx = outValueX

    outValueY = FloatField()
    outy = outValueY

    outValueZ = FloatField()
    outz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField()
    outx = outValueX

    outValueY = FloatField()
    outy = outValueY

    outValueZ = FloatField()
    outz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField()
    outx = outValueX

    outValueY = FloatField()
    outy = outValueY

    outValueZ = FloatField()
    outz = outValueZ


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


class Input1PlugOperator(
    Float3CompoundBasePlugOperator["Input1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1X", "input1x"),
        ("input1Y", "input1y"),
        ("input1Z", "input1z"),
    )

    input1X = FloatField()
    input1x = input1X

    input1Y = FloatField()
    input1y = input1Y

    input1Z = FloatField()
    input1z = input1Z


class Input1AttrOperator(
    Float3CompoundBaseAttrOperator[Input1PlugOperator]
):
    __slots__ = ()

    input1X = FloatField()
    input1x = input1X

    input1Y = FloatField()
    input1y = input1Y

    input1Z = FloatField()
    input1z = input1Z


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1X = FloatField()
    input1x = input1X

    input1Y = FloatField()
    input1y = input1Y

    input1Z = FloatField()
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

    input2X = FloatField()
    input2x = input2X

    input2Y = FloatField()
    input2y = input2Y

    input2Z = FloatField()
    input2z = input2Z


class Input2AttrOperator(
    Float3CompoundBaseAttrOperator[Input2PlugOperator]
):
    __slots__ = ()

    input2X = FloatField()
    input2x = input2X

    input2Y = FloatField()
    input2y = input2Y

    input2Z = FloatField()
    input2z = input2Z


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2X = FloatField()
    input2x = input2X

    input2Y = FloatField()
    input2y = input2Y

    input2Z = FloatField()
    input2z = input2Z
