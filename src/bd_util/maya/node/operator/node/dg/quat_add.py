# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.quat_add import (
    Input1QuatField,
    Input2QuatField,
    OutputQuatField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class QuatAdd(DG):
    __slots__ = ()

    NODE_TYPE = "quatAdd"

    input1Quat = Input1QuatField()
    iq1 = input1Quat
    input1QuatX = input1Quat.input1QuatX
    i1x = input1QuatX
    input1QuatY = input1Quat.input1QuatY
    i1y = input1QuatY
    input1QuatZ = input1Quat.input1QuatZ
    i1z = input1QuatZ
    input1QuatW = input1Quat.input1QuatW
    i1w = input1QuatW

    input2Quat = Input2QuatField()
    iq2 = input2Quat
    input2QuatX = input2Quat.input2QuatX
    i2x = input2QuatX
    input2QuatY = input2Quat.input2QuatY
    i2y = input2QuatY
    input2QuatZ = input2Quat.input2QuatZ
    i2z = input2QuatZ
    input2QuatW = input2Quat.input2QuatW
    i2w = input2QuatW

    outputQuat = OutputQuatField()
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW

    input1QuatWDEPRECATED = DoubleField()
