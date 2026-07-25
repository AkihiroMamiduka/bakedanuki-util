# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
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

    computeNodeColorR = DoubleField(default_value=0.0)
    cncr = computeNodeColorR

    computeNodeColorG = DoubleField(default_value=0.0)
    cncg = computeNodeColorG

    computeNodeColorB = DoubleField(default_value=0.0)
    cncb = computeNodeColorB


class ComputeNodeColorAttrOperator(
    Double3CompoundBaseAttrOperator[ComputeNodeColorPlugOperator]
):
    __slots__ = ()

    computeNodeColorR = DoubleField(default_value=0.0)
    cncr = computeNodeColorR

    computeNodeColorG = DoubleField(default_value=0.0)
    cncg = computeNodeColorG

    computeNodeColorB = DoubleField(default_value=0.0)
    cncb = computeNodeColorB


class ComputeNodeColorField(
    Double3CompoundBaseField[ComputeNodeColorAttrOperator, ComputeNodeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComputeNodeColorAttrOperator
    PLUG_CLS = ComputeNodeColorPlugOperator

    computeNodeColorR = DoubleField(default_value=0.0)
    cncr = computeNodeColorR

    computeNodeColorG = DoubleField(default_value=0.0)
    cncg = computeNodeColorG

    computeNodeColorB = DoubleField(default_value=0.0)
    cncb = computeNodeColorB
