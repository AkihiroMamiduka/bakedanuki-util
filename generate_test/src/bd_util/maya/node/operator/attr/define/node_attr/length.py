# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleLinearField()
    ix = inputX

    inputY = DoubleLinearField()
    iy = inputY

    inputZ = DoubleLinearField()
    iz = inputZ


class InputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputX = DoubleLinearField()
    ix = inputX

    inputY = DoubleLinearField()
    iy = inputY

    inputZ = DoubleLinearField()
    iz = inputZ


class InputField(
    DoubleLinear3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleLinearField()
    ix = inputX

    inputY = DoubleLinearField()
    iy = inputY

    inputZ = DoubleLinearField()
    iz = inputZ
