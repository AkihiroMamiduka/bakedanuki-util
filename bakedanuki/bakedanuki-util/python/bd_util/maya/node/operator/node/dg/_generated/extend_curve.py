# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.extend_curve import InputPointField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class _GeneratedExtendCurve(DG):
    __slots__ = ()

    NODE_TYPE = "extendCurve"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    inputPoint = InputPointField(default_value=(0.0, 0.0, 0.0))
    ip = inputPoint
    pointX = inputPoint.pointX
    px = pointX
    pointY = inputPoint.pointY
    py = pointY
    pointZ = inputPoint.pointZ
    pz = pointZ

    extensionType = ExtensionTypeEnumField(default_value=0)
    et = extensionType

    extendMethod = ExtendMethodEnumField(default_value=0)
    em = extendMethod

    start = StartEnumField(default_value=1)
    s = start

    bothEnds = BoolField(default_value=False, readable=False)
    be = bothEnds

    join = BoolField(default_value=True)
    jn = join

    distance = DoubleLinearField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=20.0)
    d = distance

    removeMultipleKnots = BoolField(default_value=False)
    rmk = removeMultipleKnots

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
