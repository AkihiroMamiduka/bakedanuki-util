# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.old_normal_constraint import (
    AimVectorField,
    ConstraintRotateField,
    TargetField,
    UpVectorField,
    WorldUpVectorField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.dt.matrix import DataMatrixField


class GeneratedOldNormalConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "oldNormalConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

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

    constraintRotate = ConstraintRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cr = constraintRotate
    constraintRotateX = constraintRotate.constraintRotateX
    crx = constraintRotateX
    constraintRotateY = constraintRotate.constraintRotateY
    cry = constraintRotateY
    constraintRotateZ = constraintRotate.constraintRotateZ
    crz = constraintRotateZ
