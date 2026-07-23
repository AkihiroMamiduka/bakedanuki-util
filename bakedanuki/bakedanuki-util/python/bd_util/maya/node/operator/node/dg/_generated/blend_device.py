# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.double_array import DataDoubleArrayField


class _GeneratedBlendDevice(DG):
    __slots__ = ()

    NODE_TYPE = "blendDevice"

    input = DoubleField(multi=True, default_value=0.0)
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output

    current = LongField(default_value=0)
    c = current

    time = TimeField(default_value=0.0)
    t = time

    deviceValue = DoubleField(default_value=0.0)
    dv = deviceValue

    deviceBlender = FloatField(default_value=0.0)
    db = deviceBlender

    inputAngle = DoubleAngleField(multi=True, default_value=0.0)
    ia = inputAngle

    outputAngle = DoubleAngleField(default_value=0.0, writable=False)
    oa = outputAngle

    inputLinear = DoubleLinearField(multi=True, default_value=0.0)
    il = inputLinear

    outputLinear = DoubleLinearField(default_value=0.0, writable=False)
    ol = outputLinear

    blender = FloatField(default_value=1.0)
    b = blender

    minTime = DoubleField(default_value=0.0)
    mnt = minTime

    period = DoubleField(default_value=0.0)
    p = period

    timeStamp = DataDoubleArrayField()
    ts = timeStamp

    data = DataDoubleArrayField()
    d = data

    stride = LongField(default_value=1)
    st = stride

    offset = LongField(default_value=0, min_value=0)
    off = offset
