# coding: utf-8
from ._core import DG
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class ApplyConnectionOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyConnectionOverride"

    enabled = BoolField()
    en = enabled

    target = GenericField()
    tg = target

    previous = MessageField()
    p = previous

    next = MessageField()
    n = next
