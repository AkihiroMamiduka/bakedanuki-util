# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.dt.nurbs_curve import DataNurbsCurveField


class EdgePlugOperator(
    CompoundPlugOperator["EdgeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputCurveA", "ica"),
        ("inputCurveB", "icb"),
        ("inSurfIdxA", "isa"),
        ("inSurfIdxB", "isb"),
        ("edgeValid", "ev"),
    )

    inputCurveA = DataNurbsCurveField()
    ica = inputCurveA

    inputCurveB = DataNurbsCurveField()
    icb = inputCurveB

    inSurfIdxA = LongField()
    isa = inSurfIdxA

    inSurfIdxB = LongField()
    isb = inSurfIdxB

    edgeValid = BoolField()
    ev = edgeValid


class EdgeAttrOperator(
    CompoundAttrOperator[EdgePlugOperator]
):
    __slots__ = ()

    inputCurveA = DataNurbsCurveField()
    ica = inputCurveA

    inputCurveB = DataNurbsCurveField()
    icb = inputCurveB

    inSurfIdxA = LongField()
    isa = inSurfIdxA

    inSurfIdxB = LongField()
    isb = inSurfIdxB

    edgeValid = BoolField()
    ev = edgeValid


class EdgeField(
    CompoundField[EdgeAttrOperator, EdgePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeAttrOperator
    PLUG_CLS = EdgePlugOperator
