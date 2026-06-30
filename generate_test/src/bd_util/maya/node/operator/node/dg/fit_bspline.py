# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class KeepRangeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _0_TO_1 = 0
    ORIGINAL = 1
    _0_TO_HASH_SPANS = 2


class KeepRangeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _0_TO_1 = 0
    ORIGINAL = 1
    _0_TO_HASH_SPANS = 2

    NAME_MAP = {
        _0_TO_1: "0 to 1",
        ORIGINAL: "Original",
        _0_TO_HASH_SPANS: "0 to #spans",
    }


class KeepRangeEnumField(
    EnumField[KeepRangeEnumAttrOperator, KeepRangeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeepRangeEnumAttrOperator
    PLUG_CLS = KeepRangeEnumPlugOperator


class FitBspline(DG):
    __slots__ = ()

    NODE_TYPE = "fitBspline"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    tolerance = DoubleLinearField()
    tol = tolerance

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    keepRange = KeepRangeEnumField()
    kr = keepRange
