# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class RebuildTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNIFORM = 0
    REDUCE_SPANS = 1
    MATCH_KNOTS = 2
    NO_MULTS = 3
    CURVATURE = 4
    END_CONDITIONS = 5
    CLEAN = 6


class RebuildTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNIFORM = 0
    REDUCE_SPANS = 1
    MATCH_KNOTS = 2
    NO_MULTS = 3
    CURVATURE = 4
    END_CONDITIONS = 5
    CLEAN = 6

    NAME_MAP = {
        UNIFORM: "Uniform",
        REDUCE_SPANS: "Reduce Spans",
        MATCH_KNOTS: "Match Knots",
        NO_MULTS: "No Mults",
        CURVATURE: "Curvature",
        END_CONDITIONS: "End Conditions",
        CLEAN: "Clean",
    }


class RebuildTypeEnumField(
    EnumField[RebuildTypeEnumAttrOperator, RebuildTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RebuildTypeEnumAttrOperator
    PLUG_CLS = RebuildTypeEnumPlugOperator


class DegreeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7


class DegreeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7

    NAME_MAP = {
        LINEAR: "Linear",
        QUADRATIC: "Quadratic",
        CUBIC: "Cubic",
        QUINTIC: "Quintic",
        HEPTIC: "Heptic",
    }


class DegreeEnumField(
    EnumField[DegreeEnumAttrOperator, DegreeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeEnumAttrOperator
    PLUG_CLS = DegreeEnumPlugOperator


class EndKnotsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NON_MULTIPLE_END_KNOTS = 0
    MULTIPLE_END_KNOTS = 1


class EndKnotsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NON_MULTIPLE_END_KNOTS = 0
    MULTIPLE_END_KNOTS = 1

    NAME_MAP = {
        NON_MULTIPLE_END_KNOTS: "Non Multiple end knots",
        MULTIPLE_END_KNOTS: "Multiple end knots",
    }


class EndKnotsEnumField(
    EnumField[EndKnotsEnumAttrOperator, EndKnotsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EndKnotsEnumAttrOperator
    PLUG_CLS = EndKnotsEnumPlugOperator


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


class _GeneratedRebuildCurve(DG):
    __slots__ = ()

    NODE_TYPE = "rebuildCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    matchCurve = DataNurbsCurveField()
    mc = matchCurve

    fitRebuild = BoolField(default_value=True)
    fr = fitRebuild

    rebuildType = RebuildTypeEnumField(default_value=0)
    rt = rebuildType

    spans = LongField(default_value=4, min_value=1, soft_max_value=100)
    s = spans

    degree = DegreeEnumField(default_value=3)
    d = degree

    tolerance = DoubleLinearField(default_value=0.01, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    endKnots = EndKnotsEnumField(default_value=0)
    end = endKnots

    keepRange = KeepRangeEnumField(default_value=1)
    kr = keepRange

    keepEndPoints = BoolField(default_value=True)
    kep = keepEndPoints

    keepTangents = BoolField(default_value=True)
    kt = keepTangents

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    keepControlPoints = BoolField(default_value=False)
    kcp = keepControlPoints

    smartSurfaceCurveRebuild = BoolField(default_value=False)
    scr = smartSurfaceCurveRebuild

    smooth = DoubleLinearField(default_value=-3.0, min_value=-3.0, soft_max_value=5.0)
    sm = smooth
