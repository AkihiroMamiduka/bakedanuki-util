# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class GroupId(DG):
    __slots__ = ()

    NODE_TYPE = "groupId"

    groupId = LongField(default_value=0, writable=False)
    id = groupId
