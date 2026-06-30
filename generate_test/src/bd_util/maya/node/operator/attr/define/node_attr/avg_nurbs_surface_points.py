# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.dt.nurbs_surface import DataNurbsSurfaceField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class SurfacePointPlugOperator(
    CompoundPlugOperator["SurfacePointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputSurface", "is"),
        ("weight", "wt"),
        ("parameterU", "u"),
        ("parameterV", "v"),
        ("cvIthIndex", "ci"),
        ("cvJthIndex", "cj"),
    )

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    weight = DoubleField()
    wt = weight

    parameterU = DoubleField()
    u = parameterU

    parameterV = DoubleField()
    v = parameterV

    cvIthIndex = LongField()
    ci = cvIthIndex

    cvJthIndex = LongField()
    cj = cvJthIndex


class SurfacePointAttrOperator(
    CompoundAttrOperator[SurfacePointPlugOperator]
):
    __slots__ = ()

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    weight = DoubleField()
    wt = weight

    parameterU = DoubleField()
    u = parameterU

    parameterV = DoubleField()
    v = parameterV

    cvIthIndex = LongField()
    ci = cvIthIndex

    cvJthIndex = LongField()
    cj = cvJthIndex


class SurfacePointField(
    CompoundField[SurfacePointAttrOperator, SurfacePointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SurfacePointAttrOperator
    PLUG_CLS = SurfacePointPlugOperator


class ResultPlugOperator(
    CompoundPlugOperator["ResultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("normal", "n"),
    )

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal


class ResultAttrOperator(
    CompoundAttrOperator[ResultPlugOperator]
):
    __slots__ = ()

    position = Double3Field()
    p = position

    normal = Double3Field()
    n = normal


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
