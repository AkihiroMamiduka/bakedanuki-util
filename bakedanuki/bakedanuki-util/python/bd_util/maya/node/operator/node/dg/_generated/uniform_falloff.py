# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField


class _GeneratedUniformFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "uniformFalloff"

    uniformWeight = DoubleLinearField(default_value=0.0)
    unw = uniformWeight

    outputWeightFunction = TypedField(writable=False)
    wft = outputWeightFunction
