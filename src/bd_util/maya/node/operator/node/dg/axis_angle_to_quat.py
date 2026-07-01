# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.axis_angle_to_quat import (
    InputAxisField,
    OutputQuatField,
)
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class AxisAngleToQuat(DG):
    __slots__ = ()

    NODE_TYPE = "axisAngleToQuat"

    inputAxis = InputAxisField()
    ia = inputAxis
    inputAxisX = inputAxis.inputAxisX
    iax = inputAxisX
    inputAxisY = inputAxis.inputAxisY
    iay = inputAxisY
    inputAxisZ = inputAxis.inputAxisZ
    iaz = inputAxisZ

    inputAngle = DoubleAngleField()
    iang = inputAngle

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
