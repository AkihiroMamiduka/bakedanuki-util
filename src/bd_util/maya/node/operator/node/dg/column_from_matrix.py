# coding: utf-8
from ._core import DG
from ...attr.define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.double4 import Double4Field
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class ColumnFromMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "columnFromMatrix"

    input = LongField()
    i = input

    matrix = MatrixField()
    m = matrix

    output = Double4Field()
    o = output
