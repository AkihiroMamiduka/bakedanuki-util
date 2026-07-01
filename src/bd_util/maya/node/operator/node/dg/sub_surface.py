# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SubSurface(DG):
    __slots__ = ()

    NODE_TYPE = "subSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    firstFaceU = LongField()
    ffu = firstFaceU

    firstFaceV = LongField()
    ffv = firstFaceV

    faceCountU = LongField()
    fcu = faceCountU

    faceCountV = LongField()
    fcv = faceCountV

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
