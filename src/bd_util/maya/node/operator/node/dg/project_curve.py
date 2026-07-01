# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.project_curve import DirectionField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class ProjectCurve(DG):
    __slots__ = ()

    NODE_TYPE = "projectCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve

    direction = DirectionField()
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    tolerance = DoubleLinearField()
    tol = tolerance

    useNormal = BoolField()
    un = useNormal
