# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class ConnectionUniqueOverride(DG):
    __slots__ = ()

    NODE_TYPE = "connectionUniqueOverride"

    parentList = MessageField()
    pls = parentList

    next = MessageField(writable=False)
    nxt = next

    previous = MessageField()
    prv = previous

    selfEnabled = BoolField(default_value=True)
    sen = selfEnabled

    parentEnabled = BoolField(default_value=True)
    pen = parentEnabled

    parentNumIsolatedChildren = LongField(default_value=0)
    pic = parentNumIsolatedChildren

    enabled = BoolField(default_value=True, writable=False)
    en = enabled

    attribute = DataStringField()
    atr = attribute

    localRender = BoolField(default_value=False)
    local = localRender

    connectionStr = DataStringField()
    cs = connectionStr

    targetNodeName = DataStringField()
    tgName = targetNodeName
