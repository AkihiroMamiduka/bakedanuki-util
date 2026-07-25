# coding: utf-8
from .._core import DG
from ....attr.define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.double4 import Double4Field
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedColumnFromMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "columnFromMatrix"

    input = LongField(default_value=0, min_value=0, max_value=3, readable=False)
    i = input

    matrix = MatrixField(readable=False)
    m = matrix

    output = Double4Field(default_value=(0.0, 0.0, 0.0, 0.0), writable=False)
    o = output
