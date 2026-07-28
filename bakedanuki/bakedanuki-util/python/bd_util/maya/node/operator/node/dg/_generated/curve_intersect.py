# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.curve_intersect import DirectionField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedCurveIntersect(DG):
    __slots__ = ()

    NODE_TYPE = "curveIntersect"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    tolerance = DoubleLinearField(
        default_value=0.001, soft_min_value=0.0001, soft_max_value=1.0
    )
    tol = tolerance

    useDirection = BoolField(default_value=False)
    ud = useDirection

    direction = DirectionField(default_value=(0.0, 1.0, 0.0))
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    parameter1 = DoubleField(
        multi=True,
        default_value=123456.0,
        soft_min_value=-1.0,
        soft_max_value=1.0,
        writable=False,
    )
    p1 = parameter1

    parameter2 = DoubleField(
        multi=True,
        default_value=123456.0,
        soft_min_value=-1.0,
        soft_max_value=1.0,
        writable=False,
    )
    p2 = parameter2
