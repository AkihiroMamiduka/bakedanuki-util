# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class Group(DG):
    __slots__ = ()

    NODE_TYPE = "group"

    parentList = MessageField()
    pls = parentList

    next = MessageField()
    nxt = next

    previous = MessageField()
    prv = previous

    listItems = MessageField()
    lit = listItems

    childLowest = MessageField()
    cl = childLowest

    childHighest = MessageField()
    ch = childHighest

    selfEnabled = BoolField()
    sen = selfEnabled

    parentEnabled = BoolField()
    pen = parentEnabled

    parentNumIsolatedChildren = LongField()
    pic = parentNumIsolatedChildren

    enabled = BoolField()
    en = enabled

    numIsolatedChildren = LongField()
    nic = numIsolatedChildren

    numIsolatedAncestors = LongField()
    nia = numIsolatedAncestors

    isolateSelected = BoolField()
    is_ = isolateSelected
