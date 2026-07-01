# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class IntersectSurface(DG):
    __slots__ = ()

    NODE_TYPE = "intersectSurface"

    inputSurface1 = DataNurbsSurfaceField()
    is1 = inputSurface1

    inputSurface2 = DataNurbsSurfaceField()
    is2 = inputSurface2

    curveOnSurface1 = DataNurbsCurveField(multi=True)
    cs1 = curveOnSurface1

    curveOnSurface2 = DataNurbsCurveField(multi=True)
    cs2 = curveOnSurface2

    output3dCurve = DataNurbsCurveField(multi=True)
    oc = output3dCurve

    tolerance = DoubleLinearField()
    tol = tolerance
