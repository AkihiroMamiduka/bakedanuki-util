# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField


class Input1QuatPlugOperator(
    CompoundPlugOperator["Input1QuatAttrOperator"]
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
    CompoundAttrOperator[Input1QuatPlugOperator]
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
    CompoundField[Input1QuatAttrOperator, Input1QuatPlugOperator]
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
    CompoundPlugOperator["Input2QuatAttrOperator"]
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
    CompoundAttrOperator[Input2QuatPlugOperator]
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
    CompoundField[Input2QuatAttrOperator, Input2QuatPlugOperator]
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
    CompoundPlugOperator["OutputQuatAttrOperator"]
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
    CompoundAttrOperator[OutputQuatPlugOperator]
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
    CompoundField[OutputQuatAttrOperator, OutputQuatPlugOperator]
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
