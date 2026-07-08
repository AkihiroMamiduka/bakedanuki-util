# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class RenderPassSet(DG):
    __slots__ = ()

    NODE_TYPE = "renderPassSet"

    owner = MessageField(multi=True, readable=False)
    ow = owner

    renderable = BoolField(default_value=True)
    r = renderable

    renderPass = MessageField(writable=False)
    rps = renderPass
