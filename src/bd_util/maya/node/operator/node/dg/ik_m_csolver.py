# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class IkMCsolver(DG):
    __slots__ = ()

    NODE_TYPE = "ikMCsolver"

    maxIterations = LongField()
    mxi = maxIterations

    tolerance = DoubleField()
    tol = tolerance
