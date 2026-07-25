# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class TangentDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    U = 1
    V = 2
    NORMAL = 3


class TangentDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    U = 1
    V = 2
    NORMAL = 3

    NAME_MAP = {
        U: "U",
        V: "V",
        NORMAL: "Normal",
    }


class TangentDirectionEnumField(
    EnumField[TangentDirectionEnumAttrOperator, TangentDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentDirectionEnumAttrOperator
    PLUG_CLS = TangentDirectionEnumPlugOperator


class _GeneratedProjectTangent(DG):
    __slots__ = ()

    NODE_TYPE = "projectTangent"

    inputCurveToProject = DataNurbsCurveField()
    ic = inputCurveToProject

    inputCurve1ToProjectTo = DataNurbsCurveField()
    ic1 = inputCurve1ToProjectTo

    inputCurve2ToProjectTo = DataNurbsCurveField()
    ic2 = inputCurve2ToProjectTo

    inputSurfaceToProjectTo = DataNurbsSurfaceField()
    is_ = inputSurfaceToProjectTo

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    tangentScale = DoubleLinearField(default_value=1.0, min_value=-10.0, max_value=10.0)
    ts = tangentScale

    curvatureScale = DoubleLinearField(default_value=0.0, min_value=-10.0, max_value=10.0)
    cs = curvatureScale

    rotate = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ro = rotate

    tangentDirection = TangentDirectionEnumField(default_value=1)
    td = tangentDirection

    curvature = BoolField(default_value=False)
    c = curvature

    reverseTangent = BoolField(default_value=False)
    rt = reverseTangent

    ignoreEdges = BoolField(default_value=False)
    ie = ignoreEdges
