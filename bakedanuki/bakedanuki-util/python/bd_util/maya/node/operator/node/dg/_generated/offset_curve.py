# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.offset_curve import NormalField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
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


class GeneratedOffsetCurve(DG):
    __slots__ = ()

    NODE_TYPE = "offsetCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    connectBreaks = ConnectBreaksEnumField(default_value=2)
    cb = connectBreaks

    reparameterize = BoolField(default_value=False)
    rp = reparameterize

    stitch = BoolField(default_value=True)
    st = stitch

    cutLoop = BoolField(default_value=False)
    cl = cutLoop

    cutRadius = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=0.1)
    cr = cutRadius

    distance = DoubleLinearField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    d = distance

    tolerance = DoubleLinearField(default_value=0.01, min_value=0.0001, soft_min_value=0.001, soft_max_value=0.5)
    tol = tolerance

    subdivisionDensity = LongField(default_value=5, min_value=0, max_value=100, soft_max_value=10)
    sd = subdivisionDensity

    useGivenNormal = BoolField(default_value=True)
    ugn = useGivenNormal

    normal = NormalField(default_value=(0.0, 1.0, 0.0))
    nr = normal
    normalX = normal.normalX
    nrx = normalX
    normalY = normal.normalY
    nry = normalY
    normalZ = normal.normalZ
    nrz = normalZ

    parameter = DoubleField(default_value=0.0)
    p = parameter

    useParameter = BoolField(default_value=False)
    up = useParameter

    outputCurve = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurve
