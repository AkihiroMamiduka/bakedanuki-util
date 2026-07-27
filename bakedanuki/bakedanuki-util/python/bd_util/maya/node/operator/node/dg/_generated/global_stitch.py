# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class StitchCornersEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    CLOSEST_POINT = 1
    CLOSEST_KNOT = 2


class StitchCornersEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    CLOSEST_POINT = 1
    CLOSEST_KNOT = 2

    NAME_MAP = {
        OFF: "Off",
        CLOSEST_POINT: "Closest Point",
        CLOSEST_KNOT: "Closest Knot",
    }


class StitchCornersEnumField(
    EnumField[StitchCornersEnumAttrOperator, StitchCornersEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StitchCornersEnumAttrOperator
    PLUG_CLS = StitchCornersEnumPlugOperator


class StitchEdgesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    CLOSEST_POINT = 1
    MATCH_PARAMETERS = 2


class StitchEdgesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    CLOSEST_POINT = 1
    MATCH_PARAMETERS = 2

    NAME_MAP = {
        OFF: "Off",
        CLOSEST_POINT: "Closest Point",
        MATCH_PARAMETERS: "Match Parameters",
    }


class StitchEdgesEnumField(
    EnumField[StitchEdgesEnumAttrOperator, StitchEdgesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StitchEdgesEnumAttrOperator
    PLUG_CLS = StitchEdgesEnumPlugOperator


class StitchSmoothnessEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    TANGENT = 1
    NORMAL = 2


class StitchSmoothnessEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    TANGENT = 1
    NORMAL = 2

    NAME_MAP = {
        OFF: "Off",
        TANGENT: "Tangent",
        NORMAL: "Normal",
    }


class StitchSmoothnessEnumField(
    EnumField[StitchSmoothnessEnumAttrOperator, StitchSmoothnessEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StitchSmoothnessEnumAttrOperator
    PLUG_CLS = StitchSmoothnessEnumPlugOperator


class GeneratedGlobalStitch(DG):
    __slots__ = ()

    NODE_TYPE = "globalStitch"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    stitchCorners = StitchCornersEnumField(default_value=1)
    sc = stitchCorners

    stitchEdges = StitchEdgesEnumField(default_value=1)
    se = stitchEdges

    stitchSmoothness = StitchSmoothnessEnumField(default_value=0)
    ss = stitchSmoothness

    stitchPartialEdges = BoolField(default_value=False)
    spe = stitchPartialEdges

    maxSeparation = DoubleLinearField(default_value=0.1, min_value=0.0001, soft_min_value=0.001, soft_max_value=1.0)
    ms = maxSeparation

    sampling = LongField(default_value=1, min_value=1, max_value=100, soft_max_value=10)
    sam = sampling

    modificationResistance = DoubleField(default_value=0.1, min_value=0.001, max_value=1000.0, soft_max_value=1.0)
    mr = modificationResistance

    lockSurface = BoolField(multi=True, default_value=False)
    lk = lockSurface

    shouldBeLast = BoolField(default_value=True, writable=False)
    sbl = shouldBeLast

    outputSurface = DataNurbsSurfaceField(multi=True, writable=False)
    os = outputSurface

    connectedEdges = DataNurbsCurveField(multi=True, writable=False)
    ce = connectedEdges

    unconnectedEdges = DataNurbsCurveField(multi=True, writable=False)
    ue = unconnectedEdges

    topology = TypedField()
    top = topology

    updateSampling = BoolField(default_value=False)
    us = updateSampling
