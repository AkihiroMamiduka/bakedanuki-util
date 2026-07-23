# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedCreatePtexUV(DG):
    __slots__ = ()

    NODE_TYPE = "createPtexUV"

    inMesh = DataMeshField()
    im = inMesh

    outMesh = DataMeshField(writable=False)
    om = outMesh

    bleed = LongField(default_value=10)
    bl = bleed

    tileCount = LongField(default_value=1)
    tc = tileCount
