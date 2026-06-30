# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


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


class RebuildCurve(DG):
    __slots__ = ()

    NODE_TYPE = "rebuildCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    matchCurve = DataNurbsCurveField()
    mc = matchCurve

    fitRebuild = BoolField()
    fr = fitRebuild

    rebuildType = RebuildTypeEnumField()
    rt = rebuildType

    spans = LongField()
    s = spans

    degree = DegreeEnumField()
    d = degree

    tolerance = DoubleLinearField()
    tol = tolerance

    endKnots = EndKnotsEnumField()
    end = endKnots

    keepRange = KeepRangeEnumField()
    kr = keepRange

    keepEndPoints = BoolField()
    kep = keepEndPoints

    keepTangents = BoolField()
    kt = keepTangents

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    keepControlPoints = BoolField()
    kcp = keepControlPoints

    smartSurfaceCurveRebuild = BoolField()
    scr = smartSurfaceCurveRebuild

    smooth = DoubleLinearField()
    sm = smooth
