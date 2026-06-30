# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.scale_from_matrix import OutputField
from ...attr.define.std.at.matrix import MatrixField


class ScaleFromMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "scaleFromMatrix"

    input = MatrixField()
    i = input

    output = OutputField()
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
