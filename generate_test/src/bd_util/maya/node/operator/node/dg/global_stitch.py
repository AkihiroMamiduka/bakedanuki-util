# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class GlobalStitch(DG):
    __slots__ = ()

    NODE_TYPE = "globalStitch"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    stitchCorners = StitchCornersEnumField()
    sc = stitchCorners

    stitchEdges = StitchEdgesEnumField()
    se = stitchEdges

    stitchSmoothness = StitchSmoothnessEnumField()
    ss = stitchSmoothness

    stitchPartialEdges = BoolField()
    spe = stitchPartialEdges

    maxSeparation = DoubleLinearField()
    ms = maxSeparation

    sampling = LongField()
    sam = sampling

    modificationResistance = DoubleField()
    mr = modificationResistance

    lockSurface = BoolField(multi=True)
    lk = lockSurface

    shouldBeLast = BoolField()
    sbl = shouldBeLast

    outputSurface = DataNurbsSurfaceField(multi=True)
    os = outputSurface

    connectedEdges = DataNurbsCurveField(multi=True)
    ce = connectedEdges

    unconnectedEdges = DataNurbsCurveField(multi=True)
    ue = unconnectedEdges

    topology = TypedField()
    top = topology

    updateSampling = BoolField()
    us = updateSampling
