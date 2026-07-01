# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class Audio(DG):
    __slots__ = ()

    NODE_TYPE = "audio"

    offset = TimeField()
    o = offset

    endFrame = TimeField()
    ef = endFrame

    silence = TimeField()
    si = silence

    sourceStart = TimeField()
    ss = sourceStart

    sourceEnd = TimeField()
    se = sourceEnd

    filename = DataStringField()
    f = filename

    order = LongField()
    r = order

    track = LongField()
    tk = track

    trackState = ShortField()
    ts = trackState

    frameCount = LongField()
    fc = frameCount

    channels = LongField()
    c = channels

    sampleRate = LongField()
    sr = sampleRate

    duration = TimeField()
    du = duration

    mute = BoolField()
    mu = mute
