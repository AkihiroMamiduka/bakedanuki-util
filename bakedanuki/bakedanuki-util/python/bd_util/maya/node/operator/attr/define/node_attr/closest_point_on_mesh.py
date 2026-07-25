# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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
    DoubleLinear3CompoundBaseField[InPositionAttrOperator, InPositionPlugOperator]
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

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    parameterU = DoubleField(default_value=0.0, writable=False)
    u = parameterU

    parameterV = DoubleField(default_value=0.0, writable=False)
    v = parameterV

    normal = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    n = normal

    closestFaceIndex = LongField(default_value=-1, writable=False)
    f = closestFaceIndex

    closestVertexIndex = LongField(default_value=-1, writable=False)
    vt = closestVertexIndex


class ResultAttrOperator(
    CompoundAttrOperator[ResultPlugOperator]
):
    __slots__ = ()

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    parameterU = DoubleField(default_value=0.0, writable=False)
    u = parameterU

    parameterV = DoubleField(default_value=0.0, writable=False)
    v = parameterV

    normal = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    n = normal

    closestFaceIndex = LongField(default_value=-1, writable=False)
    f = closestFaceIndex

    closestVertexIndex = LongField(default_value=-1, writable=False)
    vt = closestVertexIndex


class ResultField(
    CompoundField[ResultAttrOperator, ResultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    parameterU = DoubleField(default_value=0.0, writable=False)
    u = parameterU

    parameterV = DoubleField(default_value=0.0, writable=False)
    v = parameterV

    normal = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    n = normal

    closestFaceIndex = LongField(default_value=-1, writable=False)
    f = closestFaceIndex

    closestVertexIndex = LongField(default_value=-1, writable=False)
    vt = closestVertexIndex
