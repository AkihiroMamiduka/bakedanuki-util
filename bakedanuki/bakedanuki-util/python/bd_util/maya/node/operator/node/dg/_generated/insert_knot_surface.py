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
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class DirectionEnumPlugOperator(EnumPlugOperator["DirectionEnumAttrOperator"]):
    __slots__ = ()

    V = 0
    U = 1


class DirectionEnumAttrOperator(EnumAttrOperator[DirectionEnumPlugOperator]):
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


class GeneratedInsertKnotSurface(DG):
    __slots__ = ()

    NODE_TYPE = "insertKnotSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    parameter = DoubleField(multi=True, default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    p = parameter

    numberOfKnots = LongField(multi=True, default_value=1, min_value=0, soft_min_value=0, soft_max_value=3)
    nk = numberOfKnots

    addKnots = BoolField(default_value=True)
    add = addKnots

    insertBetween = BoolField(default_value=False)
    ib = insertBetween

    direction = DirectionEnumField(default_value=1)
    d = direction

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
