# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.symmetry_constraint import (
    ConstrainedField,
    SymmetryMiddlePointField,
    SymmetryRootOffsetField,
    TargetField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.dt.matrix import DataMatrixField


class GeneratedSymmetryConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "symmetryConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField()
    tg = target
    targetTranslate = target.targetTranslate
    tt = targetTranslate
    targetRotate = target.targetRotate
    tr = targetRotate
    targetScale = target.targetScale
    ts = targetScale
    targetRotateOrder = target.targetRotateOrder
    tro = targetRotateOrder
    targetJointOrientType = target.targetJointOrientType
    tjt = targetJointOrientType
    targetJointOrient = target.targetJointOrient
    tjo = targetJointOrient
    targetChildTranslate = target.targetChildTranslate
    tct = targetChildTranslate
    targetWorldMatrix = target.targetWorldMatrix
    twm = targetWorldMatrix
    targetParentMatrix = target.targetParentMatrix
    tpm = targetParentMatrix

    constraintInverseParentWorldMatrix = DataMatrixField()
    cipm = constraintInverseParentWorldMatrix

    symmetryRootOffset = SymmetryRootOffsetField(default_value=(0.0, 0.0, 0.0))
    srof = symmetryRootOffset
    symmetryRootOffsetX = symmetryRootOffset.symmetryRootOffsetX
    srox = symmetryRootOffsetX
    symmetryRootOffsetY = symmetryRootOffset.symmetryRootOffsetY
    sroy = symmetryRootOffsetY
    symmetryRootOffsetZ = symmetryRootOffset.symmetryRootOffsetZ
    sroz = symmetryRootOffsetZ

    symmetryMiddlePoint = SymmetryMiddlePointField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cmwp = symmetryMiddlePoint
    symmetryMiddlePointX = symmetryMiddlePoint.symmetryMiddlePointX
    cmpx = symmetryMiddlePointX
    symmetryMiddlePointY = symmetryMiddlePoint.symmetryMiddlePointY
    cmpy = symmetryMiddlePointY
    symmetryMiddlePointZ = symmetryMiddlePoint.symmetryMiddlePointZ
    cmpz = symmetryMiddlePointZ

    xAxis = BoolField(default_value=True)
    syx = xAxis

    yAxis = BoolField(default_value=False)
    syy = yAxis

    zAxis = BoolField(default_value=False)
    syz = zAxis

    xChildAxis = BoolField(default_value=True)
    cyx = xChildAxis

    yChildAxis = BoolField(default_value=False)
    cyy = yChildAxis

    zChildAxis = BoolField(default_value=False)
    cyz = zChildAxis

    symmetryRootWorldMatrix = DataMatrixField()
    cpim = symmetryRootWorldMatrix

    constrained = ConstrainedField(writable=False)
    co = constrained
    constraintTranslate = constrained.constraintTranslate
    ct = constraintTranslate
    constraintRotateOrder = constrained.constraintRotateOrder
    cro = constraintRotateOrder
    constraintJointOrient = constrained.constraintJointOrient
    cjo = constraintJointOrient
    constraintRotate = constrained.constraintRotate
    cr = constraintRotate
    constraintScale = constrained.constraintScale
    cs = constraintScale
