# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.joint_lattice import (
    BendVectorField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class JointLattice(DG):
    __slots__ = ()

    NODE_TYPE = "jointLattice"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    creasing = DoubleLinearField(default_value=0.0, soft_min_value=-20.0, soft_max_value=80.0)
    cr = creasing

    rounding = DoubleLinearField(default_value=0.0, soft_min_value=-20.0, soft_max_value=80.0)
    ro = rounding

    lengthIn = DoubleLinearField(default_value=0.0, soft_min_value=-20.0, soft_max_value=80.0)
    li = lengthIn

    lengthOut = DoubleLinearField(default_value=0.0, soft_min_value=-20.0, soft_max_value=80.0)
    lo = lengthOut

    widthLeft = DoubleLinearField(default_value=0.0, soft_min_value=-20.0, soft_max_value=80.0)
    wl = widthLeft

    widthRight = DoubleLinearField(default_value=0.0, soft_min_value=-20.0, soft_max_value=80.0)
    wr = widthRight

    upperMatrix = MatrixField()
    um = upperMatrix

    lowerMatrix = MatrixField()
    lm = lowerMatrix

    initialUpperMatrix = MatrixField()
    iu = initialUpperMatrix

    initialLowerMatrix = MatrixField()
    il = initialLowerMatrix

    deformedLatticeMatrix = MatrixField()
    md = deformedLatticeMatrix

    baseLatticeMatrix = MatrixField()
    mb = baseLatticeMatrix

    adjustedUpperBaseLatticeMatrix = MatrixField(writable=False)
    au = adjustedUpperBaseLatticeMatrix

    adjustedLowerBaseLatticeMatrix = MatrixField(writable=False)
    al = adjustedLowerBaseLatticeMatrix

    bendVector = BendVectorField(default_value=(0.0, 0.0, 0.0))
    bv = bendVector
    bendVectorX = bendVector.bendVectorX
    bx = bendVectorX
    bendVectorY = bendVector.bendVectorY
    by = bendVectorY
    bendVectorZ = bendVector.bendVectorZ
    bz = bendVectorZ

    bendMagnitude = DoubleLinearField(default_value=0.0)
    bm = bendMagnitude
