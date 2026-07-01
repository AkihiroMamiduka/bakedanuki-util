# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.offset_curve import NormalField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
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


class OffsetCurve(DG):
    __slots__ = ()

    NODE_TYPE = "offsetCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    connectBreaks = ConnectBreaksEnumField()
    cb = connectBreaks

    reparameterize = BoolField()
    rp = reparameterize

    stitch = BoolField()
    st = stitch

    cutLoop = BoolField()
    cl = cutLoop

    cutRadius = DoubleLinearField()
    cr = cutRadius

    distance = DoubleLinearField()
    d = distance

    tolerance = DoubleLinearField()
    tol = tolerance

    subdivisionDensity = LongField()
    sd = subdivisionDensity

    useGivenNormal = BoolField()
    ugn = useGivenNormal

    normal = NormalField()
    nr = normal
    normalX = normal.normalX
    nrx = normalX
    normalY = normal.normalY
    nry = normalY
    normalZ = normal.normalZ
    nrz = normalZ

    parameter = DoubleField()
    p = parameter

    useParameter = BoolField()
    up = useParameter

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve
