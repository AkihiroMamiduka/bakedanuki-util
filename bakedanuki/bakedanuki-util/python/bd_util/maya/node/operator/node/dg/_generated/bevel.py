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


class _GeneratedBevel(DG):
    __slots__ = ()

    NODE_TYPE = "bevel"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    useDirectionCurve = DataNurbsCurveField()
    udc = useDirectionCurve

    outputSurface1 = DataNurbsSurfaceField(writable=False)
    os1 = outputSurface1

    outputSurface2 = DataNurbsSurfaceField(writable=False)
    os2 = outputSurface2

    outputSurface3 = DataNurbsSurfaceField(writable=False)
    os3 = outputSurface3

    tolerance = DoubleLinearField(default_value=0.01, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    width = DoubleLinearField(default_value=0.5, soft_min_value=0.0, soft_max_value=10.0)
    w = width

    depth = DoubleLinearField(default_value=0.5, soft_min_value=0.0, soft_max_value=10.0)
    d = depth

    extrudeDepth = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    ed = extrudeDepth

    cornerType = CornerTypeEnumField(default_value=2)
    ct = cornerType

    numberOfSides = LongField(default_value=4, min_value=1, max_value=4)
    ns = numberOfSides

    bevelShapeType = BevelShapeTypeEnumField(default_value=1)
    bst = bevelShapeType

    joinSurfaces = BoolField(default_value=True)
    js = joinSurfaces
