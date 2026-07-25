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
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class ContinuityType1EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3


class ContinuityType1EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3

    NAME_MAP = {
        FIXED_BOUNDARY: "Fixed Boundary",
        TANGENT: "Tangent",
        IMPLIED_TANGENT: "Implied Tangent",
    }


class ContinuityType1EnumField(
    EnumField[ContinuityType1EnumAttrOperator, ContinuityType1EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContinuityType1EnumAttrOperator
    PLUG_CLS = ContinuityType1EnumPlugOperator


class ContinuityType2EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3


class ContinuityType2EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3

    NAME_MAP = {
        FIXED_BOUNDARY: "Fixed Boundary",
        TANGENT: "Tangent",
        IMPLIED_TANGENT: "Implied Tangent",
    }


class ContinuityType2EnumField(
    EnumField[ContinuityType2EnumAttrOperator, ContinuityType2EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContinuityType2EnumAttrOperator
    PLUG_CLS = ContinuityType2EnumPlugOperator


class ContinuityType3EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3


class ContinuityType3EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3

    NAME_MAP = {
        FIXED_BOUNDARY: "Fixed Boundary",
        TANGENT: "Tangent",
        IMPLIED_TANGENT: "Implied Tangent",
    }


class ContinuityType3EnumField(
    EnumField[ContinuityType3EnumAttrOperator, ContinuityType3EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContinuityType3EnumAttrOperator
    PLUG_CLS = ContinuityType3EnumPlugOperator


class ContinuityType4EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3


class ContinuityType4EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED_BOUNDARY = 1
    TANGENT = 2
    IMPLIED_TANGENT = 3

    NAME_MAP = {
        FIXED_BOUNDARY: "Fixed Boundary",
        TANGENT: "Tangent",
        IMPLIED_TANGENT: "Implied Tangent",
    }


class ContinuityType4EnumField(
    EnumField[ContinuityType4EnumAttrOperator, ContinuityType4EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContinuityType4EnumAttrOperator
    PLUG_CLS = ContinuityType4EnumPlugOperator


class _GeneratedSquareSrf(DG):
    __slots__ = ()

    NODE_TYPE = "squareSrf"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    inputCurve3 = DataNurbsCurveField()
    ic3 = inputCurve3

    inputCurve4 = DataNurbsCurveField()
    ic4 = inputCurve4

    endPointTolerance = DoubleLinearField(default_value=0.1, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    ept = endPointTolerance

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    curveFitCheckpoints = LongField(default_value=5, min_value=1, max_value=100)
    cfc = curveFitCheckpoints

    continuityType1 = ContinuityType1EnumField(default_value=2)
    ct1 = continuityType1

    continuityType2 = ContinuityType2EnumField(default_value=2)
    ct2 = continuityType2

    continuityType3 = ContinuityType3EnumField(default_value=2)
    ct3 = continuityType3

    continuityType4 = ContinuityType4EnumField(default_value=2)
    ct4 = continuityType4

    rebuildCurve1 = BoolField(default_value=False)
    rc1 = rebuildCurve1

    rebuildCurve2 = BoolField(default_value=False)
    rc2 = rebuildCurve2

    rebuildCurve3 = BoolField(default_value=False)
    rc3 = rebuildCurve3

    rebuildCurve4 = BoolField(default_value=False)
    rc4 = rebuildCurve4

    continuityPassed1 = BoolField(default_value=False, writable=False)
    cp1 = continuityPassed1

    continuityPassed2 = BoolField(default_value=False, writable=False)
    cp2 = continuityPassed2

    continuityPassed3 = BoolField(default_value=False, writable=False)
    cp3 = continuityPassed3

    continuityPassed4 = BoolField(default_value=False, writable=False)
    cp4 = continuityPassed4
