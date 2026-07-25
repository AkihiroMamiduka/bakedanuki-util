# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class _GeneratedFrameCache(DG):
    __slots__ = ()

    NODE_TYPE = "frameCache"

    future = DoubleField(multi=True, default_value=0.0, writable=False)
    f = future

    past = DoubleField(multi=True, default_value=0.0, writable=False)
    p = past

    varying = DoubleField(default_value=0.0, writable=False)
    v = varying

    varyTime = DoubleField(default_value=0.0)
    vt = varyTime

    stream = DoubleField(default_value=0.0)
    s = stream
