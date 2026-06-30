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

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    creasing = DoubleLinearField()
    cr = creasing

    rounding = DoubleLinearField()
    ro = rounding

    lengthIn = DoubleLinearField()
    li = lengthIn

    lengthOut = DoubleLinearField()
    lo = lengthOut

    widthLeft = DoubleLinearField()
    wl = widthLeft

    widthRight = DoubleLinearField()
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

    adjustedUpperBaseLatticeMatrix = MatrixField()
    au = adjustedUpperBaseLatticeMatrix

    adjustedLowerBaseLatticeMatrix = MatrixField()
    al = adjustedLowerBaseLatticeMatrix

    bendVector = BendVectorField()
    bv = bendVector
    bendVectorX = bendVector.bendVectorX
    bx = bendVectorX
    bendVectorY = bendVector.bendVectorY
    by = bendVectorY
    bendVectorZ = bendVector.bendVectorZ
    bz = bendVectorZ

    bendMagnitude = DoubleLinearField()
    bm = bendMagnitude
