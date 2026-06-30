# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.least_squares_modifier import PointConstraintField
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
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

    # TODO: pointConstraint.pointPositionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: pointConstraint.pointPositionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: pointConstraint.pointPositionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: pointConstraint.pointConstraintU (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: pointConstraint.pointConstraintV (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: pointConstraint.pointConstraintW (attributeType=None, dataType=None) は未対応のため手動で追加してください

    outputNurbsObject = GenericField()
    ono = outputNurbsObject

    objectModifier = TypedField()
    om = objectModifier

    resetModifier = BoolField()
    rm = resetModifier

    updatePointModifier = BoolField()
    upm = updatePointModifier

    inputCache = GenericField()
    ipc = inputCache

    pointSymbolicIndex = TypedField()
    psi = pointSymbolicIndex
