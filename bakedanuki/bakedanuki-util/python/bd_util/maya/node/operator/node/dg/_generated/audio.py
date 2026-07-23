# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAudio(DG):
    __slots__ = ()

    NODE_TYPE = "audio"

    offset = TimeField(default_value=0.0)
    o = offset

    endFrame = TimeField(default_value=0.0)
    ef = endFrame

    silence = TimeField(default_value=0.0, min_value=0.0)
    si = silence

    sourceStart = TimeField(default_value=0.0, min_value=0.0)
    ss = sourceStart

    sourceEnd = TimeField(default_value=0.0)
    se = sourceEnd

    filename = DataStringField()
    f = filename

    order = LongField(default_value=1, min_value=1)
    r = order

    track = LongField(default_value=1, min_value=1)
    tk = track

    trackState = ShortField(default_value=0, min_value=0)
    ts = trackState

    frameCount = LongField(default_value=0, writable=False)
    fc = frameCount

    channels = LongField(default_value=0, writable=False)
    c = channels

    sampleRate = LongField(default_value=0, writable=False)
    sr = sampleRate

    duration = TimeField(default_value=0.0, writable=False)
    du = duration

    mute = BoolField(default_value=False)
    mu = mute
