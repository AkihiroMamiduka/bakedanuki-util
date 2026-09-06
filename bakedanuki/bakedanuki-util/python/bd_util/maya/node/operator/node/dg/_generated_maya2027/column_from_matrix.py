# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.column_from_matrix import OutputField
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedColumnFromMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "columnFromMatrix"

    input = LongField(
        default_value=0, min_value=0, max_value=3, readable=False
    )
    i = input

    matrix = MatrixField(readable=False)
    m = matrix

    output = OutputField(default_value=(0.0, 0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
    outputW = output.outputW
    ow = outputW
