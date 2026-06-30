# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class ConnectBreaksEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    CIRCULAR = 1
    LINEAR = 2


class ConnectBreaksEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    CIRCULAR = 1
    LINEAR = 2

    NAME_MAP = {
        OFF: "Off",
        CIRCULAR: "Circular",
        LINEAR: "Linear",
    }


class ConnectBreaksEnumField(
    EnumField[ConnectBreaksEnumAttrOperator, ConnectBreaksEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConnectBreaksEnumAttrOperator
    PLUG_CLS = ConnectBreaksEnumPlugOperator


class OffsetCos(DG):
    __slots__ = ()

    NODE_TYPE = "offsetCos"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    cutLoop = BoolField()
    cl = cutLoop

    connectBreaks = ConnectBreaksEnumField()
    cb = connectBreaks

    distance = DoubleLinearField()
    d = distance

    tolerance = DoubleLinearField()
    tol = tolerance

    subdivisionDensity = LongField()
    sd = subdivisionDensity

    checkPoints = ShortField()
    cp = checkPoints

    stitch = BoolField()
    st = stitch

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve
