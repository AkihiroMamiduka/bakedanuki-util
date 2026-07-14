# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class RenderLayerManager(DG):
    __slots__ = ()

    NODE_TYPE = "renderLayerManager"

    currentRenderLayer = ShortField(default_value=0)
    crl = currentRenderLayer

    renderLayerId = ShortField(multi=True, default_value=0)
    rlmi = renderLayerId
