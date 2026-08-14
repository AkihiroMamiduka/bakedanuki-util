# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.skin_binding import FalloffCurveField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.matrix import DataMatrixField


class GeneratedSkinBinding(DG):
    __slots__ = ()

    NODE_TYPE = "skinBinding"

    length = DoubleField(multi=True, default_value=0.0)
    l = length

    rightRadius = DoubleField(multi=True, default_value=0.0)
    rr = rightRadius

    leftRadius = DoubleField(multi=True, default_value=0.0)
    lr = leftRadius

    rightCap = DoubleField(multi=True, default_value=1.0)
    rc = rightCap

    leftCap = DoubleField(multi=True, default_value=1.0)
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

    falloffCurve = FalloffCurveField(multi=True, default_value=(0.0, 0.0, 0.0))
    fc = falloffCurve

    inputGeometry = TypedField()
    ig = inputGeometry

    currentInfluence = LongField(default_value=0)
    ci = currentInfluence
