# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class CoordinatePlugOperator(
    Double2CompoundBasePlugOperator["CoordinateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coordinateU", "cu"),
        ("coordinateV", "cv"),
    )

    coordinateU = DoubleField()
    cu = coordinateU

    coordinateV = DoubleField()
    cv = coordinateV


class CoordinateAttrOperator(
    Double2CompoundBaseAttrOperator[CoordinatePlugOperator]
):
    __slots__ = ()

    coordinateU = DoubleField()
    cu = coordinateU

    coordinateV = DoubleField()
    cv = coordinateV


class CoordinateField(
    Double2CompoundBaseField[CoordinateAttrOperator, CoordinatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordinateAttrOperator
    PLUG_CLS = CoordinatePlugOperator


class OutputTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputTranslateX", "otx"),
        ("outputTranslateY", "oty"),
        ("outputTranslateZ", "otz"),
    )

    outputTranslateX = DoubleLinearField()
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField()
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField()
    otz = outputTranslateZ


class OutputTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputTranslatePlugOperator]
):
    __slots__ = ()

    outputTranslateX = DoubleLinearField()
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField()
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField()
    otz = outputTranslateZ


class OutputTranslateField(
    DoubleLinear3CompoundBaseField[OutputTranslateAttrOperator, OutputTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputTranslateAttrOperator
    PLUG_CLS = OutputTranslatePlugOperator
