# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.point_matrix_mult import (
    InPointField,
    OutputField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class PointMatrixMult(DG):
    __slots__ = ()

    NODE_TYPE = "pointMatrixMult"

    inPoint = InPointField()
    ip = inPoint
    inPointX = inPoint.inPointX
    ipx = inPointX
    inPointY = inPoint.inPointY
    ipy = inPointY
    inPointZ = inPoint.inPointZ
    ipz = inPointZ

    inMatrix = MatrixField()
    im = inMatrix

    vectorMultiply = BoolField()
    vm = vectorMultiply

    output = OutputField()
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
