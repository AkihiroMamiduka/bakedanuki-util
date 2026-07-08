# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class IkSplineSolver(DG):
    __slots__ = ()

    NODE_TYPE = "ikSplineSolver"

    maxIterations = LongField(default_value=2147483647)
    mxi = maxIterations

    tolerance = DoubleField(default_value=1e-05)
    tol = tolerance
