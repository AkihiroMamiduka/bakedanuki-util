# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class CurveFromSurfaceBnd(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromSurfaceBnd"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    minValue = DoubleField()
    min = minValue

    maxValue = DoubleField()
    max = maxValue

    relative = BoolField()
    r = relative

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    face = LongField()
    f = face

    boundary = LongField()
    b = boundary

    edge = LongField()
    e = edge
