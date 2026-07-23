# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class _GeneratedDeterminant(DG):
    __slots__ = ()

    NODE_TYPE = "determinant"

    input = MatrixField()
    i = input

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
