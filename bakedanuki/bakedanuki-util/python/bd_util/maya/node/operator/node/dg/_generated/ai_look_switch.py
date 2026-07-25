# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_look_switch import LooksField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedAiLookSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "aiLookSwitch"

    enable = BoolField(default_value=True)
    en = enable

    index = LongField(default_value=0)
    idx = index

    looks = LooksField(multi=True)

    out = MessageField(writable=False)
