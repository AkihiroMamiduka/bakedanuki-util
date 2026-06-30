# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
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


class XgmCurveToSpline(DG):
    __slots__ = ()

    NODE_TYPE = "xgmCurveToSpline"

    inSplineData = TypedField()
    isd = inSplineData

    useMayaCurve = BoolField()
    umc = useMayaCurve

    inputCurves = DataNurbsCurveField(multi=True)
    ics = inputCurves

    inMeshData = TypedField()
    imd = inMeshData

    cachedInSplineData = TypedField()
    csd = cachedInSplineData

    mute = BoolField()
    m = mute

    outSplineData = TypedField()
    osd = outSplineData

    useAlembicCurve = BoolField()
    uac = useAlembicCurve

    fileName = DataStringField()
    fn = fileName

    loadedData = DataStringArrayField()
    ld = loadedData

    activeData = DataStringField()
    ad = activeData

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

    alignToNormal = BoolField()
    atn = alignToNormal
