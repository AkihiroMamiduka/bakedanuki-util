# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.long import LongField
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

    inputCurveA = DataNurbsCurveField(multi=True)
    ica = inputCurveA

    inputCurveB = DataNurbsCurveField(multi=True)
    icb = inputCurveB

    inSurfIdxA = LongField(multi=True, default_value=123456)
    isa = inSurfIdxA

    inSurfIdxB = LongField(multi=True, default_value=123456)
    isb = inSurfIdxB

    edgeValid = BoolField(default_value=True)
    ev = edgeValid


class EdgeAttrOperator(
    CompoundAttrOperator[EdgePlugOperator]
):
    __slots__ = ()

    inputCurveA = DataNurbsCurveField(multi=True)
    ica = inputCurveA

    inputCurveB = DataNurbsCurveField(multi=True)
    icb = inputCurveB

    inSurfIdxA = LongField(multi=True, default_value=123456)
    isa = inSurfIdxA

    inSurfIdxB = LongField(multi=True, default_value=123456)
    isb = inSurfIdxB

    edgeValid = BoolField(default_value=True)
    ev = edgeValid


class EdgeField(
    CompoundField[EdgeAttrOperator, EdgePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeAttrOperator
    PLUG_CLS = EdgePlugOperator
