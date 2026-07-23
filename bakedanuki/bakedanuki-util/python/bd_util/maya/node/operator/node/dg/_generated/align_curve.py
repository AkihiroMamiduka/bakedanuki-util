# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class PositionalContinuityTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MOVE_FIRST = 1
    MOVE_SECOND = 2
    MOVE_BOTH = 3
    MODIFY_FIRST = 4
    MODIFY_SECOND = 5
    MODIFY_BOTH = 6


class PositionalContinuityTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MOVE_FIRST = 1
    MOVE_SECOND = 2
    MOVE_BOTH = 3
    MODIFY_FIRST = 4
    MODIFY_SECOND = 5
    MODIFY_BOTH = 6

    NAME_MAP = {
        MOVE_FIRST: "Move First",
        MOVE_SECOND: "Move Second",
        MOVE_BOTH: "Move Both",
        MODIFY_FIRST: "Modify First",
        MODIFY_SECOND: "Modify Second",
        MODIFY_BOTH: "Modify Both",
    }


class PositionalContinuityTypeEnumField(
    EnumField[PositionalContinuityTypeEnumAttrOperator, PositionalContinuityTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionalContinuityTypeEnumAttrOperator
    PLUG_CLS = PositionalContinuityTypeEnumPlugOperator


class TangentContinuityTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIRST = 1
    SECOND = 2


class TangentContinuityTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIRST = 1
    SECOND = 2

    NAME_MAP = {
        FIRST: "First",
        SECOND: "Second",
    }


class TangentContinuityTypeEnumField(
    EnumField[TangentContinuityTypeEnumAttrOperator, TangentContinuityTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentContinuityTypeEnumAttrOperator
    PLUG_CLS = TangentContinuityTypeEnumPlugOperator


class _GeneratedAlignCurve(DG):
    __slots__ = ()

    NODE_TYPE = "alignCurve"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    outputCurve1 = DataNurbsCurveField(writable=False)
    oc1 = outputCurve1

    outputCurve2 = DataNurbsCurveField(writable=False)
    oc2 = outputCurve2

    tangentScale1 = DoubleField(default_value=1.0, min_value=-100.0, max_value=100.0)
    ts1 = tangentScale1

    tangentScale2 = DoubleField(default_value=1.0, min_value=-100.0, max_value=100.0)
    ts2 = tangentScale2

    curvatureScale1 = DoubleField(default_value=0.0, min_value=-100.0, max_value=100.0)
    cs1 = curvatureScale1

    curvatureScale2 = DoubleField(default_value=0.0, min_value=-100.0, max_value=100.0)
    cs2 = curvatureScale2

    positionalContinuityType = PositionalContinuityTypeEnumField(default_value=1)
    pct = positionalContinuityType

    tangentContinuityType = TangentContinuityTypeEnumField(default_value=1)
    tct = tangentContinuityType

    joinParameter = FloatField(default_value=123456.0, min_value=-123456.0, max_value=123456.0)
    jnp = joinParameter

    reverse1 = BoolField(default_value=False)
    rv1 = reverse1

    reverse2 = BoolField(default_value=False)
    rv2 = reverse2

    attach = BoolField(default_value=False)
    at = attach

    keepMultipleKnots = BoolField(default_value=True)
    kmk = keepMultipleKnots

    positionalContinuity = BoolField(default_value=True)
    pc = positionalContinuity

    tangentContinuity = BoolField(default_value=True)
    tc = tangentContinuity

    curvatureContinuity = BoolField(default_value=False)
    cc = curvatureContinuity
