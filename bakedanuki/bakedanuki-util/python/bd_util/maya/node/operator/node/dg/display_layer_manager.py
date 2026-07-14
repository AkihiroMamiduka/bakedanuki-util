# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class DisplayLayerManager(DG):
    __slots__ = ()

    NODE_TYPE = "displayLayerManager"

    currentDisplayLayer = ShortField(default_value=0)
    cdl = currentDisplayLayer

    displayLayerId = ShortField(multi=True, default_value=0)
    dli = displayLayerId
