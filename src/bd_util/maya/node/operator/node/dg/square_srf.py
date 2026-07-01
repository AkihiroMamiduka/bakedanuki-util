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
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class SquareSrf(DG):
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

    endPointTolerance = DoubleLinearField()
    ept = endPointTolerance

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    curveFitCheckpoints = LongField()
    cfc = curveFitCheckpoints

    continuityType1 = ContinuityType1EnumField()
    ct1 = continuityType1

    continuityType2 = ContinuityType2EnumField()
    ct2 = continuityType2

    continuityType3 = ContinuityType3EnumField()
    ct3 = continuityType3

    continuityType4 = ContinuityType4EnumField()
    ct4 = continuityType4

    rebuildCurve1 = BoolField()
    rc1 = rebuildCurve1

    rebuildCurve2 = BoolField()
    rc2 = rebuildCurve2

    rebuildCurve3 = BoolField()
    rc3 = rebuildCurve3

    rebuildCurve4 = BoolField()
    rc4 = rebuildCurve4

    continuityPassed1 = BoolField()
    cp1 = continuityPassed1

    continuityPassed2 = BoolField()
    cp2 = continuityPassed2

    continuityPassed3 = BoolField()
    cp3 = continuityPassed3

    continuityPassed4 = BoolField()
    cp4 = continuityPassed4
