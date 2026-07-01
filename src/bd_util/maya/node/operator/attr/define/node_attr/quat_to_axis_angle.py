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


class InputQuatPlugOperator(
    QuatCompoundBasePlugOperator["InputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuatX", "iqx"),
        ("inputQuatY", "iqy"),
        ("inputQuatZ", "iqz"),
        ("inputQuatW", "iqw"),
    )

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class InputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[InputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class InputQuatField(
    QuatCompoundBaseField[InputQuatAttrOperator, InputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputQuatAttrOperator
    PLUG_CLS = InputQuatPlugOperator

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class OutputAxisPlugOperator(
    Double3CompoundBasePlugOperator["OutputAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputAxisX", "oax"),
        ("outputAxisY", "oay"),
        ("outputAxisZ", "oaz"),
    )

    outputAxisX = DoubleField()
    oax = outputAxisX

    outputAxisY = DoubleField()
    oay = outputAxisY

    outputAxisZ = DoubleField()
    oaz = outputAxisZ


class OutputAxisAttrOperator(
    Double3CompoundBaseAttrOperator[OutputAxisPlugOperator]
):
    __slots__ = ()

    outputAxisX = DoubleField()
    oax = outputAxisX

    outputAxisY = DoubleField()
    oay = outputAxisY

    outputAxisZ = DoubleField()
    oaz = outputAxisZ


class OutputAxisField(
    Double3CompoundBaseField[OutputAxisAttrOperator, OutputAxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAxisAttrOperator
    PLUG_CLS = OutputAxisPlugOperator

    outputAxisX = DoubleField()
    oax = outputAxisX

    outputAxisY = DoubleField()
    oay = outputAxisY

    outputAxisZ = DoubleField()
    oaz = outputAxisZ
