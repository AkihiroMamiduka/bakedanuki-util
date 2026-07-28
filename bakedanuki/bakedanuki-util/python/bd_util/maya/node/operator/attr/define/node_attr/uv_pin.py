# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    coordinateU = DoubleField(default_value=0.0, readable=False)
    cu = coordinateU

    coordinateV = DoubleField(default_value=0.0, readable=False)
    cv = coordinateV


class CoordinateAttrOperator(
    Double2CompoundBaseAttrOperator[CoordinatePlugOperator]
):
    __slots__ = ()

    coordinateU = DoubleField(default_value=0.0, readable=False)
    cu = coordinateU

    coordinateV = DoubleField(default_value=0.0, readable=False)
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

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputTranslatePlugOperator]
):
    __slots__ = ()

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputTranslateField(
    DoubleLinear3CompoundBaseField[
        OutputTranslateAttrOperator, OutputTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputTranslateAttrOperator
    PLUG_CLS = OutputTranslatePlugOperator
