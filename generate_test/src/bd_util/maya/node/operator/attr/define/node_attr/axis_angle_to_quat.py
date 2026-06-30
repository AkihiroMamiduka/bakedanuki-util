# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound._base import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class InputAxisPlugOperator(
    Double3CompoundBasePlugOperator["InputAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputAxisX", "iax"),
        ("inputAxisY", "iay"),
        ("inputAxisZ", "iaz"),
    )

    inputAxisX = DoubleField()
    iax = inputAxisX

    inputAxisY = DoubleField()
    iay = inputAxisY

    inputAxisZ = DoubleField()
    iaz = inputAxisZ


class InputAxisAttrOperator(
    Double3CompoundBaseAttrOperator[InputAxisPlugOperator]
):
    __slots__ = ()

    inputAxisX = DoubleField()
    iax = inputAxisX

    inputAxisY = DoubleField()
    iay = inputAxisY

    inputAxisZ = DoubleField()
    iaz = inputAxisZ


class InputAxisField(
    Double3CompoundBaseField[InputAxisAttrOperator, InputAxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAxisAttrOperator
    PLUG_CLS = InputAxisPlugOperator

    inputAxisX = DoubleField()
    iax = inputAxisX

    inputAxisY = DoubleField()
    iay = inputAxisY

    inputAxisZ = DoubleField()
    iaz = inputAxisZ


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

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW


class OutputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[OutputQuatPlugOperator]
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
    QuatCompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
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
