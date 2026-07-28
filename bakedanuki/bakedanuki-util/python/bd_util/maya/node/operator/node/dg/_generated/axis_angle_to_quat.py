# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.axis_angle_to_quat import (
    InputAxisField,
    OutputQuatField,
)
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedAxisAngleToQuat(DG):
    __slots__ = ()

    NODE_TYPE = "axisAngleToQuat"

    inputAxis = InputAxisField(default_value=(0.0, 0.0, 0.0))
    ia = inputAxis
    inputAxisX = inputAxis.inputAxisX
    iax = inputAxisX
    inputAxisY = inputAxis.inputAxisY
    iay = inputAxisY
    inputAxisZ = inputAxis.inputAxisZ
    iaz = inputAxisZ

    inputAngle = DoubleAngleField(default_value=0.0)
    iang = inputAngle

    outputQuat = OutputQuatField(
        default_value=(0.0, 0.0, 0.0, 0.0), writable=False
    )
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW
