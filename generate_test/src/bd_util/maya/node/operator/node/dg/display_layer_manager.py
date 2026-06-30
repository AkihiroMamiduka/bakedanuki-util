# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class DisplayLayerManager(DG):
    __slots__ = ()

    NODE_TYPE = "displayLayerManager"

    currentDisplayLayer = ShortField()
    cdl = currentDisplayLayer

    displayLayerId = ShortField(multi=True)
    dli = displayLayerId
