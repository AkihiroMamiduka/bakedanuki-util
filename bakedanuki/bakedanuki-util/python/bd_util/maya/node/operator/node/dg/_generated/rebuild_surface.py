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
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class RebuildTypeEnumPlugOperator(EnumPlugOperator["RebuildTypeEnumAttrOperator"]):
    __slots__ = ()

    UNIFORM = 0
    REDUCE_SPANS = 1
    MATCH_KNOTS = 2
    NO_MULTS = 3
    NON_MINUS_RATIONAL = 4
    END_CONDITIONS = 5
    TRIM_CONVERT = 6
    BEZIER = 7


class RebuildTypeEnumAttrOperator(EnumAttrOperator[RebuildTypeEnumPlugOperator]):
    __slots__ = ()

    UNIFORM = 0
    REDUCE_SPANS = 1
    MATCH_KNOTS = 2
    NO_MULTS = 3
    NON_MINUS_RATIONAL = 4
    END_CONDITIONS = 5
    TRIM_CONVERT = 6
    BEZIER = 7

    NAME_MAP = {
        UNIFORM: "Uniform",
        REDUCE_SPANS: "Reduce Spans",
        MATCH_KNOTS: "Match Knots",
        NO_MULTS: "No Mults",
        NON_MINUS_RATIONAL: "Non-rational",
        END_CONDITIONS: "End Conditions",
        TRIM_CONVERT: "Trim Convert",
        BEZIER: "Bezier",
    }


class RebuildTypeEnumField(
    EnumField[RebuildTypeEnumAttrOperator, RebuildTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RebuildTypeEnumAttrOperator
    PLUG_CLS = RebuildTypeEnumPlugOperator


class DirectionEnumPlugOperator(EnumPlugOperator["DirectionEnumAttrOperator"]):
    __slots__ = ()

    U = 0
    V = 1
    U_RREBUILDSURFACEBOTH_V = 2


class DirectionEnumAttrOperator(EnumAttrOperator[DirectionEnumPlugOperator]):
    __slots__ = ()

    U = 0
    V = 1
    U_RREBUILDSURFACEBOTH_V = 2

    NAME_MAP = {
        U: "U",
        V: "V",
        U_RREBUILDSURFACEBOTH_V: "U rRebuildSurfaceBoth V",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class DegreeUEnumPlugOperator(EnumPlugOperator["DegreeUEnumAttrOperator"]):
    __slots__ = ()

    ORIGINAL = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7


class DegreeUEnumAttrOperator(EnumAttrOperator[DegreeUEnumPlugOperator]):
    __slots__ = ()

    ORIGINAL = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7

    NAME_MAP = {
        ORIGINAL: "Original",
        LINEAR: "Linear",
        QUADRATIC: "Quadratic",
        CUBIC: "Cubic",
        QUINTIC: "Quintic",
        HEPTIC: "Heptic",
    }


class DegreeUEnumField(
    EnumField[DegreeUEnumAttrOperator, DegreeUEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeUEnumAttrOperator
    PLUG_CLS = DegreeUEnumPlugOperator


class DegreeVEnumPlugOperator(EnumPlugOperator["DegreeVEnumAttrOperator"]):
    __slots__ = ()

    ORIGINAL = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7


class DegreeVEnumAttrOperator(EnumAttrOperator[DegreeVEnumPlugOperator]):
    __slots__ = ()

    ORIGINAL = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7

    NAME_MAP = {
        ORIGINAL: "Original",
        LINEAR: "Linear",
        QUADRATIC: "Quadratic",
        CUBIC: "Cubic",
        QUINTIC: "Quintic",
        HEPTIC: "Heptic",
    }


class DegreeVEnumField(
    EnumField[DegreeVEnumAttrOperator, DegreeVEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeVEnumAttrOperator
    PLUG_CLS = DegreeVEnumPlugOperator


class EndKnotsEnumPlugOperator(EnumPlugOperator["EndKnotsEnumAttrOperator"]):
    __slots__ = ()

    NON_MULTIPLE_END_KNOTS = 0
    MULTIPLE_END_KNOTS = 1


class EndKnotsEnumAttrOperator(EnumAttrOperator[EndKnotsEnumPlugOperator]):
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


class FitRebuildEnumPlugOperator(EnumPlugOperator["FitRebuildEnumAttrOperator"]):
    __slots__ = ()

    CONVERT_CLASSIC = 0
    FIT_LEAST_SQUARES = 1
    CONVERT_OPEN = 2
    CONVERT_GRID = 3


class FitRebuildEnumAttrOperator(EnumAttrOperator[FitRebuildEnumPlugOperator]):
    __slots__ = ()

    CONVERT_CLASSIC = 0
    FIT_LEAST_SQUARES = 1
    CONVERT_OPEN = 2
    CONVERT_GRID = 3

    NAME_MAP = {
        CONVERT_CLASSIC: "Convert Classic",
        FIT_LEAST_SQUARES: "Fit (Least Squares)",
        CONVERT_OPEN: "Convert Open",
        CONVERT_GRID: "Convert Grid",
    }


class FitRebuildEnumField(
    EnumField[FitRebuildEnumAttrOperator, FitRebuildEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FitRebuildEnumAttrOperator
    PLUG_CLS = FitRebuildEnumPlugOperator


class GeneratedRebuildSurface(DG):
    __slots__ = ()

    NODE_TYPE = "rebuildSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    matchSurface = DataNurbsSurfaceField()
    ms = matchSurface

    rebuildType = RebuildTypeEnumField(default_value=0)
    rt = rebuildType

    direction = DirectionEnumField(default_value=2)
    dir = direction

    spansU = LongField(default_value=4, min_value=0, soft_max_value=100)
    su = spansU

    spansV = LongField(default_value=4, min_value=0, soft_max_value=100)
    sv = spansV

    degreeU = DegreeUEnumField(default_value=3)
    du = degreeU

    degreeV = DegreeVEnumField(default_value=3)
    dv = degreeV

    tolerance = DoubleLinearField(default_value=0.01, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    endKnots = EndKnotsEnumField(default_value=0)
    end = endKnots

    keepCorners = BoolField(default_value=True)
    kc = keepCorners

    keepRange = KeepRangeEnumField(default_value=1)
    kr = keepRange

    keepControlPoints = BoolField(default_value=False)
    kcp = keepControlPoints

    fitRebuild = FitRebuildEnumField(default_value=0)
    fr = fitRebuild

    oldRebuildRational = BoolField(default_value=False)
    orr = oldRebuildRational

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
