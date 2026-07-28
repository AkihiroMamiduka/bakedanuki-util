# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedCurveFromSurfaceCoS(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromSurfaceCoS"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    minValue = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    min = minValue

    maxValue = DoubleField(
        default_value=-1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    max = maxValue

    relative = BoolField(default_value=False)
    r = relative

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    curveOnSurface = DataNurbsCurveField()
    cos = curveOnSurface
