# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.geometry_constraint import TargetField
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.matrix import DataMatrixField


class GeometryConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "geometryConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    constraintGeometry = GenericField(writable=False)
    cgm = constraintGeometry
