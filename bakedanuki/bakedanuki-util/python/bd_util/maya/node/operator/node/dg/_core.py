# coding: utf-8

# self
from .._core import NodeOperator
from ...attr.define.std.at.scalar.numeric.bool import BoolField
from ...attr.define.std.at.scalar.numeric.range.byte import ByteField
from ...attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.dt.string import DataStringField


class NodeStateEnumPlug(EnumPlugOperator["NodeStateEnumAttr"]):
    """Maya 標準の `nodeState` 値をプラグから扱う。"""

    __slots__ = ()

    NORMAL = 0
    HAS_NO_EFFECT = 1
    BLOCKING = 2
    WAITING_NORMAL = 8
    WAITING_HAS_NO_EFFECT = 9
    WAITING_BLOCKING = 10


class NodeStateEnumAttr(EnumAttrOperator[NodeStateEnumPlug]):
    """Maya 標準の `nodeState` 値と表示名を定義する。"""

    __slots__ = ()

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


class NodeStateEnumField(EnumField[NodeStateEnumAttr, NodeStateEnumPlug]):
    """DG ノードの `nodeState` 属性を公開する。"""

    __slots__ = ()

    ATTR_CLS = NodeStateEnumAttr
    PLUG_CLS = NodeStateEnumPlug


class DG(NodeOperator):
    """DG ノードに共通する Maya 標準属性を公開する。"""

    __slots__ = ()

    message = MessageField()
    msg = message
    caching = BoolField()
    cch = caching
    frozen = BoolField()
    fzn = frozen
    isHistoricallyInteresting = ByteField()
    ihi = isHistoricallyInteresting
    nodeState = NodeStateEnumField()
    nds = nodeState
    binMembership = DataStringField()
    bnm = binMembership
