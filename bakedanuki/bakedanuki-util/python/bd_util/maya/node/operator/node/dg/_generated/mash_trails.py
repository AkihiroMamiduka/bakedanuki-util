# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_trails import (
    BevelCapCurveField,
    ConnectionPointField,
    TrailTaperCurveField,
    TranslateInPPField,
    TranslateOutPPField,
    UpVectorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


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


class _GeneratedMASH_Trails(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Trails"

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP

    outputMesh = DataMeshField()
    outMesh = outputMesh

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP

    outputPoints = TypedField(writable=False)

    inputPoints = TypedField()

    connectionNetwork = TypedField()

    trailLength = LongField(default_value=25, min_value=0, soft_max_value=100)

    maxTrails = LongField(default_value=100, min_value=0, soft_max_value=300)

    trailCount = LongField(default_value=1, min_value=1, soft_max_value=10)

    searchRadius = FloatField(default_value=150.0, min_value=0.0, soft_max_value=50.0)

    bevelCapDistance = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)

    bevelCapDivisions = LongField(default_value=6, min_value=3, soft_max_value=10)

    randomLength = LongField(default_value=0, min_value=0, soft_max_value=100)

    curveSamples = LongField(default_value=6, min_value=2, soft_max_value=12)

    trailWidth = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    autoUpVector = BoolField(default_value=False)

    inheritScale = BoolField(default_value=False)

    quadraticSpacing = BoolField(default_value=True)

    outputTrailPoints = BoolField(default_value=False)

    decay = BoolField(default_value=False)

    upVector = UpVectorField(default_value=(1.0, 0.0, 0.0))
    upVector0 = upVector.upVector0
    upVector1 = upVector.upVector1
    upVector2 = upVector.upVector2

    inputCurve = DataNurbsCurveField()

    frontCapMode = FrontCapModeEnumField(default_value=1)

    rearCapMode = RearCapModeEnumField(default_value=1)

    trailsMode = TrailsModeEnumField(default_value=1)

    trailTaperCurve = TrailTaperCurveField(multi=True, default_value=(0.0, 0.0))

    bevelCapCurve = BevelCapCurveField(multi=True, default_value=(0.0, 0.0))

    time = TimeField(default_value=0.0)
    tm = time

    connectionPoint = ConnectionPointField(default_value=(0.0, 0.0, 0.0))
    conLoc = connectionPoint
    connectionPointX = connectionPoint.connectionPointX
    conLocx = connectionPointX
    connectionPointY = connectionPoint.connectionPointY
    conLocy = connectionPointY
    connectionPointZ = connectionPoint.connectionPointZ
    conLocz = connectionPointZ
