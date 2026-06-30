# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
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

    inPositionX = DoubleLinearField()
    ipx = inPositionX

    inPositionY = DoubleLinearField()
    ipy = inPositionY

    inPositionZ = DoubleLinearField()
    ipz = inPositionZ


class InPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InPositionPlugOperator]
):
    __slots__ = ()

    inPositionX = DoubleLinearField()
    ipx = inPositionX

    inPositionY = DoubleLinearField()
    ipy = inPositionY

    inPositionZ = DoubleLinearField()
    ipz = inPositionZ


class InPositionField(
    DoubleLinear3CompoundBaseField[InPositionAttrOperator, InPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InPositionAttrOperator
    PLUG_CLS = InPositionPlugOperator

    inPositionX = DoubleLinearField()
    ipx = inPositionX

    inPositionY = DoubleLinearField()
    ipy = inPositionY

    inPositionZ = DoubleLinearField()
    ipz = inPositionZ


class ResultPlugOperator(
    CompoundPlugOperator["ResultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("parameterU", "u"),
        ("parameterV", "v"),
        ("normal", "n"),
        ("closestFaceIndex", "f"),
        ("closestVertexIndex", "vt"),
    )

    position = Double3Field()
    p = position

    parameterU = DoubleField()
    u = parameterU

    parameterV = DoubleField()
    v = parameterV

    normal = Double3Field()
    n = normal

    closestFaceIndex = LongField()
    f = closestFaceIndex

    closestVertexIndex = LongField()
    vt = closestVertexIndex


class ResultAttrOperator(
    CompoundAttrOperator[ResultPlugOperator]
):
    __slots__ = ()

    position = Double3Field()
    p = position

    parameterU = DoubleField()
    u = parameterU

    parameterV = DoubleField()
    v = parameterV

    normal = Double3Field()
    n = normal

    closestFaceIndex = LongField()
    f = closestFaceIndex

    closestVertexIndex = LongField()
    vt = closestVertexIndex


class ResultField(
    CompoundField[ResultAttrOperator, ResultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field()
    p = position

    parameterU = DoubleField()
    u = parameterU

    parameterV = DoubleField()
    v = parameterV

    normal = Double3Field()
    n = normal

    closestFaceIndex = LongField()
    f = closestFaceIndex

    closestVertexIndex = LongField()
    vt = closestVertexIndex
