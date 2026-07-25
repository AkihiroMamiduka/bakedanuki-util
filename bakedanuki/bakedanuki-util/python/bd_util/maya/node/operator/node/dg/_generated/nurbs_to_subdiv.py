# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedNurbsToSubdiv(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsToSubdiv"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputSubd = TypedField(writable=False)
    os = outputSubd

    maxPolyCount = LongField(default_value=1000, min_value=1, max_value=100000)
    mpc = maxPolyCount

    reverseNormal = BoolField(default_value=True)
    rn = reverseNormal

    matchPeriodic = BoolField(default_value=False)
    mp = matchPeriodic

    collapsePoles = BoolField(default_value=False)
    cp = collapsePoles
