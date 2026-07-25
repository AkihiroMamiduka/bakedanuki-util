# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.short import ShortField


class _GeneratedDisplayLayerManager(DG):
    __slots__ = ()

    NODE_TYPE = "displayLayerManager"

    currentDisplayLayer = ShortField(default_value=0)
    cdl = currentDisplayLayer

    displayLayerId = ShortField(multi=True, default_value=0)
    dli = displayLayerId
