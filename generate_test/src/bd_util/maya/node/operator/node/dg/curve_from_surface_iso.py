# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class IsoparmDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    U = 0
    V = 1


class IsoparmDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    U = 0
    V = 1

    NAME_MAP = {
        U: "U",
        V: "V",
    }


class IsoparmDirectionEnumField(
    EnumField[IsoparmDirectionEnumAttrOperator, IsoparmDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IsoparmDirectionEnumAttrOperator
    PLUG_CLS = IsoparmDirectionEnumPlugOperator


class CurveFromSurfaceIso(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromSurfaceIso"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    minValue = DoubleField()
    min = minValue

    maxValue = DoubleField()
    max = maxValue

    relative = BoolField()
    r = relative

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    isoparmValue = DoubleField()
    iv = isoparmValue

    isoparmDirection = IsoparmDirectionEnumField()
    idr = isoparmDirection

    relativeValue = BoolField()
    rv = relativeValue
