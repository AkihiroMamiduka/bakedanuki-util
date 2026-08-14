# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class MethodEnumPlugOperator(EnumPlugOperator["MethodEnumAttrOperator"]):
    __slots__ = ()

    CONNECT = 0
    BLEND = 1


class MethodEnumAttrOperator(EnumAttrOperator[MethodEnumPlugOperator]):
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


class GeneratedAttachCurve(DG):
    __slots__ = ()

    NODE_TYPE = "attachCurve"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    inputCurves = DataNurbsCurveField(multi=True)
    ics = inputCurves

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    reverse1 = BoolField(default_value=False)
    rv1 = reverse1

    reverse2 = BoolField(default_value=False)
    rv2 = reverse2

    method = MethodEnumField(default_value=0)
    m = method

    keepMultipleKnots = BoolField(default_value=True)
    kmk = keepMultipleKnots

    blendBias = DoubleField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=1.0
    )
    bb = blendBias

    blendKnotInsertion = BoolField(default_value=False)
    bki = blendKnotInsertion

    parameter = DoubleField(
        default_value=0.1, soft_min_value=-1.0, soft_max_value=1.0
    )
    p = parameter
