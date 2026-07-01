# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.mesh import DataMeshField


class CreatePtexUV(DG):
    __slots__ = ()

    NODE_TYPE = "createPtexUV"

    inMesh = DataMeshField()
    im = inMesh

    outMesh = DataMeshField()
    om = outMesh

    bleed = LongField()
    bl = bleed

    tileCount = LongField()
    tc = tileCount
