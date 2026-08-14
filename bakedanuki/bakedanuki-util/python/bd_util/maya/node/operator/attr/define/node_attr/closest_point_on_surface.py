# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double3Field,
)


class InPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inPositionX", "ipx"),
        ("inPositionY", "ipy"),
        ("inPositionZ", "ipz"),
    )

    inPositionX = DoubleLinearField(default_value=0.0)
    ipx = inPositionX

    inPositionY = DoubleLinearField(default_value=0.0)
    ipy = inPositionY

    inPositionZ = DoubleLinearField(default_value=0.0)
    ipz = inPositionZ


class InPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InPositionPlugOperator]
):
    __slots__ = ()

    inPositionX = DoubleLinearField(default_value=0.0)
    ipx = inPositionX

    inPositionY = DoubleLinearField(default_value=0.0)
    ipy = inPositionY

    inPositionZ = DoubleLinearField(default_value=0.0)
    ipz = inPositionZ


class InPositionField(
    DoubleLinear3CompoundBaseField[
        InPositionAttrOperator, InPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InPositionAttrOperator
    PLUG_CLS = InPositionPlugOperator

    inPositionX = DoubleLinearField(default_value=0.0)
    ipx = inPositionX

    inPositionY = DoubleLinearField(default_value=0.0)
    ipy = inPositionY

    inPositionZ = DoubleLinearField(default_value=0.0)
    ipz = inPositionZ


class ResultPlugOperator(CompoundPlugOperator["ResultAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("parameterU", "u"),
        ("parameterV", "v"),
    )

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    parameterU = DoubleField(default_value=0.0, writable=False)
    u = parameterU

    parameterV = DoubleField(default_value=0.0, writable=False)
    v = parameterV


class ResultAttrOperator(CompoundAttrOperator[ResultPlugOperator]):
    __slots__ = ()

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    parameterU = DoubleField(default_value=0.0, writable=False)
    u = parameterU

    parameterV = DoubleField(default_value=0.0, writable=False)
    v = parameterV


class ResultField(CompoundField[ResultAttrOperator, ResultPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    parameterU = DoubleField(default_value=0.0, writable=False)
    u = parameterU

    parameterV = DoubleField(default_value=0.0, writable=False)
    v = parameterV
