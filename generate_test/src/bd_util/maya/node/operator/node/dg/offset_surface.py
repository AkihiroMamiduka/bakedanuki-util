# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class MethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SURFACE_FIT = 0
    CV_FIT = 1


class MethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SURFACE_FIT = 0
    CV_FIT = 1

    NAME_MAP = {
        SURFACE_FIT: "Surface Fit",
        CV_FIT: "CV Fit",
    }


class MethodEnumField(
    EnumField[MethodEnumAttrOperator, MethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MethodEnumAttrOperator
    PLUG_CLS = MethodEnumPlugOperator


class OffsetSurface(DG):
    __slots__ = ()

    NODE_TYPE = "offsetSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    distance = DoubleLinearField()
    d = distance

    method = MethodEnumField()
    m = method

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
