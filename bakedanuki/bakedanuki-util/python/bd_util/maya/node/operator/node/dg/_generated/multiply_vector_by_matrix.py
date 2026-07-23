# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.multiply_vector_by_matrix import (
    InputField,
    OutputField,
)
from ....attr.define.std.at.matrix import MatrixField


class _GeneratedMultiplyVectorByMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "multiplyVectorByMatrix"

    input = InputField(default_value=(0.0, 0.0, 0.0), readable=False)
    i = input
    inputX = input.inputX
    x = inputX
    inputY = input.inputY
    y = inputY
    inputZ = input.inputZ
    z = inputZ

    matrix = MatrixField(readable=False)
    m = matrix

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
