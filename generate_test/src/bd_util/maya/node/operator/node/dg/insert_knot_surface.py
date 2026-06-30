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
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class InsertKnotSurface(DG):
    __slots__ = ()

    NODE_TYPE = "insertKnotSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    parameter = DoubleField(multi=True)
    p = parameter

    numberOfKnots = LongField(multi=True)
    nk = numberOfKnots

    addKnots = BoolField()
    add = addKnots

    insertBetween = BoolField()
    ib = insertBetween

    direction = DirectionEnumField()
    d = direction

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
