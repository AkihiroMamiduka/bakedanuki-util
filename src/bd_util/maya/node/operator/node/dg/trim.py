# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SelectedEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    KEEP = 0
    DISCARD = 1


class SelectedEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    KEEP = 0
    DISCARD = 1

    NAME_MAP = {
        KEEP: "Keep",
        DISCARD: "Discard",
    }


class SelectedEnumField(
    EnumField[SelectedEnumAttrOperator, SelectedEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelectedEnumAttrOperator
    PLUG_CLS = SelectedEnumPlugOperator


class Trim(DG):
    __slots__ = ()

    NODE_TYPE = "trim"

    inputCurve = DataNurbsCurveField(multi=True)
    ic = inputCurve

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    locatorU = DoubleField(multi=True)
    lu = locatorU

    locatorV = DoubleField(multi=True)
    lv = locatorV

    selected = SelectedEnumField()
    sl = selected

    shrink = BoolField()
    sh = shrink

    tolerance = DoubleLinearField()
    tol = tolerance

    usedCurves = BoolField(multi=True)
    uc = usedCurves

    splitSurface = DataNurbsSurfaceField()
    ss = splitSurface

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    shouldBeLast = BoolField()
    sbl = shouldBeLast
