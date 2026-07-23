# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class StyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STRAIGHT_OUT = 0
    STRAIGHT_IN = 1
    CONVEX_OUT = 2
    CONVEX_IN = 3
    CONCAVE_OUT = 4
    CONCAVE_IN = 5
    STRAIGHT_SIDE_EDGE = 6
    STRAIGHT_FRONT_EDGE = 7
    STRAIGHT_CORNER = 8
    CONVEX_SIDE_EDGE = 9
    CONVEX_FRONT_EDGE = 10
    CONVEX_CORNER = 11
    CONCAVE_SIDE_EDGE = 12
    CONCAVE_FRONT_EDGE = 13
    CONVEX_CREASE = 14


class StyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STRAIGHT_OUT = 0
    STRAIGHT_IN = 1
    CONVEX_OUT = 2
    CONVEX_IN = 3
    CONCAVE_OUT = 4
    CONCAVE_IN = 5
    STRAIGHT_SIDE_EDGE = 6
    STRAIGHT_FRONT_EDGE = 7
    STRAIGHT_CORNER = 8
    CONVEX_SIDE_EDGE = 9
    CONVEX_FRONT_EDGE = 10
    CONVEX_CORNER = 11
    CONCAVE_SIDE_EDGE = 12
    CONCAVE_FRONT_EDGE = 13
    CONVEX_CREASE = 14

    NAME_MAP = {
        STRAIGHT_OUT: "Straight Out",
        STRAIGHT_IN: "Straight In",
        CONVEX_OUT: "Convex Out",
        CONVEX_IN: "Convex In",
        CONCAVE_OUT: "Concave Out",
        CONCAVE_IN: "Concave In",
        STRAIGHT_SIDE_EDGE: "Straight Side Edge",
        STRAIGHT_FRONT_EDGE: "Straight Front Edge",
        STRAIGHT_CORNER: "Straight Corner",
        CONVEX_SIDE_EDGE: "Convex Side Edge",
        CONVEX_FRONT_EDGE: "Convex Front Edge",
        CONVEX_CORNER: "Convex Corner",
        CONCAVE_SIDE_EDGE: "Concave Side Edge",
        CONCAVE_FRONT_EDGE: "Concave Front Edge",
        CONVEX_CREASE: "Convex Crease",
    }


class StyleEnumField(
    EnumField[StyleEnumAttrOperator, StyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StyleEnumAttrOperator
    PLUG_CLS = StyleEnumPlugOperator


class _GeneratedStyleCurve(DG):
    __slots__ = ()

    NODE_TYPE = "styleCurve"

    style = StyleEnumField(default_value=0)
    s = style

    outCurve = DataNurbsCurveField(writable=False)
    oc = outCurve
