# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.make_nurb_circle import (
    CenterField,
    FirstField,
    NormalField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class DegreeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3


class DegreeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3

    NAME_MAP = {
        LINEAR: "Linear",
        CUBIC: "Cubic",
    }


class DegreeEnumField(
    EnumField[DegreeEnumAttrOperator, DegreeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeEnumAttrOperator
    PLUG_CLS = DegreeEnumPlugOperator


class _GeneratedMakeNurbCircle(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbCircle"

    first = FirstField(default_value=(1.0, 0.0, 0.0))
    fp = first
    firstPointX = first.firstPointX
    fpx = firstPointX
    firstPointY = first.firstPointY
    fpy = firstPointY
    firstPointZ = first.firstPointZ
    fpz = firstPointZ

    normal = NormalField(default_value=(0.0, 0.0, 1.0))
    nr = normal
    normalX = normal.normalX
    nrx = normalX
    normalY = normal.normalY
    nry = normalY
    normalZ = normal.normalZ
    nrz = normalZ

    center = CenterField(default_value=(0.0, 0.0, 0.0))
    c = center
    centerX = center.centerX
    cx = centerX
    centerY = center.centerY
    cy = centerY
    centerZ = center.centerZ
    cz = centerZ

    radius = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    r = radius

    sweep = DoubleAngleField(default_value=360.0, soft_min_value=0.0, soft_max_value=360.0)
    sw = sweep

    useTolerance = BoolField(default_value=False)
    ut = useTolerance

    degree = DegreeEnumField(default_value=3)
    d = degree

    sections = LongField(default_value=8, min_value=1, soft_max_value=100)
    s = sections

    tolerance = DoubleLinearField(default_value=0.01, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    fixCenter = BoolField(default_value=True)
    fc = fixCenter

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
