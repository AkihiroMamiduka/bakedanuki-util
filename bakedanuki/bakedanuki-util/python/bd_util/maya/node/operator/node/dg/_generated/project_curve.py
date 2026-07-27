# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.project_curve import DirectionField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedProjectCurve(DG):
    __slots__ = ()

    NODE_TYPE = "projectCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputCurve = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurve

    direction = DirectionField(default_value=(0.0, 0.0, 1.0))
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    tolerance = DoubleLinearField(default_value=0.01, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    useNormal = BoolField(default_value=False)
    un = useNormal
