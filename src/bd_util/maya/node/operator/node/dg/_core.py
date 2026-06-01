# coding: utf-8

# self
from .._core import NodeOperator
from ...attr.at.bool import BoolAttrOperator
from ...attr.at.byte import ByteAttrOperator
from ...attr.at.enum import EnumAttrOperator, EnumPlugOperator
from ...attr.at.message import MessageAttrOperator
from ...attr.dt.string import DataStringAttrOperator


class NodeStateEnumPlug(EnumPlugOperator):
    NORMAL = 0
    HAS_NO_EFFECT = 1
    BLOCKING = 2
    WAITING_NORMAL = 8
    WAITING_HAS_NO_EFFECT = 9
    WAITING_BLOCKING = 10


class NodeStateEnumAttr(EnumAttrOperator):
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


class DG(NodeOperator):
    __slots__ = ()

    message = MessageAttrOperator()
    msg = message
    caching = BoolAttrOperator()
    cch = caching
    frozen = BoolAttrOperator()
    fzn = frozen
    isHistoricallyInteresting = ByteAttrOperator()
    ihi = isHistoricallyInteresting
    nodeState = NodeStateEnumAttr()
    nds = nodeState
    binMembership = DataStringAttrOperator()
    bnm = binMembership
