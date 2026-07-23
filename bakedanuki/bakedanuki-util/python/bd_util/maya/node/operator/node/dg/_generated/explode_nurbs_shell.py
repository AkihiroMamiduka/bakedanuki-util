# coding: utf-8
from .._core import DG
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedExplodeNurbsShell(DG):
    __slots__ = ()

    NODE_TYPE = "explodeNurbsShell"

    inputShell = TypedField()
    ish = inputShell

    outputSurface = DataNurbsSurfaceField(multi=True, writable=False)
    os = outputSurface
