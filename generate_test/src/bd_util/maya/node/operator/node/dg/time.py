# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time import TimewarpInField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
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

    # TODO: timewarpIn_Inmap.timewarpIn_InmapTo (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: timewarpIn_Inmap.timewarpIn_InmapFrom (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: timewarpIn_Outmap.timewarpIn_OutmapTo (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: timewarpIn_Outmap.timewarpIn_OutmapFrom (attributeType=None, dataType=None) は未対応のため手動で追加してください

    enableTimewarp = BoolField()
    etw = enableTimewarp

    timecodeProductionStart = TimeField()
    tps = timecodeProductionStart

    timecodeMayaStart = TimeField()
    tms = timecodeMayaStart
