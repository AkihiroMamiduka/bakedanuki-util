# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class Boundary(DG):
    __slots__ = ()

    NODE_TYPE = "boundary"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    inputCurve3 = DataNurbsCurveField()
    ic3 = inputCurve3

    inputCurve4 = DataNurbsCurveField()
    ic4 = inputCurve4

    endPointTolerance = DoubleLinearField()
    ept = endPointTolerance

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    order = BoolField()
    or_ = order

    endPoint = BoolField()
    ep = endPoint
