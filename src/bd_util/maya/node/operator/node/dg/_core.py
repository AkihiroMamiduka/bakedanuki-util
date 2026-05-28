# coding: utf-8

# self
from .._core import Node
from ...attr.at.bool import BoolAttr
from ...attr.at.byte import ByteAttr
from ...attr.at.enum import EnumAttr, EnumPlug
from ...attr.at.message import MessageAttr
from ...attr.dt.string import DataStringAttr


class NodeStateEnumPlug(EnumPlug):
    NORMAL = 0
    HAS_NO_EFFECT = 1
    BLOCKING = 2
    WAITING_NORMAL = 8
    WAITING_HAS_NO_EFFECT = 9
    WAITING_BLOCKING = 10


class NodeStateEnumAttr(EnumAttr):
    PLUG_CLS = NodeStateEnumPlug

    NORMAL = 0
    HAS_NO_EFFECT = 1
    BLOCKING = 2
    WAITING_NORMAL = 8
    WAITING_HAS_NO_EFFECT = 9
    WAITING_BLOCKING = 10

    NAME_MAP = {
        NORMAL: "Normal",
        HAS_NO_EFFECT: "HasNoEffect",
        BLOCKING: "Blocking",
        WAITING_NORMAL: "Waiting-Normal",
        WAITING_HAS_NO_EFFECT: "Waiting-HasNoEffect",
        WAITING_BLOCKING: "Waiting-Blocking",
    }


class DG(Node):
    __slots__ = ()

    message = MessageAttr()
    msg = message
    caching = BoolAttr()
    cch = caching
    frozen = BoolAttr()
    fzn = frozen
    isHistoricallyInteresting = ByteAttr()
    ihi = isHistoricallyInteresting
    nodeState = NodeStateEnumAttr()
    nds = nodeState
    binMembership = DataStringAttr()
    bnm = binMembership
