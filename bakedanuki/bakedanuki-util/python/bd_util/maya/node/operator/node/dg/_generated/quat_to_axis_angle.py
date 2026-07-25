# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.quat_to_axis_angle import (
    InputQuatField,
    OutputAxisField,
)
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField


class _GeneratedQuatToAxisAngle(DG):
    __slots__ = ()

    NODE_TYPE = "quatToAxisAngle"

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

    outputAxis = OutputAxisField(default_value=(0.0, 0.0, 0.0), writable=False)
    oa = outputAxis
    outputAxisX = outputAxis.outputAxisX
    oax = outputAxisX
    outputAxisY = outputAxis.outputAxisY
    oay = outputAxisY
    outputAxisZ = outputAxis.outputAxisZ
    oaz = outputAxisZ

    outputAngle = DoubleAngleField(default_value=0.0, writable=False)
    oang = outputAngle
