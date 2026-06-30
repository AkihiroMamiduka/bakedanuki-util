# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double4_compound._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)


class Input1QuatPlugOperator(
    Double4CompoundBasePlugOperator["Input1QuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1QuatX", "i1x"),
        ("input1QuatY", "i1y"),
        ("input1QuatZ", "i1z"),
        ("input1QuatW", "i1w"),
    )

    input1QuatX = DoubleField()
    i1x = input1QuatX

    input1QuatY = DoubleField()
    i1y = input1QuatY

    input1QuatZ = DoubleField()
    i1z = input1QuatZ

    input1QuatW = DoubleField()
    i1w = input1QuatW


class Input1QuatAttrOperator(
    Double4CompoundBaseAttrOperator[Input1QuatPlugOperator]
):
    __slots__ = ()

    input1QuatX = DoubleField()
    i1x = input1QuatX

    input1QuatY = DoubleField()
    i1y = input1QuatY

    input1QuatZ = DoubleField()
    i1z = input1QuatZ

    input1QuatW = DoubleField()
    i1w = input1QuatW


class Input1QuatField(
    Double4CompoundBaseField[Input1QuatAttrOperator, Input1QuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1QuatAttrOperator
    PLUG_CLS = Input1QuatPlugOperator

    input1QuatX = DoubleField()
    i1x = input1QuatX

    input1QuatY = DoubleField()
    i1y = input1QuatY

    input1QuatZ = DoubleField()
    i1z = input1QuatZ

    input1QuatW = DoubleField()
    i1w = input1QuatW


class Input2QuatPlugOperator(
    Double4CompoundBasePlugOperator["Input2QuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2QuatX", "i2x"),
        ("input2QuatY", "i2y"),
        ("input2QuatZ", "i2z"),
        ("input2QuatW", "i2w"),
    )

    input2QuatX = DoubleField()
    i2x = input2QuatX

    input2QuatY = DoubleField()
    i2y = input2QuatY

    input2QuatZ = DoubleField()
    i2z = input2QuatZ

    input2QuatW = DoubleField()
    i2w = input2QuatW


class Input2QuatAttrOperator(
    Double4CompoundBaseAttrOperator[Input2QuatPlugOperator]
):
    __slots__ = ()

    input2QuatX = DoubleField()
    i2x = input2QuatX

    input2QuatY = DoubleField()
    i2y = input2QuatY

    input2QuatZ = DoubleField()
    i2z = input2QuatZ

    input2QuatW = DoubleField()
    i2w = input2QuatW


class Input2QuatField(
    Double4CompoundBaseField[Input2QuatAttrOperator, Input2QuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2QuatAttrOperator
    PLUG_CLS = Input2QuatPlugOperator

    input2QuatX = DoubleField()
    i2x = input2QuatX

    input2QuatY = DoubleField()
    i2y = input2QuatY

    input2QuatZ = DoubleField()
    i2z = input2QuatZ

    input2QuatW = DoubleField()
    i2w = input2QuatW


class OutputQuatPlugOperator(
    Double4CompoundBasePlugOperator["OutputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputQuatX", "oqx"),
        ("outputQuatY", "oqy"),
        ("outputQuatZ", "oqz"),
        ("outputQuatW", "oqw"),
    )

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW


class OutputQuatAttrOperator(
    Double4CompoundBaseAttrOperator[OutputQuatPlugOperator]
):
    __slots__ = ()

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW


class OutputQuatField(
    Double4CompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputQuatAttrOperator
    PLUG_CLS = OutputQuatPlugOperator

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW
