# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedSubSurface(DG):
    __slots__ = ()

    NODE_TYPE = "subSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    firstFaceU = LongField(default_value=0, min_value=0, soft_min_value=0)
    ffu = firstFaceU

    firstFaceV = LongField(default_value=0, min_value=0, soft_min_value=0)
    ffv = firstFaceV

    faceCountU = LongField(default_value=1, min_value=1, soft_min_value=1)
    fcu = faceCountU

    faceCountV = LongField(default_value=1, min_value=1, soft_min_value=1)
    fcv = faceCountV

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
