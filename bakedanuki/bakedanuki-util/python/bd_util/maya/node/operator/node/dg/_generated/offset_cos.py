# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class ConnectBreaksEnumPlugOperator(EnumPlugOperator["ConnectBreaksEnumAttrOperator"]):
    __slots__ = ()

    OFF = 0
    CIRCULAR = 1
    LINEAR = 2


class ConnectBreaksEnumAttrOperator(EnumAttrOperator[ConnectBreaksEnumPlugOperator]):
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


class GeneratedOffsetCos(DG):
    __slots__ = ()

    NODE_TYPE = "offsetCos"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    cutLoop = BoolField(default_value=False)
    cl = cutLoop

    connectBreaks = ConnectBreaksEnumField(default_value=2)
    cb = connectBreaks

    distance = DoubleLinearField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    d = distance

    tolerance = DoubleLinearField(default_value=0.01, min_value=0.0001, soft_min_value=0.001, soft_max_value=0.5)
    tol = tolerance

    subdivisionDensity = LongField(default_value=5, min_value=0, max_value=100, soft_max_value=10)
    sd = subdivisionDensity

    checkPoints = ShortField(default_value=3, min_value=1, max_value=100, soft_max_value=10)
    cp = checkPoints

    stitch = BoolField(default_value=True)
    st = stitch

    outputCurve = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurve
