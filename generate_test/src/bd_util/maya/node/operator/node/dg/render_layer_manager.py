# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class RenderLayerManager(DG):
    __slots__ = ()

    NODE_TYPE = "renderLayerManager"

    currentRenderLayer = ShortField()
    crl = currentRenderLayer

    renderLayerId = ShortField(multi=True)
    rlmi = renderLayerId
