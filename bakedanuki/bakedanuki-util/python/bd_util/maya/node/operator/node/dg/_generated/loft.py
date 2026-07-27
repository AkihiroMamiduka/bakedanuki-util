# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class GeneratedLoft(DG):
    __slots__ = ()

    NODE_TYPE = "loft"

    inputCurve = DataNurbsCurveField(multi=True)
    ic = inputCurve

    uniform = BoolField(default_value=False)
    u = uniform

    close = BoolField(default_value=False)
    c = close

    degree = DegreeEnumField(default_value=3)
    d = degree

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    autoReverse = BoolField(default_value=True)
    ar = autoReverse

    reverse = BoolField(multi=True, default_value=False)
    r = reverse

    reverseSurfaceNormals = BoolField(default_value=False)
    rsn = reverseSurfaceNormals

    sectionSpans = LongField(default_value=1, min_value=1, soft_min_value=1, soft_max_value=10)
    ss = sectionSpans

    createCusp = BoolField(multi=True, default_value=False)
    cc = createCusp
