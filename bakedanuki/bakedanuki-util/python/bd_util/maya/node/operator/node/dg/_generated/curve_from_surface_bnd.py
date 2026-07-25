# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedCurveFromSurfaceBnd(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromSurfaceBnd"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    minValue = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    min = minValue

    maxValue = DoubleField(default_value=-1.0, soft_min_value=0.0, soft_max_value=1.0)
    max = maxValue

    relative = BoolField(default_value=False)
    r = relative

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    face = LongField(default_value=0, min_value=1, soft_max_value=4)
    f = face

    boundary = LongField(default_value=0, min_value=1, soft_max_value=4)
    b = boundary

    edge = LongField(default_value=-1, min_value=-1, soft_max_value=10)
    e = edge
