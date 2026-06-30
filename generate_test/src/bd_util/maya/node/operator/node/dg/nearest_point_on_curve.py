# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.nearest_point_on_curve import (
    InPositionField,
    ResultField,
)
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class NearestPointOnCurve(DG):
    __slots__ = ()

    NODE_TYPE = "nearestPointOnCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    inPosition = InPositionField()
    ip = inPosition
    inPositionX = inPosition.inPositionX
    ipx = inPositionX
    inPositionY = inPosition.inPositionY
    ipy = inPositionY
    inPositionZ = inPosition.inPositionZ
    ipz = inPositionZ

    result = ResultField()
    r = result
    position = result.position
    p = position
    parameter = result.parameter
    pr = parameter
