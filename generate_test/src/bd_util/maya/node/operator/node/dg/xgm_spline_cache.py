# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_spline_cache import WidthRampField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField


class CycleTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HOLD = 0
    LOOP = 1
    REVERSE = 2
    BOUNCE = 3


class CycleTypeEnumAttrOperator(EnumAttrOperator):
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


class XgmSplineCache(DG):
    __slots__ = ()

    NODE_TYPE = "xgmSplineCache"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    fileName = DataStringField()
    fn = fileName

    descriptions = DataStringArrayField()
    dc = descriptions

    activeDescription = DataStringField()
    ad = activeDescription

    startFrame = DoubleField()
    sf = startFrame

    endFrame = DoubleField()
    ef = endFrame

    time = TimeField()
    tm = time

    speed = DoubleField()
    sp = speed

    offset = DoubleField()
    of = offset

    cycleType = CycleTypeEnumField()
    ct = cycleType

    width = FloatField()
    w = width

    widthTaper = FloatField()
    wdt = widthTaper

    widthTaperStart = FloatField()
    wdts = widthTaperStart

    widthRamp = WidthRampField(multi=True)
    wdr = widthRamp
