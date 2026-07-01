# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.rotation_from_matrix import OutputField
from ...attr.define.std.at.matrix import MatrixField


class RotationFromMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "rotationFromMatrix"

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
