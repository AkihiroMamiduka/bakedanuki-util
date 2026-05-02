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
    normal = 0
    has_no_effect = 1
    blocking = 2
    waiting_normal = 8
    waiting_has_no_effect = 9
    waiting_blocking = 10


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
