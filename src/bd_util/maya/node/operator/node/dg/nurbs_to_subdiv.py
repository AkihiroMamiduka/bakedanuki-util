# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class NurbsToSubdiv(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsToSubdiv"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputSubd = TypedField()
    os = outputSubd

    maxPolyCount = LongField()
    mpc = maxPolyCount

    reverseNormal = BoolField()
    rn = reverseNormal

    matchPeriodic = BoolField()
    mp = matchPeriodic

    collapsePoles = BoolField()
    cp = collapsePoles
