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

    minValue = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    min = minValue

    maxValue = DoubleField(default_value=-1.0, soft_min_value=0.0, soft_max_value=1.0)
    max = maxValue

    relative = BoolField(default_value=False)
    r = relative

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    isoparmValue = DoubleField(default_value=0.0)
    iv = isoparmValue

    isoparmDirection = IsoparmDirectionEnumField(default_value=0)
    idr = isoparmDirection

    relativeValue = BoolField(default_value=False)
    rv = relativeValue
