# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal

    normalizedNormal = Double3Field()
    nn = normalizedNormal

    tangent = Double3Field()
    t = tangent

    normalizedTangent = Double3Field()
    nt = normalizedTangent

    curvatureCenter = Double3Field()
    cc = curvatureCenter

    curvatureRadius = DoubleLinearField()
    cr = curvatureRadius


class ResultAttrOperator(
    CompoundAttrOperator[ResultPlugOperator]
):
    __slots__ = ()

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal

    normalizedNormal = Double3Field()
    nn = normalizedNormal

    tangent = Double3Field()
    t = tangent

    normalizedTangent = Double3Field()
    nt = normalizedTangent

    curvatureCenter = Double3Field()
    cc = curvatureCenter

    curvatureRadius = DoubleLinearField()
    cr = curvatureRadius


class ResultField(
    CompoundField[ResultAttrOperator, ResultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal

    normalizedNormal = Double3Field()
    nn = normalizedNormal

    tangent = Double3Field()
    t = tangent

    normalizedTangent = Double3Field()
    nt = normalizedTangent

    curvatureCenter = Double3Field()
    cc = curvatureCenter

    curvatureRadius = DoubleLinearField()
    cr = curvatureRadius
