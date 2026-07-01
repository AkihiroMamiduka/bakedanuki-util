# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time import TimewarpInField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar.time import TimeField


class Time(DG):
    __slots__ = ()

    NODE_TYPE = "time"

    outTime = TimeField()
    o = outTime

    unwarpedTime = TimeField()
    unw = unwarpedTime

    timewarpIn = TimewarpInField()
    twi = timewarpIn
    timewarpIn_Hidden = timewarpIn.timewarpIn_Hidden
    twih = timewarpIn_Hidden
    timewarpIn_Raw = timewarpIn.timewarpIn_Raw
    twir = timewarpIn_Raw
    timewarpIn_Inmap = timewarpIn.timewarpIn_Inmap
    twii = timewarpIn_Inmap
    timewarpIn_Outmap = timewarpIn.timewarpIn_Outmap
    twio = timewarpIn_Outmap

    timewarpIn_InmapTo = ShortField()
    twiit = timewarpIn_InmapTo

    timewarpIn_InmapFrom = ShortField()
    twiif = timewarpIn_InmapFrom

    timewarpIn_OutmapTo = ShortField()
    twiot = timewarpIn_OutmapTo

    timewarpIn_OutmapFrom = ShortField()
    twiof = timewarpIn_OutmapFrom

    enableTimewarp = BoolField()
    etw = enableTimewarp

    timecodeProductionStart = TimeField()
    tps = timecodeProductionStart

    timecodeMayaStart = TimeField()
    tms = timecodeMayaStart
