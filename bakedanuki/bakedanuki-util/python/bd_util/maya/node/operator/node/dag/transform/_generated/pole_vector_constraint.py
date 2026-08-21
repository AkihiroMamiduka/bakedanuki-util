# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.pole_vector_constraint import (
    ConstraintRotatePivotField,
    ConstraintRotateTranslateField,
    ConstraintTranslateField,
    OffsetField,
    RestTranslateField,
    TargetField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.dt.matrix import DataMatrixField


class GeneratedPoleVectorConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "poleVectorConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    constraintRotatePivot = ConstraintRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    crp = constraintRotatePivot
    constraintRotatePivotX = constraintRotatePivot.constraintRotatePivotX
    crpx = constraintRotatePivotX
    constraintRotatePivotY = constraintRotatePivot.constraintRotatePivotY
    crpy = constraintRotatePivotY
    constraintRotatePivotZ = constraintRotatePivot.constraintRotatePivotZ
    crpz = constraintRotatePivotZ

    constraintRotateTranslate = ConstraintRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    crt = constraintRotateTranslate
    constraintRotateTranslateX = (
        constraintRotateTranslate.constraintRotateTranslateX
    )
    crtx = constraintRotateTranslateX
    constraintRotateTranslateY = (
        constraintRotateTranslate.constraintRotateTranslateY
    )
    crty = constraintRotateTranslateY
    constraintRotateTranslateZ = (
        constraintRotateTranslate.constraintRotateTranslateZ
    )
    crtz = constraintRotateTranslateZ

    offset = OffsetField(default_value=(0.0, 0.0, 0.0))
    o = offset
    offsetX = offset.offsetX
    ox = offsetX
    offsetY = offset.offsetY
    oy = offsetY
    offsetZ = offset.offsetZ
    oz = offsetZ

    constraintOffsetPolarity = DoubleField(default_value=1.0)
    cop = constraintOffsetPolarity

    constraintTranslate = ConstraintTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ct = constraintTranslate
    constraintTranslateX = constraintTranslate.constraintTranslateX
    ctx = constraintTranslateX
    constraintTranslateY = constraintTranslate.constraintTranslateY
    cty = constraintTranslateY
    constraintTranslateZ = constraintTranslate.constraintTranslateZ
    ctz = constraintTranslateZ

    restTranslate = RestTranslateField(default_value=(0.0, 0.0, 0.0))
    rst = restTranslate
    restTranslateX = restTranslate.restTranslateX
    rtx = restTranslateX
    restTranslateY = restTranslate.restTranslateY
    rty = restTranslateY
    restTranslateZ = restTranslate.restTranslateZ
    rtz = restTranslateZ

    pivotSpace = DataMatrixField()
    ps = pivotSpace
