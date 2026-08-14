# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.long_long_int import (
    LongLongIntField,
)


class GeneratedMayaUsdProxyShapeListenerBase(DG):
    __slots__ = ()

    NODE_TYPE = "mayaUsdProxyShapeListenerBase"

    stageCacheId = LongField(default_value=-1, readable=False)
    stcid = stageCacheId

    outStageCacheId = LongField(default_value=-1, writable=False)
    ostcid = outStageCacheId

    updateId = LongLongIntField(default_value=0, writable=False)
    upid = updateId

    resyncId = LongLongIntField(default_value=0, writable=False)
    rsid = resyncId
