# coding: utf-8
from .._core import DG
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedCurveFromMeshCoM(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromMeshCoM"

    inputMesh = DataMeshField()
    im = inputMesh

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    curveOnMesh = DataNurbsCurveField()
    com = curveOnMesh
