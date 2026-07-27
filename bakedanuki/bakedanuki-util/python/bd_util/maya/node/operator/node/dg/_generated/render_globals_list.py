# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedRenderGlobalsList(DG):
    __slots__ = ()

    NODE_TYPE = "renderGlobalsList"

    renderGlobals = MessageField(multi=True)
    rg = renderGlobals

    renderQualities = MessageField(multi=True)
    rq = renderQualities

    renderResolutions = MessageField(multi=True)
    rr = renderResolutions
