# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_decompose_twist import (
    AxisQuatField,
    InputQuatField,
)
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdQuatDecomposeTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_DecomposeTwist"

    inputQuat = InputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW

    axisQuat = AxisQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    aq = axisQuat
    axisQuatX = axisQuat.axisQuatX
    aqx = axisQuatX
    axisQuatY = axisQuat.axisQuatY
    aqy = axisQuatY
    axisQuatZ = axisQuat.axisQuatZ
    aqz = axisQuatZ
    axisQuatW = axisQuat.axisQuatW
    aqw = axisQuatW

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist
