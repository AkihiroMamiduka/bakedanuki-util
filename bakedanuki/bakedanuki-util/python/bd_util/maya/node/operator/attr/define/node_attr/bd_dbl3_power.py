# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class Input1PlugOperator(
    Double3CompoundBasePlugOperator["Input1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1X", "i1x"),
        ("input1Y", "i1y"),
        ("input1Z", "i1z"),
    )

    input1X = DoubleField(default_value=1.0)
    i1x = input1X

    input1Y = DoubleField(default_value=1.0)
    i1y = input1Y

    input1Z = DoubleField(default_value=1.0)
    i1z = input1Z


class Input1AttrOperator(Double3CompoundBaseAttrOperator[Input1PlugOperator]):
    __slots__ = ()

    input1X = DoubleField(default_value=1.0)
    i1x = input1X

    input1Y = DoubleField(default_value=1.0)
    i1y = input1Y

    input1Z = DoubleField(default_value=1.0)
    i1z = input1Z


class Input1Field(
    Double3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1X = DoubleField(default_value=1.0)
    i1x = input1X

    input1Y = DoubleField(default_value=1.0)
    i1y = input1Y

    input1Z = DoubleField(default_value=1.0)
    i1z = input1Z


class Input2PlugOperator(
    Double3CompoundBasePlugOperator["Input2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2X", "i2x"),
        ("input2Y", "i2y"),
        ("input2Z", "i2z"),
    )

    input2X = DoubleField(default_value=1.0)
    i2x = input2X

    input2Y = DoubleField(default_value=1.0)
    i2y = input2Y

    input2Z = DoubleField(default_value=1.0)
    i2z = input2Z


class Input2AttrOperator(Double3CompoundBaseAttrOperator[Input2PlugOperator]):
    __slots__ = ()

    input2X = DoubleField(default_value=1.0)
    i2x = input2X

    input2Y = DoubleField(default_value=1.0)
    i2y = input2Y

    input2Z = DoubleField(default_value=1.0)
    i2z = input2Z


class Input2Field(
    Double3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2X = DoubleField(default_value=1.0)
    i2x = input2X

    input2Y = DoubleField(default_value=1.0)
    i2y = input2Y

    input2Z = DoubleField(default_value=1.0)
    i2z = input2Z


class OutputPlugOperator(
    Double3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleField(default_value=1.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=1.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=1.0, writable=False)
    oz = outputZ


class OutputAttrOperator(Double3CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = DoubleField(default_value=1.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=1.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=1.0, writable=False)
    oz = outputZ


class OutputField(
    Double3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleField(default_value=1.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=1.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=1.0, writable=False)
    oz = outputZ
