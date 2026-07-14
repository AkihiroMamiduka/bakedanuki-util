# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.subd_tweak import TweakField
from ...attr.define.std.at.typed import TypedField


class SubdTweak(DG):
    __slots__ = ()

    NODE_TYPE = "subdTweak"

    outSubdiv = TypedField(writable=False)
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    tweak = TweakField(multi=True, default_value=(0.0, 0.0, 0.0))
    tk = tweak

    map64BitIndices = TypedField()
    map = map64BitIndices
