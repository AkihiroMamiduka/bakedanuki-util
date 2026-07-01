# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.cache_blend import (
    CacheDataField,
    InCacheField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField


class CacheBlend(DG):
    __slots__ = ()

    NODE_TYPE = "cacheBlend"

    outCacheData = GenericField(multi=True)
    ocd = outCacheData

    outCacheArrayData = TypedField()
    ocad = outCacheArrayData

    inRange = BoolField()
    ir = inRange

    inCache = InCacheField(multi=True)
    ic = inCache

    disableAll = BoolField()
    da = disableAll

    cacheData = CacheDataField(multi=True)
    cd = cacheData
