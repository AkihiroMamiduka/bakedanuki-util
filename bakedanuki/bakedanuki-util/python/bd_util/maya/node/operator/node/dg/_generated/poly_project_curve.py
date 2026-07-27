# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_project_curve import (
    CurvePointsField,
    DirectionField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedPolyProjectCurve(DG):
    __slots__ = ()

    NODE_TYPE = "polyProjectCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    inputMesh = DataMeshField()
    ims = inputMesh

    inputMatrix = DataMatrixField()
    imt = inputMatrix

    outputCurve = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurve

    pointsOnEdges = BoolField(default_value=False)
    poe = pointsOnEdges

    curveSamples = LongField(default_value=50, min_value=2)
    cs = curveSamples

    automatic = BoolField(default_value=True)
    as_ = automatic

    curvePoints = CurvePointsField(multi=True)
    cps = curvePoints

    baryCoord1 = DoubleLinearField()
    bc1 = baryCoord1

    baryCoord2 = DoubleLinearField()
    bc2 = baryCoord2

    baryCoord3 = DoubleLinearField()
    bc3 = baryCoord3

    direction = DirectionField(default_value=(0.0, 0.0, 1.0))
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    tolerance = DoubleLinearField(default_value=0.0001, min_value=1e-05, max_value=1.0)
    tol = tolerance
