# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.blend_matrix import TargetField
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class BlendMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "blendMatrix"

    enable = BoolField()
    enb = enable

    envelope = DoubleField()
    env = envelope

    target = TargetField(multi=True)
    tgt = target

    preSpaceMatrix = MatrixField()
    premat = preSpaceMatrix

    postSpaceMatrix = MatrixField()
    pstmat = postSpaceMatrix

    inputMatrix = MatrixField()
    imat = inputMatrix

    outputMatrix = MatrixField()
    omat = outputMatrix
