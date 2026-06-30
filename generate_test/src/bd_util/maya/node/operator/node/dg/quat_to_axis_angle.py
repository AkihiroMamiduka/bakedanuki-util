# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.quat_to_axis_angle import (
    InputQuatField,
    OutputAxisField,
)
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class QuatToAxisAngle(DG):
    __slots__ = ()

    NODE_TYPE = "quatToAxisAngle"

    inputQuat = InputQuatField()
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW

    outputAxis = OutputAxisField()
    oa = outputAxis
    outputAxisX = outputAxis.outputAxisX
    oax = outputAxisX
    outputAxisY = outputAxis.outputAxisY
    oay = outputAxisY
    outputAxisZ = outputAxis.outputAxisZ
    oaz = outputAxisZ

    outputAngle = DoubleAngleField()
    oang = outputAngle
