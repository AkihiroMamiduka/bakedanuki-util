# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.skin_binding import FalloffCurveField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.matrix import DataMatrixField


class SkinBinding(DG):
    __slots__ = ()

    NODE_TYPE = "skinBinding"

    length = DoubleField(multi=True)
    l = length

    rightRadius = DoubleField(multi=True)
    rr = rightRadius

    leftRadius = DoubleField(multi=True)
    lr = leftRadius

    rightCap = DoubleField(multi=True)
    rc = rightCap

    leftCap = DoubleField(multi=True)
    lc = leftCap

    bindPreMatrix = DataMatrixField(multi=True)
    bpm = bindPreMatrix

    geomMatrix = DataMatrixField()
    gm = geomMatrix

    parentMatrix = DataMatrixField(multi=True)
    pm = parentMatrix

    localMatrix = DataMatrixField(multi=True)
    lm = localMatrix

    updateWeights = MessageField()
    uw = updateWeights

    outWeights = DataDoubleArrayField()
    otw = outWeights

    falloffCurve = FalloffCurveField(multi=True)
    fc = falloffCurve

    inputGeometry = TypedField()
    ig = inputGeometry

    currentInfluence = LongField()
    ci = currentInfluence
