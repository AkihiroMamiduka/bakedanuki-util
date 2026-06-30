# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class ComputeNodeColorPlugOperator(
    Double3CompoundBasePlugOperator["ComputeNodeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("computeNodeColorR", "cncr"),
        ("computeNodeColorG", "cncg"),
        ("computeNodeColorB", "cncb"),
    )

    computeNodeColorR = DoubleField()
    cncr = computeNodeColorR

    computeNodeColorG = DoubleField()
    cncg = computeNodeColorG

    computeNodeColorB = DoubleField()
    cncb = computeNodeColorB


class ComputeNodeColorAttrOperator(
    Double3CompoundBaseAttrOperator[ComputeNodeColorPlugOperator]
):
    __slots__ = ()

    computeNodeColorR = DoubleField()
    cncr = computeNodeColorR

    computeNodeColorG = DoubleField()
    cncg = computeNodeColorG

    computeNodeColorB = DoubleField()
    cncb = computeNodeColorB


class ComputeNodeColorField(
    Double3CompoundBaseField[ComputeNodeColorAttrOperator, ComputeNodeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComputeNodeColorAttrOperator
    PLUG_CLS = ComputeNodeColorPlugOperator

    computeNodeColorR = DoubleField()
    cncr = computeNodeColorR

    computeNodeColorG = DoubleField()
    cncg = computeNodeColorG

    computeNodeColorB = DoubleField()
    cncb = computeNodeColorB
