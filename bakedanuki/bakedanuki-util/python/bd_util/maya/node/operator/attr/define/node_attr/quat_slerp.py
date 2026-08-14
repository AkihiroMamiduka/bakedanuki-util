# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class Input1QuatPlugOperator(
    QuatCompoundBasePlugOperator["Input1QuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1QuatX", "i1x"),
        ("input1QuatY", "i1y"),
        ("input1QuatZ", "i1z"),
        ("input1QuatW", "i1w"),
    )

    input1QuatX = DoubleField(default_value=0.0)
    i1x = input1QuatX

    input1QuatY = DoubleField(default_value=0.0)
    i1y = input1QuatY

    input1QuatZ = DoubleField(default_value=0.0)
    i1z = input1QuatZ

    input1QuatW = DoubleField(default_value=1.0)
    i1w = input1QuatW


class Input1QuatAttrOperator(
    QuatCompoundBaseAttrOperator[Input1QuatPlugOperator]
):
    __slots__ = ()

    input1QuatX = DoubleField(default_value=0.0)
    i1x = input1QuatX

    input1QuatY = DoubleField(default_value=0.0)
    i1y = input1QuatY

    input1QuatZ = DoubleField(default_value=0.0)
    i1z = input1QuatZ

    input1QuatW = DoubleField(default_value=1.0)
    i1w = input1QuatW


class Input1QuatField(
    QuatCompoundBaseField[Input1QuatAttrOperator, Input1QuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1QuatAttrOperator
    PLUG_CLS = Input1QuatPlugOperator

    input1QuatX = DoubleField(default_value=0.0)
    i1x = input1QuatX

    input1QuatY = DoubleField(default_value=0.0)
    i1y = input1QuatY

    input1QuatZ = DoubleField(default_value=0.0)
    i1z = input1QuatZ

    input1QuatW = DoubleField(default_value=1.0)
    i1w = input1QuatW


class Input2QuatPlugOperator(
    QuatCompoundBasePlugOperator["Input2QuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2QuatX", "i2x"),
        ("input2QuatY", "i2y"),
        ("input2QuatZ", "i2z"),
        ("input2QuatW", "i2w"),
    )

    input2QuatX = DoubleField(default_value=0.0)
    i2x = input2QuatX

    input2QuatY = DoubleField(default_value=0.0)
    i2y = input2QuatY

    input2QuatZ = DoubleField(default_value=0.0)
    i2z = input2QuatZ

    input2QuatW = DoubleField(default_value=1.0)
    i2w = input2QuatW


class Input2QuatAttrOperator(
    QuatCompoundBaseAttrOperator[Input2QuatPlugOperator]
):
    __slots__ = ()

    input2QuatX = DoubleField(default_value=0.0)
    i2x = input2QuatX

    input2QuatY = DoubleField(default_value=0.0)
    i2y = input2QuatY

    input2QuatZ = DoubleField(default_value=0.0)
    i2z = input2QuatZ

    input2QuatW = DoubleField(default_value=1.0)
    i2w = input2QuatW


class Input2QuatField(
    QuatCompoundBaseField[Input2QuatAttrOperator, Input2QuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2QuatAttrOperator
    PLUG_CLS = Input2QuatPlugOperator

    input2QuatX = DoubleField(default_value=0.0)
    i2x = input2QuatX

    input2QuatY = DoubleField(default_value=0.0)
    i2y = input2QuatY

    input2QuatZ = DoubleField(default_value=0.0)
    i2z = input2QuatZ

    input2QuatW = DoubleField(default_value=1.0)
    i2w = input2QuatW


class OutputQuatPlugOperator(
    QuatCompoundBasePlugOperator["OutputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputQuatX", "oqx"),
        ("outputQuatY", "oqy"),
        ("outputQuatZ", "oqz"),
        ("outputQuatW", "oqw"),
    )

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW


class OutputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[OutputQuatPlugOperator]
):
    __slots__ = ()

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW


class OutputQuatField(
    QuatCompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputQuatAttrOperator
    PLUG_CLS = OutputQuatPlugOperator

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW
