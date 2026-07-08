# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.old_geometry_constraint import (
    InputField,
    ObjectRotPivotField,
    ObjectRotTransField,
    OutputField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class OldGeometryConstraint(DG):
    __slots__ = ()

    NODE_TYPE = "oldGeometryConstraint"

    input = InputField(multi=True)
    i = input

    inputTransX = DoubleLinearField()
    itx = inputTransX

    inputTransY = DoubleLinearField()
    ity = inputTransY

    inputTransZ = DoubleLinearField()
    itz = inputTransZ

    inputRotPivotX = DoubleLinearField()
    irpx = inputRotPivotX

    inputRotPivotY = DoubleLinearField()
    irpy = inputRotPivotY

    inputRotPivotZ = DoubleLinearField()
    irpz = inputRotPivotZ

    inputRotTransX = DoubleLinearField()
    irtx = inputRotTransX

    inputRotTransY = DoubleLinearField()
    irty = inputRotTransY

    inputRotTransZ = DoubleLinearField()
    irtz = inputRotTransZ

    geometry = GenericField()
    g = geometry

    parentInverseMatrix = GenericField()
    pim = parentInverseMatrix

    objectRotPivot = ObjectRotPivotField(default_value=(0.0, 0.0, 0.0))
    orp = objectRotPivot
    objectRotPivotX = objectRotPivot.objectRotPivotX
    orpx = objectRotPivotX
    objectRotPivotY = objectRotPivot.objectRotPivotY
    orpy = objectRotPivotY
    objectRotPivotZ = objectRotPivot.objectRotPivotZ
    orpz = objectRotPivotZ

    objectRotTrans = ObjectRotTransField(default_value=(0.0, 0.0, 0.0))
    ort = objectRotTrans
    objectRotTransX = objectRotTrans.objectRotTransX
    ortx = objectRotTransX
    objectRotTransY = objectRotTrans.objectRotTransY
    orty = objectRotTransY
    objectRotTransZ = objectRotTrans.objectRotTransZ
    ortz = objectRotTransZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
