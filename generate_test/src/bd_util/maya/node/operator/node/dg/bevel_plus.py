# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.bevel_plus import PositionField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class PolyOutMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    COUNT = 0
    SAMPLING = 2


class PolyOutMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    COUNT = 0
    SAMPLING = 2

    NAME_MAP = {
        COUNT: "Count",
        SAMPLING: "Sampling",
    }


class PolyOutMethodEnumField(
    EnumField[PolyOutMethodEnumAttrOperator, PolyOutMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolyOutMethodEnumAttrOperator
    PLUG_CLS = PolyOutMethodEnumPlugOperator


class PolyOutExtrusionTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    COMPLETE_EXTRUSION = 2
    EXTRUSION_SECTION = 3


class PolyOutExtrusionTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    COMPLETE_EXTRUSION = 2
    EXTRUSION_SECTION = 3

    NAME_MAP = {
        COMPLETE_EXTRUSION: "Complete Extrusion",
        EXTRUSION_SECTION: "Extrusion Section",
    }


class PolyOutExtrusionTypeEnumField(
    EnumField[PolyOutExtrusionTypeEnumAttrOperator, PolyOutExtrusionTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolyOutExtrusionTypeEnumAttrOperator
    PLUG_CLS = PolyOutExtrusionTypeEnumPlugOperator


class PolyOutCurveTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    COMPLETE_CURVE = 2
    CURVE_SPAN = 3


class PolyOutCurveTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    COMPLETE_CURVE = 2
    CURVE_SPAN = 3

    NAME_MAP = {
        COMPLETE_CURVE: "Complete Curve",
        CURVE_SPAN: "Curve Span",
    }


class PolyOutCurveTypeEnumField(
    EnumField[PolyOutCurveTypeEnumAttrOperator, PolyOutCurveTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolyOutCurveTypeEnumAttrOperator
    PLUG_CLS = PolyOutCurveTypeEnumPlugOperator


class BevelPlus(DG):
    __slots__ = ()

    NODE_TYPE = "bevelPlus"

    inputCurves = DataNurbsCurveField(multi=True)
    ics = inputCurves

    outerStyleCurve = DataNurbsCurveField()
    osc = outerStyleCurve

    innerStyleCurve = DataNurbsCurveField()
    isc = innerStyleCurve

    outputPoly = DataMeshField()
    op = outputPoly

    startCapSurface = DataNurbsSurfaceField()
    scs = startCapSurface

    endCapSurface = DataNurbsSurfaceField()
    ecs = endCapSurface

    outputSurfaces = DataNurbsSurfaceField(multi=True)
    os1 = outputSurfaces

    bevelInside = BoolField()
    bin = bevelInside

    count = LongField(multi=True)
    c = count

    position = PositionField(multi=True)
    p = position

    tolerance = DoubleLinearField()
    tol = tolerance

    width = DoubleLinearField()
    w = width

    depth = DoubleLinearField()
    d = depth

    extrudeDepth = DoubleLinearField()
    ed = extrudeDepth

    numberOfSides = LongField()
    ns = numberOfSides

    capSides = LongField()
    cap = capSides

    joinSurfaces = BoolField()
    js = joinSurfaces

    orderedCurves = BoolField()
    oc = orderedCurves

    normalsOutwards = BoolField()
    no = normalsOutwards

    polyOutMethod = PolyOutMethodEnumField()
    pom = polyOutMethod

    polyOutCount = LongField()
    poc = polyOutCount

    polyOutExtrusionType = PolyOutExtrusionTypeEnumField()
    pet = polyOutExtrusionType

    polyOutExtrusionSamples = LongField()
    pes = polyOutExtrusionSamples

    polyOutCurveType = PolyOutCurveTypeEnumField()
    pct = polyOutCurveType

    polyOutCurveSamples = LongField()
    pcs = polyOutCurveSamples

    polyOutUseChordHeight = BoolField()
    uch = polyOutUseChordHeight

    polyOutChordHeight = DoubleLinearField()
    cht = polyOutChordHeight

    polyOutUseChordHeightRatio = BoolField()
    ucr = polyOutUseChordHeightRatio

    polyOutChordHeightRatio = DoubleField()
    chr = polyOutChordHeightRatio
