# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.c_muscle_smart_constraint import (
    ConstrainDataField,
    OutDataField,
)


class CMuscleSmartConstraint(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleSmartConstraint"

    constrainData = ConstrainDataField()
    cdata = constrainData
    worldMatrixA = constrainData.worldMatrixA
    wma = worldMatrixA
    worldMatrixB = constrainData.worldMatrixB
    wmb = worldMatrixB
    worldMatrixABase = constrainData.worldMatrixABase
    wmab = worldMatrixABase
    worldMatrixBBase = constrainData.worldMatrixBBase
    wmbb = worldMatrixBBase
    axis = constrainData.axis
    ax = axis
    triggerMin = constrainData.triggerMin
    trgmin = triggerMin
    bias = constrainData.bias
    bis = bias
    biasAdjust = constrainData.biasAdjust
    bisadj = biasAdjust

    outData = OutDataField()
    odat = outData
    outTranslate = outData.outTranslate
    ot = outTranslate
    outRotate = outData.outRotate
    or_ = outRotate
    outTrigger = outData.outTrigger
    otrg = outTrigger
