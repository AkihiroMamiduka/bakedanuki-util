# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
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

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class InputField(
    DoubleLinear3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ
