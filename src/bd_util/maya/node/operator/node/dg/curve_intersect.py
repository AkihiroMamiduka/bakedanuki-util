# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.curve_intersect import DirectionField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class CurveIntersect(DG):
    __slots__ = ()

    NODE_TYPE = "curveIntersect"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    tolerance = DoubleLinearField()
    tol = tolerance

    useDirection = BoolField()
    ud = useDirection

    direction = DirectionField()
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    parameter1 = DoubleField(multi=True)
    p1 = parameter1

    parameter2 = DoubleField(multi=True)
    p2 = parameter2
