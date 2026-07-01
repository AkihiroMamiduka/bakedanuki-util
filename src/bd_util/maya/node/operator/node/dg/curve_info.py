# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.curve_info import ControlPointsField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class CurveInfo(DG):
    __slots__ = ()

    NODE_TYPE = "curveInfo"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    arcLength = DoubleLinearField()
    al = arcLength

    controlPoints = ControlPointsField(multi=True)
    cp = controlPoints

    weights = DoubleField(multi=True)
    wt = weights

    knots = DoubleField(multi=True)
    kn = knots
