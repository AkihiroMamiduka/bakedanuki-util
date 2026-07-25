# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedBoundary(DG):
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

    endPointTolerance = DoubleLinearField(default_value=0.1, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    ept = endPointTolerance

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    order = BoolField(default_value=True)
    or_ = order

    endPoint = BoolField(default_value=False)
    ep = endPoint
