# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.old_tangent_constraint import (
    AimVectorField,
    ConstraintRotateField,
    TargetField,
    UpVectorField,
    WorldUpVectorField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField


class OldTangentConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "oldTangentConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    targetTranslateX = DoubleLinearField()
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField()
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField()
    ttz = targetTranslateZ

    targetRotatePivotX = DoubleLinearField()
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField()
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField()
    trpz = targetRotatePivotZ

    targetRotateTranslateX = DoubleLinearField()
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField()
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField()
    trtz = targetRotateTranslateZ

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    aimVector = AimVectorField(default_value=(1.0, 0.0, 0.0))
    a = aimVector
    aimVectorX = aimVector.aimVectorX
    ax = aimVectorX
    aimVectorY = aimVector.aimVectorY
    ay = aimVectorY
    aimVectorZ = aimVector.aimVectorZ
    az = aimVectorZ

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    u = upVector
    upVectorX = upVector.upVectorX
    ux = upVectorX
    upVectorY = upVector.upVectorY
    uy = upVectorY
    upVectorZ = upVector.upVectorZ
    uz = upVectorZ

    worldUpVector = WorldUpVectorField(default_value=(0.0, 1.0, 0.0))
    wu = worldUpVector
    worldUpVectorX = worldUpVector.worldUpVectorX
    wux = worldUpVectorX
    worldUpVectorY = worldUpVector.worldUpVectorY
    wuy = worldUpVectorY
    worldUpVectorZ = worldUpVector.worldUpVectorZ
    wuz = worldUpVectorZ

    constraintRotate = ConstraintRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate
    constraintRotateX = constraintRotate.constraintRotateX
    crx = constraintRotateX
    constraintRotateY = constraintRotate.constraintRotateY
    cry = constraintRotateY
    constraintRotateZ = constraintRotate.constraintRotateZ
    crz = constraintRotateZ
