# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class _GeneratedTrim(DG):
    __slots__ = ()

    NODE_TYPE = "trim"

    inputCurve = DataNurbsCurveField(multi=True)
    ic = inputCurve

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    locatorU = DoubleField(multi=True, default_value=0.5)
    lu = locatorU

    locatorV = DoubleField(multi=True, default_value=0.5)
    lv = locatorV

    selected = SelectedEnumField(default_value=0)
    sl = selected

    shrink = BoolField(default_value=False)
    sh = shrink

    tolerance = DoubleLinearField(default_value=0.001, soft_min_value=0.0001, soft_max_value=1.0)
    tol = tolerance

    usedCurves = BoolField(multi=True, default_value=False, writable=False)
    uc = usedCurves

    splitSurface = DataNurbsSurfaceField(writable=False)
    ss = splitSurface

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    shouldBeLast = BoolField(default_value=True, writable=False)
    sbl = shouldBeLast
