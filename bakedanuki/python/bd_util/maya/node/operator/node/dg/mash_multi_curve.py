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

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    enable = BoolField(default_value=True)
    en = enable

    startPositions = DataVectorArrayField()

    extraPoints = BoolField(default_value=False)

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    raEn = randEnvelope

    StepEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    StEnv = StepEnvelope

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    curveClosed = BoolField(default_value=False)

    fixZeroPoints = BoolField(default_value=True)

    numberOfCurves = LongField(default_value=1, min_value=0, soft_max_value=50)

    maxCurveLength = LongField(default_value=100, min_value=0, soft_max_value=100)

    maxLengthVariance = LongField(default_value=0, min_value=0, soft_max_value=100)

    curveDegree = LongField(default_value=1, min_value=1, max_value=7)

    pointLocation = PointLocationField(default_value=(0.0, 0.0, 0.0))
    pointLoc = pointLocation
    pointLocation0 = pointLocation.pointLocation0
    pointLoc0 = pointLocation0
    pointLocation1 = pointLocation.pointLocation1
    pointLoc1 = pointLocation1
    pointLocation2 = pointLocation.pointLocation2
    pointLoc2 = pointLocation2

    offsetType = OffsetTypeEnumField(default_value=1)
    oft = offsetType
