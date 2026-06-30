# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField


class DefaultRenderUtilityList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultRenderUtilityList"

    utilities = MessageField(multi=True)
    u = utilities
