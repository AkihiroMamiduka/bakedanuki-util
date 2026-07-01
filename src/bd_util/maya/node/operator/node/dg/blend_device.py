# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.double_array import DataDoubleArrayField


class BlendDevice(DG):
    __slots__ = ()

    NODE_TYPE = "blendDevice"

    input = DoubleField(multi=True)
    i = input

    output = DoubleField()
    o = output

    current = LongField()
    c = current

    time = TimeField()
    t = time

    deviceValue = DoubleField()
    dv = deviceValue

    deviceBlender = FloatField()
    db = deviceBlender

    inputAngle = DoubleAngleField(multi=True)
    ia = inputAngle

    outputAngle = DoubleAngleField()
    oa = outputAngle

    inputLinear = DoubleLinearField(multi=True)
    il = inputLinear

    outputLinear = DoubleLinearField()
    ol = outputLinear

    blender = FloatField()
    b = blender

    minTime = DoubleField()
    mnt = minTime

    period = DoubleField()
    p = period

    timeStamp = DataDoubleArrayField()
    ts = timeStamp

    data = DataDoubleArrayField()
    d = data

    stride = LongField()
    st = stride

    offset = LongField()
    off = offset
