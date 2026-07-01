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
        ("inputX", "x"),
        ("inputY", "y"),
        ("inputZ", "z"),
    )

    inputX = DoubleLinearField()
    x = inputX

    inputY = DoubleLinearField()
    y = inputY

    inputZ = DoubleLinearField()
    z = inputZ


class InputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputX = DoubleLinearField()
    x = inputX

    inputY = DoubleLinearField()
    y = inputY

    inputZ = DoubleLinearField()
    z = inputZ


class InputField(
    DoubleLinear3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleLinearField()
    x = inputX

    inputY = DoubleLinearField()
    y = inputY

    inputZ = DoubleLinearField()
    z = inputZ


class OutputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ


class OutputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ


class OutputField(
    DoubleLinear3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ
