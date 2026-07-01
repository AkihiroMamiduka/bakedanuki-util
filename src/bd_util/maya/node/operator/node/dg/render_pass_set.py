# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class RenderPassSet(DG):
    __slots__ = ()

    NODE_TYPE = "renderPassSet"

    owner = MessageField(multi=True)
    ow = owner

    renderable = BoolField()
    r = renderable

    renderPass = MessageField()
    rps = renderPass
