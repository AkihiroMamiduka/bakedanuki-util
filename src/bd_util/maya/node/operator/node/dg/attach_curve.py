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


class MethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONNECT = 0
    BLEND = 1


class MethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONNECT = 0
    BLEND = 1

    NAME_MAP = {
        CONNECT: "Connect",
        BLEND: "Blend",
    }


class MethodEnumField(
    EnumField[MethodEnumAttrOperator, MethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MethodEnumAttrOperator
    PLUG_CLS = MethodEnumPlugOperator


class AttachCurve(DG):
    __slots__ = ()

    NODE_TYPE = "attachCurve"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    inputCurves = DataNurbsCurveField(multi=True)
    ics = inputCurves

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    reverse1 = BoolField()
    rv1 = reverse1

    reverse2 = BoolField()
    rv2 = reverse2

    method = MethodEnumField()
    m = method

    keepMultipleKnots = BoolField()
    kmk = keepMultipleKnots

    blendBias = DoubleField()
    bb = blendBias

    blendKnotInsertion = BoolField()
    bki = blendKnotInsertion

    parameter = DoubleField()
    p = parameter
