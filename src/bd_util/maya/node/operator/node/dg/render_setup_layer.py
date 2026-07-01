# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class RenderSetupLayer(DG):
    __slots__ = ()

    NODE_TYPE = "renderSetupLayer"

    parentList = MessageField()
    pls = parentList

    next = MessageField()
    nxt = next

    previous = MessageField()
    prv = previous

    listItems = MessageField()
    lit = listItems

    containerLowest = MessageField()
    cl = containerLowest

    containerHighest = MessageField()
    ch = containerHighest

    legacyRenderLayer = MessageField()
    lrl = legacyRenderLayer

    numIsolatedChildren = LongField()
    nic = numIsolatedChildren
