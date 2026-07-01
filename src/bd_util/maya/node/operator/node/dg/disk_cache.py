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

    enable = BoolField()
    ebl = enable

    cacheName = DataStringField()
    cn = cacheName

    startTime = TimeField()
    stim = startTime

    endTime = TimeField()
    etim = endTime

    samplingType = SamplingTypeEnumField()
    st = samplingType

    samplingRate = LongField()
    sr = samplingRate

    cacheType = DataStringField()
    ct = cacheType

    hiddenCacheName = DataStringField()
    hcn = hiddenCacheName

    copyLocally = BoolField()
    cpl = copyLocally
