# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.point_on_curve_info import ResultField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class PointOnCurveInfo(DG):
    __slots__ = ()

    NODE_TYPE = "pointOnCurveInfo"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    parameter = DoubleField(default_value=0.0)
    pr = parameter

    turnOnPercentage = BoolField(default_value=False)
    top = turnOnPercentage

    result = ResultField(writable=False)
    rs = result
    position = result.position
    p = position
    normal = result.normal
    n = normal
    normalizedNormal = result.normalizedNormal
    nn = normalizedNormal
    tangent = result.tangent
    t = tangent
    normalizedTangent = result.normalizedTangent
    nt = normalizedTangent
    curvatureCenter = result.curvatureCenter
    cc = curvatureCenter
    curvatureRadius = result.curvatureRadius
    cr = curvatureRadius
