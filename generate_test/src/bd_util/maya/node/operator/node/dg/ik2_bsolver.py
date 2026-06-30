# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class Ik2Bsolver(DG):
    __slots__ = ()

    NODE_TYPE = "ik2Bsolver"

    maxIterations = LongField()
    mxi = maxIterations

    tolerance = DoubleField()
    tol = tolerance
