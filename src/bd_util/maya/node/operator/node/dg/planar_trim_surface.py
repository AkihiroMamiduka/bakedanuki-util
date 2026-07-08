# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class DegreeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3


class DegreeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3

    NAME_MAP = {
        LINEAR: "Linear",
        CUBIC: "Cubic",
    }


class DegreeEnumField(
    EnumField[DegreeEnumAttrOperator, DegreeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeEnumAttrOperator
    PLUG_CLS = DegreeEnumPlugOperator


class PlanarTrimSurface(DG):
    __slots__ = ()

    NODE_TYPE = "planarTrimSurface"

    inputCurve = DataNurbsCurveField(multi=True)
    ic = inputCurve

    degree = DegreeEnumField(default_value=3)
    d = degree

    keepOutside = BoolField(default_value=False)
    ko = keepOutside

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    tolerance = DoubleLinearField(default_value=0.01, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance
