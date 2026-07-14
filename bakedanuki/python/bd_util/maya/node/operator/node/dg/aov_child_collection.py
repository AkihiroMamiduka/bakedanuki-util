# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class AovChildCollection(DG):
    __slots__ = ()

    NODE_TYPE = "aovChildCollection"

    parentList = MessageField()
    pls = parentList

    next = MessageField(writable=False)
    nxt = next

    previous = MessageField()
    prv = previous

    listItems = MessageField(writable=False)
    lit = listItems

    childLowest = MessageField()
    cl = childLowest

    childHighest = MessageField()
    ch = childHighest

    selfEnabled = BoolField(default_value=True)
    sen = selfEnabled

    parentEnabled = BoolField(default_value=True)
    pen = parentEnabled

    parentNumIsolatedChildren = LongField(default_value=0)
    pic = parentNumIsolatedChildren

    enabled = BoolField(default_value=True, writable=False)
    en = enabled

    numIsolatedChildren = LongField(default_value=0)
    nic = numIsolatedChildren

    numIsolatedAncestors = LongField(default_value=0)
    nia = numIsolatedAncestors

    isolateSelected = BoolField(default_value=False)
    is_ = isolateSelected

    selector = MessageField()
    sel = selector
