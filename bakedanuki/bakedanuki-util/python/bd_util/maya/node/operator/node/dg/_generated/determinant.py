# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedDeterminant(DG):
    __slots__ = ()

    NODE_TYPE = "determinant"

    input = MatrixField()
    i = input

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
