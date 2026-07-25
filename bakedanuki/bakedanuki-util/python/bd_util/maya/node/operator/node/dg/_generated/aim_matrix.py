# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.aim_matrix import (
    PrimaryField,
    SecondaryField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class _GeneratedAimMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "aimMatrix"

    enable = BoolField(default_value=True)
    enb = enable

    envelope = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = envelope

    inputMatrix = MatrixField()
    imat = inputMatrix

    primary = PrimaryField()
    pm = primary
    primaryInputAxis = primary.primaryInputAxis
    pmi = primaryInputAxis
    primaryMode = primary.primaryMode
    prmd = primaryMode
    primaryTargetVector = primary.primaryTargetVector
    pmiv = primaryTargetVector
    primaryTargetMatrix = primary.primaryTargetMatrix
    pmat = primaryTargetMatrix

    secondary = SecondaryField()
    sc = secondary
    secondaryInputAxis = secondary.secondaryInputAxis
    smi = secondaryInputAxis
    secondaryMode = secondary.secondaryMode
    sm = secondaryMode
    secondaryTargetVector = secondary.secondaryTargetVector
    smiv = secondaryTargetVector
    secondaryTargetMatrix = secondary.secondaryTargetMatrix
    smat = secondaryTargetMatrix

    preSpaceMatrix = MatrixField()
    premat = preSpaceMatrix

    postSpaceMatrix = MatrixField()
    pstmat = postSpaceMatrix

    outputMatrix = MatrixField(writable=False)
    tmat = outputMatrix
