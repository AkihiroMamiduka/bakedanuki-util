# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Input1PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Input1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1X", "i1x"),
        ("input1Y", "i1y"),
        ("input1Z", "i1z"),
    )

    input1X = DoubleLinearField()
    i1x = input1X

    input1Y = DoubleLinearField()
    i1y = input1Y

    input1Z = DoubleLinearField()
    i1z = input1Z


class Input1AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Input1PlugOperator]
):
    __slots__ = ()

    input1X = DoubleLinearField()
    i1x = input1X

    input1Y = DoubleLinearField()
    i1y = input1Y

    input1Z = DoubleLinearField()
    i1z = input1Z


class Input1Field(
    DoubleLinear3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1X = DoubleLinearField()
    i1x = input1X

    input1Y = DoubleLinearField()
    i1y = input1Y

    input1Z = DoubleLinearField()
    i1z = input1Z


class Input2PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Input2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2X", "i2x"),
        ("input2Y", "i2y"),
        ("input2Z", "i2z"),
    )

    input2X = DoubleLinearField()
    i2x = input2X

    input2Y = DoubleLinearField()
    i2y = input2Y

    input2Z = DoubleLinearField()
    i2z = input2Z


class Input2AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Input2PlugOperator]
):
    __slots__ = ()

    input2X = DoubleLinearField()
    i2x = input2X

    input2Y = DoubleLinearField()
    i2y = input2Y

    input2Z = DoubleLinearField()
    i2z = input2Z


class Input2Field(
    DoubleLinear3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2X = DoubleLinearField()
    i2x = input2X

    input2Y = DoubleLinearField()
    i2y = input2Y

    input2Z = DoubleLinearField()
    i2z = input2Z
