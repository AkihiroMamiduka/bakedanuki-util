# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputRotateX", "irx"),
        ("inputRotateY", "iry"),
        ("inputRotateZ", "irz"),
    )

    inputRotateX = DoubleAngleField()
    irx = inputRotateX

    inputRotateY = DoubleAngleField()
    iry = inputRotateY

    inputRotateZ = DoubleAngleField()
    irz = inputRotateZ


class InputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputRotatePlugOperator]
):
    __slots__ = ()

    inputRotateX = DoubleAngleField()
    irx = inputRotateX

    inputRotateY = DoubleAngleField()
    iry = inputRotateY

    inputRotateZ = DoubleAngleField()
    irz = inputRotateZ


class InputRotateField(
    DoubleAngle3CompoundBaseField[InputRotateAttrOperator, InputRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputRotateAttrOperator
    PLUG_CLS = InputRotatePlugOperator

    inputRotateX = DoubleAngleField()
    irx = inputRotateX

    inputRotateY = DoubleAngleField()
    iry = inputRotateY

    inputRotateZ = DoubleAngleField()
    irz = inputRotateZ


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
