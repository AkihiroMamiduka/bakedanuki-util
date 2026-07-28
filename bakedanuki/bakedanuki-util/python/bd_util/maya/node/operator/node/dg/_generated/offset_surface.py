# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class MethodEnumPlugOperator(EnumPlugOperator["MethodEnumAttrOperator"]):
    __slots__ = ()

    SURFACE_FIT = 0
    CV_FIT = 1


class MethodEnumAttrOperator(EnumAttrOperator[MethodEnumPlugOperator]):
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


class GeneratedOffsetSurface(DG):
    __slots__ = ()

    NODE_TYPE = "offsetSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    distance = DoubleLinearField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    d = distance

    method = MethodEnumField(default_value=0)
    m = method

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
