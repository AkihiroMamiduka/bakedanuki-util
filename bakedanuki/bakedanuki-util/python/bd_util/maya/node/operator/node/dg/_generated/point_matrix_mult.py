# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.point_matrix_mult import (
    InPointField,
    OutputField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField


class GeneratedPointMatrixMult(DG):
    __slots__ = ()

    NODE_TYPE = "pointMatrixMult"

    inPoint = InPointField(default_value=(0.0, 0.0, 0.0), readable=False)
    ip = inPoint
    inPointX = inPoint.inPointX
    ipx = inPointX
    inPointY = inPoint.inPointY
    ipy = inPointY
    inPointZ = inPoint.inPointZ
    ipz = inPointZ

    inMatrix = MatrixField(readable=False)
    im = inMatrix

    vectorMultiply = BoolField(default_value=False, readable=False)
    vm = vectorMultiply

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
