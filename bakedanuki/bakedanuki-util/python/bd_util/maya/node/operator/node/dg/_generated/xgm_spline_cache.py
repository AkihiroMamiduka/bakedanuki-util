# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_spline_cache import WidthRampField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.string_array import DataStringArrayField


class CycleTypeEnumPlugOperator(EnumPlugOperator["CycleTypeEnumAttrOperator"]):
    __slots__ = ()

    HOLD = 0
    LOOP = 1
    REVERSE = 2
    BOUNCE = 3


class CycleTypeEnumAttrOperator(EnumAttrOperator[CycleTypeEnumPlugOperator]):
    __slots__ = ()

    HOLD = 0
    LOOP = 1
    REVERSE = 2
    BOUNCE = 3

    NAME_MAP = {
        HOLD: "Hold",
        LOOP: "Loop",
        REVERSE: "Reverse",
        BOUNCE: "Bounce",
    }


class CycleTypeEnumField(
    EnumField[CycleTypeEnumAttrOperator, CycleTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CycleTypeEnumAttrOperator
    PLUG_CLS = CycleTypeEnumPlugOperator


class GeneratedXgmSplineCache(DG):
    __slots__ = ()

    NODE_TYPE = "xgmSplineCache"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    fileName = DataStringField()
    fn = fileName

    descriptions = DataStringArrayField()
    dc = descriptions

    activeDescription = DataStringField()
    ad = activeDescription

    startFrame = DoubleField(default_value=0.0, writable=False)
    sf = startFrame

    endFrame = DoubleField(default_value=0.0, writable=False)
    ef = endFrame

    time = TimeField(default_value=0.0)
    tm = time

    speed = DoubleField(default_value=1.0)
    sp = speed

    offset = DoubleField(default_value=0.0)
    of = offset

    cycleType = CycleTypeEnumField(default_value=0)
    ct = cycleType

    width = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    w = width

    widthTaper = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wdt = widthTaper

    widthTaperStart = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    wdts = widthTaperStart

    widthRamp = WidthRampField(multi=True, default_value=(0.0, 0.0, 1.0))
    wdr = widthRamp
