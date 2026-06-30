# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.old_geometry_constraint import (
    InputField,
    ObjectRotPivotField,
    ObjectRotTransField,
    OutputField,
)
from ...attr.define.std.at.generic import GenericField


class OldGeometryConstraint(DG):
    __slots__ = ()

    NODE_TYPE = "oldGeometryConstraint"

    input = InputField(multi=True)
    i = input

    # TODO: input.inputTransX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputTransY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputTransZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputRotPivotX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputRotPivotY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputRotPivotZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputRotTransX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputRotTransY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inputRotTransZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    geometry = GenericField()
    g = geometry

    parentInverseMatrix = GenericField()
    pim = parentInverseMatrix

    objectRotPivot = ObjectRotPivotField()
    orp = objectRotPivot
    objectRotPivotX = objectRotPivot.objectRotPivotX
    orpx = objectRotPivotX
    objectRotPivotY = objectRotPivot.objectRotPivotY
    orpy = objectRotPivotY
    objectRotPivotZ = objectRotPivot.objectRotPivotZ
    orpz = objectRotPivotZ

    objectRotTrans = ObjectRotTransField()
    ort = objectRotTrans
    objectRotTransX = objectRotTrans.objectRotTransX
    ortx = objectRotTransX
    objectRotTransY = objectRotTrans.objectRotTransY
    orty = objectRotTransY
    objectRotTransZ = objectRotTrans.objectRotTransZ
    ortz = objectRotTransZ

    output = OutputField()
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
