# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.cache_blend import (
    CacheDataField,
    InCacheField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class _GeneratedCacheBlend(DG):
    __slots__ = ()

    NODE_TYPE = "cacheBlend"

    outCacheData = GenericField(multi=True)
    ocd = outCacheData

    outCacheArrayData = TypedField(writable=False)
    ocad = outCacheArrayData

    inRange = BoolField(default_value=True, writable=False)
    ir = inRange

    inCache = InCacheField(multi=True)
    ic = inCache

    disableAll = BoolField(default_value=False)
    da = disableAll

    cacheData = CacheDataField(multi=True, default_value=(0.0, 0.0, 0.0, 1.0))
    cd = cacheData
