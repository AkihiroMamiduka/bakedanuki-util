# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.blend_matrix import TargetField
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBlendMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "blendMatrix"

    enable = BoolField(default_value=True)
    enb = enable

    envelope = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = envelope

    target = TargetField(multi=True)
    tgt = target

    preSpaceMatrix = MatrixField()
    premat = preSpaceMatrix

    postSpaceMatrix = MatrixField()
    pstmat = postSpaceMatrix

    inputMatrix = MatrixField()
    imat = inputMatrix

    outputMatrix = MatrixField(writable=False)
    omat = outputMatrix
