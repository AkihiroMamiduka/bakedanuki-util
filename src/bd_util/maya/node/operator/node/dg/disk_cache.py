# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class SamplingTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVER_SAMPLING = 0
    UNDER_SAMPLING = 1


class SamplingTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVER_SAMPLING = 0
    UNDER_SAMPLING = 1

    NAME_MAP = {
        OVER_SAMPLING: "Over Sampling",
        UNDER_SAMPLING: "Under Sampling",
    }


class SamplingTypeEnumField(
    EnumField[SamplingTypeEnumAttrOperator, SamplingTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SamplingTypeEnumAttrOperator
    PLUG_CLS = SamplingTypeEnumPlugOperator


class DiskCache(DG):
    __slots__ = ()

    NODE_TYPE = "diskCache"

    diskCache = MessageField()
    dc = diskCache

    enable = BoolField(default_value=True)
    ebl = enable

    cacheName = DataStringField()
    cn = cacheName

    startTime = TimeField(default_value=0.0, writable=False)
    stim = startTime

    endTime = TimeField(default_value=0.0, writable=False)
    etim = endTime

    samplingType = SamplingTypeEnumField(default_value=0, writable=False)
    st = samplingType

    samplingRate = LongField(default_value=0, writable=False)
    sr = samplingRate

    cacheType = DataStringField()
    ct = cacheType

    hiddenCacheName = DataStringField()
    hcn = hiddenCacheName

    copyLocally = BoolField(default_value=True)
    cpl = copyLocally
