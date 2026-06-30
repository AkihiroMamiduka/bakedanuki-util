# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.extend_curve import InputPointField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class ExtensionTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    CIRCULAR = 1
    EXTRAPOLATE = 2


class ExtensionTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    CIRCULAR = 1
    EXTRAPOLATE = 2

    NAME_MAP = {
        LINEAR: "Linear",
        CIRCULAR: "Circular",
        EXTRAPOLATE: "Extrapolate",
    }


class ExtensionTypeEnumField(
    EnumField[ExtensionTypeEnumAttrOperator, ExtensionTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtensionTypeEnumAttrOperator
    PLUG_CLS = ExtensionTypeEnumPlugOperator


class ExtendMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISTANCE = 0
    POINT = 2


class ExtendMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISTANCE = 0
    POINT = 2

    NAME_MAP = {
        DISTANCE: "Distance",
        POINT: "Point",
    }


class ExtendMethodEnumField(
    EnumField[ExtendMethodEnumAttrOperator, ExtendMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtendMethodEnumAttrOperator
    PLUG_CLS = ExtendMethodEnumPlugOperator


class StartEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    END = 0
    START = 1
    BOTH = 2


class StartEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    END = 0
    START = 1
    BOTH = 2

    NAME_MAP = {
        END: "End",
        START: "Start",
        BOTH: "Both",
    }


class StartEnumField(
    EnumField[StartEnumAttrOperator, StartEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StartEnumAttrOperator
    PLUG_CLS = StartEnumPlugOperator


class ExtendCurve(DG):
    __slots__ = ()

    NODE_TYPE = "extendCurve"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    inputPoint = InputPointField()
    ip = inputPoint
    pointX = inputPoint.pointX
    px = pointX
    pointY = inputPoint.pointY
    py = pointY
    pointZ = inputPoint.pointZ
    pz = pointZ

    extensionType = ExtensionTypeEnumField()
    et = extensionType

    extendMethod = ExtendMethodEnumField()
    em = extendMethod

    start = StartEnumField()
    s = start

    bothEnds = BoolField()
    be = bothEnds

    join = BoolField()
    jn = join

    distance = DoubleLinearField()
    d = distance

    removeMultipleKnots = BoolField()
    rmk = removeMultipleKnots

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
