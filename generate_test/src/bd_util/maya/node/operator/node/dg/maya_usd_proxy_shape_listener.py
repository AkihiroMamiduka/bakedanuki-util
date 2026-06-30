# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.long_long_int import LongLongIntField


class MayaUsdProxyShapeListener(DG):
    __slots__ = ()

    NODE_TYPE = "mayaUsdProxyShapeListener"

    stageCacheId = LongField()
    stcid = stageCacheId

    outStageCacheId = LongField()
    ostcid = outStageCacheId

    updateId = LongLongIntField()
    upid = updateId

    resyncId = LongLongIntField()
    rsid = resyncId
