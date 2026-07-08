# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.parent_matrix import TargetField
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class ParentMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "parentMatrix"

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
