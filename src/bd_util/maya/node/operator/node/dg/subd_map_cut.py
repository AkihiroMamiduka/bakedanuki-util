# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField


class SubdMapCut(DG):
    __slots__ = ()

    NODE_TYPE = "subdMapCut"

    outSubdiv = TypedField(writable=False)
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents
