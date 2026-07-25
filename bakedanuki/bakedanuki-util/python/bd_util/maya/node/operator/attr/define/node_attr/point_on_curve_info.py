# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class ResultPlugOperator(
    CompoundPlugOperator["ResultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("normal", "n"),
        ("normalizedNormal", "nn"),
        ("tangent", "t"),
        ("normalizedTangent", "nt"),
        ("curvatureCenter", "cc"),
        ("curvatureRadius", "cr"),
    )

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal

    normalizedNormal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    nn = normalizedNormal

    tangent = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    t = tangent

    normalizedTangent = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    nt = normalizedTangent

    curvatureCenter = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cc = curvatureCenter

    curvatureRadius = DoubleLinearField(default_value=1.0, writable=False)
    cr = curvatureRadius


class ResultAttrOperator(
    CompoundAttrOperator[ResultPlugOperator]
):
    __slots__ = ()

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal

    normalizedNormal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    nn = normalizedNormal

    tangent = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    t = tangent

    normalizedTangent = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    nt = normalizedTangent

    curvatureCenter = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cc = curvatureCenter

    curvatureRadius = DoubleLinearField(default_value=1.0, writable=False)
    cr = curvatureRadius


class ResultField(
    CompoundField[ResultAttrOperator, ResultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal

    normalizedNormal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    nn = normalizedNormal

    tangent = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    t = tangent

    normalizedTangent = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    nt = normalizedTangent

    curvatureCenter = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cc = curvatureCenter

    curvatureRadius = DoubleLinearField(default_value=1.0, writable=False)
    cr = curvatureRadius
