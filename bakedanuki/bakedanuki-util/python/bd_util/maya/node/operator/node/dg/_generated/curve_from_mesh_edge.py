# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class _GeneratedCurveFromMeshEdge(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromMeshEdge"

    inputMesh = DataMeshField()
    im = inputMesh

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    edgeIndex = LongField(multi=True, default_value=0)
    ei = edgeIndex
