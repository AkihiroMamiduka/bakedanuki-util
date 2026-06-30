# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class ProjectTangent(DG):
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

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    tangentScale = DoubleLinearField()
    ts = tangentScale

    curvatureScale = DoubleLinearField()
    cs = curvatureScale

    rotate = DoubleAngleField()
    ro = rotate

    tangentDirection = TangentDirectionEnumField()
    td = tangentDirection

    curvature = BoolField()
    c = curvature

    reverseTangent = BoolField()
    rt = reverseTangent

    ignoreEdges = BoolField()
    ie = ignoreEdges
