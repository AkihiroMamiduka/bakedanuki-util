# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_project_curve import (
    CurvePointsField,
    DirectionField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class PolyProjectCurve(DG):
    __slots__ = ()

    NODE_TYPE = "polyProjectCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    inputMesh = DataMeshField()
    ims = inputMesh

    inputMatrix = DataMatrixField()
    imt = inputMatrix

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve

    pointsOnEdges = BoolField()
    poe = pointsOnEdges

    curveSamples = LongField()
    cs = curveSamples

    automatic = BoolField()
    as_ = automatic

    curvePoints = CurvePointsField(multi=True)
    cps = curvePoints

    # TODO: curvePoints.projectedPoint.baryCoord1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: curvePoints.projectedPoint.baryCoord2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: curvePoints.projectedPoint.baryCoord3 (attributeType=None, dataType=None) は未対応のため手動で追加してください

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
