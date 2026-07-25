# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
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

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[InputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatField(
    QuatCompoundBaseField[InputQuatAttrOperator, InputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputQuatAttrOperator
    PLUG_CLS = InputQuatPlugOperator

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
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

    outputAxisX = DoubleField(default_value=0.0, writable=False)
    oax = outputAxisX

    outputAxisY = DoubleField(default_value=0.0, writable=False)
    oay = outputAxisY

    outputAxisZ = DoubleField(default_value=0.0, writable=False)
    oaz = outputAxisZ


class OutputAxisAttrOperator(
    Double3CompoundBaseAttrOperator[OutputAxisPlugOperator]
):
    __slots__ = ()

    outputAxisX = DoubleField(default_value=0.0, writable=False)
    oax = outputAxisX

    outputAxisY = DoubleField(default_value=0.0, writable=False)
    oay = outputAxisY

    outputAxisZ = DoubleField(default_value=0.0, writable=False)
    oaz = outputAxisZ


class OutputAxisField(
    Double3CompoundBaseField[OutputAxisAttrOperator, OutputAxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAxisAttrOperator
    PLUG_CLS = OutputAxisPlugOperator

    outputAxisX = DoubleField(default_value=0.0, writable=False)
    oax = outputAxisX

    outputAxisY = DoubleField(default_value=0.0, writable=False)
    oay = outputAxisY

    outputAxisZ = DoubleField(default_value=0.0, writable=False)
    oaz = outputAxisZ
