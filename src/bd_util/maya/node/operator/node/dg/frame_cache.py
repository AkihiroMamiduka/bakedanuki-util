# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class FrameCache(DG):
    __slots__ = ()

    NODE_TYPE = "frameCache"

    future = DoubleField(multi=True)
    f = future

    past = DoubleField(multi=True)
    p = past

    varying = DoubleField()
    v = varying

    varyTime = DoubleField()
    vt = varyTime

    stream = DoubleField()
    s = stream
