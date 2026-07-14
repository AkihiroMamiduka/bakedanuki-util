# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.least_squares_modifier import PointConstraintField
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


class LeastSquaresModifier(DG):
    __slots__ = ()

    NODE_TYPE = "leastSquaresModifier"

    inputNurbsObject = GenericField()
    ino = inputNurbsObject

    worldSpaceToObjectSpace = DataMatrixField()
    wto = worldSpaceToObjectSpace

    pointConstraint = PointConstraintField(multi=True)
    pc = pointConstraint

    pointPositionX = DoubleLinearField()
    ppx = pointPositionX

    pointPositionY = DoubleLinearField()
    ppy = pointPositionY

    pointPositionZ = DoubleLinearField()
    ppz = pointPositionZ

    pointConstraintU = DoubleField()
    pcu = pointConstraintU

    pointConstraintV = DoubleField()
    pcv = pointConstraintV

    pointConstraintW = DoubleField()
    pcw = pointConstraintW

    outputNurbsObject = GenericField(writable=False)
    ono = outputNurbsObject

    objectModifier = TypedField()
    om = objectModifier

    resetModifier = BoolField(default_value=True)
    rm = resetModifier

    updatePointModifier = BoolField(default_value=True)
    upm = updatePointModifier

    inputCache = GenericField()
    ipc = inputCache

    pointSymbolicIndex = TypedField()
    psi = pointSymbolicIndex
