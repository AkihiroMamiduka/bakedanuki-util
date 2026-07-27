# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.mesh import DataMeshField


class GeneratedCreatePtexUV(DG):
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
