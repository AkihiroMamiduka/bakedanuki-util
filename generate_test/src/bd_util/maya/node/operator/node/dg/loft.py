# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class Loft(DG):
    __slots__ = ()

    NODE_TYPE = "loft"

    inputCurve = DataNurbsCurveField(multi=True)
    ic = inputCurve

    uniform = BoolField()
    u = uniform

    close = BoolField()
    c = close

    degree = DegreeEnumField()
    d = degree

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    autoReverse = BoolField()
    ar = autoReverse

    reverse = BoolField(multi=True)
    r = reverse

    reverseSurfaceNormals = BoolField()
    rsn = reverseSurfaceNormals

    sectionSpans = LongField()
    ss = sectionSpans

    createCusp = BoolField(multi=True)
    cc = createCusp
