# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_multi_curve import (
    FalloffObjectField,
    PointLocationField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class OffsetTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    JOIN_THE_DOTS = 1
    TRACER = 2
    POINT_TO_POINT = 3


class OffsetTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    JOIN_THE_DOTS = 1
    TRACER = 2
    POINT_TO_POINT = 3

    NAME_MAP = {
        JOIN_THE_DOTS: "Join the Dots",
        TRACER: "Tracer",
        POINT_TO_POINT: "Point to Point",
    }


class OffsetTypeEnumField(
    EnumField[OffsetTypeEnumAttrOperator, OffsetTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetTypeEnumAttrOperator
    PLUG_CLS = OffsetTypeEnumPlugOperator


class MASH_MultiCurve(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_MultiCurve"

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputCurves = DataNurbsCurveField(multi=True)
    oc = outputCurves

    outputArray = DataVectorArrayField()
    outArray = outputArray

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    Envelope = FloatField()
    env = Envelope

    enable = BoolField()
    en = enable

    startPositions = DataVectorArrayField()

    extraPoints = BoolField()

    randEnvelope = FloatField()
    raEn = randEnvelope

    StepEnvelope = FloatField()
    StEnv = StepEnvelope

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    curveClosed = BoolField()

    fixZeroPoints = BoolField()

    numberOfCurves = LongField()

    maxCurveLength = LongField()

    maxLengthVariance = LongField()

    curveDegree = LongField()

    pointLocation = PointLocationField()
    pointLoc = pointLocation
    pointLocation0 = pointLocation.pointLocation0
    pointLoc0 = pointLocation0
    pointLocation1 = pointLocation.pointLocation1
    pointLoc1 = pointLocation1
    pointLocation2 = pointLocation.pointLocation2
    pointLoc2 = pointLocation2

    offsetType = OffsetTypeEnumField()
    oft = offsetType
