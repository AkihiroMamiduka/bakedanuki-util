# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class KeepRangeEnumPlugOperator(EnumPlugOperator["KeepRangeEnumAttrOperator"]):
    __slots__ = ()

    _0_TO_1 = 0
    ORIGINAL = 1
    _0_TO_HASH_SPANS = 2


class KeepRangeEnumAttrOperator(EnumAttrOperator[KeepRangeEnumPlugOperator]):
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


class GeneratedFitBspline(DG):
    __slots__ = ()

    NODE_TYPE = "fitBspline"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    tolerance = DoubleLinearField(default_value=0.1, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    keepRange = KeepRangeEnumField(default_value=1)
    kr = keepRange
