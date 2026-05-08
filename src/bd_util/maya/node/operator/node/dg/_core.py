# coding: utf-8

# self
from .._core import Node
from .....attr.enum import AttributeEnum
from ...attr.at.bool import BoolAttr
from ...attr.at.byte import ByteAttr
from ...attr.at.enum import EnumAttr
from ...attr.at.message import MessageAttr
from ...attr.dt.string import DataStringAttr


class NodeStateEnum(AttributeEnum):
    NORMAL = "Normal"
    HAS_NO_EFFECT = "HasNoEffect"
    BLOCKING = "Blocking"
    WAITING_NORMAL = ("Waiting-Normal", 8)
    WAITING_HAS_NO_EFFECT = "Waiting-HasNoEffect"
    WAITING_BLOCKING = "WWaiting-Blocking"


class DG(Node):
    message = MessageAttr()
    msg = message
    caching = BoolAttr()
    cch = caching
    frozen = BoolAttr()
    fzn = frozen
    isHistoricallyInteresting = ByteAttr()
    ihi = isHistoricallyInteresting
    nodeState = EnumAttr(enum_name=NodeStateEnum)
    nds = nodeState
    binMembership = DataStringAttr()
    bnm = binMembership
