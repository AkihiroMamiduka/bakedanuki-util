# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class UniformFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "uniformFalloff"

    uniformWeight = DoubleLinearField(default_value=0.0)
    unw = uniformWeight

    outputWeightFunction = TypedField(writable=False)
    wft = outputWeightFunction
