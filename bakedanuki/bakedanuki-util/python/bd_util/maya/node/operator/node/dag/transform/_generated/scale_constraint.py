# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.scale_constraint import (
    ConstraintScaleField,
    OffsetField,
    RestScaleField,
    TargetField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.dt.matrix import DataMatrixField


class GeneratedScaleConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "scaleConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    constraintScaleCompensate = BoolField(default_value=False)
    tsc = constraintScaleCompensate

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    offset = OffsetField(default_value=(1.0, 1.0, 1.0))
    o = offset
    offsetX = offset.offsetX
    ox = offsetX
    offsetY = offset.offsetY
    oy = offsetY
    offsetZ = offset.offsetZ
    oz = offsetZ

    constraintScale = ConstraintScaleField(
        default_value=(1.0, 1.0, 1.0), writable=False
    )
    cs = constraintScale
    constraintScaleX = constraintScale.constraintScaleX
    csx = constraintScaleX
    constraintScaleY = constraintScale.constraintScaleY
    csy = constraintScaleY
    constraintScaleZ = constraintScale.constraintScaleZ
    csz = constraintScaleZ

    restScale = RestScaleField(default_value=(1.0, 1.0, 1.0), writable=False)
    rs = restScale
    restScaleX = restScale.restScaleX
    rsx = restScaleX
    restScaleY = restScale.restScaleY
    rsy = restScaleY
    restScaleZ = restScale.restScaleZ
    rsz = restScaleZ
