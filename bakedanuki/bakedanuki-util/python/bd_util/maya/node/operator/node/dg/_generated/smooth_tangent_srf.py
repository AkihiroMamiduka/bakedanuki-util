# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class DirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    V = 0
    U = 1


class DirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    V = 0
    U = 1

    NAME_MAP = {
        V: "V",
        U: "U",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class SmoothnessEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TANGENT = 0
    MAXIMUM = 1


class SmoothnessEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TANGENT = 0
    MAXIMUM = 1

    NAME_MAP = {
        TANGENT: "Tangent",
        MAXIMUM: "Maximum",
    }


class SmoothnessEnumField(
    EnumField[SmoothnessEnumAttrOperator, SmoothnessEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothnessEnumAttrOperator
    PLUG_CLS = SmoothnessEnumPlugOperator


class _GeneratedSmoothTangentSrf(DG):
    __slots__ = ()

    NODE_TYPE = "smoothTangentSrf"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    parameter = DoubleField(multi=True, default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    p = parameter

    direction = DirectionEnumField(default_value=1)
    d = direction

    smoothness = SmoothnessEnumField(default_value=0)
    s = smoothness

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
