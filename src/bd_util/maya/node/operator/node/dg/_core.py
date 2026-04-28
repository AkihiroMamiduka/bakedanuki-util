# coding: utf-8

# self
from .._core import Node
from ...attr.at.bool import BoolAttr
from ...attr.at.byte import ByteAttr
from ...attr.at.enum import EnumAttr
from ...attr.at.message import MessageAttr
from ...attr.dt.string import DataStringAttr


class DG(Node):
    message = MessageAttr()
    msg = message
    caching = BoolAttr()
    cch = caching
    frozen = BoolAttr()
    fzn = frozen
    isHistoricallyInteresting = ByteAttr()
    ihi = isHistoricallyInteresting
    nodeState = EnumAttr(
        enum_name=[
            "Normal",
            "HasNoEffect",
            "Blocking",
            "Waiting-Normal=8",
            "Waiting-HasNoEffect",
            "Waiting-Blocking",
        ]
    )
    nds = nodeState
    binMembership = DataStringAttr()
    bnm = binMembership
