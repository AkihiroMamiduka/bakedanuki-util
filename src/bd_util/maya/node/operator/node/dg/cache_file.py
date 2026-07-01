# coding: utf-8
from ._core import DG
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.string import DataStringField


class CacheFile(DG):
    __slots__ = ()

    NODE_TYPE = "cacheFile"

    outCacheData = GenericField(multi=True)
    ocd = outCacheData

    outCacheArrayData = TypedField()
    ocad = outCacheArrayData

    inRange = BoolField()
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

    originalStart = TimeField()
    os = originalStart

    originalEnd = TimeField()
    oe = originalEnd

    sourceStart = TimeField()
    ss = sourceStart

    sourceEnd = TimeField()
    se = sourceEnd

    startFrame = TimeField()
    sf = startFrame

    scale = DoubleField()
    sc = scale

    hold = TimeField()
    h = hold

    preCycle = DoubleField()
    cb = preCycle

    postCycle = DoubleField()
    ca = postCycle

    start = TimeField()
    st = start

    end = TimeField()
    e = end

    time = TimeField()
    tim = time

    enable = BoolField()
    en = enable

    reverse = BoolField()
    rev = reverse

    oscillate = BoolField()
    osc = oscillate

    track = ShortField()
    tr = track

    trackState = ShortField()
    ts = trackState

    multiThread = BoolField()
    mt = multiThread

    memQueueSize = LongField()
    qs = memQueueSize

    displayLoadProgress = BoolField()
    dp = displayLoadProgress
