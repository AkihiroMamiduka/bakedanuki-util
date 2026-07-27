# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.string_array import DataStringArrayField


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


class GeneratedXgmCurveToSpline(DG):
    __slots__ = ()

    NODE_TYPE = "xgmCurveToSpline"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    useMayaCurve = BoolField(default_value=True)
    umc = useMayaCurve

    inputCurves = DataNurbsCurveField(multi=True, readable=False)
    ics = inputCurves

    inMeshData = TypedField(readable=False)
    imd = inMeshData

    cachedInSplineData = TypedField()
    csd = cachedInSplineData

    mute = BoolField(default_value=False)
    m = mute

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    useAlembicCurve = BoolField(default_value=False)
    uac = useAlembicCurve

    fileName = DataStringField()
    fn = fileName

    loadedData = DataStringArrayField()
    ld = loadedData

    activeData = DataStringField()
    ad = activeData

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

    alignToNormal = BoolField(default_value=True)
    atn = alignToNormal
