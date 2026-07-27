# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
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


class GeneratedDetachSurface(DG):
    __slots__ = ()

    NODE_TYPE = "detachSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputSurface = DataNurbsSurfaceField(multi=True, writable=False)
    os = outputSurface

    direction = DirectionEnumField(default_value=1)
    d = direction

    parameter = DoubleField(multi=True, default_value=0.0, soft_min_value=0.0, soft_max_value=1000.0)
    p = parameter

    keep = BoolField(multi=True, default_value=True)
    k = keep
