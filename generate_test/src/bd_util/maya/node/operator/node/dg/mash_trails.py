# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_trails import (
    BevelCapCurveField,
    ConnectionPointField,
    TrailTaperCurveField,
    TranslateInPPField,
    TranslateOutPPField,
    UpVectorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class FrontCapModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 1
    CAP = 2
    BEVEL_CAP = 3


class FrontCapModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 1
    CAP = 2
    BEVEL_CAP = 3

    NAME_MAP = {
        NONE: "None",
        CAP: "Cap",
        BEVEL_CAP: "Bevel Cap",
    }


class FrontCapModeEnumField(
    EnumField[FrontCapModeEnumAttrOperator, FrontCapModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrontCapModeEnumAttrOperator
    PLUG_CLS = FrontCapModeEnumPlugOperator


class RearCapModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 1
    CAP = 2
    BEVEL_CAP = 3


class RearCapModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 1
    CAP = 2
    BEVEL_CAP = 3

    NAME_MAP = {
        NONE: "None",
        CAP: "Cap",
        BEVEL_CAP: "Bevel Cap",
    }


class RearCapModeEnumField(
    EnumField[RearCapModeEnumAttrOperator, RearCapModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RearCapModeEnumAttrOperator
    PLUG_CLS = RearCapModeEnumPlugOperator


class TrailsModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRAILS = 1
    JOIN_THE_DOTS = 2
    CONNECT_TO_POINT = 3
    CONNECT_TO_NEAREST = 4
    CONNECT_BY_DISTANCE = 5
    CONSTRAINT_PAIRS = 6


class TrailsModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRAILS = 1
    JOIN_THE_DOTS = 2
    CONNECT_TO_POINT = 3
    CONNECT_TO_NEAREST = 4
    CONNECT_BY_DISTANCE = 5
    CONSTRAINT_PAIRS = 6

    NAME_MAP = {
        TRAILS: "Trails",
        JOIN_THE_DOTS: "Join the Dots",
        CONNECT_TO_POINT: "Connect to Point",
        CONNECT_TO_NEAREST: "Connect to Nearest",
        CONNECT_BY_DISTANCE: "Connect by Distance",
        CONSTRAINT_PAIRS: "Constraint Pairs",
    }


class TrailsModeEnumField(
    EnumField[TrailsModeEnumAttrOperator, TrailsModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrailsModeEnumAttrOperator
    PLUG_CLS = TrailsModeEnumPlugOperator


class MASH_Trails(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Trails"

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP

    outputMesh = DataMeshField()
    outMesh = outputMesh

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP

    outputPoints = TypedField()

    inputPoints = TypedField()

    connectionNetwork = TypedField()

    trailLength = LongField()

    maxTrails = LongField()

    trailCount = LongField()

    searchRadius = FloatField()

    bevelCapDistance = FloatField()

    bevelCapDivisions = LongField()

    randomLength = LongField()

    curveSamples = LongField()

    trailWidth = FloatField()

    autoUpVector = BoolField()

    inheritScale = BoolField()

    quadraticSpacing = BoolField()

    outputTrailPoints = BoolField()

    decay = BoolField()

    upVector = UpVectorField()
    upVector0 = upVector.upVector0
    upVector1 = upVector.upVector1
    upVector2 = upVector.upVector2

    inputCurve = DataNurbsCurveField()

    frontCapMode = FrontCapModeEnumField()

    rearCapMode = RearCapModeEnumField()

    trailsMode = TrailsModeEnumField()

    trailTaperCurve = TrailTaperCurveField(multi=True)

    bevelCapCurve = BevelCapCurveField(multi=True)

    time = TimeField()
    tm = time

    connectionPoint = ConnectionPointField()
    conLoc = connectionPoint
    connectionPointX = connectionPoint.connectionPointX
    conLocx = connectionPointX
    connectionPointY = connectionPoint.connectionPointY
    conLocy = connectionPointY
    connectionPointZ = connectionPoint.connectionPointZ
    conLocz = connectionPointZ
