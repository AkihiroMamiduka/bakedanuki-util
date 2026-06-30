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


class CornerTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    CIRCULAR = 2


class CornerTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 1
    CIRCULAR = 2

    NAME_MAP = {
        LINEAR: "Linear",
        CIRCULAR: "Circular",
    }


class CornerTypeEnumField(
    EnumField[CornerTypeEnumAttrOperator, CornerTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CornerTypeEnumAttrOperator
    PLUG_CLS = CornerTypeEnumPlugOperator


class BevelShapeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STRAIGHT_CUT = 1
    CURVE_OUT = 2
    CURVE_IN = 3


class BevelShapeTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STRAIGHT_CUT = 1
    CURVE_OUT = 2
    CURVE_IN = 3

    NAME_MAP = {
        STRAIGHT_CUT: "Straight Cut",
        CURVE_OUT: "Curve Out",
        CURVE_IN: "Curve In",
    }


class BevelShapeTypeEnumField(
    EnumField[BevelShapeTypeEnumAttrOperator, BevelShapeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BevelShapeTypeEnumAttrOperator
    PLUG_CLS = BevelShapeTypeEnumPlugOperator


class Bevel(DG):
    __slots__ = ()

    NODE_TYPE = "bevel"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    useDirectionCurve = DataNurbsCurveField()
    udc = useDirectionCurve

    outputSurface1 = DataNurbsSurfaceField()
    os1 = outputSurface1

    outputSurface2 = DataNurbsSurfaceField()
    os2 = outputSurface2

    outputSurface3 = DataNurbsSurfaceField()
    os3 = outputSurface3

    tolerance = DoubleLinearField()
    tol = tolerance

    width = DoubleLinearField()
    w = width

    depth = DoubleLinearField()
    d = depth

    extrudeDepth = DoubleLinearField()
    ed = extrudeDepth

    cornerType = CornerTypeEnumField()
    ct = cornerType

    numberOfSides = LongField()
    ns = numberOfSides

    bevelShapeType = BevelShapeTypeEnumField()
    bst = bevelShapeType

    joinSurfaces = BoolField()
    js = joinSurfaces
