# coding: utf-8
from .._core import DG
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedCacheFile(DG):
    __slots__ = ()

    NODE_TYPE = "cacheFile"

    outCacheData = GenericField(multi=True)
    ocd = outCacheData

    outCacheArrayData = TypedField(writable=False)
    ocad = outCacheArrayData

    inRange = BoolField(default_value=True, writable=False)
    ir = inRange

    cacheName = DataStringField()
    cn = cacheName

    cachePath = DataStringField()
    cp = cachePath

    format = DataStringField()
    fmt = format

    channel = DataStringField(multi=True)
    ch = channel

    cacheWeights = DataDoubleArrayField()
    cw = cacheWeights

    perPtWeights = DataDoubleArrayField(multi=True)
    ppw = perPtWeights

    originalStart = TimeField(default_value=0.0)
    os = originalStart

    originalEnd = TimeField(default_value=0.0)
    oe = originalEnd

    sourceStart = TimeField(default_value=0.0)
    ss = sourceStart

    sourceEnd = TimeField(default_value=0.0)
    se = sourceEnd

    startFrame = TimeField(default_value=0.0)
    sf = startFrame

    scale = DoubleField(default_value=1.0, min_value=0.0)
    sc = scale

    hold = TimeField(default_value=0.0, min_value=0.0)
    h = hold

    preCycle = DoubleField(default_value=0.0, min_value=0.0)
    cb = preCycle

    postCycle = DoubleField(default_value=0.0, min_value=0.0)
    ca = postCycle

    start = TimeField(default_value=0.0, writable=False)
    st = start

    end = TimeField(default_value=0.0, writable=False)
    e = end

    time = TimeField(default_value=0.0)
    tim = time

    enable = BoolField(default_value=True)
    en = enable

    reverse = BoolField(default_value=False)
    rev = reverse

    oscillate = BoolField(default_value=False)
    osc = oscillate

    track = ShortField(default_value=0, min_value=0)
    tr = track

    trackState = ShortField(default_value=0, min_value=0)
    ts = trackState

    multiThread = BoolField(default_value=False)
    mt = multiThread

    memQueueSize = LongField(default_value=20)
    qs = memQueueSize

    displayLoadProgress = BoolField(default_value=True)
    dp = displayLoadProgress
